/**
 * ARCHIVA360 — démo interactive.
 * Application autonome : toutes les données restent dans le navigateur (IndexedDB).
 */
( function () {
	'use strict';

	/* =====================================================================
	 * Utilities
	 * ===================================================================== */
	var $ = function ( s, c ) { return ( c || document ).querySelector( s ); };
	var $$ = function ( s, c ) { return Array.prototype.slice.call( ( c || document ).querySelectorAll( s ) ); };
	var esc = function ( s ) { return String( s == null ? '' : s ).replace( /[&<>"']/g, function ( c ) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ c ]; } ); };
	var norm = function ( s ) { return String( s || '' ).toLowerCase().normalize( 'NFD' ).replace( /[̀-ͯ]/g, '' ); };
	var pad = function ( n, l ) { n = String( n ); while ( n.length < ( l || 2 ) ) n = '0' + n; return n; };
	function todayISO() { var d = new Date(); return d.getFullYear() + '-' + pad( d.getMonth() + 1 ) + '-' + pad( d.getDate() ); }
	function nowISO() { return new Date().toISOString(); }
	function addYears( iso, y ) { var p = iso.split( '-' ); return ( parseInt( p[ 0 ], 10 ) + y ) + '-' + p[ 1 ] + '-' + p[ 2 ]; }
	function addDays( iso, n ) { var d = new Date( iso + 'T12:00:00' ); d.setDate( d.getDate() + n ); return d.getFullYear() + '-' + pad( d.getMonth() + 1 ) + '-' + pad( d.getDate() ); }
	function frDate( iso ) { if ( ! iso ) return '—'; var p = iso.slice( 0, 10 ).split( '-' ); return p[ 2 ] + '/' + p[ 1 ] + '/' + p[ 0 ]; }
	function frDateTime( iso ) { var d = new Date( iso ); return frDate( d.getFullYear() + '-' + pad( d.getMonth() + 1 ) + '-' + pad( d.getDate() ) ) + ' ' + pad( d.getHours() ) + ':' + pad( d.getMinutes() ); }
	function fcfa( n ) { if ( n === '' || n == null || isNaN( n ) ) return '—'; return Number( n ).toLocaleString( 'fr-FR' ).replace( / | /g, ' ' ) + ' FCFA'; }
	function size( b ) { return b < 1024 ? b + ' o' : b < 1048576 ? ( b / 1024 ).toFixed( 1 ).replace( '.', ',' ) + ' Ko' : ( b / 1048576 ).toFixed( 1 ).replace( '.', ',' ) + ' Mo'; }
	function hex( buf ) { return Array.prototype.map.call( new Uint8Array( buf ), function ( b ) { return ( '0' + b.toString( 16 ) ).slice( -2 ); } ).join( '' ).toUpperCase(); }
	function sha256( data ) {
		var bytes = typeof data === 'string' ? new TextEncoder().encode( data ) : data;
		return crypto.subtle.digest( 'SHA-256', bytes ).then( hex );
	}
	function b64( buf ) { var s = '', a = new Uint8Array( buf ); for ( var i = 0; i < a.length; i += 0x8000 ) s += String.fromCharCode.apply( null, a.subarray( i, i + 0x8000 ) ); return btoa( s ); }
	function unb64( s ) { var bin = atob( s ), a = new Uint8Array( bin.length ); for ( var i = 0; i < bin.length; i++ ) a[ i ] = bin.charCodeAt( i ); return a.buffer; }
	function ext( name, mime ) {
		var e = ( /\.([a-z0-9]+)$/i.exec( name || '' ) || [] )[ 1 ];
		e = ( e || '' ).toLowerCase();
		if ( mime === 'application/pdf' || e === 'pdf' ) return 'pdf';
		if ( /^image\//.test( mime ) ) return 'img';
		if ( /docx?|odt|rtf/.test( e ) ) return 'doc';
		if ( /xlsx?|ods|csv/.test( e ) ) return 'xls';
		return 'txt';
	}
	function icon( name ) {
		var P = {
			chart: '<path d="M4 20V4M4 20h16"/><path d="M8 16v-5M12 16V8M16 16v-8"/>', files: '<path d="M15 3H9a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V7z"/><path d="M15 3v4h4"/><path d="M5 7v12a2 2 0 0 0 2 2h8"/>',
			search: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>', clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', box: '<path d="M21 8l-9-5-9 5v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
			hourglass: '<path d="M6 3h12M6 21h12M7 3c0 5 10 6 10 9s-10 4-10 9M17 3c0 5-10 6-10 9s10 4 10 9"/>', eye: '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
			shield: '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>', users: '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
			drive: '<path d="M22 12H2M5.5 5h13L22 12v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6z"/><path d="M6 16h.01M10 16h.01"/>', upload: '<path d="M12 20V9M7 14l5-5 5 5M4 4h16"/>', download: '<path d="M12 4v11M7 10l5 5 5-5M4 20h16"/>',
			check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>', lock: '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>', finger: '<path d="M12 11v3a8 8 0 0 1-1.5 5M8.5 7.5A5 5 0 0 1 17 11v2a13 13 0 0 1-.6 4M7 11a5 5 0 0 1 .3-1.8M7 14.5a11 11 0 0 1-1.2 3.5M4 10a8 8 0 0 1 14.5-4.5M20 11v1.5"/>',
			archive: '<rect x="3" y="4" width="18" height="5" rx="1"/><path d="M5 9v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9M10 13h4"/>', sparkles: '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>', layers: '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>', home: '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>'
		};
		return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ( P[ name ] || '' ) + '</svg>';
	}
	var toastTimer;
	function toast( msg ) {
		var t = $( '#toast' );
		t.textContent = msg; t.hidden = false;
		clearTimeout( toastTimer );
		toastTimer = setTimeout( function () { t.hidden = true; }, 3200 );
	}
	function loadScript( src ) {
		return new Promise( function ( res, rej ) {
			if ( document.querySelector( 'script[src="' + src + '"]' ) ) return res();
			var s = document.createElement( 'script' ); s.src = src; s.onload = res; s.onerror = function () { rej( new Error( 'Chargement impossible : ' + src ) ); };
			document.head.appendChild( s );
		} );
	}

	/* =====================================================================
	 * Storage (IndexedDB with in-memory fallback)
	 * ===================================================================== */
	var DBNAME = 'ada-archiva360-demo';
	var store = {
		db: null, mem: { kv: {}, files: {} }, persistent: false,
		open: function () {
			var self = this;
			return new Promise( function ( res ) {
				try {
					var r = indexedDB.open( DBNAME, 1 );
					r.onupgradeneeded = function () { r.result.createObjectStore( 'kv' ); r.result.createObjectStore( 'files' ); };
					r.onsuccess = function () { self.db = r.result; self.persistent = true; res(); };
					r.onerror = function () { res(); };
				} catch ( e ) { res(); }
			} );
		},
		tx: function ( name, mode, fn ) {
			var self = this;
			if ( ! self.db ) return Promise.resolve( fn( null ) );
			return new Promise( function ( res, rej ) {
				var t = self.db.transaction( name, mode ), os = t.objectStore( name ), out;
				var r = fn( os );
				if ( r ) r.onsuccess = function () { out = r.result; };
				t.oncomplete = function () { res( out ); };
				t.onerror = function () { rej( t.error ); };
			} );
		},
		get: function ( s, k ) { var m = this.mem; return this.db ? this.tx( s, 'readonly', function ( os ) { return os.get( k ); } ) : Promise.resolve( m[ s ][ k ] ); },
		put: function ( s, k, v ) { var m = this.mem; if ( ! this.db ) { m[ s ][ k ] = v; return Promise.resolve(); } return this.tx( s, 'readwrite', function ( os ) { return os.put( v, k ); } ); },
		del: function ( s, k ) { var m = this.mem; if ( ! this.db ) { delete m[ s ][ k ]; return Promise.resolve(); } return this.tx( s, 'readwrite', function ( os ) { return os.delete( k ); } ); },
		clear: function () { var self = this; self.mem = { kv: {}, files: {} }; if ( ! self.db ) return Promise.resolve(); return self.tx( 'kv', 'readwrite', function ( os ) { return os.clear(); } ).then( function () { return self.tx( 'files', 'readwrite', function ( os ) { return os.clear(); } ); } ); }
	};

	/* =====================================================================
	 * Reference data
	 * ===================================================================== */
	var ROLES = {
		admin: { label: 'Administrateur (organisation)', perms: [ 'upload', 'edit', 'editAny', 'archive', 'eliminate', 'hold', 'boxes', 'rules', 'users', 'backup', 'confidential', 'audit', 'delete', 'tamper' ] },
		archiviste: { label: 'Archiviste', perms: [ 'upload', 'edit', 'editAny', 'archive', 'eliminate', 'hold', 'boxes', 'backup', 'confidential', 'audit', 'delete', 'tamper' ] },
		records: { label: 'Records manager', perms: [ 'upload', 'edit', 'editAny', 'rules', 'confidential', 'audit', 'hold' ] },
		employe: { label: 'Employé', perms: [ 'upload', 'edit' ] },
		auditeur: { label: 'Auditeur (lecture)', perms: [ 'confidential', 'audit' ] }
	};
	var CONF = [ 'Public', 'Interne', 'Confidentiel', 'Secret' ];
	var FINALS = [ 'Destruction', 'Conservation définitive', 'Examen' ];
	var TRIGGERS = { date: 'Date du document', 'field:echeance': 'Échéance du contrat', 'field:depart': 'Départ de l’agent', archive: 'Date d’archivage' };

	function seedState() {
		var series = [
			{ code: 'DG.01', fn: 'Direction générale', label: 'Procès-verbaux et délibérations' },
			{ code: 'FIN.01', fn: 'Direction financière', label: 'Factures fournisseurs' },
			{ code: 'FIN.02', fn: 'Direction financière', label: 'États financiers' },
			{ code: 'RH.01', fn: 'Ressources humaines', label: 'Dossiers du personnel' },
			{ code: 'JUR.01', fn: 'Juridique', label: 'Contrats' },
			{ code: 'JUR.02', fn: 'Juridique', label: 'Contentieux' },
			{ code: 'TEC.01', fn: 'Technique', label: 'Plans et rapports techniques' },
			{ code: 'COU.01', fn: 'Secrétariat', label: 'Courrier' },
			{ code: 'HIS.01', fn: 'Archives', label: 'Archives historiques' }
		];
		var rules = [
			{ id: 'r-compta', label: 'Pièces comptables', years: 10, trigger: 'date', final: 'Destruction' },
			{ id: 'r-contrat', label: 'Contrats', years: 10, trigger: 'field:echeance', final: 'Examen' },
			{ id: 'r-pv', label: 'Procès-verbaux des instances', years: null, trigger: 'date', final: 'Conservation définitive' },
			{ id: 'r-rh', label: 'Dossiers du personnel', years: 5, trigger: 'field:depart', final: 'Destruction' },
			{ id: 'r-tech', label: 'Plans et dossiers techniques', years: 30, trigger: 'date', final: 'Examen' },
			{ id: 'r-courrier', label: 'Courrier courant', years: 5, trigger: 'date', final: 'Destruction' },
			{ id: 'r-perm', label: 'Archives historiques', years: null, trigger: 'date', final: 'Conservation définitive' }
		];
		var types = [
			{ id: 'facture', label: 'Facture', series: 'FIN.01', rule: 'r-compta', fields: [ { k: 'fournisseur', l: 'Fournisseur', req: 1 }, { k: 'numero', l: 'Numéro de facture', req: 1 }, { k: 'montant', l: 'Montant TTC (FCFA)', req: 1, num: 1 } ] },
			{ id: 'contrat', label: 'Contrat', series: 'JUR.01', rule: 'r-contrat', fields: [ { k: 'parties', l: 'Parties', req: 1 }, { k: 'echeance', l: 'Date d’échéance', req: 1, date: 1 }, { k: 'montant', l: 'Montant (FCFA)', num: 1 } ] },
			{ id: 'pv', label: 'Procès-verbal', series: 'DG.01', rule: 'r-pv', fields: [ { k: 'instance', l: 'Instance', req: 1 } ] },
			{ id: 'personnel', label: 'Dossier du personnel', series: 'RH.01', rule: 'r-rh', fields: [ { k: 'matricule', l: 'Matricule', req: 1 }, { k: 'agent', l: 'Agent', req: 1 }, { k: 'depart', l: 'Date de départ', date: 1 } ] },
			{ id: 'etats', label: 'États financiers', series: 'FIN.02', rule: 'r-compta', fields: [ { k: 'exercice', l: 'Exercice', req: 1 } ] },
			{ id: 'plan', label: 'Plan / rapport technique', series: 'TEC.01', rule: 'r-tech', fields: [ { k: 'ouvrage', l: 'Ouvrage', req: 1 } ] },
			{ id: 'courrier', label: 'Courrier', series: 'COU.01', rule: 'r-courrier', fields: [ { k: 'correspondant', l: 'Correspondant', req: 1 }, { k: 'sens', l: 'Sens (entrant / sortant)' } ] },
			{ id: 'historique', label: 'Archive historique', series: 'HIS.01', rule: 'r-perm', fields: [ { k: 'periode', l: 'Période' } ] },
			{ id: 'autre', label: 'Autre document', series: 'COU.01', rule: 'r-courrier', fields: [] }
		];
		var users = [
			{ id: 'u1', name: 'Awa Koné', role: 'archiviste', service: 'Archives' },
			{ id: 'u2', name: 'Jean Kouassi', role: 'employe', service: 'Juridique' },
			{ id: 'u3', name: 'Marie Diallo', role: 'employe', service: 'Comptabilité' },
			{ id: 'u4', name: 'Koffi Yao', role: 'admin', service: 'Direction des systèmes d’information' },
			{ id: 'u5', name: 'Fatou Traoré', role: 'records', service: 'Archives' },
			{ id: 'u6', name: 'Auditeur externe', role: 'auditeur', service: 'Cabinet d’audit' }
		];
		var boxes = [
			{ id: 'CI-ABJ-PLT-2026-000457', site: 'Abidjan', bat: 'B', salle: '03', rayon: '12', etagere: '04', boite: '457', contents: 'Contrats fournisseurs et maintenance (originaux signés)', service: 'Direction juridique', status: 'En rayon', moves: [] },
			{ id: 'CI-ABJ-PLT-2026-000458', site: 'Abidjan', bat: 'B', salle: '03', rayon: '12', etagere: '05', boite: '458', contents: 'Factures fournisseurs 2016 (originaux)', service: 'Comptabilité', status: 'En rayon', moves: [] }
		];
		return { v: 1, org: 'Organisation démo', seq: 100, certSeq: 0, current: 'u1', series: series, rules: rules, types: types, users: users, boxes: boxes, docs: [], audit: [], certificates: [], lastBackup: null, created: nowISO() };
	}

	var SAMPLES = [
		{ title: 'Facture FAC-0045 — ABC SA', type: 'facture', date: '2023-04-12', conf: 'Interne', status: 'Archivé', meta: { fournisseur: 'ABC SA', numero: 'FAC-0045', montant: 4500000 }, file: 'Facture_2023_0045.txt', by: 'u3',
			text: 'ABC SA\nZone industrielle de Yopougon, Abidjan\n\nFACTURE N° FAC-0045\nDate : 12/04/2023\nClient : Organisation démo — Direction financière\nRéf. commande : BC-2023-118\n\nRayonnages mobiles d’archives ........ 2 400 000\nBoîtes de conservation neutres ....... 900 000\nInstallation et transport ............ 513 559\n\nTotal HT : 3 813 559 FCFA\nTVA 18 % : 686 441 FCFA\nTotal TTC : 4 500 000 FCFA' },
		{ title: 'Facture FAC-0092 — SOTRA Équipements', type: 'facture', date: '2025-11-03', conf: 'Interne', status: 'Actif', meta: { fournisseur: 'SOTRA Équipements', numero: 'FAC-0092', montant: 12800000 }, file: 'Facture_2025_0092.txt', by: 'u3',
			text: 'SOTRA ÉQUIPEMENTS\nFACTURE N° FAC-0092\nDate : 03/11/2025\nScanners de production A3 (2 unités)\nTotal TTC : 12 800 000 FCFA' },
		{ title: 'Facture F-2016-311 — Imprimerie du Plateau', type: 'facture', date: '2016-05-18', conf: 'Interne', status: 'Archivé', meta: { fournisseur: 'Imprimerie du Plateau', numero: 'F-2016-311', montant: 6120000 }, file: 'Facture_2016_311.txt', by: 'u3', box: 'CI-ABJ-PLT-2026-000458',
			text: 'IMPRIMERIE DU PLATEAU\nFacture F-2016-311 du 18/05/2016\nImpression des rapports annuels 2015\nTotal TTC : 6 120 000 FCFA' },
		{ title: 'Facture 2016-077 — Bâtir CI', type: 'facture', date: '2016-09-02', conf: 'Interne', status: 'Archivé', meta: { fournisseur: 'Bâtir CI', numero: '2016-077', montant: 27350000 }, file: 'Facture_2016_077.txt', by: 'u3', box: 'CI-ABJ-PLT-2026-000458',
			text: 'BÂTIR CI SARL\nFacture n° 2016-077 — 02/09/2016\nRéfection de la salle d’archives, bâtiment B\nTotal TTC : 27 350 000 FCFA' },
		{ title: 'Contrat de maintenance des ascenseurs — ABC SA', type: 'contrat', date: '2014-11-20', conf: 'Confidentiel', status: 'Archivé', meta: { parties: 'Organisation démo / ABC SA', echeance: '2016-12-31', montant: 18000000 }, file: 'Contrat_maintenance_ascenseurs_2014.txt', by: 'u2', box: 'CI-ABJ-PLT-2026-000457',
			text: 'CONTRAT DE MAINTENANCE\nEntre Organisation démo et ABC SA\nSigné à Abidjan le 20/11/2014\nDurée : jusqu’au 31/12/2016\nMontant annuel : 18 000 000 FCFA' },
		{ title: 'Contrat fournisseur 2026-0045 — Réseaux & Énergie', type: 'contrat', date: '2026-03-02', conf: 'Confidentiel', status: 'Actif', meta: { parties: 'Organisation démo / Réseaux & Énergie', echeance: '2029-03-01', montant: 54000000 }, file: 'Contrat_2026_0045.txt', by: 'u2',
			text: 'CONTRAT DE FOURNITURE\nEntre Organisation démo et Réseaux & Énergie\nObjet : alimentation électrique secourue du centre de numérisation\nDurée : 3 ans à compter du 02/03/2026\nMontant : 54 000 000 FCFA' },
		{ title: 'PV du conseil d’administration du 14/09/2026', type: 'pv', date: '2026-09-14', conf: 'Confidentiel', status: 'Actif', meta: { instance: 'Conseil d’administration' }, file: 'PV_CA_2026-09-14.txt', by: 'u4',
			text: 'PROCÈS-VERBAL DU CONSEIL D’ADMINISTRATION\nSéance du 14/09/2026\nOrdre du jour : approbation du plan de numérisation 2027\nDécision : le plan est approuvé à l’unanimité.' },
		{ title: 'Registre des délibérations 1987', type: 'historique', date: '1987-12-31', conf: 'Public', status: 'Archivé', meta: { periode: '1987' }, file: 'Registre_deliberations_1987.txt', by: 'u1',
			text: 'REGISTRE DES DÉLIBÉRATIONS — ANNÉE 1987\nTranscription des délibérations du conseil, séances de janvier à décembre 1987.' },
		{ title: 'Dossier du personnel — matricule 0412', type: 'personnel', date: '2009-02-01', conf: 'Secret', status: 'Archivé', hold: true, meta: { matricule: '0412', agent: 'Kouamé N’Guessan', depart: '2021-03-31' }, file: 'Dossier_personnel_0412.txt', by: 'u1',
			text: 'DOSSIER DU PERSONNEL\nMatricule 0412 — Kouamé N’Guessan\nEntrée : 01/02/2009 — Départ : 31/03/2021\nPièces : contrat de travail, avenants, évaluations, certificat de travail.' },
		{ title: 'États financiers 2025', type: 'etats', date: '2026-03-31', conf: 'Confidentiel', status: 'Archivé', meta: { exercice: '2025' }, file: 'Etats_financiers_2025.txt', by: 'u3',
			text: 'ÉTATS FINANCIERS — EXERCICE 2025\nBilan, compte de résultat et annexes, arrêtés au 31/12/2025.' },
		{ title: 'Plan du bâtiment B — niveau 2', type: 'plan', date: '2019-06-10', conf: 'Interne', status: 'Actif', meta: { ouvrage: 'Bâtiment B' }, file: 'Plan_batiment_B_niveau2.txt', by: 'u1',
			text: 'PLAN — BÂTIMENT B, NIVEAU 2\nSalle d’archives 03 : 12 rayons de 6 étagères, système de détection incendie.' },
		{ title: 'Courrier entrant — demande d’extrait d’acte', type: 'courrier', date: '2026-09-28', conf: 'Interne', status: 'Actif', meta: { correspondant: 'M. Yao Konan', sens: 'Entrant' }, file: 'Courrier_2026-09-28.txt', by: 'u2',
			text: 'Abidjan, le 28/09/2026\nObjet : demande d’extrait d’acte\nMadame, Monsieur, je sollicite la délivrance d’un extrait de la délibération du 14/09/2026.' },
		{ title: 'Facture scannée 2024-77', type: 'facture', date: '2024-02-21', conf: 'Interne', status: 'Actif', meta: {}, file: 'Facture_scannee_2024-77.png', by: 'u3', image: true }
	];

	function drawInvoicePNG() {
		return new Promise( function ( res ) {
			var c = document.createElement( 'canvas' ); c.width = 900; c.height = 1200;
			var g = c.getContext( '2d' );
			g.fillStyle = '#fbfaf6'; g.fillRect( 0, 0, 900, 1200 );
			g.fillStyle = '#1a1a1a';
			g.font = 'bold 40px Arial'; g.fillText( 'IMPRIMERIE MODERNE SARL', 60, 110 );
			g.font = '24px Arial'; g.fillText( 'Boulevard Lagunaire, Abidjan', 60, 150 );
			g.font = 'bold 44px Arial'; g.fillText( 'FACTURE N° 2024-77', 60, 260 );
			g.font = '28px Arial';
			[ 'Date : 21/02/2024', 'Client : Organisation démo', '', 'Impression de 5 000 étiquettes QR', 'pour boîtes d’archives ........ 2 100 000', 'Reliure de registres ........... 1 300 000', '', 'Total HT : 2 881 356 FCFA', 'TVA 18 % : 518 644 FCFA', 'Total TTC : 3 400 000 FCFA' ].forEach( function ( l, i ) { g.fillText( l, 60, 340 + i * 52 ); } );
			g.strokeStyle = '#999'; g.lineWidth = 2; g.strokeRect( 40, 40, 820, 1120 );
			g.font = 'italic 22px Arial'; g.fillStyle = '#555'; g.fillText( 'Document d’exemple — démo ARCHIVA360', 60, 1120 );
			c.toBlob( function ( b ) { b.arrayBuffer().then( res ); }, 'image/png' );
		} );
	}

	/* =====================================================================
	 * State
	 * ===================================================================== */
	var S = null;
	var ui = { view: 'dashboard', series: 'all', type: 'all', status: 'all', q: '', open: null, tab: 'apercu', horizon: '90', confirm: null, box: null, auditUser: 'all', searchQ: '' };
	var saveTimer;
	function persist() { clearTimeout( saveTimer ); saveTimer = setTimeout( function () { store.put( 'kv', 'state', JSON.parse( JSON.stringify( S ) ) ); }, 80 ); }
	function me() { return S.users.filter( function ( u ) { return u.id === S.current; } )[ 0 ] || S.users[ 0 ]; }
	function can( p ) { return ROLES[ me().role ].perms.indexOf( p ) !== -1; }
	function userName( id ) { var u = S.users.filter( function ( x ) { return x.id === id; } )[ 0 ]; return u ? u.name : id; }
	function typeOf( id ) { return S.types.filter( function ( t ) { return t.id === id; } )[ 0 ] || S.types[ S.types.length - 1 ]; }
	function ruleOf( id ) { return S.rules.filter( function ( r ) { return r.id === id; } )[ 0 ]; }
	function seriesOf( code ) { return S.series.filter( function ( s ) { return s.code === code; } )[ 0 ]; }
	function docById( id ) { return S.docs.filter( function ( d ) { return d.id === id; } )[ 0 ]; }
	function visible( d ) {
		if ( can( 'confidential' ) ) return true;
		return d.conf === 'Public' || d.conf === 'Interne' || d.createdBy === S.current;
	}
	function current( d ) { return d.versions[ d.versions.length - 1 ]; }

	/* Retention */
	function dueOf( d ) {
		var t = typeOf( d.type ), r = ruleOf( d.rule || t.rule );
		if ( ! r ) return { label: '—' };
		if ( r.years == null ) return { permanent: true, label: 'Permanente', rule: r };
		var base = null;
		if ( r.trigger === 'date' ) base = d.date;
		else if ( r.trigger === 'archive' ) base = d.archivedAt ? d.archivedAt.slice( 0, 10 ) : null;
		else if ( r.trigger.indexOf( 'field:' ) === 0 ) base = d.meta[ r.trigger.slice( 6 ) ] || null;
		if ( ! base ) return { pending: true, label: 'En attente : ' + TRIGGERS[ r.trigger ].toLowerCase(), rule: r };
		var due = addYears( base, r.years );
		if ( d.reviewUntil && d.reviewUntil > due ) due = d.reviewUntil;
		return { due: due, label: frDate( due ), rule: r, past: due <= todayISO() };
	}
	function missingMeta( d ) {
		return typeOf( d.type ).fields.filter( function ( f ) { return f.req && ( d.meta[ f.k ] === undefined || d.meta[ f.k ] === '' || d.meta[ f.k ] === null ); } );
	}

	/* Audit trail (chained SHA-256) */
	var auditQueue = Promise.resolve();
	function log( action, object, detail ) {
		var u = me();
		auditQueue = auditQueue.then( function () {
			var prev = S.audit.length ? S.audit[ S.audit.length - 1 ].hash : 'GENESIS';
			var e = { n: S.audit.length + 1, at: nowISO(), user: u.name, role: ROLES[ u.role ].label, action: action, object: object || '', detail: detail || '', prev: prev };
			return sha256( prev + '|' + JSON.stringify( [ e.n, e.at, e.user, e.role, e.action, e.object, e.detail ] ) ).then( function ( h ) {
				e.hash = h; S.audit.push( e ); persist();
				if ( ui.view === 'audit' || ui.view === 'dashboard' ) render();
			} );
		} );
		return auditQueue;
	}
	function verifyChain() {
		var prev = 'GENESIS', i = 0;
		function step() {
			if ( i >= S.audit.length ) return Promise.resolve( { ok: true, n: S.audit.length } );
			var e = S.audit[ i ];
			if ( e.prev !== prev ) return Promise.resolve( { ok: false, at: e.n } );
			return sha256( prev + '|' + JSON.stringify( [ e.n, e.at, e.user, e.role, e.action, e.object, e.detail ] ) ).then( function ( h ) {
				if ( h !== e.hash ) return { ok: false, at: e.n };
				prev = e.hash; i++; return step();
			} );
		}
		return step();
	}

	/* Documents */
	function newId() { S.seq++; return 'DOC-' + new Date().getFullYear() + '-' + pad( S.seq, 5 ); }
	function addDocument( file, buf, opts ) {
		opts = opts || {};
		var id = opts.id || newId();
		return sha256( buf ).then( function ( h ) {
			var t = typeOf( opts.type || 'autre' );
			var d = {
				id: id, title: opts.title || file.name.replace( /\.[^.]+$/, '' ).replace( /[_-]+/g, ' ' ), type: t.id, series: opts.series || t.series,
				date: opts.date || todayISO(), conf: opts.conf || 'Interne', status: opts.status || 'Actif', hold: !! opts.hold, meta: opts.meta || {},
				text: opts.text || '', textSource: opts.text ? 'contenu texte' : '', versions: [ { v: 1, name: file.name, mime: file.type || 'text/plain', size: buf.byteLength, sha: h, at: nowISO(), by: opts.by || S.current } ],
				createdAt: nowISO(), createdBy: opts.by || S.current, archivedAt: opts.status === 'Archivé' ? nowISO() : null, box: opts.box || null, integrity: null, proposed: opts.proposed || null
			};
			S.docs.push( d );
			return store.put( 'files', id + '@1', buf ).then( function () { return d; } );
		} );
	}

	function seed() {
		S = seedState();
		var chain = Promise.resolve();
		var me0 = S.current;
		SAMPLES.forEach( function ( s ) {
			chain = chain.then( function () {
				var bufP = s.image ? drawInvoicePNG() : Promise.resolve( new TextEncoder().encode( s.text ).buffer );
				return bufP.then( function ( buf ) {
					return addDocument( { name: s.file, type: s.image ? 'image/png' : 'text/plain' }, buf, { title: s.title, type: s.type, date: s.date, conf: s.conf, status: s.status, meta: s.meta, text: s.text || '', by: s.by, hold: s.hold, box: s.box } );
				} );
			} );
		} );
		return chain.then( function () {
			S.current = 'u4';
			return log( 'INITIALISATION', 'Organisation démo', 'Espace de démonstration créé avec ' + SAMPLES.length + ' documents d’exemple' );
		} ).then( function () {
			S.current = me0;
			S.docs.filter( function ( d ) { return d.hold; } ).forEach( function ( d ) { log( 'GEL JURIDIQUE', d.title, 'Contentieux prud’homal en cours (exemple)' ); } );
			return auditQueue;
		} ).then( function () { persist(); } );
	}

	/* =====================================================================
	 * Text extraction ("OCR") and metadata proposals
	 * ===================================================================== */
	var PDFJS = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js';
	var TESS = 'https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js';
	function extractText( d, onProgress ) {
		var v = current( d );
		return store.get( 'files', d.id + '@' + v.v ).then( function ( buf ) {
			if ( ! buf ) throw new Error( 'Fichier introuvable' );
			var kind = ext( v.name, v.mime );
			if ( kind === 'txt' && ! /\.(docx?|xlsx?|odt|ods|zip)$/i.test( v.name ) ) return { text: new TextDecoder().decode( buf ), source: 'contenu texte' };
			if ( kind === 'pdf' ) {
				return loadScript( PDFJS ).then( function () {
					var lib = window.pdfjsLib;
					lib.GlobalWorkerOptions.workerSrc = PDFJS.replace( 'pdf.min.js', 'pdf.worker.min.js' );
					return lib.getDocument( { data: new Uint8Array( buf.slice( 0 ) ) } ).promise;
				} ).then( function ( pdf ) {
					var out = [], n = Math.min( pdf.numPages, 30 ), p = Promise.resolve();
					for ( var i = 1; i <= n; i++ ) ( function ( i ) {
						p = p.then( function () { return pdf.getPage( i ); } ).then( function ( pg ) { return pg.getTextContent(); } ).then( function ( tc ) {
							out.push( tc.items.map( function ( it ) { return it.str; } ).join( ' ' ) ); if ( onProgress ) onProgress( 'Page ' + i + ' / ' + n );
						} );
					} )( i );
					return p.then( function () { return { text: out.join( '\n' ), source: 'texte du PDF' }; } );
				} );
			}
			if ( kind === 'img' ) {
				return loadScript( TESS ).then( function () {
					return window.Tesseract.recognize( new Blob( [ buf ], { type: v.mime } ), 'fra', { logger: function ( m ) { if ( onProgress && m.status ) onProgress( m.status + ( m.progress ? ' ' + Math.round( m.progress * 100 ) + ' %' : '' ) ); } } );
				} ).then( function ( r ) { return { text: r.data.text, source: 'OCR (Tesseract)' }; } );
			}
			throw new Error( 'Extraction non disponible pour ce format dans la démo (Word, Excel…).' );
		} );
	}
	function parseAmount( s ) { var n = parseFloat( String( s ).replace( /[\s  .]/g, '' ).replace( ',', '.' ) ); return isNaN( n ) ? null : n; }
	function propose( text, filename ) {
		var t = norm( text + ' ' + filename ), p = {};
		if ( /facture/.test( t ) ) p.type = 'facture';
		else if ( /contrat/.test( t ) ) p.type = 'contrat';
		else if ( /proces-verbal|proces verbal|\bpv\b|deliberation/.test( t ) ) p.type = 'pv';
		else if ( /etats? financiers?|bilan/.test( t ) ) p.type = 'etats';
		else if ( /dossier du personnel|matricule/.test( t ) ) p.type = 'personnel';
		else if ( /\bplan\b|rapport technique/.test( t ) ) p.type = 'plan';
		else if ( /objet\s*:|madame|monsieur/.test( t ) ) p.type = 'courrier';
		var dm = /(\d{2})[\/.-](\d{2})[\/.-](\d{4})/.exec( text ) || null;
		if ( dm ) p.date = dm[ 3 ] + '-' + dm[ 2 ] + '-' + dm[ 1 ];
		var meta = {};
		var amounts = [], re = /(\d[\d\s.  ]{2,})\s*(?:F\s?CFA|FCFA|XOF)/gi, m;
		while ( ( m = re.exec( text ) ) ) { var a = parseAmount( m[ 1 ] ); if ( a ) amounts.push( a ); }
		var ttc = /total\s*ttc\s*:?\s*([\d\s.  ]+)/i.exec( text );
		if ( ttc ) amounts.push( parseAmount( ttc[ 1 ] ) );
		if ( amounts.length ) meta.montant = Math.max.apply( null, amounts );
		var num = /(?:facture\s*(?:n[°o]\s*)?|n[°o]\s*)([A-Z]{0,4}-?\d{2,4}[-\d]*)/i.exec( text );
		if ( num ) meta.numero = num[ 1 ].toUpperCase();
		var first = String( text ).split( /\n/ ).map( function ( l ) { return l.trim(); } ).filter( Boolean )[ 0 ];
		if ( p.type === 'facture' && first && first.length < 60 && ! /facture/i.test( first ) ) meta.fournisseur = first.replace( /\b([A-ZÀ-Ý])([A-ZÀ-Ý]+)\b/g, function ( w, a, b ) { return w.length <= 4 ? w : a + b.toLowerCase(); } );
		var entre = /entre\s+(.+?)\s+et\s+(.+?)(?:\n|$)/i.exec( text );
		if ( entre ) meta.parties = entre[ 1 ] + ' / ' + entre[ 2 ];
		var mat = /matricule\s*:?\s*(\w+)/i.exec( text ); if ( mat ) meta.matricule = mat[ 1 ];
		var ex = /exercice\s*:?\s*(\d{4})/i.exec( text ); if ( ex ) meta.exercice = ex[ 1 ];
		p.meta = meta;
		return p;
	}

	/* =====================================================================
	 * Search (natural-language-ish)
	 * ===================================================================== */
	var TYPE_WORDS = [ [ /^factur/, 'facture' ], [ /^contrat/, 'contrat' ], [ /^(pv|proces|deliberation)/, 'pv' ], [ /^personnel$/, 'personnel' ], [ /^plans?$/, 'plan' ], [ /^(courrier|lettre)/, 'courrier' ], [ /^(etats?|bilan)/, 'etats' ] ];
	var STOP = 'document documents dossier dossiers a au aux avec ce ces dans de des du en et la le les leur moi mon ma mes ou par pour qui que sur tous tout toute toutes trouve trouver montre affiche liste un une signe signes signees signe concernant fcfa f cfa xof millions million m superieur superieure superieurs superieures inferieur inferieure inferieurs inferieures plus moins de a arrivant arrive echeance archive archives archivee archivees confidentiel confidentiels sous gel juridique'.split( ' ' );
	function parseQuery( q ) {
		var n = norm( q ), f = { chips: [] };
		var amt = /(superieur\w*|plus de|au-dessus de|>)\s*(?:a\s*)?([\d\s.,]+)\s*(millions?|m\b|milliards?)?/.exec( n );
		if ( amt ) { var v = parseAmount( amt[ 2 ] ); if ( amt[ 3 ] ) v *= /milliard/.test( amt[ 3 ] ) ? 1e9 : 1e6; f.min = v; f.chips.push( 'Montant > ' + fcfa( v ) ); }
		var amt2 = /(inferieur\w*|moins de|<)\s*(?:a\s*)?([\d\s.,]+)\s*(millions?|m\b)?/.exec( n );
		if ( amt2 ) { var v2 = parseAmount( amt2[ 2 ] ); if ( amt2[ 3 ] ) v2 *= 1e6; f.max = v2; f.chips.push( 'Montant < ' + fcfa( v2 ) ); }
		var year = /\b(19|20)\d{2}\b/.exec( n.replace( /([\d\s.,]+)\s*(millions?|milliards?)/g, '' ) );
		if ( year ) {
			if ( /echeance|expir/.test( n ) ) { f.dueYear = year[ 0 ]; f.chips.push( 'Échéance en ' + year[ 0 ] ); }
			else { f.year = year[ 0 ]; f.chips.push( 'Année ' + year[ 0 ] ); }
		} else if ( /echeance|expir/.test( n ) ) { f.dueSoon = true; f.chips.push( 'Échéance dans l’année' ); }
		if ( /archive/.test( n ) ) { f.status = 'Archivé'; f.chips.push( 'Statut : archivé' ); }
		if ( /gel/.test( n ) ) { f.hold = true; f.chips.push( 'Sous gel juridique' ); }
		if ( /confidentiel/.test( n ) ) { f.conf = true; f.chips.push( 'Confidentiel ou secret' ); }
		var words = n.replace( /[^a-z0-9\s'-]/g, ' ' ).split( /\s+/ ).filter( Boolean );
		var terms = [];
		words.forEach( function ( w ) {
			var hit = TYPE_WORDS.filter( function ( tw ) { return tw[ 0 ].test( w ); } )[ 0 ];
			if ( hit ) { if ( ! f.type ) { f.type = hit[ 1 ]; f.chips.push( 'Type : ' + typeOf( hit[ 1 ] ).label ); } return; }
			if ( STOP.indexOf( w ) !== -1 || /^\d/.test( w ) || w.length < 2 || /^(superieur|inferieur|fournisseur)s?$/.test( w ) && ( f.min || f.max ) ) return;
			if ( w === 'fournisseurs' || w === 'fournisseur' ) { if ( f.type === 'contrat' || f.type === 'facture' ) return; }
			terms.push( w );
		} );
		f.terms = terms;
		if ( terms.length ) f.chips.push( 'Mots : ' + terms.join( ', ' ) );
		return f;
	}
	function runSearch( q ) {
		var f = parseQuery( q );
		var res = S.docs.filter( function ( d ) {
			if ( d.status === 'Éliminé' || ! visible( d ) ) return false;
			if ( f.type && d.type !== f.type ) return false;
			if ( f.min != null && ! ( Number( d.meta.montant ) > f.min ) ) return false;
			if ( f.max != null && ! ( Number( d.meta.montant ) < f.max ) ) return false;
			if ( f.year && d.date.slice( 0, 4 ) !== f.year ) return false;
			if ( f.status && d.status !== f.status ) return false;
			if ( f.hold && ! d.hold ) return false;
			if ( f.conf && ! ( d.conf === 'Confidentiel' || d.conf === 'Secret' ) ) return false;
			var du = dueOf( d );
			if ( f.dueYear && ! ( du.due && du.due.slice( 0, 4 ) === f.dueYear ) ) return false;
			if ( f.dueSoon && ! ( du.due && du.due <= addDays( todayISO(), 365 ) ) ) return false;
			if ( f.terms.length ) {
				var hay = norm( [ d.title, d.id, typeOf( d.type ).label, ( seriesOf( d.series ) || {} ).label, d.text, Object.keys( d.meta ).map( function ( k ) { return d.meta[ k ]; } ).join( ' ' ) ].join( ' ' ) );
				return f.terms.every( function ( t ) { return hay.indexOf( t ) !== -1; } );
			}
			return true;
		} );
		return { f: f, res: res };
	}

	/* =====================================================================
	 * Views
	 * ===================================================================== */
	function ftype( d ) { var v = current( d ); var k = d.status === 'Éliminé' ? 'gone' : ext( v.name, v.mime ); return '<span class="ft ' + k + '">' + ( k === 'gone' ? '—' : k === 'img' ? 'IMG' : k ) + '</span>'; }
	function statusTag( d ) {
		var t = { 'Actif': 'b', 'Archivé': 'g', 'Éliminé': '' }[ d.status ];
		return '<span class="tag ' + t + '">' + esc( d.status ) + '</span>' + ( d.hold ? ' <span class="tag r">Gel juridique</span>' : '' ) + ( d.integrity === 'altéré' ? ' <span class="tag r">Altéré</span>' : '' );
	}
	function confTag( c ) { return '<span class="tag ' + ( c === 'Secret' ? 'n' : c === 'Confidentiel' ? 'a' : '' ) + '">' + esc( c ) + '</span>'; }
	function head( title, sub, actions ) { return '<div class="head"><div><h1>' + title + '</h1>' + ( sub ? '<p class="sub">' + sub + '</p>' : '' ) + '</div><div class="btns">' + ( actions || '' ) + '</div></div>'; }
	function docRows( list, cols ) {
		if ( ! list.length ) return '<div class="empty">Aucun document.</div>';
		return '<div class="tbl"><table><thead><tr><th>Document</th>' + cols.map( function ( c ) { return '<th>' + c[ 0 ] + '</th>'; } ).join( '' ) + '</tr></thead><tbody>' +
			list.map( function ( d ) {
				return '<tr class="clickable" data-open="' + d.id + '" tabindex="0"><td><div class="fi">' + ftype( d ) + '<div>' + esc( d.title ) + '<div class="muted" style="font-size:11.5px;font-weight:400">' + esc( d.id ) + ' · ' + esc( ( seriesOf( d.series ) || {} ).code || '' ) + ' ' + esc( ( seriesOf( d.series ) || {} ).label || '' ) + '</div></div></div></td>' +
					cols.map( function ( c ) { return '<td>' + c[ 1 ]( d ) + '</td>'; } ).join( '' ) + '</tr>';
			} ).join( '' ) + '</tbody></table></div>';
	}

	var V = {};
	V.dashboard = function () {
		var live = S.docs.filter( function ( d ) { return d.status !== 'Éliminé'; } );
		var arch = live.filter( function ( d ) { return d.status === 'Archivé'; } ).length;
		var soon = live.filter( function ( d ) { var u = dueOf( d ); return u.due && u.due <= addDays( todayISO(), 90 ); } ).length;
		var bytes = live.reduce( function ( a, d ) { return a + d.versions.reduce( function ( b, v ) { return b + v.size; }, 0 ); }, 0 );
		var miss = live.filter( function ( d ) { return missingMeta( d ).length; } ).length;
		var bad = live.filter( function ( d ) { return d.integrity === 'altéré'; } ).length;
		var years = {}, y0 = new Date().getFullYear();
		for ( var y = y0 - 9; y <= y0; y++ ) years[ y ] = 0;
		live.forEach( function ( d ) { var yy = parseInt( d.date.slice( 0, 4 ), 10 ); if ( years[ yy ] !== undefined ) years[ yy ]++; } );
		var max = Math.max.apply( null, Object.keys( years ).map( function ( k ) { return years[ k ]; } ).concat( [ 1 ] ) );
		var chart = Object.keys( years ).map( function ( k ) { return '<div class="' + ( +k === y0 ? 'cur' : '' ) + '" title="' + years[ k ] + ' document(s)"><i style="height:' + Math.round( years[ k ] / max * 110 ) + 'px"></i>' + k.slice( 2 ) + '</div>'; } ).join( '' );
		var alerts = [];
		if ( bad ) alerts.push( [ 'bad', bad + ' document(s) : intégrité altérée', 'compliance' ] );
		if ( soon ) alerts.push( [ 'warn', soon + ' document(s) arrivent à échéance dans 90 jours', 'retention' ] );
		if ( miss ) alerts.push( [ 'warn', miss + ' document(s) sans métadonnées obligatoires', 'compliance' ] );
		var holds = live.filter( function ( d ) { return d.hold; } ).length;
		if ( holds ) alerts.push( [ '', holds + ' document(s) sous gel juridique', 'retention' ] );
		alerts.push( S.lastBackup ? [ 'ok', 'Dernière sauvegarde : ' + frDateTime( S.lastBackup ), 'backup' ] : [ 'warn', 'Aucune sauvegarde exportée', 'backup' ] );
		var recent = S.audit.slice( -7 ).reverse();
		return head( 'Tableau de bord', esc( S.org ) + ' · ' + new Date().toLocaleDateString( 'fr-FR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' } ),
			( can( 'upload' ) ? '<button class="btn" data-go="documents" data-then="upload">' + icon( 'upload' ) + 'Importer des documents</button>' : '' ) ) +
			'<div class="grid g4" style="margin-bottom:14px">' +
			'<div class="box kpi"><small>' + icon( 'files' ) + 'Documents gérés</small><b>' + live.length + '</b><span class="muted">' + S.docs.filter( function ( d ) { return d.status === 'Éliminé'; } ).length + ' éliminé(s)</span></div>' +
			'<div class="box kpi"><small>' + icon( 'archive' ) + 'Archivés (SAE)</small><b>' + arch + '</b><span class="ok">' + ( live.length ? Math.round( arch / live.length * 100 ) : 0 ) + ' % du fonds</span></div>' +
			'<div class="box kpi"><small>' + icon( 'clock' ) + 'Échéances à 90 jours</small><b>' + soon + '</b><span class="' + ( soon ? 'warn' : 'ok' ) + '">' + ( soon ? 'À examiner' : 'Rien à traiter' ) + '</span></div>' +
			'<div class="box kpi"><small>' + icon( 'drive' ) + 'Stockage utilisé</small><b>' + size( bytes ) + '</b><span class="muted">' + ( store.persistent ? 'dans ce navigateur' : 'en mémoire (session)' ) + '</span></div></div>' +
			'<div class="grid g21" style="margin-bottom:14px"><div class="box"><h2>Documents par année <small>date du document</small></h2><div class="chart">' + chart + '</div></div>' +
			'<div class="box"><h2>Alertes</h2>' + alerts.map( function ( a ) { return '<p style="margin:0 0 8px"><button class="btn o sm" data-go="' + a[ 2 ] + '">Voir</button> <span class="' + a[ 0 ] + '">' + esc( a[ 1 ] ) + '</span></p>'; } ).join( '' ) + '</div></div>' +
			'<div class="box"><h2>Activité récente <small><a href="#audit" data-go="audit">Journal complet</a></small></h2><div class="tbl"><table><tbody>' +
			recent.map( function ( e ) { return '<tr><td class="muted" style="width:140px">' + frDateTime( e.at ) + '</td><td>' + esc( e.user ) + '</td><td><span class="tag">' + esc( e.action ) + '</span></td><td>' + esc( e.object ) + '</td></tr>'; } ).join( '' ) +
			'</tbody></table></div></div>';
	};

	V.documents = function () {
		var list = S.docs.filter( function ( d ) {
			if ( ! visible( d ) ) return false;
			if ( ui.series !== 'all' && d.series !== ui.series ) return false;
			if ( ui.type !== 'all' && d.type !== ui.type ) return false;
			if ( ui.status === 'all' ? d.status === 'Éliminé' : d.status !== ui.status ) return false;
			if ( ui.q && norm( d.title + ' ' + d.id + ' ' + d.text ).indexOf( norm( ui.q ) ) === -1 ) return false;
			return true;
		} ).sort( function ( a, b ) { return a.date < b.date ? 1 : -1; } );
		var counts = {};
		S.docs.forEach( function ( d ) { if ( d.status !== 'Éliminé' && visible( d ) ) counts[ d.series ] = ( counts[ d.series ] || 0 ) + 1; } );
		var fns = {};
		S.series.forEach( function ( s ) { ( fns[ s.fn ] = fns[ s.fn ] || [] ).push( s ); } );
		var tree = '<div class="tree"><button data-series="all" aria-pressed="' + ( ui.series === 'all' ) + '"><span>Tout le plan de classement</span></button>' +
			Object.keys( fns ).map( function ( fn ) {
				return '<div class="muted" style="font-size:11px;text-transform:uppercase;letter-spacing:.08em;margin:10px 8px 2px;font-weight:700">' + esc( fn ) + '</div>' +
					fns[ fn ].map( function ( s ) { return '<button data-series="' + s.code + '" aria-pressed="' + ( ui.series === s.code ) + '"><span><span class="code">' + s.code + '</span> ' + esc( s.label ) + '</span><span class="muted">' + ( counts[ s.code ] || 0 ) + '</span></button>'; } ).join( '' );
			} ).join( '' ) + '</div>';
		var hidden = S.docs.filter( function ( d ) { return d.status !== 'Éliminé' && ! visible( d ); } ).length;
		return head( 'Documents', 'GED : importer, décrire, classer, versionner', '' ) +
			( can( 'upload' ) ? '<label class="drop" id="drop" for="file-input"><input type="file" id="file-input" multiple class="sr"><b>Glissez-déposez des fichiers ici</b> ou cliquez pour choisir · PDF, images, textes, Office<br><small>Les fichiers restent dans votre navigateur. L’empreinte SHA-256 est calculée à l’import.</small></label>' : '<div class="notice">Votre rôle (' + esc( ROLES[ me().role ].label ) + ') ne permet pas d’importer des documents.</div>' ) +
			( hidden ? '<div class="notice warn">' + hidden + ' document(s) confidentiel(s) ne sont pas visibles avec votre rôle.</div>' : '' ) +
			'<div class="layout-docs"><div class="box">' + tree + '</div><div class="box">' +
			'<div class="toolbar"><label class="sr" for="f-q">Filtrer</label><input id="f-q" placeholder="Filtrer par titre ou contenu…" value="' + esc( ui.q ) + '" style="flex:1;min-width:160px">' +
			'<label class="sr" for="f-type">Type</label><select id="f-type"><option value="all">Tous les types</option>' + S.types.map( function ( t ) { return '<option value="' + t.id + '"' + ( ui.type === t.id ? ' selected' : '' ) + '>' + esc( t.label ) + '</option>'; } ).join( '' ) + '</select>' +
			'<label class="sr" for="f-status">Statut</label><select id="f-status">' + [ [ 'all', 'Actifs et archivés' ], [ 'Actif', 'Actifs' ], [ 'Archivé', 'Archivés' ], [ 'Éliminé', 'Éliminés' ] ].map( function ( o ) { return '<option value="' + o[ 0 ] + '"' + ( ui.status === o[ 0 ] ? ' selected' : '' ) + '>' + o[ 1 ] + '</option>'; } ).join( '' ) + '</select></div>' +
			docRows( list, [ [ 'Type', function ( d ) { return esc( typeOf( d.type ).label ); } ], [ 'Date', function ( d ) { return frDate( d.date ); } ], [ 'Confidentialité', function ( d ) { return confTag( d.conf ); } ], [ 'Statut', statusTag ], [ 'Échéance', function ( d ) { return esc( dueOf( d ).label ); } ] ] ) +
			'</div></div>';
	};

	V.search = function () {
		var r = ui.searchQ ? runSearch( ui.searchQ ) : null;
		var ex = [ 'Factures supérieures à 5 millions FCFA', 'Contrats signés en 2026', 'Documents archivés sous gel juridique', 'Contrats arrivant à échéance en 2026', 'Tous les documents concernant ABC SA', 'Registre 1987' ];
		var terms = r ? r.f.terms : [];
		function hl( s ) { var o = esc( s ); terms.forEach( function ( t ) { if ( t.length > 2 ) o = o.replace( new RegExp( '(' + t.replace( /[.*+?^${}()|[\]\\]/g, '\\$&' ) + ')', 'gi' ), '<mark>$1</mark>' ); } ); return o; }
		return head( 'Recherche intelligente', 'Posez la question en français : type, montant, année, échéance, statut, mots du contenu', '' ) +
			'<form class="searchbig" id="search-form">' + icon( 'sparkles' ) + '<label class="sr" for="search-q">Votre recherche</label><input id="search-q" value="' + esc( ui.searchQ ) + '" placeholder="Ex. : Factures supérieures à 5 millions FCFA"><button class="btn">' + icon( 'search' ) + 'Rechercher</button></form>' +
			'<div class="examples">' + ex.map( function ( e ) { return '<button type="button" data-example="' + esc( e ) + '">' + esc( e ) + '</button>'; } ).join( '' ) + '</div>' +
			( r ? '<div class="box"><div class="chips" style="margin-bottom:10px"><span class="muted">Compris comme :</span>' + ( r.f.chips.length ? r.f.chips.map( function ( c ) { return '<span class="tag b">' + esc( c ) + '</span>'; } ).join( '' ) : '<span class="tag">Tous les documents</span>' ) + '</div>' +
				'<h2>' + r.res.length + ' résultat' + ( r.res.length > 1 ? 's' : '' ) + '</h2>' +
				docRows( r.res, [ [ 'Montant', function ( d ) { return d.meta.montant ? '<b>' + fcfa( d.meta.montant ) + '</b>' : '—'; } ], [ 'Date', function ( d ) { return frDate( d.date ); } ], [ 'Statut', statusTag ], [ 'Extrait', function ( d ) { var i = norm( d.text ).indexOf( terms[ 0 ] || '§' ); return i < 0 ? '<span class="muted">—</span>' : '<span class="muted">' + hl( d.text.slice( Math.max( 0, i - 30 ), i + 60 ) ) + '…</span>'; } ] ] ) +
				'<p class="muted" style="font-size:12px;margin:10px 0 0">Seuls les documents auxquels votre rôle donne accès sont affichés. L’analyse de la question repose sur des règles (type, montant, année, échéance, statut) : c’est une démonstration du principe.</p></div>' : '' );
	};

	V.retention = function () {
		var h = ui.horizon, limit = h === 'past' ? todayISO() : addDays( todayISO(), parseInt( h, 10 ) );
		var list = S.docs.filter( function ( d ) { if ( d.status === 'Éliminé' || ! visible( d ) ) return false; var u = dueOf( d ); return u.due && u.due <= limit; } )
			.sort( function ( a, b ) { return dueOf( a ).due < dueOf( b ).due ? -1 : 1; } );
		var stages = { Actif: 0, Archivé: 0, Permanent: 0, Éliminé: 0 };
		S.docs.forEach( function ( d ) { if ( d.status === 'Éliminé' ) stages[ 'Éliminé' ]++; else if ( dueOf( d ).permanent ) stages.Permanent++; else stages[ d.status ]++; } );
		var tot = S.docs.length || 1, colors = { Actif: '#CFE2FD', Archivé: '#3D8CF2', Permanent: '#0A1541', Éliminé: '#C6CCDB' };
		var c = ui.confirm;
		return head( 'Retention Center', 'Échéances de conservation et sort final. Aucune élimination n’est automatique.', '<button class="btn o" data-go="rules">' + icon( 'hourglass' ) + 'Règles de conservation</button>' ) +
			'<div class="box" style="margin-bottom:14px"><h2>Cycle de vie du fonds</h2><div class="stage">' + Object.keys( stages ).map( function ( k ) { return '<div style="width:' + ( stages[ k ] / tot * 100 ) + '%;background:' + colors[ k ] + '"></div>'; } ).join( '' ) + '</div>' +
			'<div class="legend">' + Object.keys( stages ).map( function ( k ) { return '<span><i style="background:' + colors[ k ] + '"></i>' + k + ' : <b>' + stages[ k ] + '</b></span>'; } ).join( '' ) + '</div></div>' +
			'<div class="box"><div class="toolbar"><label for="horizon"><b>Afficher les échéances</b></label><select id="horizon">' + [ [ 'past', 'déjà dépassées' ], [ '90', 'dans les 90 jours' ], [ '365', 'dans l’année' ], [ '3650', 'dans les 10 ans' ] ].map( function ( o ) { return '<option value="' + o[ 0 ] + '"' + ( h === o[ 0 ] ? ' selected' : '' ) + '>' + o[ 1 ] + '</option>'; } ).join( '' ) + '</select><span class="muted">' + list.length + ' document(s)</span></div>' +
			( c ? '<div class="confirm" id="confirm-box"><p><b>Confirmer l’élimination de « ' + esc( docById( c ).title ) + ' » ?</b> Le fichier sera supprimé définitivement. Un certificat d’élimination sera créé et conservé avec l’empreinte du document.</p><div class="field"><label for="confirm-reason">Motif et référence de la décision</label><input id="confirm-reason" value="Échéance atteinte — validation du responsable"></div><div class="btns"><button class="btn danger" data-act="eliminate-confirm" data-id="' + c + '">Éliminer définitivement</button><button class="btn o" data-act="eliminate-cancel">Annuler</button></div></div>' : '' ) +
			( list.length ? '<div class="tbl"><table><thead><tr><th>Document</th><th>Règle</th><th>Échéance</th><th>Sort final</th><th>Actions</th></tr></thead><tbody>' + list.map( function ( d ) {
				var u = dueOf( d ), r = u.rule;
				var elim = r.final !== 'Conservation définitive';
				var reasons = [];
				if ( d.hold ) reasons.push( 'gel juridique' );
				if ( ! u.past ) reasons.push( 'échéance non atteinte' );
				if ( ! can( 'eliminate' ) ) reasons.push( 'droit réservé à l’archiviste' );
				return '<tr><td><a href="#" data-open="' + d.id + '">' + esc( d.title ) + '</a><div class="muted" style="font-size:11.5px">' + esc( d.id ) + '</div></td><td>' + esc( r.label ) + ' · ' + r.years + ' ans<div class="muted" style="font-size:11.5px">' + esc( TRIGGERS[ r.trigger ] ) + '</div></td>' +
					'<td><b class="' + ( u.past ? 'bad' : 'warn' ) + '">' + frDate( u.due ) + '</b></td><td>' + esc( r.final ) + ( d.hold ? '<br><span class="tag r">Gel juridique</span>' : '' ) + '</td><td><div class="btns">' +
					( can( 'hold' ) ? '<button class="btn o sm" data-act="hold" data-id="' + d.id + '">' + ( d.hold ? 'Lever le gel' : 'Geler' ) + '</button>' : '' ) +
					( can( 'archive' ) ? '<select class="inp" style="width:auto;padding:4px 6px;font-size:12px" data-act-select="postpone" data-id="' + d.id + '" aria-label="Prolonger la conservation"><option value="">Conserver…</option><option value="1">+1 an</option><option value="3">+3 ans</option><option value="5">+5 ans</option></select>' : '' ) +
					( elim ? '<button class="btn danger o sm" data-act="eliminate" data-id="' + d.id + '"' + ( reasons.length ? ' disabled title="Impossible : ' + esc( reasons.join( ', ' ) ) + '"' : '' ) + '>Éliminer</button>' : '' ) +
					'</div>' + ( elim && reasons.length ? '<div class="muted" style="font-size:11px;margin-top:4px">Élimination bloquée : ' + esc( reasons.join( ', ' ) ) + '</div>' : '' ) + '</td></tr>';
			} ).join( '' ) + '</tbody></table></div>' : '<div class="empty">Aucune échéance sur cette période.</div>' ) + '</div>' +
			( S.certificates.length ? '<div class="box" style="margin-top:14px"><h2>Certificats d’élimination <small>conservés définitivement</small></h2><div class="tbl"><table><thead><tr><th>Certificat</th><th>Document</th><th>Date</th><th>Par</th><th>Empreinte du document éliminé</th></tr></thead><tbody>' +
				S.certificates.slice().reverse().map( function ( c ) { return '<tr><td><b>' + esc( c.id ) + '</b></td><td>' + esc( c.title ) + '<div class="muted" style="font-size:11.5px">' + esc( c.doc ) + ' · ' + esc( c.reason ) + '</div></td><td>' + frDateTime( c.at ) + '</td><td>' + esc( c.by ) + '</td><td class="mono">' + esc( c.sha.slice( 0, 24 ) ) + '…</td></tr>'; } ).join( '' ) + '</tbody></table></div></div>' : '' );
	};

	V.boxes = function () {
		var b = ui.box ? S.boxes.filter( function ( x ) { return x.id === ui.box; } )[ 0 ] : null;
		var list = '<div class="tbl"><table><thead><tr><th>ARCHIVA ID</th><th>Contenu</th><th>Localisation</th><th>Statut</th><th>Docs liés</th></tr></thead><tbody>' + S.boxes.map( function ( x ) {
			var n = S.docs.filter( function ( d ) { return d.box === x.id && d.status !== 'Éliminé'; } ).length;
			return '<tr class="clickable" data-box="' + x.id + '" tabindex="0"><td class="mono"><b>' + esc( x.id ) + '</b></td><td>' + esc( x.contents ) + '<div class="muted" style="font-size:11.5px">' + esc( x.service ) + '</div></td><td>' + esc( x.site + ', bât. ' + x.bat + ', salle ' + x.salle + ', rayon ' + x.rayon + ', étagère ' + x.etagere ) + '</td><td><span class="tag ' + ( x.status === 'En rayon' ? 'g' : 'a' ) + '">' + esc( x.status ) + '</span></td><td>' + n + '</td></tr>';
		} ).join( '' ) + '</tbody></table></div>';
		var form = can( 'boxes' ) ? '<div class="box"><h2>Nouvelle boîte</h2><form id="box-form"><div class="field"><label for="bx-contents">Contenu <span class="req">*</span></label><input id="bx-contents" required placeholder="Ex. : Dossiers du personnel 2010–2015"></div><div class="field"><label for="bx-service">Service versant</label><input id="bx-service" placeholder="Ex. : Ressources humaines"></div>' +
			'<div class="row2"><div class="field"><label for="bx-site">Site</label><input id="bx-site" value="Abidjan"></div><div class="field"><label for="bx-bat">Bâtiment</label><input id="bx-bat" value="B"></div></div>' +
			'<div class="row2"><div class="field"><label for="bx-salle">Salle</label><input id="bx-salle" value="03"></div><div class="field"><label for="bx-rayon">Rayon</label><input id="bx-rayon" value="12"></div></div>' +
			'<div class="field"><label for="bx-etagere">Étagère</label><input id="bx-etagere" value="06"></div><button class="btn">' + icon( 'box' ) + 'Créer la boîte et son QR code</button></form></div>' : '';
		var detail = '';
		if ( b ) {
			var docs = S.docs.filter( function ( d ) { return d.box === b.id && d.status !== 'Éliminé'; } );
			detail = '<div class="box" style="margin-bottom:14px"><h2>Boîte ' + esc( b.id ) + ' <small><button class="btn o sm" data-act="box-close">Fermer</button></small></h2><div class="grid g21"><div>' +
				'<div class="loc">' + [ [ 'Site', b.site ], [ 'Bâtiment', b.bat ], [ 'Salle', b.salle ], [ 'Rayon', b.rayon ], [ 'Étagère', b.etagere ], [ 'Boîte', b.boite ] ].map( function ( x ) { return '<div><small>' + x[ 0 ] + '</small><b>' + esc( x[ 1 ] ) + '</b></div>'; } ).join( '' ) + '</div>' +
				'<dl class="kv"><dt>Contenu</dt><dd>' + esc( b.contents ) + '</dd><dt>Service versant</dt><dd>' + esc( b.service ) + '</dd><dt>Statut</dt><dd>' + esc( b.status ) + '</dd></dl>' +
				'<h3 style="margin-top:14px">Documents numériques liés (originaux dans la boîte)</h3>' + ( docs.length ? docs.map( function ( d ) { return '<div><a href="#" data-open="' + d.id + '">' + esc( d.title ) + '</a></div>'; } ).join( '' ) : '<p class="muted">Aucun.</p>' ) +
				'<h3 style="margin-top:14px">Mouvements</h3>' + ( b.moves.length ? b.moves.slice().reverse().map( function ( m ) { return '<div class="muted">' + frDateTime( m.at ) + ' — ' + esc( m.what ) + ' (' + esc( m.by ) + ')</div>'; } ).join( '' ) : '<p class="muted">Aucun mouvement enregistré.</p>' ) +
				( can( 'boxes' ) ? '<div class="btns" style="margin-top:10px"><button class="btn o sm" data-act="box-move" data-id="' + b.id + '" data-what="' + ( b.status === 'En rayon' ? 'Sortie pour consultation' : 'Retour en rayon' ) + '">' + ( b.status === 'En rayon' ? 'Enregistrer une sortie' : 'Enregistrer le retour' ) + '</button></div>' : '' ) +
				'</div><div class="label"><div class="qr" id="qr"></div><b class="mono" style="display:block;margin-top:6px">' + esc( b.id ) + '</b><div class="muted" style="font-size:11.5px">' + esc( b.site + ' · Bât. ' + b.bat + ' · Salle ' + b.salle + ' · R' + b.rayon + ' · É' + b.etagere ) + '</div><button class="btn o sm" style="margin-top:10px" data-act="print">Imprimer l’étiquette</button></div></div></div>';
		}
		return head( 'Archives physiques', 'Chaque boîte a un identifiant unique, une localisation et un QR code', '' ) + detail + '<div class="grid g21"><div class="box">' + list + '</div>' + form + '</div>';
	};

	V.rules = function () {
		var edit = can( 'rules' );
		return head( 'Plan de classement et règles', 'Records management : séries, types de documents, durées de conservation', '' ) +
			'<div class="notice warn">Les durées affichées sont des <b>exemples</b>. Dans un vrai déploiement, elles sont fixées avec un archiviste et validées par un juriste selon votre secteur. ' + ( edit ? 'Toute modification recalcule les échéances et est inscrite au journal.' : 'Votre rôle ne permet pas de les modifier (Records manager ou Administrateur).' ) + '</div>' +
			'<div class="box" style="margin-bottom:14px"><h2>Règles de conservation</h2><div class="tbl"><table><thead><tr><th>Règle</th><th>Durée (ans)</th><th>Événement déclencheur</th><th>Sort final</th><th>Types concernés</th></tr></thead><tbody>' +
			S.rules.map( function ( r ) {
				return '<tr><td><b>' + esc( r.label ) + '</b></td><td>' + ( edit ? '<input class="inp" type="number" min="1" max="100" style="width:80px" data-rule="' + r.id + '" data-k="years" value="' + ( r.years == null ? '' : r.years ) + '" placeholder="perm." aria-label="Durée en années, vide pour permanent">' : ( r.years == null ? 'Permanente' : r.years ) ) + '</td>' +
					'<td>' + esc( TRIGGERS[ r.trigger ] ) + '</td><td>' + ( edit ? '<select class="inp" data-rule="' + r.id + '" data-k="final" aria-label="Sort final">' + FINALS.map( function ( f ) { return '<option' + ( f === r.final ? ' selected' : '' ) + '>' + f + '</option>'; } ).join( '' ) + '</select>' : esc( r.final ) ) + '</td>' +
					'<td class="muted">' + S.types.filter( function ( t ) { return t.rule === r.id; } ).map( function ( t ) { return esc( t.label ); } ).join( ', ' ) + '</td></tr>';
			} ).join( '' ) + '</tbody></table></div></div>' +
			'<div class="grid g2"><div class="box"><h2>Plan de classement</h2><div class="tbl"><table><thead><tr><th>Code</th><th>Fonction</th><th>Série</th></tr></thead><tbody>' + S.series.map( function ( s ) { return '<tr><td class="mono">' + s.code + '</td><td>' + esc( s.fn ) + '</td><td>' + esc( s.label ) + '</td></tr>'; } ).join( '' ) + '</tbody></table></div>' +
			( edit ? '<form id="series-form" style="margin-top:12px"><div class="row2"><div class="field"><label for="se-code">Code</label><input id="se-code" required placeholder="RH.02"></div><div class="field"><label for="se-fn">Fonction</label><input id="se-fn" required placeholder="Ressources humaines"></div></div><div class="field"><label for="se-label">Intitulé de la série</label><input id="se-label" required placeholder="Recrutement"></div><button class="btn o">Ajouter la série</button></form>' : '' ) + '</div>' +
			'<div class="box"><h2>Types de documents et métadonnées obligatoires</h2>' + S.types.map( function ( t ) { return '<div style="margin-bottom:10px"><b>' + esc( t.label ) + '</b> <span class="muted">→ ' + esc( t.series ) + ' · ' + esc( ( ruleOf( t.rule ) || {} ).label ) + '</span><div class="chips" style="margin-top:4px">' + ( t.fields.length ? t.fields.map( function ( f ) { return '<span class="tag ' + ( f.req ? 'b' : '' ) + '">' + esc( f.l ) + ( f.req ? ' *' : '' ) + '</span>'; } ).join( '' ) : '<span class="muted">Aucune métadonnée spécifique</span>' ) + '</div></div>'; } ).join( '' ) + '</div></div>';
	};

	V.audit = function () {
		var users = {};
		S.audit.forEach( function ( e ) { users[ e.user ] = 1; } );
		var list = S.audit.filter( function ( e ) { return ui.auditUser === 'all' || e.user === ui.auditUser; } ).slice().reverse();
		if ( ! can( 'audit' ) ) list = list.filter( function ( e ) { return e.user === me().name; } );
		return head( 'Audit trail', 'Qui, quoi, quand, quelle action. Chaque entrée est chaînée à la précédente par une empreinte SHA-256.',
			'<button class="btn o" data-act="verify-chain">' + icon( 'finger' ) + 'Vérifier l’intégrité du journal</button><button class="btn" data-act="export-audit">' + icon( 'download' ) + 'Exporter (CSV)</button>' ) +
			( can( 'audit' ) ? '' : '<div class="notice">Votre rôle ne voit que ses propres actions. Les rôles Archiviste, Records manager, Auditeur et Administrateur voient tout le journal.</div>' ) +
			'<div id="chain-result"></div><div class="box"><div class="toolbar"><label for="audit-user">Utilisateur</label><select id="audit-user"><option value="all">Tous</option>' + Object.keys( users ).map( function ( u ) { return '<option' + ( ui.auditUser === u ? ' selected' : '' ) + '>' + esc( u ) + '</option>'; } ).join( '' ) + '</select><span class="muted">' + list.length + ' événement(s)</span></div>' +
			'<div class="tbl"><table><thead><tr><th>#</th><th>Date et heure</th><th>Utilisateur</th><th>Action</th><th>Objet</th><th>Détail</th><th>Empreinte</th></tr></thead><tbody>' +
			list.slice( 0, 300 ).map( function ( e ) { return '<tr><td class="muted">' + e.n + '</td><td style="white-space:nowrap">' + frDateTime( e.at ) + '</td><td>' + esc( e.user ) + '<div class="muted" style="font-size:11px">' + esc( e.role ) + '</div></td><td><span class="tag ' + ( /ÉLIMINATION|ALTÉR|ÉCHEC/.test( e.action ) ? 'r' : /ARCHIV|VÉRIF/.test( e.action ) ? 'g' : '' ) + '">' + esc( e.action ) + '</span></td><td>' + esc( e.object ) + '</td><td class="muted">' + esc( e.detail ) + '</td><td class="mono" title="' + e.hash + '">' + e.hash.slice( 0, 10 ) + '…</td></tr>'; } ).join( '' ) +
			'</tbody></table></div></div>';
	};

	V.compliance = function () {
		var live = S.docs.filter( function ( d ) { return d.status !== 'Éliminé'; } );
		var miss = live.filter( function ( d ) { return missingMeta( d ).length; } );
		var bad = live.filter( function ( d ) { return d.integrity === 'altéré'; } );
		var never = live.filter( function ( d ) { return ! d.integrity; } );
		var past = live.filter( function ( d ) { var u = dueOf( d ); return u.past && ! d.hold; } );
		var admins = S.users.filter( function ( u ) { return u.role === 'admin'; } ).length;
		var backupOld = ! S.lastBackup || ( Date.now() - new Date( S.lastBackup ).getTime() ) > 7 * 864e5;
		var checks = [
			[ bad.length ? 'r' : 'g', bad.length ? bad.length + ' document(s) dont l’intégrité est altérée' : 'Intégrité : aucune altération détectée', bad.length ? 'Restaurez le document depuis une sauvegarde saine.' : 'Contrôle par empreinte SHA-256.', bad ],
			[ miss.length ? 'a' : 'g', miss.length ? miss.length + ' document(s) sans métadonnées obligatoires' : 'Métadonnées obligatoires complètes', 'Complétez les champs marqués * dans la fiche du document.', miss ],
			[ past.length ? 'a' : 'g', past.length ? past.length + ' document(s) ont dépassé leur échéance' : 'Aucune échéance dépassée non traitée', 'Examinez-les dans le Retention Center.', past ],
			[ never.length ? 'a' : 'g', never.length ? never.length + ' document(s) jamais vérifiés' : 'Tous les documents ont été vérifiés', 'Lancez « Vérifier tout » pour contrôler les empreintes.', [] ],
			[ backupOld ? 'a' : 'g', backupOld ? 'Sauvegarde : aucune exportée depuis 7 jours' : 'Sauvegarde récente (moins de 7 jours)', 'Exportez une sauvegarde et testez sa restauration.', [] ],
			[ admins > 2 ? 'a' : 'g', admins + ' administrateur(s)', admins > 2 ? 'Réduisez le nombre d’administrateurs (moindre privilège).' : 'Nombre d’administrateurs raisonnable.', [] ]
		];
		var okN = checks.filter( function ( c ) { return c[ 0 ] === 'g'; } ).length;
		var score = Math.round( okN / checks.length * 100 );
		var lab = { r: 'Risque', a: 'Action nécessaire', g: 'Conforme' }, col = { r: 'var(--red)', a: '#E5A93A', g: 'var(--green)' };
		return head( 'Compliance Center', 'État de conformité de l’organisation', ( can( 'audit' ) || can( 'archive' ) ? '<button class="btn" data-act="verify-all">' + icon( 'finger' ) + 'Vérifier tout</button>' : '' ) ) +
			'<div class="grid g21"><div class="box"><h2>Points de contrôle</h2>' + checks.map( function ( c ) {
				return '<div style="display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px solid #EEF1F6"><span style="width:10px;height:10px;border-radius:50%;background:' + col[ c[ 0 ] ] + ';margin-top:5px;flex-shrink:0"></span><div style="flex:1;min-width:0"><b>' + esc( c[ 1 ] ) + '</b><div class="muted" style="font-size:12px">' + esc( c[ 2 ] ) + '</div>' +
					( c[ 3 ].length ? '<div style="margin-top:4px">' + c[ 3 ].slice( 0, 6 ).map( function ( d ) { return '<a href="#" data-open="' + d.id + '" style="margin-right:10px;font-size:12.5px">' + esc( d.title ) + '</a>'; } ).join( '' ) + '</div>' : '' ) + '</div><span class="tag ' + c[ 0 ] + '">' + lab[ c[ 0 ] ] + '</span></div>';
			} ).join( '' ) + '</div><div class="box" style="text-align:center"><h2 style="justify-content:center">Score de conformité</h2><div style="font-size:48px;font-weight:800;color:var(--navy);letter-spacing:-.03em">' + score + '<span class="muted" style="font-size:16px"> / 100</span></div><div class="bar" style="margin:10px 0"><i style="width:' + score + '%"></i></div><p class="muted" style="font-size:12.5px">' + okN + ' contrôle(s) conforme(s) sur ' + checks.length + '. Indicateur de démonstration, sans valeur de certification.</p></div></div>';
	};

	V.users = function () {
		var adm = can( 'users' );
		return head( 'Utilisateurs et rôles', 'Rôle + périmètre + confidentialité, selon le principe du moindre privilège', '' ) +
			'<div class="grid g21"><div class="box"><div class="tbl"><table><thead><tr><th>Utilisateur</th><th>Service</th><th>Rôle</th></tr></thead><tbody>' + S.users.map( function ( u ) {
				return '<tr><td><div class="fi"><span class="av">' + esc( u.name.split( ' ' ).map( function ( w ) { return w[ 0 ]; } ).join( '' ).slice( 0, 2 ) ) + '</span>' + esc( u.name ) + ( u.id === S.current ? ' <span class="tag b">vous</span>' : '' ) + '</div></td><td>' + esc( u.service ) + '</td><td>' +
					( adm && u.id !== S.current ? '<select class="inp" style="width:auto" data-user-role="' + u.id + '" aria-label="Rôle de ' + esc( u.name ) + '">' + Object.keys( ROLES ).map( function ( r ) { return '<option value="' + r + '"' + ( u.role === r ? ' selected' : '' ) + '>' + ROLES[ r ].label + '</option>'; } ).join( '' ) + '</select>' : esc( ROLES[ u.role ].label ) ) + '</td></tr>';
			} ).join( '' ) + '</tbody></table></div>' + ( adm ? '' : '<p class="muted" style="margin:10px 0 0">Seul l’administrateur peut modifier les rôles. Utilisez le sélecteur en haut à droite pour changer d’utilisateur dans la démo.</p>' ) + '</div>' +
			'<div class="box"><h2>Ce que permet chaque rôle</h2>' + Object.keys( ROLES ).map( function ( r ) {
				var P = { upload: 'importer', edit: 'modifier', archive: 'archiver', eliminate: 'éliminer', hold: 'geler', boxes: 'boîtes', rules: 'règles', users: 'utilisateurs', backup: 'sauvegarde', confidential: 'voir le confidentiel', audit: 'journal complet', delete: 'supprimer (actifs)', tamper: 'simuler une altération' };
				return '<div style="margin-bottom:10px"><b>' + ROLES[ r ].label + '</b><div class="chips" style="margin-top:4px">' + ( ROLES[ r ].perms.filter( function ( p ) { return P[ p ]; } ).map( function ( p ) { return '<span class="tag">' + P[ p ] + '</span>'; } ).join( '' ) || '<span class="muted">lecture seule</span>' ) + '</div></div>';
			} ).join( '' ) + '</div></div>' +
			( adm ? '<div class="box" style="margin-top:14px;max-width:560px"><h2>Ajouter un utilisateur</h2><form id="user-form"><div class="row2"><div class="field"><label for="us-name">Nom</label><input id="us-name" required></div><div class="field"><label for="us-service">Service</label><input id="us-service"></div></div><div class="field"><label for="us-role">Rôle</label><select id="us-role">' + Object.keys( ROLES ).map( function ( r ) { return '<option value="' + r + '"' + ( r === 'employe' ? ' selected' : '' ) + '>' + ROLES[ r ].label + '</option>'; } ).join( '' ) + '</select></div><button class="btn">Ajouter</button></form></div>' : '' );
	};

	V.backup = function () {
		var ok = can( 'backup' );
		return head( 'Sauvegarde et restauration', 'Exportez l’intégralité de l’espace (documents, métadonnées, journal), puis restaurez-le : les empreintes sont vérifiées à la restauration.', '' ) +
			( ok ? '' : '<div class="notice">Votre rôle ne permet pas de sauvegarder ou restaurer. Passez en Archiviste ou Administrateur.</div>' ) +
			'<div class="grid g3"><div class="box"><h2>' + icon( 'download' ) + ' Exporter une sauvegarde</h2><p class="muted">Un fichier JSON contenant tous les documents (encodés), leurs métadonnées, les règles, les boîtes et le journal d’audit.</p><p>Dernière sauvegarde : <b>' + ( S.lastBackup ? frDateTime( S.lastBackup ) : 'jamais' ) + '</b></p><button class="btn" data-act="backup-export"' + ( ok ? '' : ' disabled' ) + '>Exporter maintenant</button></div>' +
			'<div class="box"><h2>' + icon( 'upload' ) + ' Restaurer</h2><p class="muted">Choisissez un fichier de sauvegarde ARCHIVA360. Chaque fichier est contrôlé par son empreinte avant d’être restauré.</p><label class="btn o" for="restore-input"' + ( ok ? '' : ' style="pointer-events:none;opacity:.45"' ) + '>Choisir un fichier…</label><input type="file" id="restore-input" accept=".json,application/json" class="sr"' + ( ok ? '' : ' disabled' ) + '><div id="restore-result" style="margin-top:10px"></div></div>' +
			'<div class="box"><h2>' + icon( 'layers' ) + ' Réinitialiser la démo</h2><p class="muted">Efface toutes les données de démonstration de ce navigateur et recrée l’espace d’exemple.</p>' + ( ui.confirm === 'reset' ? '<div class="confirm"><p><b>Tout effacer et recommencer ?</b></p><div class="btns"><button class="btn danger" data-act="reset-confirm">Réinitialiser</button><button class="btn o" data-act="eliminate-cancel">Annuler</button></div></div>' : '<button class="btn danger o" data-act="reset">Réinitialiser…</button>' ) + '</div></div>' +
			'<div class="box" style="margin-top:14px"><h2>La règle 3-2-1</h2><p class="muted" style="margin:0">Dans un vrai déploiement ARCHIVA360 : 3 copies, sur 2 supports différents, dont 1 hors site, avec des tests de restauration planifiés. Ici, la sauvegarde exportée est votre copie hors site : conservez-la ailleurs que sur cet ordinateur.</p></div>';
	};

	/* Document drawer */
	function drawer() {
		var d = docById( ui.open );
		if ( ! d ) return '';
		var t = typeOf( d.type ), v = current( d ), u = dueOf( d ), miss = missingMeta( d ).map( function ( f ) { return f.k; } );
		var locked = d.status !== 'Actif' || ! ( can( 'editAny' ) || ( can( 'edit' ) && d.createdBy === S.current ) );
		var prop = d.proposed || {};
		var tabs = [ [ 'apercu', 'Aperçu' ], [ 'meta', 'Métadonnées' ], [ 'versions', 'Versions et intégrité' ], [ 'historique', 'Historique' ] ];
		var body = '';
		if ( ui.tab === 'apercu' ) {
			body = ( d.status === 'Éliminé' ? '<div class="notice bad">Document éliminé le ' + frDateTime( d.eliminatedAt ) + '. Seules ses métadonnées et le certificat d’élimination sont conservés.</div>' : '<div class="preview" id="preview"><span class="muted">Chargement de l’aperçu…</span></div>' ) +
				'<h3>Texte du document ' + ( d.textSource ? '<span class="tag">' + esc( d.textSource ) + '</span>' : '' ) + '</h3>' +
				( d.text ? '<div class="preview" style="min-height:0;place-items:stretch"><pre>' + esc( d.text.slice( 0, 4000 ) ) + '</pre></div>' : '<p class="muted">Aucun texte extrait pour l’instant.</p>' ) +
				( d.status !== 'Éliminé' && can( 'edit' ) ? '<button class="btn o" data-act="ocr" data-id="' + d.id + '">' + icon( 'sparkles' ) + ( d.text ? 'Relancer l’extraction' : 'Extraire le texte (OCR)' ) + '</button><div class="progress-ocr" id="ocr-progress"></div>' : '' );
		} else if ( ui.tab === 'meta' ) {
			body = ( prop && Object.keys( prop ).length ? '<div class="notice">' + icon( 'sparkles' ) + ' Des valeurs ont été <b>proposées automatiquement</b> à partir du texte (champs en bleu). Vérifiez-les puis enregistrez.</div>' : '' ) +
				( miss.length ? '<div class="notice warn">Champs obligatoires manquants : ' + missingMeta( d ).map( function ( f ) { return esc( f.l ); } ).join( ', ' ) + '.</div>' : '' ) +
				( locked && d.status === 'Archivé' ? '<div class="notice">Document archivé : ses métadonnées sont figées (intégrité du SAE).</div>' : locked ? '<div class="notice">Lecture seule pour votre rôle.</div>' : '' ) +
				'<form id="meta-form"><div class="field"><label for="m-title">Titre</label><input id="m-title" value="' + esc( d.title ) + '"' + ( locked ? ' disabled' : '' ) + '></div>' +
				'<div class="row2"><div class="field' + ( prop.type ? ' proposed' : '' ) + '"><label for="m-type">Type de document</label><select id="m-type"' + ( locked ? ' disabled' : '' ) + '>' + S.types.map( function ( x ) { return '<option value="' + x.id + '"' + ( x.id === d.type ? ' selected' : '' ) + '>' + esc( x.label ) + '</option>'; } ).join( '' ) + '</select></div>' +
				'<div class="field"><label for="m-series">Série (plan de classement)</label><select id="m-series"' + ( locked ? ' disabled' : '' ) + '>' + S.series.map( function ( s ) { return '<option value="' + s.code + '"' + ( s.code === d.series ? ' selected' : '' ) + '>' + s.code + ' — ' + esc( s.label ) + '</option>'; } ).join( '' ) + '</select></div></div>' +
				'<div class="row2"><div class="field' + ( prop.date ? ' proposed' : '' ) + '"><label for="m-date">Date du document</label><input type="date" id="m-date" value="' + esc( d.date ) + '"' + ( locked ? ' disabled' : '' ) + '></div>' +
				'<div class="field"><label for="m-conf">Confidentialité</label><select id="m-conf"' + ( locked ? ' disabled' : '' ) + '>' + CONF.map( function ( c ) { return '<option' + ( c === d.conf ? ' selected' : '' ) + '>' + c + '</option>'; } ).join( '' ) + '</select></div></div>' +
				t.fields.map( function ( f ) {
					var val = d.meta[ f.k ] != null ? d.meta[ f.k ] : '';
					var isProp = prop.meta && prop.meta[ f.k ] != null && String( prop.meta[ f.k ] ) === String( val );
					return '<div class="field' + ( isProp ? ' proposed' : '' ) + '"><label for="mf-' + f.k + '">' + esc( f.l ) + ( f.req ? ' <span class="req">*</span>' : '' ) + '</label><input id="mf-' + f.k + '" data-meta="' + f.k + '"' + ( f.date ? ' type="date"' : f.num ? ' type="number" min="0" step="1"' : '' ) + ' value="' + esc( val ) + '"' + ( locked ? ' disabled' : '' ) + '>' + ( isProp ? '<span class="hint">Proposé par l’extraction automatique</span>' : '' ) + ( f.num && val ? '<span class="hint">' + fcfa( val ) + '</span>' : '' ) + '</div>';
				} ).join( '' ) +
				( locked ? '' : '<button class="btn">' + icon( 'check' ) + 'Enregistrer les métadonnées</button>' ) + '</form>' +
				'<dl class="kv" style="margin-top:14px"><dt>Identifiant</dt><dd class="mono">' + esc( d.id ) + '</dd><dt>Règle</dt><dd>' + esc( u.rule ? u.rule.label + ( u.rule.years ? ' · ' + u.rule.years + ' ans' : '' ) + ' · ' + u.rule.final : '—' ) + '</dd><dt>Échéance</dt><dd>' + esc( u.label ) + '</dd><dt>Créé par</dt><dd>' + esc( userName( d.createdBy ) ) + ' le ' + frDateTime( d.createdAt ) + '</dd>' + ( d.archivedAt ? '<dt>Archivé le</dt><dd>' + frDateTime( d.archivedAt ) + '</dd>' : '' ) + '</dl>';
		} else if ( ui.tab === 'versions' ) {
			body = '<div class="tbl"><table><thead><tr><th>Version</th><th>Fichier</th><th>Taille</th><th>Déposée</th><th>SHA-256</th></tr></thead><tbody>' + d.versions.slice().reverse().map( function ( x ) { return '<tr><td><b>v' + x.v + '</b></td><td>' + esc( x.name ) + '</td><td>' + size( x.size ) + '</td><td>' + frDateTime( x.at ) + '<div class="muted" style="font-size:11px">' + esc( userName( x.by ) ) + '</div></td><td class="mono">' + x.sha + '</td></tr>'; } ).join( '' ) + '</tbody></table></div>' +
				'<div style="margin:12px 0" id="verify-out">' + ( d.integrity === 'intègre' ? '<div class="notice ok">Dernière vérification : empreinte identique, document intègre (' + frDateTime( d.verifiedAt ) + ').</div>' : d.integrity === 'altéré' ? '<div class="notice bad">Dernière vérification : <b>empreinte différente, document altéré</b> (' + frDateTime( d.verifiedAt ) + '). Restaurez-le depuis une sauvegarde.</div>' : '<div class="notice">Ce document n’a pas encore été vérifié.</div>' ) + '</div>' +
				'<div class="btns">' + ( d.status !== 'Éliminé' ? '<button class="btn" data-act="verify" data-id="' + d.id + '">' + icon( 'finger' ) + 'Vérifier l’intégrité</button>' : '' ) +
				( d.status === 'Actif' && ( can( 'editAny' ) || ( can( 'edit' ) && d.createdBy === S.current ) ) ? '<label class="btn o" for="version-input">' + icon( 'upload' ) + 'Déposer une nouvelle version</label><input type="file" id="version-input" class="sr" data-id="' + d.id + '">' : '' ) +
				( d.status !== 'Éliminé' && can( 'tamper' ) ? '<button class="btn danger o" data-act="tamper" data-id="' + d.id + '" title="Modifie un octet du fichier stocké sans passer par l’application, pour montrer la détection">Simuler une altération</button>' : '' ) + '</div>' +
				'<p class="muted" style="font-size:12px;margin-top:10px">La simulation modifie directement le fichier stocké, comme le ferait une corruption de disque ou une manipulation hors application. La vérification recalcule l’empreinte et la compare à celle enregistrée au dépôt.</p>';
		} else {
			var hist = S.audit.filter( function ( e ) { return e.object === d.title || e.object === d.id || e.detail.indexOf( d.id ) !== -1; } ).slice().reverse();
			body = hist.length ? '<div class="tbl"><table><tbody>' + hist.map( function ( e ) { return '<tr><td class="muted" style="white-space:nowrap">' + frDateTime( e.at ) + '</td><td>' + esc( e.user ) + '</td><td><span class="tag">' + esc( e.action ) + '</span></td><td class="muted">' + esc( e.detail ) + '</td></tr>'; } ).join( '' ) + '</tbody></table></div>' : '<p class="muted">Aucun événement.</p>';
		}
		var actions = '';
		if ( d.status !== 'Éliminé' ) {
			actions += '<button class="btn o" data-act="download" data-id="' + d.id + '">' + icon( 'download' ) + 'Télécharger</button>';
			if ( d.status === 'Actif' && can( 'archive' ) ) actions += '<button class="btn" data-act="archive" data-id="' + d.id + '"' + ( miss.length ? ' disabled title="Complétez d’abord les métadonnées obligatoires"' : '' ) + '>' + icon( 'archive' ) + 'Verser au SAE</button>';
			if ( can( 'hold' ) ) actions += '<button class="btn o" data-act="hold" data-id="' + d.id + '">' + icon( 'lock' ) + ( d.hold ? 'Lever le gel juridique' : 'Gel juridique' ) + '</button>';
			if ( can( 'boxes' ) ) actions += '<select class="inp" style="width:auto" data-act-select="link-box" data-id="' + d.id + '" aria-label="Boîte de l’original"><option value="">Original papier : ' + ( d.box ? esc( d.box ) : 'aucune boîte' ) + '</option><option value="none">Aucune boîte</option>' + S.boxes.map( function ( b ) { return '<option value="' + b.id + '">' + esc( b.id ) + '</option>'; } ).join( '' ) + '</select>';
			if ( d.status === 'Actif' && ( can( 'delete' ) || ( can( 'edit' ) && d.createdBy === S.current ) ) ) actions += ui.confirm === 'del-' + d.id ? '<span class="confirm" style="margin:0;padding:6px 10px">Supprimer ce document actif ? <button class="btn danger sm" data-act="delete-confirm" data-id="' + d.id + '">Supprimer</button> <button class="btn o sm" data-act="eliminate-cancel">Annuler</button></span>' : '<button class="btn danger o" data-act="delete" data-id="' + d.id + '">Supprimer</button>';
		}
		return '<div class="drawer-backdrop" data-act="close"></div><aside class="drawer" role="dialog" aria-modal="true" aria-labelledby="dr-title"><header><div>' + ftype( d ) + '</div><div style="min-width:0"><h1 id="dr-title">' + esc( d.title ) + '</h1><p class="sub">' + esc( d.id ) + ' · ' + esc( t.label ) + ' · ' + statusTag( d ) + ' ' + confTag( d.conf ) + ( d.box ? ' <span class="tag">Original : ' + esc( d.box ) + '</span>' : '' ) + '</p></div><button class="x" data-act="close" aria-label="Fermer">×</button></header>' +
			'<div class="body"><div class="tabs" role="tablist">' + tabs.map( function ( x ) { return '<button role="tab" data-tab="' + x[ 0 ] + '" aria-selected="' + ( ui.tab === x[ 0 ] ) + '">' + x[ 1 ] + '</button>'; } ).join( '' ) + '</div>' + body + '</div>' +
			( actions ? '<div class="actions">' + actions + '</div>' : '' ) + '</aside>';
	}

	/* =====================================================================
	 * Rendering
	 * ===================================================================== */
	var NAV = [
		[ 'dashboard', 'Tableau de bord', 'chart' ], [ 'documents', 'Documents', 'files' ], [ 'search', 'Recherche', 'search' ],
		[ 'SEP', 'Archivage' ], [ 'retention', 'Retention Center', 'clock' ], [ 'rules', 'Plan et règles', 'hourglass' ], [ 'boxes', 'Archives physiques', 'box' ],
		[ 'SEP', 'Pilotage' ], [ 'audit', 'Audit trail', 'eye' ], [ 'compliance', 'Conformité', 'shield' ], [ 'users', 'Utilisateurs et rôles', 'users' ], [ 'backup', 'Sauvegarde', 'drive' ]
	];
	var urlCache = [];
	function render() {
		if ( ! S ) return;
		var live = S.docs.filter( function ( d ) { return d.status !== 'Éliminé' && visible( d ); } );
		var due = live.filter( function ( d ) { var u = dueOf( d ); return u.due && u.due <= addDays( todayISO(), 90 ); } ).length;
		$( '#nav' ).innerHTML = NAV.map( function ( n ) {
			if ( n[ 0 ] === 'SEP' ) return '<div class="sep">' + n[ 1 ] + '</div>';
			var badge = n[ 0 ] === 'documents' ? '<span class="n">' + live.length + '</span>' : n[ 0 ] === 'retention' && due ? '<span class="n warn">' + due + '</span>' : '';
			return '<button data-go="' + n[ 0 ] + '"' + ( ui.view === n[ 0 ] ? ' aria-current="page"' : '' ) + '>' + icon( n[ 2 ] ) + n[ 1 ] + badge + '</button>';
		} ).join( '' );
		$( '#who' ).innerHTML = S.users.map( function ( u ) { return '<option value="' + u.id + '"' + ( u.id === S.current ? ' selected' : '' ) + '>' + esc( u.name ) + ' — ' + esc( ROLES[ u.role ].label ) + '</option>'; } ).join( '' );
		$( '#who-av' ).textContent = me().name.split( ' ' ).map( function ( w ) { return w[ 0 ]; } ).join( '' ).slice( 0, 2 );
		var focusId = document.activeElement && document.activeElement.id;
		var caret = focusId && document.activeElement.selectionStart;
		$( '#view' ).innerHTML = V[ ui.view ]();
		$( '#drawer' ).innerHTML = drawer();
		if ( focusId && $( '#' + focusId ) && /f-q|search-q|confirm-reason/.test( focusId ) ) { var el = $( '#' + focusId ); el.focus(); try { el.setSelectionRange( caret, caret ); } catch ( e ) {} }
		urlCache.forEach( URL.revokeObjectURL ); urlCache = [];
		if ( ui.open && ui.tab === 'apercu' ) renderPreview();
		if ( ui.view === 'boxes' && ui.box ) renderQR();
		bindDrop();
	}
	function renderPreview() {
		var d = docById( ui.open ), box = $( '#preview' );
		if ( ! d || ! box ) return;
		var v = current( d );
		store.get( 'files', d.id + '@' + v.v ).then( function ( buf ) {
			if ( ! buf ) { box.innerHTML = '<span class="muted">Fichier introuvable.</span>'; return; }
			var kind = ext( v.name, v.mime ), url = URL.createObjectURL( new Blob( [ buf ], { type: v.mime || 'application/octet-stream' } ) );
			urlCache.push( url );
			if ( kind === 'img' ) box.innerHTML = '<img src="' + url + '" alt="Aperçu de ' + esc( d.title ) + '">';
			else if ( kind === 'pdf' ) box.innerHTML = '<iframe src="' + url + '" title="Aperçu PDF"></iframe>';
			else if ( kind === 'txt' && ! /\.(docx?|xlsx?|odt|ods|zip)$/i.test( v.name ) ) box.innerHTML = '<pre>' + esc( new TextDecoder().decode( buf ).slice( 0, 20000 ) ) + '</pre>';
			else box.innerHTML = '<p class="muted" style="padding:20px;text-align:center">Aperçu non disponible pour ce format dans la démo.<br>Utilisez « Télécharger ».</p>';
		} );
	}
	function renderQR() {
		var b = S.boxes.filter( function ( x ) { return x.id === ui.box; } )[ 0 ], el = $( '#qr' );
		if ( ! b || ! el ) return;
		var payload = 'ARCHIVA360|' + b.id + '|' + b.site + '|B' + b.bat + '|S' + b.salle + '|R' + b.rayon + '|E' + b.etagere;
		loadScript( 'https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js' ).then( function () {
			var q = window.qrcode( 0, 'M' ); q.addData( payload ); q.make();
			el.innerHTML = '<img alt="QR code de la boîte ' + esc( b.id ) + '" style="image-rendering:pixelated" src="' + q.createDataURL( 4, 0 ) + '">';
		} ).catch( function () { el.innerHTML = '<p class="muted" style="font-size:12px">QR code indisponible hors connexion.<br><span class="mono">' + esc( payload ) + '</span></p>'; } );
	}

	/* =====================================================================
	 * Actions
	 * ===================================================================== */
	function go( view ) { ui.view = view; ui.open = null; ui.confirm = null; try { history.replaceState( null, '', '#' + view ); } catch ( e ) {} render(); window.scrollTo( 0, 0 ); }
	function openDoc( id, tab ) {
		var d = docById( id ); if ( ! d ) return;
		ui.open = id; ui.tab = tab || 'apercu'; ui.confirm = null; render();
		if ( d.status !== 'Éliminé' ) log( 'CONSULTATION', d.title, d.id );
	}
	function importFiles( files ) {
		if ( ! can( 'upload' ) ) { toast( 'Votre rôle ne permet pas d’importer.' ); return; }
		var list = Array.prototype.slice.call( files || [] );
		if ( ! list.length ) return;
		var chain = Promise.resolve(), last = null;
		list.forEach( function ( f ) {
			chain = chain.then( function () {
				if ( f.size > 25 * 1048576 ) { toast( f.name + ' : fichier trop volumineux pour la démo (25 Mo max).' ); return; }
				return f.arrayBuffer().then( function ( buf ) {
					var isText = /^text\//.test( f.type ) || /\.(txt|csv|md)$/i.test( f.name );
					var text = isText ? new TextDecoder().decode( buf ) : '';
					var p = propose( text, f.name );
					var meta = p.meta || {};
					return addDocument( f, buf, { type: p.type || 'autre', date: p.date, meta: meta, text: text, proposed: ( p.type || p.date || Object.keys( meta ).length ) ? p : null } ).then( function ( d ) {
						last = d;
						return log( 'IMPORT', d.title, d.id + ' · ' + f.name + ' · SHA-256 ' + d.versions[ 0 ].sha.slice( 0, 16 ) + '…' );
					} );
				} );
			} );
		} );
		chain.then( function () {
			persist();
			toast( list.length + ' document(s) importé(s). Empreinte SHA-256 calculée.' );
			if ( last ) { ui.view = 'documents'; openDoc( last.id, last.proposed ? 'meta' : 'apercu' ); } else render();
		} );
	}
	function bindDrop() {
		var drop = $( '#drop' );
		if ( ! drop || drop.dataset.bound ) return;
		drop.dataset.bound = '1';
		[ 'dragenter', 'dragover' ].forEach( function ( ev ) { drop.addEventListener( ev, function ( e ) { e.preventDefault(); drop.classList.add( 'over' ); } ); } );
		[ 'dragleave', 'drop' ].forEach( function ( ev ) { drop.addEventListener( ev, function ( e ) { e.preventDefault(); drop.classList.remove( 'over' ); } ); } );
		drop.addEventListener( 'drop', function ( e ) { importFiles( e.dataTransfer.files ); } );
	}
	function verifyDoc( d, quiet ) {
		var v = current( d );
		return store.get( 'files', d.id + '@' + v.v ).then( function ( buf ) {
			if ( ! buf ) return 'absent';
			return sha256( buf ).then( function ( h ) {
				var ok = h === v.sha;
				d.integrity = ok ? 'intègre' : 'altéré'; d.verifiedAt = nowISO(); persist();
				if ( ! quiet || ! ok ) log( ok ? 'VÉRIFICATION INTÉGRITÉ' : 'ÉCHEC INTÉGRITÉ', d.title, ok ? 'Empreinte identique' : 'Empreinte calculée ' + h.slice( 0, 16 ) + '… ≠ enregistrée ' + v.sha.slice( 0, 16 ) + '…' );
				return d.integrity;
			} );
		} );
	}
	function download( blob, name ) {
		var a = document.createElement( 'a' ); a.href = URL.createObjectURL( blob ); a.download = name;
		document.body.appendChild( a ); a.click(); setTimeout( function () { URL.revokeObjectURL( a.href ); a.remove(); }, 1000 );
	}

	document.addEventListener( 'click', function ( e ) {
		var t = e.target.closest( '[data-go],[data-open],[data-act],[data-tab],[data-series],[data-example],[data-box]' );
		if ( ! t ) return;
		if ( t.tagName === 'SELECT' ) return;
		if ( t.hasAttribute( 'data-go' ) ) {
			e.preventDefault(); go( t.getAttribute( 'data-go' ) );
			if ( t.getAttribute( 'data-then' ) === 'upload' ) setTimeout( function () { var fi = $( '#file-input' ); if ( fi ) fi.click(); }, 50 );
			return;
		}
		if ( t.hasAttribute( 'data-open' ) ) { e.preventDefault(); openDoc( t.getAttribute( 'data-open' ) ); return; }
		if ( t.hasAttribute( 'data-tab' ) ) { ui.tab = t.getAttribute( 'data-tab' ); render(); return; }
		if ( t.hasAttribute( 'data-series' ) ) { ui.series = t.getAttribute( 'data-series' ); render(); return; }
		if ( t.hasAttribute( 'data-example' ) ) { ui.searchQ = t.getAttribute( 'data-example' ); log( 'RECHERCHE', ui.searchQ, '' ); render(); return; }
		if ( t.hasAttribute( 'data-box' ) ) { ui.box = t.getAttribute( 'data-box' ); render(); log( 'CONSULTATION', 'Boîte ' + ui.box, 'Fiche de la boîte' ); return; }
		var act = t.getAttribute( 'data-act' ), id = t.getAttribute( 'data-id' ), d = id ? docById( id ) : null;
		switch ( act ) {
			case 'close': ui.open = null; ui.confirm = null; render(); break;
			case 'box-close': ui.box = null; render(); break;
			case 'print': window.print(); break;
			case 'download':
				store.get( 'files', d.id + '@' + current( d ).v ).then( function ( buf ) { download( new Blob( [ buf ], { type: current( d ).mime } ), current( d ).name ); log( 'TÉLÉCHARGEMENT', d.title, d.id ); } );
				break;
			case 'archive':
				if ( missingMeta( d ).length ) { toast( 'Complétez les métadonnées obligatoires avant le versement.' ); break; }
				verifyDoc( d, true ).then( function ( st ) {
					if ( st !== 'intègre' ) { toast( 'Versement refusé : intégrité non confirmée.' ); render(); return; }
					d.status = 'Archivé'; d.archivedAt = nowISO(); persist();
					log( 'ARCHIVAGE (VERSEMENT SAE)', d.title, d.id + ' figé · règle ' + dueOf( d ).rule.label + ' · échéance ' + dueOf( d ).label );
					toast( 'Document versé au SAE : il est désormais figé.' ); render();
				} );
				break;
			case 'hold':
				d.hold = ! d.hold; persist();
				log( d.hold ? 'GEL JURIDIQUE' : 'LEVÉE DU GEL JURIDIQUE', d.title, d.id );
				toast( d.hold ? 'Gel juridique appliqué : toute élimination est bloquée.' : 'Gel juridique levé.' ); render(); break;
			case 'eliminate':
				if ( d.hold ) { toast( 'Impossible : document sous gel juridique.' ); break; }
				ui.confirm = id; render(); var r = $( '#confirm-reason' ); if ( r ) r.focus(); break;
			case 'eliminate-cancel': ui.confirm = null; render(); break;
			case 'eliminate-confirm':
				if ( ! can( 'eliminate' ) || d.hold || ! dueOf( d ).past ) { toast( 'Élimination refusée.' ); ui.confirm = null; render(); break; }
				var reason = ( $( '#confirm-reason' ) || {} ).value || '';
				S.certSeq++;
				var cert = { id: 'CERT-ELIM-' + new Date().getFullYear() + '-' + pad( S.certSeq, 4 ), doc: d.id, title: d.title, at: nowISO(), by: me().name, reason: reason, sha: current( d ).sha, rule: dueOf( d ).rule.label };
				S.certificates.push( cert );
				var keys = d.versions.map( function ( x ) { return d.id + '@' + x.v; } );
				Promise.all( keys.map( function ( k ) { return store.del( 'files', k ); } ) ).then( function () {
					d.status = 'Éliminé'; d.eliminatedAt = cert.at; d.text = ''; persist();
					log( 'ÉLIMINATION', d.title, cert.id + ' · ' + d.id + ' · motif : ' + reason + ' · SHA-256 ' + cert.sha.slice( 0, 16 ) + '…' );
					ui.confirm = null; toast( 'Document éliminé. Certificat ' + cert.id + ' créé.' ); render();
				} );
				break;
			case 'delete': ui.confirm = 'del-' + id; render(); break;
			case 'delete-confirm':
				Promise.all( d.versions.map( function ( x ) { return store.del( 'files', d.id + '@' + x.v ); } ) ).then( function () {
					S.docs = S.docs.filter( function ( x ) { return x !== d; } ); persist();
					log( 'SUPPRESSION (DOCUMENT ACTIF)', d.title, d.id ); ui.open = null; ui.confirm = null; toast( 'Document supprimé. Il reste récupérable depuis une sauvegarde.' ); render();
				} );
				break;
			case 'verify':
				verifyDoc( d ).then( function ( st ) { toast( st === 'intègre' ? 'Document intègre : empreinte identique.' : 'Altération détectée : empreinte différente.' ); render(); } );
				break;
			case 'verify-all':
				var live = S.docs.filter( function ( x ) { return x.status !== 'Éliminé'; } ), bad = 0;
				live.reduce( function ( p, x ) { return p.then( function () { return verifyDoc( x, true ).then( function ( st ) { if ( st !== 'intègre' ) bad++; } ); } ); }, Promise.resolve() ).then( function () {
					log( 'VÉRIFICATION GLOBALE', live.length + ' documents', bad ? bad + ' altération(s) détectée(s)' : 'Aucune altération' );
					toast( live.length + ' documents vérifiés · ' + ( bad ? bad + ' altération(s)' : 'aucune altération' ) ); render();
				} );
				break;
			case 'tamper':
				var key = d.id + '@' + current( d ).v;
				store.get( 'files', key ).then( function ( buf ) {
					var a = new Uint8Array( buf.slice( 0 ) ); a[ Math.floor( a.length / 2 ) ] ^= 0x20;
					return store.put( 'files', key, a.buffer );
				} ).then( function () { log( 'SIMULATION D’ALTÉRATION', d.title, 'Un octet du fichier stocké a été modifié hors application (démonstration)' ); toast( 'Fichier altéré. Lancez « Vérifier l’intégrité ».' ); render(); } );
				break;
			case 'ocr':
				var prog = $( '#ocr-progress' ); t.disabled = true;
				if ( prog ) prog.textContent = 'Extraction en cours…';
				extractText( d, function ( m ) { if ( prog ) prog.textContent = m; } ).then( function ( r ) {
					d.text = r.text.trim(); d.textSource = r.source;
					var p = propose( d.text, current( d ).name ), filled = [];
					if ( d.status === 'Actif' ) {
						if ( d.type === 'autre' && p.type ) { d.type = p.type; d.series = typeOf( p.type ).series; filled.push( 'type' ); }
						Object.keys( p.meta || {} ).forEach( function ( k ) { if ( d.meta[ k ] == null || d.meta[ k ] === '' ) { d.meta[ k ] = p.meta[ k ]; filled.push( k ); } } );
						d.proposed = p;
					}
					persist();
					log( 'EXTRACTION DU TEXTE', d.title, r.source + ' · ' + d.text.length + ' caractères' + ( filled.length ? ' · proposés : ' + filled.join( ', ' ) : '' ) );
					toast( 'Texte extrait' + ( filled.length ? ' et ' + filled.length + ' métadonnée(s) proposée(s)' : '' ) + '.' );
					ui.tab = filled.length ? 'meta' : 'apercu'; render();
				} ).catch( function ( err ) { if ( prog ) prog.textContent = err.message + ( /Chargement/.test( err.message ) ? ' Vérifiez votre connexion internet : le moteur OCR est chargé à la demande.' : '' ); t.disabled = false; } );
				break;
			case 'verify-chain':
				verifyChain().then( function ( r ) {
					$( '#chain-result' ).innerHTML = r.ok ? '<div class="notice ok">Journal intègre : les ' + r.n + ' entrées sont correctement chaînées.</div>' : '<div class="notice bad">Rupture de la chaîne à l’entrée n°' + r.at + ' : le journal a été modifié.</div>';
				} );
				break;
			case 'export-audit':
				var rows = [ [ 'n', 'date', 'utilisateur', 'role', 'action', 'objet', 'detail', 'empreinte_precedente', 'empreinte' ] ].concat( S.audit.map( function ( x ) { return [ x.n, x.at, x.user, x.role, x.action, x.object, x.detail, x.prev, x.hash ]; } ) );
				download( new Blob( [ '﻿' + rows.map( function ( r ) { return r.map( function ( c ) { return '"' + String( c ).replace( /"/g, '""' ) + '"'; } ).join( ';' ); } ).join( '\r\n' ) ], { type: 'text/csv;charset=utf-8' } ), 'archiva360-audit-trail-' + todayISO() + '.csv' );
				log( 'EXPORT DU JOURNAL', 'Audit trail', S.audit.length + ' entrées' );
				break;
			case 'box-move':
				var b = S.boxes.filter( function ( x ) { return x.id === id; } )[ 0 ], what = t.getAttribute( 'data-what' );
				b.moves.push( { at: nowISO(), what: what, by: me().name } ); b.status = b.status === 'En rayon' ? 'Sortie' : 'En rayon'; persist();
				log( 'MOUVEMENT DE BOÎTE', 'Boîte ' + b.id, what ); render(); break;
			case 'backup-export': exportBackup(); break;
			case 'reset': ui.confirm = 'reset'; render(); break;
			case 'reset-confirm':
				store.clear().then( seed ).then( function () { ui = { view: 'dashboard', series: 'all', type: 'all', status: 'all', q: '', open: null, tab: 'apercu', horizon: '90', confirm: null, box: null, auditUser: 'all', searchQ: '' }; toast( 'Démo réinitialisée.' ); render(); } );
				break;
		}
	} );

	document.addEventListener( 'keydown', function ( e ) {
		if ( e.key === 'Escape' && ui.open ) { ui.open = null; render(); }
		if ( e.key === 'Enter' && e.target.matches( 'tr[data-open],tr[data-box]' ) ) e.target.click();
	} );

	document.addEventListener( 'change', function ( e ) {
		var t = e.target;
		if ( t.id === 'who' ) {
			var prev = me(); S.current = t.value; persist();
			log( 'CHANGEMENT D’UTILISATEUR', me().name, 'De ' + prev.name + ' (' + ROLES[ prev.role ].label + ') vers ' + me().name + ' (' + ROLES[ me().role ].label + ')' );
			ui.open = null; ui.confirm = null; toast( 'Vous êtes maintenant ' + me().name + ' — ' + ROLES[ me().role ].label ); render(); return;
		}
		if ( t.id === 'file-input' ) { importFiles( t.files ); t.value = ''; return; }
		if ( t.id === 'version-input' ) {
			var d = docById( t.getAttribute( 'data-id' ) ), f = t.files[ 0 ];
			if ( ! f ) return;
			f.arrayBuffer().then( function ( buf ) {
				return sha256( buf ).then( function ( h ) {
					var v = { v: current( d ).v + 1, name: f.name, mime: f.type || 'application/octet-stream', size: buf.byteLength, sha: h, at: nowISO(), by: S.current };
					return store.put( 'files', d.id + '@' + v.v, buf ).then( function () {
						d.versions.push( v ); d.integrity = null; d.text = ''; d.textSource = ''; persist();
						log( 'NOUVELLE VERSION', d.title, d.id + ' · v' + v.v + ' · SHA-256 ' + h.slice( 0, 16 ) + '…' ); toast( 'Version ' + v.v + ' déposée.' ); render();
					} );
				} );
			} );
			return;
		}
		if ( t.id === 'restore-input' ) { restoreBackup( t.files[ 0 ] ); t.value = ''; return; }
		if ( t.id === 'f-type' ) { ui.type = t.value; render(); return; }
		if ( t.id === 'f-status' ) { ui.status = t.value; render(); return; }
		if ( t.id === 'horizon' ) { ui.horizon = t.value; ui.confirm = null; render(); return; }
		if ( t.id === 'audit-user' ) { ui.auditUser = t.value; render(); return; }
		if ( t.hasAttribute( 'data-user-role' ) ) {
			var u = S.users.filter( function ( x ) { return x.id === t.getAttribute( 'data-user-role' ); } )[ 0 ], old = u.role;
			u.role = t.value; persist(); log( 'MODIFICATION DE RÔLE', u.name, ROLES[ old ].label + ' → ' + ROLES[ u.role ].label ); toast( 'Rôle de ' + u.name + ' modifié.' ); render(); return;
		}
		if ( t.hasAttribute( 'data-rule' ) ) {
			var r = ruleOf( t.getAttribute( 'data-rule' ) ), k = t.getAttribute( 'data-k' ), before = k === 'years' ? ( r.years == null ? 'permanente' : r.years + ' ans' ) : r.final;
			if ( k === 'years' ) { var n = parseInt( t.value, 10 ); r.years = isNaN( n ) || n < 1 ? null : Math.min( n, 100 ); }
			else r.final = t.value;
			var after = k === 'years' ? ( r.years == null ? 'permanente' : r.years + ' ans' ) : r.final;
			persist();
			var affected = S.docs.filter( function ( d ) { return d.status !== 'Éliminé' && ( d.rule || typeOf( d.type ).rule ) === r.id; } ).length;
			log( 'MODIFICATION DE RÈGLE', r.label, ( k === 'years' ? 'Durée ' : 'Sort final ' ) + before + ' → ' + after + ' · ' + affected + ' document(s) recalculé(s)' );
			toast( 'Règle modifiée : ' + affected + ' échéance(s) recalculée(s).' ); render(); return;
		}
		if ( t.getAttribute( 'data-act-select' ) === 'postpone' && t.value ) {
			var dd = docById( t.getAttribute( 'data-id' ) ), base = dueOf( dd ).due > todayISO() ? dueOf( dd ).due : todayISO();
			dd.reviewUntil = addYears( base, parseInt( t.value, 10 ) ); persist();
			log( 'CONSERVATION PROLONGÉE', dd.title, 'Nouvel examen le ' + frDate( dd.reviewUntil ) ); toast( 'Conservation prolongée jusqu’au ' + frDate( dd.reviewUntil ) + '.' ); render(); return;
		}
		if ( t.getAttribute( 'data-act-select' ) === 'link-box' && t.value ) {
			var d2 = docById( t.getAttribute( 'data-id' ) ); d2.box = t.value === 'none' ? null : t.value; persist();
			log( 'LIEN PAPIER–NUMÉRIQUE', d2.title, d2.box ? 'Original dans la boîte ' + d2.box : 'Lien retiré' ); render(); return;
		}
	} );

	var qTimer;
	document.addEventListener( 'input', function ( e ) {
		if ( e.target.id === 'f-q' ) { clearTimeout( qTimer ); var v = e.target.value; qTimer = setTimeout( function () { ui.q = v; render(); }, 200 ); }
	} );

	document.addEventListener( 'submit', function ( e ) {
		var f = e.target;
		if ( f.id === 'top-search' || f.id === 'search-form' ) {
			e.preventDefault();
			ui.searchQ = ( f.id === 'top-search' ? $( '#top-q' ) : $( '#search-q' ) ).value.trim();
			if ( f.id === 'top-search' ) $( '#top-q' ).value = '';
			if ( ui.searchQ ) log( 'RECHERCHE', ui.searchQ, '' );
			go( 'search' ); return;
		}
		if ( f.id === 'meta-form' ) {
			e.preventDefault();
			var d = docById( ui.open );
			var oldType = d.type;
			d.title = $( '#m-title' ).value.trim() || d.title; d.type = $( '#m-type' ).value; d.date = $( '#m-date' ).value || d.date; d.conf = $( '#m-conf' ).value;
			d.series = d.type !== oldType && $( '#m-series' ).value === d.series ? typeOf( d.type ).series : $( '#m-series' ).value;
			$$( '[data-meta]', f ).forEach( function ( i ) { var k = i.getAttribute( 'data-meta' ); d.meta[ k ] = i.type === 'number' ? ( i.value === '' ? '' : Number( i.value ) ) : i.value.trim(); } );
			d.proposed = null; persist();
			log( 'MODIFICATION DES MÉTADONNÉES', d.title, d.id + ( d.type !== oldType ? ' · type ' + typeOf( oldType ).label + ' → ' + typeOf( d.type ).label : '' ) );
			toast( 'Métadonnées enregistrées.' ); render(); return;
		}
		if ( f.id === 'box-form' ) {
			e.preventDefault();
			var nb = S.boxes.length + 457, bid = 'CI-ABJ-PLT-' + new Date().getFullYear() + '-' + pad( nb, 6 );
			var b = { id: bid, site: $( '#bx-site' ).value || 'Abidjan', bat: $( '#bx-bat' ).value, salle: $( '#bx-salle' ).value, rayon: $( '#bx-rayon' ).value, etagere: $( '#bx-etagere' ).value, boite: String( nb ), contents: $( '#bx-contents' ).value.trim(), service: $( '#bx-service' ).value.trim() || '—', status: 'En rayon', moves: [] };
			S.boxes.push( b ); ui.box = bid; persist(); log( 'CRÉATION DE BOÎTE', 'Boîte ' + bid, b.contents ); toast( 'Boîte ' + bid + ' créée.' ); render(); return;
		}
		if ( f.id === 'series-form' ) {
			e.preventDefault();
			var code = $( '#se-code' ).value.trim().toUpperCase();
			if ( seriesOf( code ) ) { toast( 'Ce code existe déjà.' ); return; }
			S.series.push( { code: code, fn: $( '#se-fn' ).value.trim(), label: $( '#se-label' ).value.trim() } ); persist();
			log( 'PLAN DE CLASSEMENT', code, 'Série ajoutée : ' + $( '#se-label' ).value.trim() ); toast( 'Série ' + code + ' ajoutée.' ); render(); return;
		}
		if ( f.id === 'user-form' ) {
			e.preventDefault();
			var nu = { id: 'u' + ( S.users.length + 1 ) + '-' + Date.now().toString( 36 ), name: $( '#us-name' ).value.trim(), service: $( '#us-service' ).value.trim() || '—', role: $( '#us-role' ).value };
			S.users.push( nu ); persist(); log( 'CRÉATION D’UTILISATEUR', nu.name, ROLES[ nu.role ].label ); toast( nu.name + ' ajouté.' ); render(); return;
		}
	} );

	/* Backup & restore */
	function exportBackup() {
		var files = {}, keys = [];
		S.docs.forEach( function ( d ) { if ( d.status !== 'Éliminé' ) d.versions.forEach( function ( v ) { keys.push( d.id + '@' + v.v ); } ); } );
		Promise.all( keys.map( function ( k ) { return store.get( 'files', k ).then( function ( b ) { if ( b ) files[ k ] = b64( b ); } ); } ) ).then( function () {
			S.lastBackup = nowISO(); persist();
			return log( 'SAUVEGARDE EXPORTÉE', 'Espace complet', S.docs.length + ' documents · ' + keys.length + ' fichiers · ' + S.audit.length + ' entrées de journal' );
		} ).then( function () {
			var payload = { format: 'archiva360-demo-backup', version: 1, exportedAt: nowISO(), state: S, files: files };
			download( new Blob( [ JSON.stringify( payload ) ], { type: 'application/json' } ), 'archiva360-sauvegarde-' + todayISO() + '.json' );
			toast( 'Sauvegarde exportée. Conservez-la hors de cet ordinateur.' ); render();
		} );
	}
	function restoreBackup( file ) {
		var out = $( '#restore-result' );
		if ( ! file ) return;
		out.innerHTML = '<p class="muted">Lecture et contrôle de la sauvegarde…</p>';
		file.text().then( function ( txt ) {
			var p = JSON.parse( txt );
			if ( p.format !== 'archiva360-demo-backup' || ! p.state || ! p.files ) throw new Error( 'Ce fichier n’est pas une sauvegarde ARCHIVA360.' );
			var checks = [], okN = 0, bad = [], missing = 0;
			p.state.docs.forEach( function ( d ) {
				if ( d.status === 'Éliminé' ) return;
				d.integrity = null;
				d.versions.forEach( function ( v ) {
					var k = d.id + '@' + v.v;
					if ( ! p.files[ k ] ) { missing++; return; }
					checks.push( sha256( unb64( p.files[ k ] ) ).then( function ( h ) {
						if ( h === v.sha ) okN++;
						else { if ( v === d.versions[ d.versions.length - 1 ] ) { d.integrity = 'altéré'; d.verifiedAt = nowISO(); } bad.push( d.title + ' (v' + v.v + ')' ); }
					} ) );
				} );
			} );
			return Promise.all( checks ).then( function () {
				return store.clear().then( function () {
					return Promise.all( Object.keys( p.files ).map( function ( k ) { return store.put( 'files', k, unb64( p.files[ k ] ) ); } ) );
				} ).then( function () {
					var who = S ? S.current : p.state.current;
					S = p.state;
					if ( S.users.some( function ( u ) { return u.id === who; } ) ) S.current = who;
					persist();
					return log( 'RESTAURATION', 'Sauvegarde du ' + frDateTime( p.exportedAt ), okN + ' fichier(s) conforme(s) à leur empreinte' + ( bad.length ? ' · ' + bad.length + ' altéré(s) : ' + bad.join( ', ' ) : '' ) + ( missing ? ' · ' + missing + ' manquant(s)' : '' ) );
				} ).then( function () {
					render();
					var o = $( '#restore-result' );
					var msg = bad.length || missing
						? '<div class="notice warn">Restauration effectuée : ' + okN + ' fichier(s) conformes. <b>' + ( bad.length + missing ) + ' fichier(s) ne correspondent pas à leur empreinte ou manquent</b> (' + esc( bad.join( ', ' ) ) + ') : ils sont signalés « Altéré ». Utilisez une sauvegarde plus ancienne pour les récupérer.</div>'
						: '<div class="notice ok">Restauration réussie : ' + okN + ' fichier(s) contrôlé(s) par empreinte et restauré(s).</div>';
					if ( o ) o.innerHTML = msg;
					toast( bad.length ? 'Restauration effectuée avec ' + bad.length + ' fichier(s) altéré(s).' : 'Restauration réussie : empreintes vérifiées.' );
				} );
			} );
		} ).catch( function ( err ) { out.innerHTML = '<div class="notice bad">' + esc( err.message || 'Fichier illisible.' ) + '</div>'; } );
	}

	/* =====================================================================
	 * Boot
	 * ===================================================================== */
	function boot() {
		if ( ! window.crypto || ! crypto.subtle ) {
			$( '#view' ).innerHTML = '<div class="notice bad">Votre navigateur ne permet pas le calcul d’empreintes (connexion non sécurisée ?). Ouvrez la démo en HTTPS.</div>';
			return;
		}
		store.open().then( function () { return store.get( 'kv', 'state' ); } ).then( function ( st ) {
			if ( st && st.v === 1 ) { S = st; return; }
			return seed();
		} ).then( function () {
			if ( ! store.persistent ) $( '#persist-note' ).textContent = 'Stockage local indisponible : les données seront perdues à la fermeture de l’onglet.';
			var h = ( location.hash || '' ).slice( 1 );
			if ( V[ h ] ) ui.view = h;
			render();
		} ).catch( function ( err ) { $( '#view' ).innerHTML = '<div class="notice bad">Erreur au démarrage : ' + esc( err.message ) + '</div>'; } );
	}
	window.addEventListener( 'hashchange', function () { var h = location.hash.slice( 1 ); if ( V[ h ] && h !== ui.view ) go( h ); } );
	boot();
}() );
