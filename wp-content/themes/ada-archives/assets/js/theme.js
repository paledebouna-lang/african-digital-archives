/**
 * ADA Archives — theme scripts
 * @version 1.4.2
 */
( function () {
	'use strict';

	var settings = window.adaSettings || {};
	var $ = function ( sel, ctx ) { return ( ctx || document ).querySelector( sel ); };
	var $$ = function ( sel, ctx ) { return Array.prototype.slice.call( ( ctx || document ).querySelectorAll( sel ) ); };

	/* ------------------------------------------------------------------
	 * Sticky header
	 * ------------------------------------------------------------------ */
	var header = $( '#masthead' );
	var scrollUp = $( '#scroll-up' );
	function onScroll() {
		var y = window.pageYOffset;
		if ( header ) header.classList.toggle( 'is-scrolled', y > 10 );
		if ( scrollUp ) scrollUp.classList.toggle( 'is-visible', y > 700 );
	}
	window.addEventListener( 'scroll', onScroll, { passive: true } );
	onScroll();
	if ( scrollUp ) {
		scrollUp.addEventListener( 'click', function () { window.scrollTo( { top: 0, behavior: 'smooth' } ); } );
	}

	/* ------------------------------------------------------------------
	 * Primary navigation (mobile)
	 * ------------------------------------------------------------------ */
	var nav = $( '#site-navigation' );
	var toggle = $( '.menu-toggle' );
	if ( nav && toggle ) {
		toggle.addEventListener( 'click', function () {
			var open = nav.classList.toggle( 'toggled' );
			toggle.setAttribute( 'aria-expanded', open ? 'true' : 'false' );
			document.body.classList.toggle( 'menu-open', open );
		} );
		$$( '.menu-item-has-children > a', nav ).forEach( function ( a ) {
			a.addEventListener( 'click', function ( e ) {
				if ( window.innerWidth > 1024 ) return;
				var li = a.parentNode;
				if ( ! li.classList.contains( 'submenu-open' ) ) {
					e.preventDefault();
					$$( '.submenu-open', nav ).forEach( function ( o ) { if ( o !== li ) o.classList.remove( 'submenu-open' ); } );
					li.classList.add( 'submenu-open' );
					a.setAttribute( 'aria-expanded', 'true' );
				}
			} );
		} );
		document.addEventListener( 'keydown', function ( e ) {
			if ( e.key === 'Escape' && nav.classList.contains( 'toggled' ) ) toggle.click();
		} );
	}

	/* ------------------------------------------------------------------
	 * Header search
	 * ------------------------------------------------------------------ */
	var searchToggle = $( '.search-toggle' );
	var headerSearch = $( '#header-search' );
	if ( searchToggle && headerSearch ) {
		searchToggle.addEventListener( 'click', function () {
			var open = headerSearch.classList.toggle( 'is-open' );
			searchToggle.setAttribute( 'aria-expanded', open ? 'true' : 'false' );
			if ( open ) $( 'input', headerSearch ).focus();
		} );
	}

	/* ------------------------------------------------------------------
	 * Tabs
	 * ------------------------------------------------------------------ */
	$$( '.ada-tabs' ).forEach( function ( wrap ) {
		var tabs = $$( '[role=tab]', wrap );
		tabs.forEach( function ( tab, i ) {
			tab.addEventListener( 'click', function () { select( i ); } );
			tab.addEventListener( 'keydown', function ( e ) {
				if ( e.key === 'ArrowRight' ) { select( ( i + 1 ) % tabs.length ); tabs[ ( i + 1 ) % tabs.length ].focus(); }
				if ( e.key === 'ArrowLeft' ) { var p = ( i - 1 + tabs.length ) % tabs.length; select( p ); tabs[ p ].focus(); }
			} );
		} );
		function select( idx ) {
			tabs.forEach( function ( t, j ) {
				t.setAttribute( 'aria-selected', j === idx ? 'true' : 'false' );
				t.tabIndex = j === idx ? 0 : -1;
				$( '#' + t.getAttribute( 'aria-controls' ) ).hidden = j !== idx;
			} );
		}
	} );

	/* ------------------------------------------------------------------
	 * Cookie notice (Cookie Notice & Compliance style)
	 * ------------------------------------------------------------------ */
	var cookie = $( '#cookie-notice' );
	function readConsent() { try { return localStorage.getItem( 'cookie_notice_accepted' ); } catch ( e ) { return null; } }
	function writeConsent( v ) { try { localStorage.setItem( 'cookie_notice_accepted', v ); } catch ( e ) {} }
	if ( cookie ) {
		if ( ! readConsent() ) cookie.classList.add( 'cookie-notice-visible' );
		$$( '[data-cookie-set]', cookie ).forEach( function ( b ) {
			b.addEventListener( 'click', function () {
				writeConsent( b.getAttribute( 'data-cookie-set' ) );
				cookie.classList.remove( 'cookie-notice-visible' );
			} );
		} );
	}

	/* ------------------------------------------------------------------
	 * Copy link (share)
	 * ------------------------------------------------------------------ */
	$$( '[data-copy-link]' ).forEach( function ( b ) {
		b.addEventListener( 'click', function () {
			var done = function () { b.setAttribute( 'title', 'Lien copié' ); b.classList.add( 'is-copied' ); };
			if ( navigator.clipboard ) navigator.clipboard.writeText( location.href ).then( done, done );
			else done();
		} );
	} );

	/* ------------------------------------------------------------------
	 * Forms (Contact Form 7 behaviour, sent through the visitor's mail app)
	 * ------------------------------------------------------------------ */
	var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
	$$( 'form.wpcf7-form' ).forEach( function ( form ) {
		var output = $( '.wpcf7-response-output', form );
		form.addEventListener( 'submit', function ( e ) {
			e.preventDefault();
			$$( '.wpcf7-not-valid-tip', form ).forEach( function ( t ) { t.remove(); } );
			$$( '.wpcf7-not-valid', form ).forEach( function ( f ) { f.classList.remove( 'wpcf7-not-valid' ); f.removeAttribute( 'aria-invalid' ); } );
			var bad = [];
			$$( '[aria-required=true]', form ).forEach( function ( f ) {
				var ok = f.type === 'checkbox' ? f.checked : f.value.trim() !== '';
				if ( ok && f.type === 'email' ) ok = emailRe.test( f.value.trim() );
				if ( ! ok ) {
					bad.push( f );
					f.classList.add( 'wpcf7-not-valid' );
					f.setAttribute( 'aria-invalid', 'true' );
					var tip = document.createElement( 'span' );
					tip.className = 'wpcf7-not-valid-tip';
					tip.textContent = f.type === 'email' && f.value.trim() ? 'L’adresse e-mail saisie n’est pas valide.' : ( f.type === 'checkbox' ? 'Vous devez accepter pour continuer.' : 'Ce champ est obligatoire.' );
					( f.closest( '.wpcf7-form-control-wrap' ) || f.parentNode ).appendChild( tip );
				}
			} );
			output.classList.add( 'is-visible' );
			if ( bad.length ) {
				output.classList.remove( 'is-success' );
				output.textContent = 'Un ou plusieurs champs contiennent une erreur. Veuillez vérifier et réessayer.';
				bad[ 0 ].focus();
				return;
			}
			var subject = form.getAttribute( 'data-subject' ) || 'Demande depuis le site';
			var lines = [];
			$$( '[name]', form ).forEach( function ( f ) {
				if ( f.type === 'submit' || f.type === 'hidden' ) return;
				if ( ( f.type === 'checkbox' || f.type === 'radio' ) && ! f.checked ) return;
				var label = f.getAttribute( 'data-label' ) || f.name;
				if ( f.value.trim() ) lines.push( label + ' : ' + f.value.trim() );
			} );
			var org = form.querySelector( '[name=organisation]' );
			if ( org && org.value.trim() ) subject += ' — ' + org.value.trim();
			var href = 'mailto:' + ( settings.contactEmail || '' ) + '?subject=' + encodeURIComponent( subject ) + '&body=' + encodeURIComponent( lines.join( '\n' ) );
			var viaMail = function () {
				output.classList.add( 'is-success' );
				output.textContent = 'Merci. Votre messagerie s’ouvre avec votre demande prête à être envoyée.';
				window.location.href = href;
			};
			if ( ! settings.formEndpoint || ! window.fetch ) { viaMail(); return; }
			var submit = $( '[type=submit]', form );
			if ( submit ) submit.disabled = true;
			output.classList.remove( 'is-success' );
			output.textContent = 'Envoi en cours…';
			var data = { _subject: subject, message_complet: lines.join( '\n' ) };
			$$( '[name]', form ).forEach( function ( f ) {
				if ( ( f.type === 'checkbox' || f.type === 'radio' ) && ! f.checked ) return;
				if ( f.type !== 'submit' && f.value.trim() ) data[ f.name ] = f.value.trim();
			} );
			fetch( settings.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify( data ) } )
				.then( function ( r ) {
					if ( ! r.ok ) throw new Error( r.status );
					output.classList.add( 'is-success' );
					output.textContent = 'Merci, votre demande a bien été envoyée. Nous vous répondons sous deux jours ouvrés.';
					form.reset();
				} )
				.catch( function () {
					output.textContent = 'L’envoi n’a pas abouti. Votre messagerie va s’ouvrir pour envoyer la demande autrement.';
					setTimeout( viaMail, 1200 );
				} )
				.then( function () { if ( submit ) submit.disabled = false; } );
		} );
	} );

	$$( 'form.newsletter-form' ).forEach( function ( form ) {
		form.addEventListener( 'submit', function ( e ) {
			e.preventDefault();
			var input = $( 'input[type=email]', form );
			var msg = $( '.nl-msg', form );
			if ( ! emailRe.test( input.value.trim() ) ) { msg.textContent = 'Saisissez une adresse e-mail valide.'; input.focus(); return; }
			msg.textContent = 'Merci. Votre messagerie s’ouvre pour confirmer l’inscription.';
			window.location.href = 'mailto:' + ( settings.contactEmail || '' ) + '?subject=' + encodeURIComponent( 'Inscription à la lettre ADA' ) + '&body=' + encodeURIComponent( 'Merci d’inscrire l’adresse ' + input.value.trim() + ' à la lettre d’information ADA.' );
		} );
	} );

	/* ------------------------------------------------------------------
	 * Blog category filter
	 * ------------------------------------------------------------------ */
	$$( '.filter-bar[data-filter-target]' ).forEach( function ( bar ) {
		var target = $( bar.getAttribute( 'data-filter-target' ) );
		$$( 'button', bar ).forEach( function ( b ) {
			b.addEventListener( 'click', function () {
				$$( 'button', bar ).forEach( function ( o ) { o.classList.toggle( 'is-active', o === b ); o.setAttribute( 'aria-pressed', o === b ? 'true' : 'false' ); } );
				var cat = b.getAttribute( 'data-cat' );
				$$( '[data-cat]', target ).forEach( function ( item ) {
					item.classList.toggle( 'is-hidden', cat !== 'all' && item.getAttribute( 'data-cat' ).split( ' ' ).indexOf( cat ) === -1 );
				} );
			} );
		} );
	} );

	/* ------------------------------------------------------------------
	 * Glossary live filter
	 * ------------------------------------------------------------------ */
	var gInput = $( '#glossary-filter' );
	if ( gInput ) {
		var norm = function ( s ) { return s.toLowerCase().normalize( 'NFD' ).replace( /[̀-ͯ]/g, '' ); };
		gInput.addEventListener( 'input', function () {
			var q = norm( gInput.value.trim() );
			$$( '.glossary-section' ).forEach( function ( sec ) {
				var any = false;
				$$( '.glossary-term', sec ).forEach( function ( t ) {
					var hit = ! q || norm( t.textContent ).indexOf( q ) !== -1;
					t.classList.toggle( 'is-hidden', ! hit );
					if ( hit ) any = true;
				} );
				sec.classList.toggle( 'is-hidden', ! any );
			} );
			var empty = $( '#glossary-empty' );
			if ( empty ) empty.classList.toggle( 'is-hidden', $$( '.glossary-section:not(.is-hidden)' ).length > 0 );
		} );
	}

	/* ------------------------------------------------------------------
	 * SHA-256 integrity demo
	 * ------------------------------------------------------------------ */
	$$( '.hash-demo' ).forEach( function ( box ) {
		var input = $( 'textarea, input', box );
		var out = $( 'code', box );
		var status = $( '.hash-status', box );
		var original = null;
		function hex( buf ) { return Array.prototype.map.call( new Uint8Array( buf ), function ( b ) { return ( '0' + b.toString( 16 ) ).slice( -2 ); } ).join( '' ).toUpperCase(); }
		function run() {
			if ( ! window.crypto || ! crypto.subtle ) { out.textContent = 'Votre navigateur ne permet pas le calcul local.'; return; }
			crypto.subtle.digest( 'SHA-256', new TextEncoder().encode( input.value ) ).then( function ( buf ) {
				var h = hex( buf );
				if ( original === null ) original = h;
				out.textContent = h.replace( /(.{8})/g, '$1 ' ).trim();
				var same = h === original;
				status.className = 'hash-status ' + ( same ? 'is-ok' : 'is-changed' );
				$( 'span', status ).textContent = same ? 'Intègre : l’empreinte est identique à celle enregistrée à l’archivage.' : 'Altéré : l’empreinte ne correspond plus. La plateforme signale le document.';
			} );
		}
		input.addEventListener( 'input', run );
		run();
	} );

	/* ------------------------------------------------------------------
	 * Document Health Check
	 * ------------------------------------------------------------------ */
	var hc = $( '#healthcheck-form' );
	if ( hc ) {
		var total = $$( '.hc-question', hc ).length;
		var ring = $( '#hc-ring' );
		var circ = 2 * Math.PI * 78;
		ring.style.strokeDasharray = circ;
		ring.style.strokeDashoffset = circ;
		var levels = [
			{ max: 30, name: 'Organisation documentaire faible', color: '#E0655A', advice: [ 'Réaliser un inventaire rapide des fonds papier et numériques', 'Mettre en place une sauvegarde hors site dès maintenant', 'Définir qui peut accéder aux documents sensibles' ] },
			{ max: 60, name: 'Organisation intermédiaire', color: '#E5A93A', advice: [ 'Formaliser un plan de classement commun', 'Fixer les durées de conservation avec un archiviste et un juriste', 'Numériser en priorité les dossiers les plus consultés' ] },
			{ max: 80, name: 'Bonne maturité', color: '#6FB1FF', advice: [ 'Automatiser les règles de conservation et les alertes d’échéance', 'Mettre en place une traçabilité complète des accès', 'Tester régulièrement la restauration des sauvegardes' ] },
			{ max: 100, name: 'Maturité avancée', color: '#3CC48D', advice: [ 'Préparer la préservation à long terme des formats', 'Mettre en place une preuve d’intégrité (empreinte et horodatage)', 'Viser un audit externe de votre dispositif' ] }
		];
		function compute() {
			var sum = 0, answered = 0;
			$$( '.hc-question', hc ).forEach( function ( q ) {
				var c = $( 'input:checked', q );
				if ( c ) { answered++; sum += parseFloat( c.value ); }
			} );
			var score = Math.round( sum / total * 100 );
			$( '#hc-score' ).textContent = answered ? score : '–';
			$( '#hc-progress' ).textContent = answered + ' / ' + total + ' questions répondues';
			ring.style.strokeDashoffset = circ - ( answered ? score : 0 ) / 100 * circ;
			var lvl = levels.filter( function ( l ) { return score <= l.max; } )[ 0 ];
			var levelEl = $( '#hc-level' );
			var adv = $( '#hc-advice' );
			if ( answered < total ) {
				levelEl.textContent = answered ? 'Score provisoire' : 'Répondez aux questions';
				ring.style.stroke = answered ? lvl.color : '#6FB1FF';
				adv.innerHTML = '<p>Votre score et nos premières recommandations s’affichent à mesure que vous répondez.</p>';
			} else {
				levelEl.textContent = lvl.name;
				ring.style.stroke = lvl.color;
				adv.innerHTML = '<strong style="color:#fff">Nos trois priorités pour vous</strong><ul>' + lvl.advice.map( function ( a ) { return '<li>' + a + '</li>'; } ).join( '' ) + '</ul>';
			}
			var link = $( '#hc-cta' );
			if ( link ) link.href = link.getAttribute( 'data-base' ) + '?diagnostic=' + ( answered === total ? score : '' );
		}
		hc.addEventListener( 'change', compute );
		compute();
	}

	/* Pre-fill contact form from health check */
	var params = new URLSearchParams( location.search );
	var diag = params.get( 'diagnostic' );
	var msgField = $( '#cf7-message' );
	if ( diag && msgField && ! msgField.value ) {
		msgField.value = 'Bonjour, j’ai obtenu un score de ' + diag + '/100 au Document Health Check et je souhaite échanger sur un audit documentaire.';
	}
	var subjectField = $( '#cf7-subject' );
	var sujet = params.get( 'sujet' );
	if ( sujet && subjectField ) {
		$$( 'option', subjectField ).forEach( function ( o ) { if ( o.value === sujet ) subjectField.value = sujet; } );
	}

	/* ------------------------------------------------------------------
	 * Site search (search results template)
	 * ------------------------------------------------------------------ */
	var resultsBox = $( '#search-results' );
	if ( resultsBox && window.adaSearchIndex ) {
		var q = ( params.get( 's' ) || '' ).trim();
		var field = $( '#search-page-field' );
		if ( field ) field.value = q;
		var title = $( '#search-title' );
		var n = function ( s ) { return ( s || '' ).toLowerCase().normalize( 'NFD' ).replace( /[̀-ͯ]/g, '' ); };
		var esc = function ( s ) { return s.replace( /[&<>"]/g, function ( c ) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ c ]; } ); };
		if ( ! q ) {
			title.textContent = 'Rechercher sur le site';
			resultsBox.innerHTML = '<p>Saisissez un ou plusieurs mots-clés : GED, numérisation, conservation, OCR…</p>';
		} else {
			var terms = n( q ).split( /\s+/ ).filter( Boolean );
			var hits = window.adaSearchIndex.map( function ( p ) {
				var hay = n( p.t + ' ' + p.d + ' ' + p.c );
				var score = 0;
				terms.forEach( function ( t ) {
					if ( n( p.t ).indexOf( t ) !== -1 ) score += 10;
					if ( hay.indexOf( t ) !== -1 ) score += 1 + hay.split( t ).length / 10; else score -= 100;
				} );
				return { p: p, s: score };
			} ).filter( function ( h ) { return h.s > 0; } ).sort( function ( a, b ) { return b.s - a.s; } );
			title.textContent = hits.length + ' résultat' + ( hits.length > 1 ? 's' : '' ) + ' pour « ' + q + ' »';
			var root = settings.root || '';
			var hl = function ( s ) {
				var out = esc( s );
				terms.forEach( function ( t ) { if ( t.length > 2 ) out = out.replace( new RegExp( '(' + t.replace( /[.*+?^${}()|[\]\\]/g, '\\$&' ) + ')', 'gi' ), '<mark>$1</mark>' ); } );
				return out;
			};
			resultsBox.innerHTML = hits.length ? hits.map( function ( h ) {
				return '<article><div class="url">' + esc( h.p.u || 'accueil' ) + '</div><h2><a href="' + root + h.p.u + '">' + esc( h.p.t ) + '</a></h2><p>' + hl( h.p.d ) + '</p></article>';
			} ).join( '' ) : '<p>Aucun contenu ne correspond à votre recherche. Essayez un autre mot-clé ou consultez le <a href="' + root + 'plan-du-site/">plan du site</a>.</p>';
		}
	}

	/* Year */
	$$( '.current-year' ).forEach( function ( el ) { el.textContent = new Date().getFullYear(); } );
}() );
