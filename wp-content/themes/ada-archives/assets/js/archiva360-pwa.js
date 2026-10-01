/**
 * ARCHIVA360 — application installable (PWA).
 * Enregistre le service worker (hors connexion) et gère les boutons « Installer l'application » ([data-install]).
 */
( function () {
	'use strict';

	var script = document.currentScript;
	// Ce fichier est servi depuis wp-content/themes/ada-archives/assets/js/ : la racine du site est 5 niveaux au-dessus.
	var root = new URL( '../../../../../', script.src );
	var standalone = window.matchMedia( '(display-mode: standalone)' ).matches || window.navigator.standalone === true;
	var ios = /iphone|ipad|ipod/i.test( navigator.userAgent ) || ( navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1 );
	var deferred = null;

	if ( standalone ) document.documentElement.classList.add( 'is-standalone' );

	if ( 'serviceWorker' in navigator ) {
		window.addEventListener( 'load', function () {
			navigator.serviceWorker.register( new URL( 'archiva360/sw.js', root ).href, { scope: new URL( 'archiva360/', root ).href } ).catch( function () {} );
		} );
	}

	function buttons() { return document.querySelectorAll( '[data-install]' ); }
	function show( on ) { Array.prototype.forEach.call( buttons(), function ( b ) { b.hidden = ! on; } ); }

	function iosHelp() {
		if ( document.getElementById( 'install-help' ) ) return;
		var d = document.createElement( 'div' );
		d.id = 'install-help';
		d.className = 'install-help';
		d.setAttribute( 'role', 'dialog' );
		d.setAttribute( 'aria-modal', 'true' );
		d.setAttribute( 'aria-labelledby', 'install-help-title' );
		d.innerHTML = '<div class="install-help__card"><h2 id="install-help-title">Installer ARCHIVA360 sur l’iPhone</h2><ol>'
			+ '<li>Ouvrez cette page dans <b>Safari</b>.</li>'
			+ '<li>Touchez le bouton <b>Partager</b> <span aria-hidden="true">(carré avec une flèche vers le haut)</span>.</li>'
			+ '<li>Choisissez <b>Sur l’écran d’accueil</b>, puis <b>Ajouter</b>.</li></ol>'
			+ '<p>L’icône ARCHIVA360 apparaît sur votre écran d’accueil et s’ouvre en plein écran.</p>'
			+ '<button class="btn wide" type="button">J’ai compris</button></div>';
		document.body.appendChild( d );
		var close = function () { d.remove(); };
		d.querySelector( 'button' ).addEventListener( 'click', close );
		d.addEventListener( 'click', function ( e ) { if ( e.target === d ) close(); } );
		document.addEventListener( 'keydown', function esc( e ) { if ( e.key === 'Escape' ) { close(); document.removeEventListener( 'keydown', esc ); } } );
		d.querySelector( 'button' ).focus();
	}

	window.addEventListener( 'beforeinstallprompt', function ( e ) {
		e.preventDefault();
		deferred = e;
		show( true );
	} );
	window.addEventListener( 'appinstalled', function () {
		deferred = null;
		show( false );
	} );

	document.addEventListener( 'click', function ( e ) {
		var b = e.target.closest( '[data-install]' );
		if ( ! b ) return;
		e.preventDefault();
		if ( deferred ) {
			deferred.prompt();
			deferred.userChoice.then( function () { deferred = null; show( false ); } );
		} else if ( ios ) {
			iosHelp();
		}
	} );

	// Sur iPhone et iPad, Safari ne propose pas d'invite automatique : on affiche le mode d'emploi.
	if ( ios && ! standalone ) document.addEventListener( 'DOMContentLoaded', function () { show( true ); } );
}() );
