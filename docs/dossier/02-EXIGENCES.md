# 02 — Exigences à satisfaire

Source : `annexes/CCAT-UFHB.txt`. Les numéros entre parenthèses renvoient aux lignes du « Tableau de conformité technique » du cahier des charges. En cas de doute, le texte de l'annexe fait foi.

Colonne **État** : ce que le site adarchives.pro annonce aujourd'hui. `Lancement` = annoncé disponible, `V2` = annoncé pour plus tard, `Absent` = non mentionné. Le Prompt 0 remplace cette colonne par l'état réel du code.

Chaque exigence doit pouvoir recevoir la réponse « existe en standard : oui », avec un écran à montrer et un test automatisé.

## A. Socle (1 à 16)

| Id | Exigence | État |
|---|---|---|
| A1 | Tous les composants du même éditeur, même cycle de version (1, 159, 160) | À tenir |
| A2 | Solution modulaire, paramétrable, performante sous charge (2, 4) | À prouver |
| A3 | Multi-sites / multi-instances natif, étanche, échanges chiffrés entre instances, sans développement (5, 13) | Absent |
| A4 | Messagerie : IMAP/IMAPS, POP/POPS en capture, SMTP en notification (6) | Absent |
| A5 | Entrepôt documentaire unique et centralisé (7) | À vérifier |
| A6 | Moteur de workflow associé à de l'IA (7) | V2 |
| A7 | Espace d'aide en ligne sécurisé : recherche, PDF, vidéos (8) | Absent |
| A8 | Multilingue, interface et documents (9) | Français et anglais sur le site |
| A9 | Espace de travail en tableau de bord à widgets, personnalisable par utilisateur et par profil (10, 11) | Tableau de bord général seulement |
| A10 | Mobile : application dédiée Android et iOS sur les stores, pas de navigateur mobile (12) | Non publiée |
| A11 | Organigramme administré en web, modélisation graphique, droits délégués, journalisé (14) | À vérifier |
| A12 | Référentiels : contacts tiers, acteurs internes, modèles, processus types, casiers, indicateurs (15) | Partiel |
| A13 | Plan de classement par entité, arborescence, liens entre documents (16) | Lancement |

## B. Courrier (17 à 31)

| Id | Exigence | État |
|---|---|---|
| B1 | Enregistrement arrivée, départ, interne ; numéro chronologique paramétrable par année et par type (17) | V2 |
| B2 | QR code ou code-barres sur chaque courrier (18) | QR code au lancement |
| B3 | Plusieurs bureaux d'ordre, central et secondaires | V2 |
| B4 | Registres arrivée, départ, interne tenus automatiquement (19) | V2 |
| B5 | Lien automatique arrivée-départ (20) ; accusés de réception automatiques (21) | V2 |
| B6 | Profils d'enregistrement par support : papier, e-mail, fax (22) | V2 |
| B7 | Regroupement en dossiers ou casiers ; rattachement à un dossier de traitement partagé (23, 24) | V2 |
| B8 | Modèles de réponse (25) ; annotations et instructions, y compris sur le document scanné avec nouvelle version (26) | V2 |
| B9 | Destinataires par défaut par type de document (27) | V2 |
| B10 | Traitement collaboratif : traiter, transférer, transférer à un groupe, classer, renvoyer à l'expéditeur | V2 |
| B11 | Suivi graphique de l'avancement avec tous les commentaires (28) | V2 |
| B12 | Courrier départ : validation hiérarchique, versions mémorisées, signature, expédition, notification du signataire (29) | V2 |
| B13 | Courrier confidentiel | V2 |
| B14 | Recherche, statistiques et délais propres au courrier (30) | V2 |
| B15 | Échéances et alertes calculées, indicateurs de retard, notifications par e-mail (31) | V2 |

## C. Archivage (32 à 36)

| Id | Exigence | État |
|---|---|---|
| C1 | Module archivistique natif, classification et réglementation respectées (32, 33, 34) | Lancement |
| C2 | Calendrier de conservation : durée d'utilité administrative et sort final, calcul automatique (35) | Lancement |
| C3 | Localisation physique, affectation de la classe à chaque document, vues de classification (36) | V2 |
| C4 | Modèles de bordereaux d'élimination, de transfert et de versement ; procédures dématérialisées (36) | Absent |
| C5 | Export sur disque au format SEDA (36) | Absent |

## D. Capture (37 à 46)

| Id | Exigence | État |
|---|---|---|
| D1 | Scan indépendant de la marque du matériel, scanners et multifonctions (37) | À vérifier |
| D2 | Couleur, compression, suppression des pages blanches (38) | Lancement (partiel) |
| D3 | E-mails en masse : comptes multiples, circuit associé à chaque compte, paramétrage web (39) | Absent |
| D4 | E-mails sélectifs depuis Outlook, avec importance, urgence, confidentialité et lancement d'un circuit (39) | Absent |
| D5 | Capture automatique des PDF des applications métier avec LAD/RAD : type reconnu, zones extraites, circuit lancé (40) | Partiel (extraction de factures) |
| D6 | Capture de flux XML, création du document et lancement du circuit (41) | Absent |
| D7 | Serveur de capture central séparé, multisite, supervision des chaînes (42) | Absent |
| D8 | Lots avec intercalaires à code-barres ou QR code (43) | Partiel |
| D9 | Casiers virtuels : routage automatique, métadonnées, circuit et échéances associés, par direction, support ou flux (44) | Absent |
| D10 | TIFF multipage, PDF image et texte, PDF/A avec conversion automatique des fichiers Office (45) | PDF/A cité |
| D11 | Stockage NFS, CIFS, SMB (46) | Absent |
| D12 | OCR multilingue, y compris document en plusieurs langues (89) | Lancement |

## E. Documents (47 à 101)

| Id | Exigence | État |
|---|---|---|
| E1 | Commentaires, annotations, consignes, pièces jointes, demandes d'information, relances (47 à 51) | Partiel |
| E2 | Versions : historique, liste depuis la fiche, version applicable unique, suivi des modifications (52, 70 à 74) | Lancement |
| E3 | Administration web des formulaires, des métadonnées et des thésaurus, sans arrêt de service (53) | Absent |
| E4 | Types de champs : texte, liste, date et intervalle, e-mail, montant et intervalle, téléphone, direction, contact, terme de thésaurus ; masques ; obligatoire ou non ; droits par champ | Absent |
| E5 | Thésaurus : créer, modifier, importer, exporter (CSV, HTML) ; navigation en arbre, liste alphabétique, recherche ; vue graphique et vue relations ; deux thésaurus livrés (classification, localisation) (58, 96) | Absent |
| E6 | Règles de saisie par expressions régulières, dates par calendrier, listes paramétrables (55, 56, 57) | Absent |
| E7 | Modèles de documents avec fusion de champs, code-barres et zone de signature ; publipostage (59, 66, 82) | Absent |
| E8 | Fond de dossier alimenté automatiquement par les circuits ; regroupement par projet (60, 61, 92) | Absent |
| E9 | Identifiant unique, horodatage du scan, lien entrant-réponse, code-barres sur les sortants, validation des sortants (62 à 68) | Partiel |
| E10 | Traitements en masse : clôture, transfert, signature (69) | Absent |
| E11 | Réservation implicite et explicite, avec libération (75, 76) | Verrouillage cité |
| E12 | Webservices consommables par le SI, SDK documenté, console de test, supervision de la capture (77, 78, 79) | API citée |
| E13 | Outlook : complément de capture, rattachement aux contacts, doublons (80) | Absent |
| E14 | Word : complément d'injection ; édition Office en mode web ; génération manuelle ou automatique depuis un modèle (54, 81, 82) | Absent |
| E15 | Actions collaboratives prédéfinies : démarrer, assigner, transférer, lire, valider ou non, signer (83) | V2 |
| E16 | Indexation plein texte, mots-clés, indexation en lot, clés d'index obligatoires par type (89 à 94) | Lancement (partiel) |
| E17 | Recherche simple et avancée, opérateurs ET, OU, SAUF, par type, plein texte multilingue, formulaire extensible, tri, recherches enregistrées, historique (97, 99, 100) | Lancement (partiel) |
| E18 | Zone de persistance : panier de documents conservé d'une session à l'autre (99) | Absent |
| E19 | Vues arborescentes dynamiques et auto-classement selon des critères paramétrables, placées dans l'espace de travail (95, 98, 101) | Absent |

## F. Signature et parapheur (84 à 88, 120 à 132, 155, 156)

| Id | Exigence | État |
|---|---|---|
| F1 | Tâches de signature ; refus avec retour arrière automatique ; indicateur au tableau de bord (84, 85, 86) | V2 |
| F2 | Signature physique : rattachement automatique du document signé rescanné (87) | Absent |
| F3 | Signature simple par spécimen et cachet, tracée et horodatée ; signature avancée par certificat ARTCI ; en masse (88) | V2 |
| F4 | Parapheur natif : contenir, annoter, signer, à l'unité ou en masse, au stylet, où que l'on soit (120, 121, 122) | Absent |
| F5 | Co-signature ; plusieurs signatures sur un même document (123) | Absent |
| F6 | Tableau de bord du parapheur ; spécimens gérés par l'utilisateur ; langue ; habilitations (124, 125, 126) | Absent |
| F7 | Accès au cycle de vie et aux métadonnées du document à signer (127) ; signature sur zone prédéfinie (128) | Absent |
| F8 | Refus, lot avec prévisualisation et retrait, notification des acteurs (129, 130, 131) | Absent |
| F9 | Vérification de toutes les formes de signature, jusqu'à la qualifiée ; identification à plusieurs facteurs (132) | Absent |
| F10 | PDF/A signé ; clé USB ou carte à puce ; code PIN ; magasin de certificats ; attributs intégrés ; affichage du certificat (155) | Absent |
| F11 | Contrôle d'expiration et de révocation du certificat (156) | Absent |

## G. Processus (102 à 119)

| Id | Exigence | État |
|---|---|---|
| G1 | Concepteur graphique natif : barre d'outils, panneau de propriétés, séquentiel et parallèle, nombre illimité (102, 103, 104) | V2 (glisser-déposer) |
| G2 | Circuits figés par l'administrateur ou créés à la volée par l'utilisateur selon ses droits (105) | V2 |
| G3 | Rôles, acteurs individuels ou entités, catégories d'action (attribution, contribution, information), refus (106, 107, 108) | V2 |
| G4 | Formulaires : texte, nombre avec bornes, date, période contrôlée, liste interne ou par requête SQL, pièces jointes, personne, rôle, contrôles de cohérence (109) | Absent |
| G5 | Modèles de documents renseignés au fil du circuit (110) | Absent |
| G6 | Suivi en temps réel, délai global et par étape, relances (111, 112) | V2 |
| G7 | Déclenchement automatique selon métadonnées, état, échéance, urgence (113) | Absent |
| G8 | Absence et intérim sans partage de mot de passe ; délégation par étape, par tâche, par critère (urgence, confidentialité, type) ; non exclusive ; plusieurs délégataires ; annulable (114 à 119) | Absent |

## H. Notifications, statistiques, sécurité, technique (133 à 160)

| Id | Exigence | État |
|---|---|---|
| H1 | Notifications au tableau de bord et par e-mail ; échéances et alertes par type ; récapitulatif périodique paramétrable (133, 134) | Absent |
| H2 | Module analytique ; l'administrateur conçoit et publie ses rapports seul (135, 136) | Absent |
| H3 | HTTPS / TLS 1.2 (137) ; détection d'anomalies remontée aux administrateurs (138) | Partiel |
| H4 | Annuaire centralisé ; SSO Active Directory, SAML ou OpenID Connect ; double authentification (139, 140, 141) | MFA citée |
| H5 | Serveur CMIS (142) | Absent |
| H6 | Droits granulaires : utilisateur, groupe, cumul de profils, dossier, document, métadonnée, fichier ; deux types d'administrateurs ; organigramme comme base (143 à 148, 152) | Partiel |
| H7 | Journalisation automatique complète, suivi en temps réel, historique des échanges ; traçabilité qui, quoi, quand, comment (149, 150) | Lancement |
| H8 | Code-barres ou QR code sur tout document créé, téléchargé ou imprimé (151) | Lancement (partiel) |
| H9 | Confidentialité des fiches et des fichiers (153) ; filtrage des extensions (154) | Absent |
| H10 | Administration centrale web ; indicateurs temps réel (157, 158) | Lancement |
| H11 | Trois environnements ; haute disponibilité ; répartition de charge | Absent |

## I. Modules métier (cités au périmètre, sans ligne dédiée dans le tableau)

| Id | Exigence | État |
|---|---|---|
| I1 | RPA : automatisation des processus répétitifs et chronophages | Absent |
| I2 | Gestion des contrats | Coffre-fort seulement |
| I3 | Gestion des appels d'offres | Absent |
| I4 | Gestion des factures | Extraction seulement |
| I5 | Composante BI pour les rapports statistiques | Absent |

## J. Mobile (détail)

Accès aux espaces de travail ; recherche de correspondances ; tâches à traiter ; transfert d'une tâche ; notifications ; consultation, traitement et dispatching en déplacement ; signature depuis le parapheur.
