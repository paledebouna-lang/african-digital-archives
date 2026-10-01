/**
 * ARCHIVA360 — comptes en ligne (Appwrite).
 *
 * Connexion, invitation, mot de passe oublié, « Mon compte » et « Utilisateurs et rôles ».
 * Le site reste statique : ce script dialogue directement avec l'API REST d'Appwrite
 * (aucune bibliothèque externe). Les rôles sont portés par l'équipe Appwrite configurée
 * dans tools/ada/core.py → SITE["appwrite"].
 */
( function () {
	'use strict';

	var cfgEl = document.getElementById( 'aw-config' );
	var CFG = cfgEl ? JSON.parse( cfgEl.textContent ) : {};
	var READY = !! ( CFG.endpoint && CFG.project );
	var TEAM = CFG.team || 'archiva360';

	var ROLES = [
		{ id: 'admin', label: 'Administrateur', desc: 'Tous les droits, dont la gestion des utilisateurs et des rôles' },
		{ id: 'archiviste', label: 'Archiviste', desc: 'Classement, versement au SAE, archives physiques' },
		{ id: 'records', label: 'Records manager', desc: 'Règles de conservation, gel juridique, éliminations' },
		{ id: 'employe', label: 'Employé', desc: 'Dépôt et consultation des documents non confidentiels' },
		{ id: 'auditeur', label: 'Auditeur', desc: 'Lecture seule : documents, journal d’audit, conformité' }
	];
	function roleOf( m ) {
		var r = ( m && m.roles ) || [];
		if ( r.indexOf( 'admin' ) > -1 || r.indexOf( 'owner' ) > -1 ) return 'admin';
		for ( var i = 0; i < ROLES.length; i++ ) if ( r.indexOf( ROLES[ i ].id ) > -1 ) return ROLES[ i ].id;
		return 'employe';
	}
	function roleLabel( id ) {
		for ( var i = 0; i < ROLES.length; i++ ) if ( ROLES[ i ].id === id ) return ROLES[ i ].label;
		return id;
	}
	// L'administrateur est « owner » de l'équipe : c'est ce qui l'autorise à gérer les membres.
	function rolesFor( id ) { return id === 'admin' ? [ 'owner', 'admin' ] : [ id ]; }

	/* ---------- Utilitaires ---------- */
	function $( s, c ) { return ( c || document ).querySelector( s ); }
	function esc( s ) {
		return String( s == null ? '' : s ).replace( /[&<>"']/g, function ( c ) {
			return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ c ];
		} );
	}
	function initials( name, email ) {
		var p = String( name || email || '?' ).trim().split( /\s+/ );
		return ( ( p[ 0 ] || '' ).charAt( 0 ) + ( p[ 1 ] || '' ).charAt( 0 ) ).toUpperCase() || '?';
	}
	function fmtDate( iso ) {
		if ( ! iso ) return '—';
		try { return new Date( iso ).toLocaleDateString( 'fr-FR', { day: '2-digit', month: 'short', year: 'numeric' } ); } catch ( e ) { return iso; }
	}
	var toastTimer;
	function toast( msg ) {
		var t = $( '#toast' );
		if ( ! t ) return;
		t.textContent = msg;
		t.hidden = false;
		clearTimeout( toastTimer );
		toastTimer = setTimeout( function () { t.hidden = true; }, 3600 );
	}
	function storage( k, v ) {
		try {
			if ( v === undefined ) return window.localStorage.getItem( k );
			if ( v === null ) window.localStorage.removeItem( k ); else window.localStorage.setItem( k, v );
		} catch ( e ) { return null; }
	}
	function here( rel ) { return new URL( rel, window.location.href ).href.split( /[?#]/ )[ 0 ]; }
	function params() { return new URLSearchParams( window.location.search ); }

	/* ---------- Client REST Appwrite ---------- */
	var MESSAGES = {
		user_invalid_credentials: 'Adresse e-mail ou mot de passe incorrect.',
		user_blocked: 'Ce compte est désactivé. Contactez votre administrateur.',
		user_password_mismatch: 'Les mots de passe ne correspondent pas.',
		user_invalid_token: 'Ce lien n’est plus valide. Demandez-en un nouveau.',
		user_password_recently_used: 'Choisissez un mot de passe que vous n’avez pas utilisé récemment.',
		password_personal_data: 'Le mot de passe ne doit pas contenir votre nom ou votre adresse e-mail.',
		password_recently_used: 'Choisissez un mot de passe que vous n’avez pas utilisé récemment.',
		team_invite_already_exists: 'Cette personne a déjà reçu une invitation.',
		membership_already_confirmed: 'Cette invitation a déjà été acceptée : connectez-vous.',
		team_invite_mismatch: 'Cette invitation est destinée à un autre compte. Déconnectez-vous puis réessayez.',
		team_invalid_secret: 'Ce lien d’invitation n’est plus valide. Demandez une nouvelle invitation.',
		general_rate_limit_exceeded: 'Trop de tentatives. Patientez une minute puis réessayez.',
		general_argument_invalid: 'Une des valeurs saisies est invalide.',
		user_unauthorized: 'Action non autorisée pour votre rôle.',
		general_unauthorized_scope: 'Votre session a expiré : reconnectez-vous.'
	};
	function AwError( body, status ) {
		this.code = ( body && body.code ) || status;
		this.type = ( body && body.type ) || '';
		this.message = MESSAGES[ this.type ] || ( body && body.message ) || 'Le service est momentanément indisponible.';
	}
	function api( method, path, data ) {
		var headers = { 'X-Appwrite-Project': CFG.project, 'Content-Type': 'application/json', 'X-Appwrite-Response-Format': '1.6.0' };
		// Navigateurs qui bloquent les cookies tiers : Appwrite renvoie la session dans X-Fallback-Cookies.
		var fallback = storage( 'cookieFallback' );
		if ( fallback ) headers[ 'X-Fallback-Cookies' ] = fallback;
		var url = CFG.endpoint.replace( /\/$/, '' ) + path;
		var opts = { method: method, headers: headers, credentials: 'include' };
		if ( data && method === 'GET' ) {
			var q = new URLSearchParams();
			Object.keys( data ).forEach( function ( k ) { q.append( k, data[ k ] ); } );
			url += '?' + q.toString();
		} else if ( data ) {
			opts.body = JSON.stringify( data );
		}
		return fetch( url, opts ).then( function ( res ) {
			var fb = res.headers.get( 'X-Fallback-Cookies' );
			if ( fb ) storage( 'cookieFallback', fb );
			if ( res.status === 204 ) return {};
			return res.json().catch( function () { return {}; } ).then( function ( body ) {
				if ( ! res.ok ) throw new AwError( body, res.status );
				return body;
			} );
		}, function () {
			throw new AwError( { message: 'Impossible de joindre le service de comptes. Vérifiez votre connexion internet.' }, 0 );
		} );
	}
	var aw = {
		me: function () { return api( 'GET', '/account' ); },
		login: function ( email, password ) { return api( 'POST', '/account/sessions/email', { email: email, password: password } ); },
		logout: function ( all ) {
			return api( 'DELETE', all ? '/account/sessions' : '/account/sessions/current' ).then( function ( r ) { storage( 'cookieFallback', null ); return r; } );
		},
		recover: function ( email ) { return api( 'POST', '/account/recovery', { email: email, url: here( '../connexion/' ) + '?reset=1' } ); },
		resetPassword: function ( userId, secret, password ) { return api( 'PUT', '/account/recovery', { userId: userId, secret: secret, password: password } ); },
		setName: function ( name ) { return api( 'PATCH', '/account/name', { name: name } ); },
		setPassword: function ( password, oldPassword ) {
			var d = { password: password };
			if ( oldPassword ) d.oldPassword = oldPassword;
			return api( 'PATCH', '/account/password', d );
		},
		members: function () { return api( 'GET', '/teams/' + TEAM + '/memberships', { 'queries[]': '{"method":"limit","values":[100]}' } ); },
		invite: function ( email, name, role ) {
			return api( 'POST', '/teams/' + TEAM + '/memberships', { email: email, name: name, roles: rolesFor( role ), url: here( '../connexion/' ) + '?invite=1' } );
		},
		setRole: function ( id, role ) { return api( 'PATCH', '/teams/' + TEAM + '/memberships/' + id, { roles: rolesFor( role ) } ); },
		remove: function ( id ) { return api( 'DELETE', '/teams/' + TEAM + '/memberships/' + id ); },
		accept: function ( id, userId, secret ) {
			return api( 'PATCH', '/teams/' + TEAM + '/memberships/' + id + '/status', { userId: userId, secret: secret } );
		}
	};

	function busy( form, on ) {
		Array.prototype.forEach.call( form.querySelectorAll( 'button,input,select' ), function ( el ) { el.disabled = on; } );
	}
	function say( el, kind, html ) { el.innerHTML = '<div class="notice ' + kind + '" role="alert">' + html + '</div>'; }
	function checkPassword( p1, p2 ) {
		if ( p1.length < 10 ) return 'Le mot de passe doit contenir au moins 10 caractères.';
		if ( ! /[a-zA-Z]/.test( p1 ) || ! /[0-9]/.test( p1 ) ) return 'Le mot de passe doit mêler lettres et chiffres.';
		if ( p2 !== undefined && p1 !== p2 ) return 'Les deux mots de passe ne correspondent pas.';
		return '';
	}

	/* ======================================================================
	 * Page de connexion
	 * ==================================================================== */
	function loginPage() {
		var card = $( '#auth-card' );
		var p = params();
		var ESPACE = here( '../espace/' );

		function view( html ) { card.innerHTML = html; var f = card.querySelector( 'input' ); if ( f ) f.focus(); }
		function loginView( msg ) {
			view( '<h1>Connexion</h1><p class="sub">Accédez à votre espace ARCHIVA360.</p><div id="auth-msg">' + ( msg || '' ) + '</div>'
				+ '<form id="login-form" novalidate><div class="field"><label for="l-email">Adresse e-mail</label><input id="l-email" type="email" autocomplete="username" required></div>'
				+ '<div class="field"><label for="l-pass">Mot de passe</label><input id="l-pass" type="password" autocomplete="current-password" required></div>'
				+ '<button class="btn wide" type="submit">Se connecter</button></form>'
				+ '<p class="alt"><a href="#" data-act="forgot">Mot de passe oublié ?</a></p>' );
		}
		function forgotView() {
			view( '<h1>Mot de passe oublié</h1><p class="sub">Indiquez votre adresse : vous recevrez un lien pour choisir un nouveau mot de passe.</p><div id="auth-msg"></div>'
				+ '<form id="forgot-form" novalidate><div class="field"><label for="f-email">Adresse e-mail</label><input id="f-email" type="email" autocomplete="username" required></div>'
				+ '<button class="btn wide" type="submit">Envoyer le lien</button></form><p class="alt"><a href="#" data-act="login">← Retour à la connexion</a></p>' );
		}
		function passwordView( title, sub, formId, label ) {
			view( '<h1>' + title + '</h1><p class="sub">' + sub + '</p><div id="auth-msg"></div>'
				+ '<form id="' + formId + '" novalidate><div class="field"><label for="p1">Nouveau mot de passe</label><input id="p1" type="password" autocomplete="new-password" required>'
				+ '<span class="hint">Au moins 10 caractères, avec des lettres et des chiffres.</span></div>'
				+ '<div class="field"><label for="p2">Confirmer le mot de passe</label><input id="p2" type="password" autocomplete="new-password" required></div>'
				+ '<button class="btn wide" type="submit">' + label + '</button></form>' );
		}

		if ( ! READY ) {
			view( '<h1>Espace ARCHIVA360</h1><div class="notice warn">Les comptes en ligne sont en cours d’activation. Revenez très bientôt, ou contactez <a href="mailto:' + esc( CFG.contact ) + '">' + esc( CFG.contact ) + '</a>.</div>'
				+ '<p>En attendant, découvrez toutes les fonctions dans la <a href="' + here( '../demo-interactive/' ) + '">démo interactive</a>.</p>' );
			return;
		}

		card.addEventListener( 'click', function ( e ) {
			var a = e.target.closest( '[data-act]' );
			if ( ! a ) return;
			e.preventDefault();
			if ( a.dataset.act === 'forgot' ) forgotView(); else loginView();
		} );

		card.addEventListener( 'submit', function ( e ) {
			e.preventDefault();
			var f = e.target, msg = $( '#auth-msg' );
			if ( f.id === 'login-form' ) {
				var email = $( '#l-email' ).value.trim(), pass = $( '#l-pass' ).value;
				if ( ! email || ! pass ) return say( msg, 'bad', 'Renseignez votre adresse e-mail et votre mot de passe.' );
				busy( f, true );
				aw.login( email, pass ).then( function () { window.location.href = ESPACE; }, function ( err ) {
					busy( f, false ); say( msg, 'bad', esc( err.message ) );
				} );
			} else if ( f.id === 'forgot-form' ) {
				var em = $( '#f-email' ).value.trim();
				if ( ! /.+@.+\..+/.test( em ) ) return say( msg, 'bad', 'Indiquez une adresse e-mail valide.' );
				busy( f, true );
				// Même réponse que le compte existe ou non : on ne révèle pas les adresses inscrites.
				var done = function () { loginView( '<div class="notice ok">Si un compte existe pour <b>' + esc( em ) + '</b>, un e-mail vient de lui être envoyé. Pensez à vérifier les indésirables.</div>' ); };
				aw.recover( em ).then( done, function ( err ) {
					if ( err.code === 404 ) return done();
					busy( f, false ); say( msg, 'bad', esc( err.message ) );
				} );
			} else if ( f.id === 'reset-form' || f.id === 'invite-form' ) {
				var p1 = $( '#p1' ).value, p2 = $( '#p2' ).value, bad = checkPassword( p1, p2 );
				if ( bad ) return say( msg, 'bad', bad );
				busy( f, true );
				var job = f.id === 'reset-form'
					? aw.resetPassword( p.get( 'userId' ), p.get( 'secret' ), p1 ).then( function () {
						window.history.replaceState( null, '', here( './' ) );
						loginView( '<div class="notice ok">Mot de passe modifié. Connectez-vous avec votre nouveau mot de passe.</div>' );
					} )
					: aw.setPassword( p1 ).then( function () { window.location.href = ESPACE + '?bienvenue=1'; } );
				job.catch( function ( err ) { busy( f, false ); say( msg, 'bad', esc( err.message ) ); } );
			}
		} );

		// Lien reçu par e-mail : réinitialisation du mot de passe
		if ( p.get( 'reset' ) && p.get( 'userId' ) && p.get( 'secret' ) ) {
			return passwordView( 'Nouveau mot de passe', 'Choisissez le mot de passe de votre compte ARCHIVA360.', 'reset-form', 'Enregistrer le mot de passe' );
		}
		// Lien d'invitation : on accepte l'invitation (ce qui ouvre une session) puis on fait choisir un mot de passe
		if ( p.get( 'invite' ) && p.get( 'membershipId' ) && p.get( 'userId' ) && p.get( 'secret' ) ) {
			view( '<h1>Invitation</h1><p class="sub">Activation de votre compte…</p>' );
			aw.accept( p.get( 'membershipId' ), p.get( 'userId' ), p.get( 'secret' ) ).then( function () {
				window.history.replaceState( null, '', here( './' ) );
				passwordView( 'Bienvenue dans ARCHIVA360', 'Votre invitation est acceptée. Choisissez maintenant le mot de passe de votre compte.', 'invite-form', 'Activer mon compte' );
			}, function ( err ) {
				loginView( '<div class="notice bad">' + esc( err.message ) + '</div>' );
			} );
			return;
		}
		// Déjà connecté ? Direction l'espace.
		view( '<p class="sub">Chargement…</p>' );
		aw.me().then( function () { window.location.replace( ESPACE ); }, function ( err ) {
			loginView( err.code === 0 ? '<div class="notice warn">Vous êtes hors connexion. La connexion sera possible dès le retour du réseau.</div>' : '' );
		} );
	}

	/* ======================================================================
	 * Espace connecté
	 * ==================================================================== */
	function espacePage() {
		var LOGIN = here( '../connexion/' );
		if ( ! READY ) { window.location.replace( LOGIN ); return; }
		var state = { me: null, mine: null, members: [] };
		var view = $( '#view' );

		function isAdmin() { return roleOf( state.mine ) === 'admin'; }
		function adminCount() { return state.members.filter( function ( m ) { return m.confirm && roleOf( m ) === 'admin'; } ).length; }

		function nav() {
			var items = [ [ 'accueil', 'Tableau de bord' ], [ 'compte', 'Mon compte' ] ];
			if ( isAdmin() ) items.push( [ 'utilisateurs', 'Utilisateurs et rôles' ] );
			var cur = currentView();
			$( '#nav' ).innerHTML = items.map( function ( i ) {
				return '<button type="button" data-go="' + i[ 0 ] + '"' + ( cur === i[ 0 ] ? ' aria-current="page"' : '' ) + '>' + i[ 1 ] + '</button>';
			} ).join( '' );
		}
		function currentView() {
			var h = window.location.hash.replace( '#', '' ) || 'accueil';
			if ( h === 'utilisateurs' && ! isAdmin() ) h = 'accueil';
			return [ 'accueil', 'compte', 'utilisateurs' ].indexOf( h ) > -1 ? h : 'accueil';
		}
		function render() {
			nav();
			var v = currentView();
			( { accueil: vHome, compte: vAccount, utilisateurs: vUsers } )[ v ]();
			$( '#view' ).focus( { preventScroll: true } );
		}

		function vHome() {
			var role = roleOf( state.mine );
			var welcome = params().get( 'bienvenue' ) ? '<div class="notice ok">Votre compte est activé. Bienvenue !</div>' : '';
			var admin = isAdmin()
				? '<div class="box"><h2>Votre équipe</h2><p><b>' + state.members.filter( function ( m ) { return m.confirm; } ).length + '</b> membre(s) actif(s), <b>'
					+ state.members.filter( function ( m ) { return ! m.confirm; } ).length + '</b> invitation(s) en attente.</p>'
					+ '<div class="btns"><a class="btn" href="#utilisateurs">Gérer les utilisateurs et les rôles</a></div></div>'
				: '';
			view.innerHTML = welcome + '<h1>Bonjour ' + esc( state.me.name || state.me.email ) + '</h1><p class="sub">Espace ' + esc( CFG.orgName ) + ' · rôle : <span class="tag b">' + roleLabel( role ) + '</span></p>'
				+ '<div class="grid g2">' + admin
				+ '<div class="box"><h2>Ce que permet votre rôle</h2><p>' + esc( ROLES.filter( function ( r ) { return r.id === role; } )[ 0 ].desc ) + '.</p></div>'
				+ '<div class="box"><h2>Modules documentaires</h2><p>Le dépôt de documents, la recherche, les règles de conservation et l’audit trail seront ouverts sur cet espace au fil du déploiement de votre organisation.</p>'
				+ '<p class="muted">En attendant, vous pouvez vous exercer dans la démo interactive (données fictives, stockées dans votre navigateur).</p>'
				+ '<div class="btns"><a class="btn o" href="' + here( '../demo-interactive/' ) + '">Ouvrir la démo interactive</a></div></div>'
				+ '<div class="box"><h2>Se former</h2><p>ARCHIVA Academy : six niveaux de formation, du classement à l’administration d’ARCHIVA360, avec certificat vérifiable.</p>'
				+ '<div class="btns"><a class="btn o" href="' + here( '../../academy/' ) + '">Accéder à l’Academy</a></div></div></div>';
		}

		function vAccount() {
			view.innerHTML = '<h1>Mon compte</h1><p class="sub">' + esc( state.me.email ) + ' · compte créé le ' + fmtDate( state.me.registration || state.me.$createdAt ) + '</p>'
				+ '<div class="grid g2"><div class="box"><h2>Profil</h2><form id="name-form"><div class="field"><label for="a-name">Nom affiché</label><input id="a-name" value="' + esc( state.me.name ) + '" required maxlength="128"></div>'
				+ '<div class="btns"><button class="btn" type="submit">Enregistrer</button></div></form></div>'
				+ '<div class="box"><h2>Mot de passe</h2><div id="pw-msg"></div><form id="pw-form" novalidate><div class="field"><label for="a-old">Mot de passe actuel</label><input id="a-old" type="password" autocomplete="current-password"></div>'
				+ '<div class="field"><label for="p1">Nouveau mot de passe</label><input id="p1" type="password" autocomplete="new-password"><span class="hint">Au moins 10 caractères, avec des lettres et des chiffres.</span></div>'
				+ '<div class="field"><label for="p2">Confirmer</label><input id="p2" type="password" autocomplete="new-password"></div>'
				+ '<div class="btns"><button class="btn" type="submit">Changer le mot de passe</button></div></form></div>'
				+ '<div class="box"><h2>Sessions</h2><p>Vous avez utilisé un ordinateur partagé ou perdu un appareil ? Fermez toutes vos sessions ouvertes.</p>'
				+ '<div class="btns"><button class="btn o" type="button" data-act="logout">Se déconnecter</button><button class="btn danger o" type="button" data-act="logout-all">Déconnecter tous les appareils</button></div></div></div>';
		}

		function vUsers() {
			var rows = state.members.map( function ( m ) {
				var role = roleOf( m ), self = m.userId === state.me.$id;
				var sel = '<label class="sr" for="r-' + m.$id + '">Rôle de ' + esc( m.userName || m.userEmail ) + '</label><select class="inp" id="r-' + m.$id + '" data-role="' + m.$id + '"' + ( self ? ' disabled title="Vous ne pouvez pas modifier votre propre rôle"' : '' ) + '>'
					+ ROLES.map( function ( r ) { return '<option value="' + r.id + '"' + ( r.id === role ? ' selected' : '' ) + '>' + r.label + '</option>'; } ).join( '' ) + '</select>';
				return '<tr data-member="' + m.$id + '"><td><div class="fi"><span class="av">' + esc( initials( m.userName, m.userEmail ) ) + '</span><div><b>' + esc( m.userName || '—' ) + '</b>' + ( self ? ' <span class="tag">vous</span>' : '' )
					+ '<div class="muted">' + esc( m.userEmail ) + '</div></div></div></td><td>' + sel + '</td><td>'
					+ ( m.confirm ? '<span class="tag g">Actif</span><div class="muted">depuis le ' + fmtDate( m.joined ) + '</div>' : '<span class="tag a">Invitation envoyée</span><div class="muted">le ' + fmtDate( m.invited ) + '</div>' )
					+ '</td><td>' + ( self ? '' : '<button class="btn sm danger o" type="button" data-act="remove" data-id="' + m.$id + '">' + ( m.confirm ? 'Retirer' : 'Annuler l’invitation' ) + '</button>' ) + '</td></tr>';
			} ).join( '' );
			view.innerHTML = '<h1>Utilisateurs et rôles</h1><p class="sub">Invitez les personnes de votre organisation et attribuez-leur un rôle. Chaque invitation est envoyée par e-mail ; la personne choisit elle-même son mot de passe.</p>'
				+ '<div class="grid g21"><div class="box"><h2>Membres <small>' + state.members.length + '</small></h2><div class="tbl"><table><thead><tr><th>Utilisateur</th><th>Rôle</th><th>Statut</th><th></th></tr></thead><tbody>' + rows + '</tbody></table></div></div>'
				+ '<div class="box"><h2>Inviter un utilisateur</h2><div id="inv-msg"></div><form id="invite-form" novalidate>'
				+ '<div class="field"><label for="i-name">Nom complet</label><input id="i-name" autocomplete="off" required maxlength="128"></div>'
				+ '<div class="field"><label for="i-email">Adresse e-mail</label><input id="i-email" type="email" autocomplete="off" required></div>'
				+ '<div class="field"><label for="i-role">Rôle</label><select id="i-role">' + ROLES.map( function ( r ) { return '<option value="' + r.id + '"' + ( r.id === 'employe' ? ' selected' : '' ) + '>' + r.label + '</option>'; } ).join( '' ) + '</select>'
				+ '<span class="hint" id="i-role-desc"></span></div><div class="btns"><button class="btn" type="submit">Envoyer l’invitation</button></div></form></div></div>'
				+ '<div class="box" style="margin-top:16px"><h2>Les rôles</h2><div class="tbl"><table><tbody>' + ROLES.map( function ( r ) { return '<tr><td><b>' + r.label + '</b></td><td>' + r.desc + '</td></tr>'; } ).join( '' ) + '</tbody></table></div></div>';
			roleHint();
		}
		function roleHint() {
			var s = $( '#i-role' ), h = $( '#i-role-desc' );
			if ( s && h ) h.textContent = ROLES.filter( function ( r ) { return r.id === s.value; } )[ 0 ].desc;
		}

		function reloadMembers() {
			return aw.members().then( function ( r ) {
				state.members = ( r.memberships || [] ).sort( function ( a, b ) { return String( a.userName || a.userEmail ).localeCompare( String( b.userName || b.userEmail ), 'fr' ); } );
				state.mine = state.members.filter( function ( m ) { return m.userId === state.me.$id; } )[ 0 ] || null;
			} );
		}

		document.addEventListener( 'click', function ( e ) {
			var go = e.target.closest( '[data-go]' );
			if ( go ) { window.location.hash = go.dataset.go; return; }
			var a = e.target.closest( '[data-act]' );
			if ( ! a ) return;
			var act = a.dataset.act;
			if ( act === 'logout' || act === 'logout-all' ) {
				a.disabled = true;
				aw.logout( act === 'logout-all' ).then( null, function () {} ).then( function () { window.location.href = LOGIN; } );
			} else if ( act === 'remove' ) {
				var m = state.members.filter( function ( x ) { return x.$id === a.dataset.id; } )[ 0 ];
				if ( ! m ) return;
				if ( m.confirm && roleOf( m ) === 'admin' && adminCount() < 2 ) return toast( 'Impossible : l’organisation doit garder au moins un administrateur.' );
				if ( ! window.confirm( ( m.confirm ? 'Retirer ' : 'Annuler l’invitation de ' ) + ( m.userName || m.userEmail ) + ' ?' ) ) return;
				a.disabled = true;
				aw.remove( m.$id ).then( reloadMembers ).then( function () { toast( 'Accès retiré.' ); render(); }, function ( err ) { a.disabled = false; toast( err.message ); } );
			}
		} );

		document.addEventListener( 'change', function ( e ) {
			if ( e.target.id === 'i-role' ) return roleHint();
			var id = e.target.dataset && e.target.dataset.role;
			if ( ! id ) return;
			var m = state.members.filter( function ( x ) { return x.$id === id; } )[ 0 ], sel = e.target;
			if ( roleOf( m ) === 'admin' && sel.value !== 'admin' && m.confirm && adminCount() < 2 ) {
				sel.value = 'admin';
				return toast( 'Impossible : l’organisation doit garder au moins un administrateur.' );
			}
			sel.disabled = true;
			aw.setRole( id, sel.value ).then( reloadMembers ).then( function () { toast( 'Rôle mis à jour : ' + roleLabel( sel.value ) + '.' ); render(); }, function ( err ) {
				sel.disabled = false; sel.value = roleOf( m ); toast( err.message );
			} );
		} );

		document.addEventListener( 'submit', function ( e ) {
			var f = e.target;
			e.preventDefault();
			if ( f.id === 'name-form' ) {
				var n = $( '#a-name' ).value.trim();
				if ( ! n ) return;
				busy( f, true );
				aw.setName( n ).then( function ( u ) { state.me = u; busy( f, false ); paintUser(); toast( 'Profil enregistré.' ); }, function ( err ) { busy( f, false ); toast( err.message ); } );
			} else if ( f.id === 'pw-form' ) {
				var msg = $( '#pw-msg' ), old = $( '#a-old' ).value, p1 = $( '#p1' ).value, bad = checkPassword( p1, $( '#p2' ).value );
				if ( ! old ) bad = 'Saisissez votre mot de passe actuel.';
				if ( bad ) return say( msg, 'bad', bad );
				busy( f, true );
				aw.setPassword( p1, old ).then( function () { f.reset(); busy( f, false ); say( msg, 'ok', 'Mot de passe modifié.' ); }, function ( err ) {
					busy( f, false ); say( msg, 'bad', err.code === 401 ? 'Mot de passe actuel incorrect.' : esc( err.message ) );
				} );
			} else if ( f.id === 'invite-form' ) {
				var im = $( '#inv-msg' ), name = $( '#i-name' ).value.trim(), email = $( '#i-email' ).value.trim().toLowerCase(), role = $( '#i-role' ).value;
				if ( ! name ) return say( im, 'bad', 'Indiquez le nom de la personne.' );
				if ( ! /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test( email ) ) return say( im, 'bad', 'Indiquez une adresse e-mail valide.' );
				if ( state.members.some( function ( m ) { return String( m.userEmail ).toLowerCase() === email; } ) ) return say( im, 'bad', 'Cette personne fait déjà partie de l’organisation.' );
				busy( f, true );
				aw.invite( email, name, role ).then( reloadMembers ).then( function () {
					render();
					say( $( '#inv-msg' ), 'ok', 'Invitation envoyée à <b>' + esc( email ) + '</b> (' + roleLabel( role ) + ').' );
				}, function ( err ) { busy( f, false ); say( im, 'bad', esc( err.message ) ); } );
			}
		} );

		function paintUser() {
			$( '#who-name' ).textContent = state.me.name || state.me.email;
			$( '#who-av' ).textContent = initials( state.me.name, state.me.email );
			$( '#who-role' ).textContent = roleLabel( roleOf( state.mine ) );
		}

		window.addEventListener( 'hashchange', render );
		aw.me().then( function ( u ) {
			state.me = u;
			return reloadMembers().then( null, function ( err ) { if ( err.code !== 401 && err.code !== 404 ) throw err; } );
		}, function ( err ) {
			// Hors connexion : on ne déconnecte pas l'utilisateur, on l'informe.
			if ( err.code === 0 ) throw new AwError( { message: 'Vous êtes hors connexion. Votre espace se rechargera dès le retour du réseau ; la démo interactive reste utilisable.' }, 0 );
			window.location.replace( LOGIN ); throw null;
		} ).then( function () {
			if ( ! state.mine ) {
				view.innerHTML = '<div class="box"><h1>Compte sans organisation</h1><p>Votre compte <b>' + esc( state.me.email ) + '</b> n’est rattaché à aucune organisation ARCHIVA360. Demandez une invitation à votre administrateur.</p>'
					+ '<div class="btns"><button class="btn o" type="button" data-act="logout">Se déconnecter</button></div></div>';
				return;
			}
			paintUser();
			render();
		} ).catch( function ( err ) {
			if ( ! err ) return;
			view.innerHTML = '<div class="notice ' + ( err.code === 0 ? 'warn' : 'bad' ) + '">' + esc( err.message ) + '</div>'
				+ ( err.code === 0 ? '<div class="btns"><a class="btn o" href="' + here( '../demo-interactive/' ) + '">Ouvrir la démo interactive</a></div>' : '' );
			if ( err.code === 0 ) window.addEventListener( 'online', function () { window.location.reload(); }, { once: true } );
		} );
	}

	if ( document.body.classList.contains( 'archiva360-login' ) ) loginPage();
	if ( document.body.classList.contains( 'archiva360-espace' ) ) espacePage();
}() );
