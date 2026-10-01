/**
 * ARCHIVA Academy — course player, quizzes, exams, certificates.
 * Progress is stored in the learner's browser (localStorage).
 */
( function () {
	'use strict';

	var KEY = 'ada_academy_v1';
	var $ = function ( s, c ) { return ( c || document ).querySelector( s ); };
	var $$ = function ( s, c ) { return Array.prototype.slice.call( ( c || document ).querySelectorAll( s ) ); };
	var esc = function ( s ) { return String( s ).replace( /[&<>"]/g, function ( c ) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ c ]; } ); };

	/* ---------------- storage ---------------- */
	function load() {
		var d = null;
		try { d = JSON.parse( localStorage.getItem( KEY ) ); } catch ( e ) {}
		if ( ! d || typeof d !== 'object' ) d = {};
		d.learner = d.learner || { name: '' };
		d.levels = d.levels || {};
		return d;
	}
	function save( d ) { try { localStorage.setItem( KEY, JSON.stringify( d ) ); return true; } catch ( e ) { return false; } }
	function level( d, slug ) {
		d.levels[ slug ] = d.levels[ slug ] || { lessons: {}, quizzes: {}, exam: null };
		return d.levels[ slug ];
	}
	var state = load();

	/* ---------------- helpers ---------------- */
	function normName( n ) { return String( n || '' ).normalize( 'NFC' ).trim().replace( /\s+/g, ' ' ).toUpperCase(); }
	function sha256hex( text ) {
		if ( ! window.crypto || ! crypto.subtle ) return Promise.reject( new Error( 'crypto' ) );
		return crypto.subtle.digest( 'SHA-256', new TextEncoder().encode( text ) ).then( function ( buf ) {
			return Array.prototype.map.call( new Uint8Array( buf ), function ( b ) { return ( '0' + b.toString( 16 ) ).slice( -2 ); } ).join( '' ).toUpperCase();
		} );
	}
	function certCode( name, slug, date, score ) {
		return sha256hex( [ 'ADA-ACADEMY', slug, normName( name ), date, String( score ) ].join( '|' ) ).then( function ( h ) {
			return h.slice( 0, 4 ) + '-' + h.slice( 4, 8 ) + '-' + h.slice( 8, 12 );
		} );
	}
	function today() {
		var d = new Date();
		return d.getFullYear() + '-' + ( '0' + ( d.getMonth() + 1 ) ).slice( -2 ) + '-' + ( '0' + d.getDate() ).slice( -2 );
	}
	function frDate( iso ) {
		var m = [ 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre' ];
		var p = String( iso ).split( '-' );
		return parseInt( p[ 2 ], 10 ) + ' ' + m[ parseInt( p[ 1 ], 10 ) - 1 ] + ' ' + p[ 0 ];
	}
	function shuffle( a ) {
		a = a.slice();
		for ( var i = a.length - 1; i > 0; i-- ) { var j = Math.floor( Math.random() * ( i + 1 ) ); var t = a[ i ]; a[ i ] = a[ j ]; a[ j ] = t; }
		return a;
	}
	function progressOf( slug, nModules ) {
		var lv = state.levels[ slug ];
		if ( ! lv ) return { pct: 0, done: 0, total: nModules * 2 + 1, passed: false, started: false };
		var done = 0;
		for ( var i = 0; i < nModules; i++ ) {
			if ( lv.lessons[ i ] ) done++;
			if ( lv.quizzes[ i ] && lv.quizzes[ i ].passed ) done++;
		}
		var passed = !! ( lv.exam && lv.exam.passed );
		if ( passed ) done++;
		var total = nModules * 2 + 1;
		return { pct: Math.round( done / total * 100 ), done: done, total: total, passed: passed, started: done > 0 };
	}

	/* ---------------- quiz rendering & grading ---------------- */
	function renderQuestions( form, questions, prefix ) {
		form.innerHTML = questions.map( function ( q, i ) {
			var type = q.t === 'multi' ? 'checkbox' : 'radio';
			var hint = q.t === 'multi' ? '<span class="quiz-q__hint">Plusieurs réponses possibles</span>' : '';
			return '<fieldset class="quiz-q" data-q="' + i + '"><legend><span class="quiz-q__num">' + ( i + 1 ) + '</span>' + esc( q.q ) + hint + '</legend>' +
				'<div class="quiz-q__options">' + q.o.map( function ( o, k ) {
					var id = prefix + '-' + i + '-' + k;
					return '<label class="quiz-opt" for="' + id + '"><input type="' + type + '" id="' + id + '" name="' + prefix + '-' + i + '" value="' + k + '"><span>' + esc( o ) + '</span></label>';
				} ).join( '' ) + '</div><div class="quiz-q__feedback" hidden></div></fieldset>';
		} ).join( '' ) +
			'<div class="quiz-actions"><button class="button" type="submit">Valider mes réponses</button><p class="quiz-msg" aria-live="polite"></p></div><div class="quiz-result" hidden></div>';
	}
	function grade( form, questions ) {
		var score = 0, unanswered = 0;
		var answers = questions.map( function ( q, i ) {
			var chosen = $$( 'input:checked', $( '[data-q="' + i + '"]', form ) ).map( function ( x ) { return parseInt( x.value, 10 ); } ).sort();
			if ( ! chosen.length ) unanswered++;
			var good = q.a.slice().sort();
			var ok = chosen.length === good.length && chosen.every( function ( v, k ) { return v === good[ k ]; } );
			if ( ok ) score++;
			return { chosen: chosen, ok: ok };
		} );
		return { score: score, total: questions.length, unanswered: unanswered, answers: answers };
	}
	function showFeedback( form, questions, res ) {
		res.answers.forEach( function ( a, i ) {
			var q = questions[ i ];
			var fs = $( '[data-q="' + i + '"]', form );
			fs.classList.toggle( 'is-correct', a.ok );
			fs.classList.toggle( 'is-wrong', ! a.ok );
			$$( '.quiz-opt', fs ).forEach( function ( lab, k ) {
				lab.classList.toggle( 'is-answer', q.a.indexOf( k ) !== -1 );
				lab.classList.toggle( 'is-chosen-wrong', a.chosen.indexOf( k ) !== -1 && q.a.indexOf( k ) === -1 );
			} );
			var fb = $( '.quiz-q__feedback', fs );
			fb.hidden = false;
			fb.innerHTML = '<strong>' + ( a.ok ? 'Bonne réponse.' : 'Réponse attendue : ' + q.a.map( function ( k ) { return esc( q.o[ k ] ); } ).join( ', ' ) + '.' ) + '</strong> ' + esc( q.e );
		} );
	}
	function lockForm( form, locked ) { $$( 'input', form ).forEach( function ( x ) { x.disabled = locked; } ); }

	/* ---------------- catalogue page ---------------- */
	function initCatalogue() {
		var cards = $$( '.course-card[data-level]' );
		if ( ! cards.length ) return;
		var nameInput = $( '#learner-name' );
		function paint() {
			var passed = 0, started = 0;
			cards.forEach( function ( c ) {
				var p = progressOf( c.getAttribute( 'data-level' ), parseInt( c.getAttribute( 'data-modules' ) || '4', 10 ) );
				$( '[data-bar]', c ).style.width = p.pct + '%';
				$( '[data-progress-label]', c ).textContent = p.pct + ' % terminé';
				var st = $( '[data-status]', c );
				st.textContent = p.passed ? 'Certifié' : ( p.started ? 'En cours' : 'Non commencé' );
				st.className = 'course-status' + ( p.passed ? ' is-passed' : ( p.started ? ' is-started' : '' ) );
				var cta = $( '[data-cta]', c );
				cta.firstChild.textContent = p.passed ? 'Revoir ' : ( p.started ? 'Continuer ' : 'Commencer ' );
				if ( p.passed ) passed++;
				if ( p.started ) started++;
			} );
			var n = state.learner.name;
			if ( nameInput && ! nameInput.value ) nameInput.value = n || '';
			$( '#learner-greeting' ).textContent = n ? 'Bonjour ' + n : 'Bienvenue dans l’Academy';
			$( '#learner-summary' ).textContent = n
				? ( passed + ' certificat' + ( passed > 1 ? 's' : '' ) + ' obtenu' + ( passed > 1 ? 's' : '' ) + ', ' + started + ' parcours commencé' + ( started > 1 ? 's' : '' ) + ' sur ' + cards.length + '. Votre progression est enregistrée dans ce navigateur.' )
				: 'Votre progression est enregistrée dans ce navigateur. Indiquez votre nom tel qu’il doit figurer sur vos certificats.';
		}
		var form = $( '#learner-form' );
		if ( form ) form.addEventListener( 'submit', function ( e ) {
			e.preventDefault();
			state.learner.name = nameInput.value.trim().replace( /\s+/g, ' ' );
			save( state );
			paint();
		} );
		paint();
	}

	/* ---------------- course player ---------------- */
	function initCourse() {
		var root = $( '#course' );
		var dataEl = $( '#course-data' );
		if ( ! root || ! dataEl ) return;
		var C = JSON.parse( dataEl.textContent );
		var slug = C.slug;
		var nM = C.modules.length;
		var week = C.unit === 'Semaine';
		var views = $$( '[data-view-id]', root );

		function lv() { return level( state, slug ); }

		function paintNav() {
			var L = state.levels[ slug ] || { lessons: {}, quizzes: {}, exam: null };
			for ( var i = 0; i < nM; i++ ) {
				var ls = $( '[data-state="lesson-' + i + '"]', root );
				ls.className = 'course-nav__state' + ( L.lessons[ i ] ? ' is-done' : '' );
				var qz = $( '[data-state="quiz-' + i + '"]', root );
				var q = L.quizzes[ i ];
				qz.className = 'course-nav__state' + ( q ? ( q.passed ? ' is-done' : ' is-failed' ) : '' );
				qz.title = q ? 'Meilleur score : ' + q.best + ' / ' + q.total : '';
			}
			var ex = $( '[data-state="exam"]', root );
			ex.className = 'course-nav__state' + ( L.exam ? ( L.exam.passed ? ' is-done' : ' is-failed' ) : ( allQuizzesPassed() ? '' : ' is-locked' ) );
			var p = progressOf( slug, nM );
			$( '#course-bar' ).style.width = p.pct + '%';
			$( '#course-progress-label' ).textContent = p.pct + ' % terminé' + ( p.passed ? ' · certifié' : '' );
			var resume = $( '[data-resume]', root );
			if ( resume ) {
				var next = firstTodo();
				resume.setAttribute( 'href', '#' + next );
				resume.firstChild.textContent = p.started ? 'Reprendre où j’en étais ' : ( week ? 'Commencer la semaine 1 ' : 'Commencer le module 1 ' );
			}
		}
		function allQuizzesPassed() {
			var L = state.levels[ slug ];
			if ( ! L ) return false;
			for ( var i = 0; i < nM; i++ ) if ( ! ( L.quizzes[ i ] && L.quizzes[ i ].passed ) ) return false;
			return true;
		}
		function firstTodo() {
			var L = state.levels[ slug ] || { lessons: {}, quizzes: {} };
			for ( var i = 0; i < nM; i++ ) {
				if ( ! L.lessons[ i ] ) return 'm' + ( i + 1 );
				if ( ! ( L.quizzes[ i ] && L.quizzes[ i ].passed ) ) return 'm' + ( i + 1 ) + '-quiz';
			}
			return 'examen';
		}

		function show( id ) {
			var target = views.filter( function ( v ) { return v.getAttribute( 'data-view-id' ) === id; } )[ 0 ] || views[ 0 ];
			id = target.getAttribute( 'data-view-id' );
			views.forEach( function ( v ) { v.hidden = v !== target; } );
			$$( '.course-nav a[data-view]', root ).forEach( function ( a ) { a.classList.toggle( 'is-current', a.getAttribute( 'data-view' ) === id ); a.setAttribute( 'aria-current', a.getAttribute( 'data-view' ) === id ? 'page' : 'false' ); } );
			var m = /^m(\d+)$/.exec( id );
			if ( m ) { lv().lessons[ parseInt( m[ 1 ], 10 ) - 1 ] = true; save( state ); }
			if ( id === 'examen' ) prepareExam();
			paintNav();
		}
		function route( scroll ) {
			show( ( location.hash || '#intro' ).slice( 1 ) );
			if ( scroll ) {
				var top = root.getBoundingClientRect().top + window.pageYOffset - 110;
				if ( window.pageYOffset > top ) window.scrollTo( 0, top );
			}
		}
		window.addEventListener( 'hashchange', function () { route( true ); } );

		// Module quizzes
		$$( '[data-quiz-form]', root ).forEach( function ( form ) {
			var idx = parseInt( form.getAttribute( 'data-quiz-form' ), 10 );
			var qs = C.modules[ idx ].quiz;
			renderQuestions( form, qs, slug + '-q' + idx );
			form.addEventListener( 'submit', function ( e ) {
				e.preventDefault();
				var resBox = $( '.quiz-result', form );
				if ( form.classList.contains( 'is-graded' ) ) { // retry
					form.classList.remove( 'is-graded' );
					renderQuestions( form, qs, slug + '-q' + idx );
					return;
				}
				var r = grade( form, qs );
				var msg = $( '.quiz-msg', form );
				if ( r.unanswered ) { msg.textContent = 'Répondez à toutes les questions (' + r.unanswered + ' sans réponse).'; return; }
				msg.textContent = '';
				showFeedback( form, qs, r );
				lockForm( form, true );
				var pct = Math.round( r.score / r.total * 100 );
				var passed = pct >= C.quizPass;
				var L = lv();
				var prev = L.quizzes[ idx ];
				L.quizzes[ idx ] = { best: Math.max( r.score, prev ? prev.best : 0 ), total: r.total, passed: passed || !! ( prev && prev.passed ), date: today() };
				L.lessons[ idx ] = true;
				save( state );
				form.classList.add( 'is-graded' );
				$( 'button[type=submit]', form ).textContent = 'Recommencer le quiz';
				var next = idx + 1 < nM ? '#m' + ( idx + 2 ) : '#examen';
				var nextLabel = idx + 1 < nM ? ( week ? 'Semaine suivante' : 'Module suivant' ) : 'Aller à l’examen final';
				resBox.hidden = false;
				resBox.className = 'quiz-result ' + ( passed ? 'is-pass' : 'is-fail' );
				resBox.innerHTML = '<p class="quiz-result__score">' + r.score + ' / ' + r.total + ' <span>(' + pct + ' %)</span></p><p>' +
					( passed ? ( week ? 'Semaine validée. Bravo !' : 'Module validé. Bravo !' ) : 'Pas encore : il faut ' + C.quizPass + ' %. Relisez la leçon puis recommencez.' ) + '</p>' +
					'<div class="wp-block-buttons">' + ( passed ? '<div class="wp-block-button"><a class="wp-block-button__link" href="' + next + '">' + nextLabel + '</a></div>' : '<div class="wp-block-button is-style-outline"><a class="wp-block-button__link" href="#m' + ( idx + 1 ) + '">Relire la leçon</a></div>' ) + '</div>';
				paintNav();
				resBox.scrollIntoView( { block: 'nearest' } );
			} );
		} );

		$$( '[data-mark-read]', root ).forEach( function ( b ) {
			b.addEventListener( 'click', function () {
				lv().lessons[ parseInt( b.getAttribute( 'data-mark-read' ), 10 ) ] = true;
				save( state );
				b.textContent = 'Leçon lue';
				b.disabled = true;
				paintNav();
			} );
		} );

		// Final exam
		var examForm = $( '#exam-form' ), examQs = null;
		function prepareExam() {
			var ok = allQuizzesPassed();
			$( '#exam-locked' ).hidden = ok;
			$( '#exam-ready' ).hidden = ! ok || ! examForm.hidden || ! $( '#exam-result' ).hidden;
			if ( ! ok ) {
				var L = state.levels[ slug ] || { quizzes: {} };
				var missing = [];
				for ( var i = 0; i < nM; i++ ) if ( ! ( L.quizzes[ i ] && L.quizzes[ i ].passed ) ) missing.push( '<a href="#m' + ( i + 1 ) + '-quiz">quiz ' + ( i + 1 ) + '</a>' );
				$( '#exam-missing' ).innerHTML = 'À valider : ' + missing.join( ', ' ) + '.';
			}
		}
		$( '#exam-start' ).addEventListener( 'click', function () {
			var pool = [];
			C.modules.forEach( function ( m ) { pool = pool.concat( m.quiz ); } );
			pool = pool.concat( C.examExtra );
			examQs = shuffle( pool ).slice( 0, C.examSize );
			renderQuestions( examForm, examQs, slug + '-exam' );
			var nameField = state.learner.name ? '' : '<div class="quiz-name"><label for="exam-name">Nom et prénom pour le certificat</label><input id="exam-name" autocomplete="name" maxlength="80" required></div>';
			$( '.quiz-actions', examForm ).insertAdjacentHTML( 'beforebegin', nameField );
			$( 'button[type=submit]', examForm ).textContent = 'Terminer l’examen';
			examForm.hidden = false;
			$( '#exam-ready' ).hidden = true;
			$( '#exam-result' ).hidden = true;
			examForm.scrollIntoView( { block: 'start' } );
		} );
		examForm.addEventListener( 'submit', function ( e ) {
			e.preventDefault();
			var msg = $( '.quiz-msg', examForm );
			var nameInput = $( '#exam-name', examForm );
			if ( nameInput ) {
				if ( ! nameInput.value.trim() ) { msg.textContent = 'Indiquez votre nom pour le certificat.'; nameInput.focus(); return; }
				state.learner.name = nameInput.value.trim().replace( /\s+/g, ' ' );
			}
			var r = grade( examForm, examQs );
			if ( r.unanswered ) { msg.textContent = 'Répondez à toutes les questions (' + r.unanswered + ' sans réponse).'; return; }
			showFeedback( examForm, examQs, r );
			lockForm( examForm, true );
			$( '.quiz-actions', examForm ).hidden = true;
			var pct = Math.round( r.score / r.total * 100 );
			var passed = pct >= C.examPass;
			var L = lv();
			var date = today();
			var box = $( '#exam-result' );
			function finish( code ) {
				var prev = L.exam;
				if ( passed && ( ! prev || ! prev.passed || pct >= prev.score ) ) {
					L.exam = { passed: true, score: pct, date: date, code: code, name: state.learner.name, attempts: ( prev ? prev.attempts || 1 : 0 ) + 1 };
				} else if ( ! prev || ! prev.passed ) {
					L.exam = { passed: false, score: pct, date: date, attempts: ( prev ? prev.attempts || 1 : 0 ) + 1 };
				} else {
					prev.attempts = ( prev.attempts || 1 ) + 1;
				}
				save( state );
				box.hidden = false;
				box.className = 'quiz-result ' + ( passed ? 'is-pass' : 'is-fail' );
				box.innerHTML = '<p class="quiz-result__score">' + r.score + ' / ' + r.total + ' <span>(' + pct + ' %)</span></p>' +
					( passed ? '<p><strong>Félicitations, vous avez réussi : ' + esc( C.label || ( 'Niveau ' + C.num + ' — ' + C.title ) ) + '.</strong> Votre certificat est prêt.</p>' +
						'<div class="wp-block-buttons"><div class="wp-block-button"><a class="wp-block-button__link" href="' + $( '#cert-link' ).getAttribute( 'href' ) + '#' + slug + '">Voir mon certificat</a></div></div>'
						: '<p>Il faut ' + C.examPass + ' % pour réussir. Revoyez les corrections ci-dessus, puis repassez l’examen : les questions seront tirées à nouveau.</p>' +
						'<div class="wp-block-buttons"><div class="wp-block-button"><button class="wp-block-button__link" type="button" id="exam-retry">Repasser l’examen</button></div></div>' );
				var retry = $( '#exam-retry' );
				if ( retry ) retry.addEventListener( 'click', function () { examForm.hidden = true; box.hidden = true; $( '#exam-start' ).click(); } );
				paintNav();
				box.scrollIntoView( { block: 'nearest' } );
			}
			if ( passed ) certCode( state.learner.name, slug, date, pct ).then( finish, function () { finish( '' ); } );
			else finish( '' );
		} );

		route( false );
	}

	/* ---------------- certificates ---------------- */
	function initCertificates() {
		var list = $( '#cert-list' );
		var levelsEl = $( '#levels-data' );
		if ( ! list || ! levelsEl ) return;
		var LV = JSON.parse( levelsEl.textContent );
		var earned = Object.keys( LV ).filter( function ( s ) { var l = state.levels[ s ]; return l && l.exam && l.exam.passed; } );
		$( '#cert-empty' ).hidden = earned.length > 0;
		list.innerHTML = earned.map( function ( s ) {
			var e = state.levels[ s ].exam;
			return '<a class="cert-chip" href="#' + s + '" data-cert="' + s + '"><b>' + esc( LV[ s ].short || ( 'Niveau ' + LV[ s ].num ) ) + '</b><span>' + esc( LV[ s ].short === LV[ s ].title ? '12 semaines' : LV[ s ].title ) + '</span><small>' + frDate( e.date ) + ' · ' + e.score + ' %</small></a>';
		} ).join( '' );
		function view() {
			var s = location.hash.slice( 1 );
			if ( earned.indexOf( s ) === -1 ) s = earned[ 0 ];
			if ( ! s ) { $( '#cert-view' ).hidden = true; return; }
			$$( '[data-cert]', list ).forEach( function ( a ) { a.classList.toggle( 'is-current', a.getAttribute( 'data-cert' ) === s ); } );
			var e = state.levels[ s ].exam;
			$( '#cert-view' ).hidden = false;
			$( '#certificate' ).innerHTML =
				'<div class="certificate__inner"><div class="certificate__brand"><svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="10" fill="#0A1541"/><path d="M13 35 24 11l11 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M17.4 26.5h13.2" stroke="#006EEF" stroke-width="3.4" stroke-linecap="round"/><rect x="31" y="31" width="6" height="6" rx="1.2" fill="#006EEF"/></svg><span>ARCHIVA Academy<small>African Digital Archives</small></span></div>' +
				'<p class="certificate__kicker">Certificat de réussite</p><p class="certificate__lead">décerné à</p><p class="certificate__name">' + esc( e.name ) + '</p>' +
				'<p class="certificate__lead">pour la réussite de l’examen final du</p><p class="certificate__level">' + esc( LV[ s ].label || ( 'Niveau ' + LV[ s ].num + ' — ' + LV[ s ].title ) ) + '</p>' +
				'<div class="certificate__meta"><div><span>Date</span><b>' + frDate( e.date ) + '</b></div><div><span>Score</span><b>' + e.score + ' %</b></div><div><span>Code de vérification</span><b class="certificate__code">' + esc( e.code ) + '</b></div></div>' +
				'<p class="certificate__foot">Certificat interne ARCHIVA Academy. Vérification : ' + esc( location.origin + location.pathname.replace( /certificat\/(index\.html)?$/, 'verifier/' ) ) + '</p></div>';
		}
		window.addEventListener( 'hashchange', view );
		view();
		var pr = $( '#cert-print' );
		if ( pr ) pr.addEventListener( 'click', function () { window.print(); } );
		var cp = $( '#cert-copy' );
		if ( cp ) cp.addEventListener( 'click', function () {
			var code = $( '.certificate__code' ).textContent;
			var done = function ( ok ) { $( '#cert-copy-msg' ).textContent = ok ? 'Code copié.' : 'Copie impossible : sélectionnez le code dans le certificat.'; };
			try { navigator.clipboard.writeText( code ).then( function () { done( true ); }, function () { done( false ); } ); } catch ( e ) { done( false ); }
		} );
	}

	/* ---------------- verification ---------------- */
	function initVerify() {
		var form = $( '#verify-form' );
		if ( ! form ) return;
		form.addEventListener( 'submit', function ( e ) {
			e.preventDefault();
			var out = $( '#verify-result' );
			var name = $( '#v-name' ).value, slug = $( '#v-level' ).value, date = $( '#v-date' ).value, score = $( '#v-score' ).value, code = $( '#v-code' ).value.trim().toUpperCase();
			if ( ! name.trim() || ! date || score === '' || ! code ) { out.innerHTML = '<div class="notice is-warning"><p>Renseignez tous les champs.</p></div>'; return; }
			certCode( name, slug, date, parseInt( score, 10 ) ).then( function ( expected ) {
				var ok = expected === code.replace( /\s/g, '' );
				out.innerHTML = ok
					? '<div class="notice is-success"><p><strong>Certificat authentique.</strong> Le code correspond au nom, au niveau, à la date et au score indiqués.</p></div>'
					: '<div class="notice is-warning"><p><strong>Le code ne correspond pas.</strong> Vérifiez l’orthographe du nom, la date et le score. Si le problème persiste, le certificat a pu être modifié.</p></div>';
			}, function () { out.innerHTML = '<div class="notice is-warning"><p>Votre navigateur ne permet pas le calcul de vérification.</p></div>'; } );
		} );
	}

	initCatalogue();
	initCourse();
	initCertificates();
	initVerify();
}() );
