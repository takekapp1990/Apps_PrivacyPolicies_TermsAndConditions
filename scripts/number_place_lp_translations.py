"""LP-specific copy. Shared controls and technique names reuse the learning/app catalogs.

Numeric keys refer to the stable Japanese source strings in number_place_lp_ja.json.
Missing translations are errors; there is no English fallback.
"""
KEYS=[7,8,9,10,11,15,16,19,21,23,25,27,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50,52,53,55,60,61,62,63,64,65,66,67,68,69,71,72,74,76,78,79,80,81,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
PACKS={}
def add(code,text):
 values=text.strip().split('\n')
 assert len(values)==len(KEYS),(code,len(values),len(KEYS))
 assert all(values),code
 PACKS[code]={str(k):v for k,v in zip(KEYS,values)}

add('en','''Camera scanning · Hints with explanations
Stuck on Sudoku?
Just the hint you need.
Scan puzzles from newspapers and magazines.
Understand why a number fits, then keep solving on your own.
iPhone & Android / Free download · In-app purchases
Actual app screens
Hints with explanations
Scan from an image
Technique practice
Notes & trial mode
Comfortable themes
Does this happen when you play?
You want the answer.
But you want to solve it yourself.
“Where should I look next?”
You check the grid again and again,
but keep getting stuck in the same place.
“The answer alone doesn’t explain it.”
Why does that number belong there?
Copying the solution isn’t enough.
“Entering a whole puzzle takes too long.”
You want to take the paper puzzle you’re solving
and carry on in the app.
Turn a sticking point into a clue
Features
Scan and get started.
Read a Sudoku puzzle from a photo of a newspaper or magazine, with less typing of individual numbers.
Understand the “why”.
Read the reasoning behind a move. Use it as a clue for your next step, rather than simply filling in the answer.
Learn how to solve.
Explore explanations and exercises for individual techniques, then practise spotting them yourself.
Tools for taking your time, too.
Color themes & dark mode
For people who enjoy finding their own solution
Who is it for?
You enjoy Sudoku in newspapers and magazines
Import your usual puzzle and carry on where you left off.
You want a hint before seeing the whole answer
Check the reasoning at the sticking point, then continue yourself.
You want to learn Sudoku techniques
For beginners and anyone ready to learn another technique.
Read · Try · Practise
Start in your browser.
Read a guide or try a complete puzzle.
From candidate notes to technique explanations and practice.
Take on a whole puzzle with hints when you need them.
Discover the rules and the fun of connecting the clues.
See how a hint works on this page
Why must this cell be 5?
Look at the blue-outlined cell and open the hint.
This is a web example for trying a solving step. The app’s display is different.
When Sudoku has you stuck.
Just the hint you need,
for the Sudoku you love.
Download {brand}
Free download · In-app purchases
Frequently asked questions
Can I use it for free?
The app is free to download and try. Hints, answer checks and image scanning have usage limits; some uses require watching a video ad.
Premium is a monthly or annual subscription. It removes ads and includes unlimited hints and answer checks. Image scanning still has a limit with Premium. See the app for prices and conditions.
Can I use newspaper or magazine puzzles?
Import a photo of a Sudoku puzzle. Check the recognized numbers and correct any errors before you start. Standard 9×9 Sudoku is supported.
Can I play without my own puzzle?
You can play the app’s built-in puzzles and use technique explanations and exercises. Some puzzles and exercises require Premium.
Can I try it before installing?
Alongside this one-step demo, you can play a complete puzzle in your browser and explore technique guides and practice.''')

add('fr','''Scanner une grille · Comprendre les indices
Bloqué sur un sudoku ?
Juste l’indice qu’il vous faut.
Scannez les grilles de vos journaux et magazines.
Comprenez pourquoi un chiffre convient, puis continuez à résoudre par vous-même.
iPhone et Android / Téléchargement gratuit · Achats intégrés
Écrans réels de l’application
Indices expliqués
Lecture d’une image
Entraînement par technique
Notes et mode hypothèse
Thèmes confortables
Cela vous arrive en jouant ?
Vous voulez la réponse.
Mais vous voulez trouver vous-même.
« Où regarder maintenant ? »
Vous examinez la grille encore et encore,
mais restez bloqué au même endroit.
« La réponse seule ne m’explique rien. »
Pourquoi ce chiffre va-t-il ici ?
Recopier la solution ne suffit pas.
« Saisir toute une grille prend trop de temps. »
Vous voulez reprendre votre grille papier
et la continuer dans l’application.
Transformer un blocage en piste
Fonctionnalités
Photographiez et commencez.
Lisez une grille de journal ou de magazine à partir d’une photo, sans saisir chaque chiffre à la main.
Comprenez le « pourquoi ».
Lisez le raisonnement derrière un coup et utilisez-le pour chercher la suite, au lieu de simplement recopier la réponse.
Apprenez à résoudre.
Consultez des explications et des exercices par technique, puis entraînez-vous à les repérer vous-même.
Des outils pour prendre son temps.
Thèmes de couleurs et mode sombre
Pour ceux qui aiment trouver eux-mêmes
À qui s’adresse l’application ?
Vous aimez les sudokus des journaux et magazines
Importez votre grille habituelle et reprenez là où vous en étiez.
Vous voulez un indice avant toute la solution
Comprenez le passage difficile, puis continuez par vous-même.
Vous voulez apprendre les techniques du sudoku
Pour les débutants comme pour ceux qui veulent apprendre une nouvelle technique.
Lire · Essayer · S’entraîner
Commencez dans votre navigateur.
Lisez un guide ou jouez une grille complète.
Des notes de candidats aux techniques et exercices.
Essayez une grille entière avec des indices au besoin.
Découvrez les règles et le plaisir de relier les indices.
Voir ici comment fonctionne un indice
Pourquoi cette case vaut-elle 5 ?
Regardez la case encadrée en bleu et ouvrez l’indice.
Cet exemple web permet d’essayer un coup. L’affichage de l’application est différent.
Quand un sudoku vous bloque.
L’indice qu’il vous faut,
pour vos sudokus préférés.
Télécharger {brand}
Téléchargement gratuit · Achats intégrés
Questions fréquentes
Puis-je l’utiliser gratuitement ?
L’application est gratuite à télécharger et à essayer. Les indices, vérifications et lectures d’images sont limités ; certaines utilisations nécessitent une publicité vidéo.
Premium est un abonnement mensuel ou annuel. Il supprime les publicités et permet des indices et vérifications illimités. La lecture d’images reste limitée même avec Premium. Tarifs et conditions dans l’application.
Puis-je utiliser des grilles de journaux ?
Importez une photo de votre sudoku. Vérifiez les chiffres reconnus et corrigez les erreurs avant de commencer. Les sudokus classiques de 9×9 sont pris en charge.
Puis-je jouer sans ma propre grille ?
L’application propose des grilles intégrées ainsi que des explications et exercices par technique. Certaines grilles et certains exercices nécessitent Premium.
Puis-je essayer avant d’installer ?
En plus de cette démo d’un coup, vous pouvez jouer une grille complète dans votre navigateur et consulter des guides et exercices.''')

add('de','''Mit der Kamera scannen · Hinweise mit Erklärung
Beim Sudoku festgefahren?
Genau der richtige Hinweis.
Scanne Rätsel aus Zeitungen und Zeitschriften.
Verstehe, warum eine Zahl passt, und löse selbst weiter.
iPhone & Android / Kostenloser Download · In-App-Käufe
Echte App-Ansichten
Hinweise mit Erklärung
Aus einem Bild einlesen
Techniken üben
Notizen & Probiermodus
Angenehme Designs
Kommt dir das bekannt vor?
Du möchtest die Antwort.
Aber selbst auf die Lösung kommen.
„Wo soll ich als Nächstes suchen?“
Du prüfst das Gitter immer wieder,
kommst aber an derselben Stelle nicht weiter.
„Die Antwort allein erklärt mir nichts.“
Warum gehört diese Zahl genau dorthin?
Die Lösung abzuschreiben reicht dir nicht.
„Das ganze Rätsel abzutippen dauert zu lange.“
Du möchtest dein begonnenes Papierrätsel
in der App weiterspielen.
Aus einem Hindernis wird ein Anhaltspunkt
Funktionen
Fotografieren und loslegen.
Lies ein Sudoku aus einer Zeitung oder Zeitschrift per Foto ein und spare dir das Eingeben einzelner Zahlen.
Das „Warum“ verstehen.
Lies die Begründung für einen Zug. Nutze sie als Anhaltspunkt für den nächsten Schritt, statt nur die Antwort einzutragen.
Lösungstechniken lernen.
Entdecke Erklärungen und Übungen zu einzelnen Techniken und übe, sie selbst zu erkennen.
Auch zum entspannten Knobeln.
Farbdesigns & Dunkelmodus
Für alle, die gern selbst auf die Lösung kommen
Für wen ist die App?
Du magst Sudoku in Zeitungen und Zeitschriften
Importiere dein gewohntes Rätsel und mache dort weiter, wo du aufgehört hast.
Du möchtest einen Hinweis vor der gesamten Lösung
Verstehe die knifflige Stelle und löse anschließend selbst weiter.
Du möchtest Sudoku-Techniken lernen
Für Einsteiger und alle, die eine weitere Technik lernen möchten.
Lesen · Ausprobieren · Üben
Starte im Browser.
Lies einen Leitfaden oder spiele ein ganzes Rätsel.
Von Kandidatennotizen bis zu Technik-Erklärungen und Übungen.
Löse ein ganzes Rätsel mit Hinweisen, wenn du sie brauchst.
Entdecke die Regeln und den Spaß am Verknüpfen von Hinweisen.
Hier ausprobieren, wie ein Hinweis funktioniert
Warum muss in dieses Feld eine 5?
Schau auf das blau umrandete Feld und öffne den Hinweis.
Dieses Web-Beispiel zeigt einen Lösungsschritt. Die Darstellung in der App ist anders.
Wenn du beim Sudoku festhängst.
Der passende Hinweis
für deine liebsten Sudokus.
{brand} herunterladen
Kostenloser Download · In-App-Käufe
Häufige Fragen
Kann ich die App kostenlos nutzen?
Download und Ausprobieren sind kostenlos. Hinweise, Antwortprüfungen und Bildscans sind begrenzt; für manche Nutzungen ist ein Werbevideo nötig.
Premium ist ein Monats- oder Jahresabo. Es entfernt Werbung und ermöglicht unbegrenzte Hinweise und Antwortprüfungen. Bildscans bleiben auch mit Premium begrenzt. Preise und Bedingungen findest du in der App.
Gehen auch Rätsel aus Zeitungen und Zeitschriften?
Importiere ein Foto deines Sudokus. Prüfe die erkannten Zahlen und korrigiere Fehler vor dem Start. Klassische 9×9-Sudokus werden unterstützt.
Kann ich ohne eigenes Rätsel spielen?
Die App enthält Rätsel sowie Erklärungen und Übungen zu Techniken. Einige Rätsel und Übungen erfordern Premium.
Kann ich vor der Installation testen?
Neben dieser Ein-Schritt-Demo kannst du im Browser ein ganzes Rätsel spielen und Technik-Anleitungen sowie Übungen ausprobieren.''')

add('es','''Escanea con la cámara · Pistas explicadas
¿Te atascaste en un sudoku?
La pista que necesitas.
Escanea sudokus de periódicos y revistas.
Entiende por qué encaja un número y sigue resolviendo por tu cuenta.
iPhone y Android / Descarga gratis · Compras en la app
Pantallas reales de la app
Pistas explicadas
Leer desde una imagen
Práctica por técnica
Notas y modo de prueba
Temas cómodos
¿Te pasa cuando juegas?
Quieres saber la respuesta.
Pero quieres resolverlo tú.
«¿Dónde debería mirar ahora?»
Revisas la cuadrícula una y otra vez,
pero sigues atascado en el mismo punto.
«La respuesta sola no me lo explica.»
¿Por qué va ese número ahí?
Copiar la solución no es suficiente.
«Introducir toda la cuadrícula lleva demasiado tiempo.»
Quieres tomar el sudoku en papel que estás resolviendo
y continuarlo en la app.
Convierte un bloqueo en una pista
Funciones
Haz una foto y empieza.
Lee un sudoku de un periódico o revista desde una foto y ahorra la introducción manual de cada número.
Entiende el «por qué».
Consulta el razonamiento de una jugada y úsalo para pensar en la siguiente, en lugar de limitarte a rellenar la respuesta.
Aprende a resolver.
Consulta explicaciones y ejercicios por técnica y practica cómo reconocerlas por tu cuenta.
Herramientas para pensar sin prisa.
Temas de color y modo oscuro
Para quienes disfrutan encontrando su solución
¿Para quién es?
Te gustan los sudokus de periódicos y revistas
Importa tu sudoku habitual y continúa donde lo dejaste.
Quieres una pista antes de ver toda la solución
Comprende el punto difícil y sigue resolviendo tú.
Quieres aprender técnicas de sudoku
Para principiantes y quienes quieren aprender otra técnica.
Leer · Probar · Practicar
Empieza en el navegador.
Lee una guía o juega un sudoku completo.
Desde notas de candidatos hasta técnicas y ejercicios.
Intenta resolverlo entero con pistas cuando las necesites.
Descubre las reglas y el placer de conectar las pistas.
Prueba aquí cómo funciona una pista
¿Por qué esta casilla debe ser un 5?
Mira la casilla con borde azul y abre la pista.
Este ejemplo web permite probar una jugada. La app tiene una presentación diferente.
Cuando te atasques en un sudoku.
La pista adecuada
para tus sudokus favoritos.
Descargar {brand}
Descarga gratis · Compras en la app
Preguntas frecuentes
¿Puedo usarla gratis?
La app se descarga y prueba gratis. Las pistas, comprobaciones y lecturas de imágenes tienen límites; algunos usos requieren ver un anuncio de vídeo.
Premium es una suscripción mensual o anual. Elimina los anuncios e incluye pistas y comprobaciones ilimitadas. La lectura de imágenes sigue teniendo un límite con Premium. Consulta los precios y condiciones en la app.
¿Puedo usar sudokus de periódicos y revistas?
Importa una foto de tu sudoku. Revisa los números reconocidos y corrige los errores antes de empezar. Se admiten sudokus clásicos de 9×9.
¿Puedo jugar sin tener un sudoku propio?
Puedes jugar los sudokus incluidos y usar las explicaciones y ejercicios por técnica. Algunos sudokus y ejercicios requieren Premium.
¿Puedo probar antes de instalar?
Además de esta demostración de una jugada, puedes jugar un sudoku completo en el navegador y consultar guías y ejercicios.''')

add('it','''Scansione con fotocamera · Indizi spiegati
Bloccato con un sudoku?
L’indizio che ti serve.
Scansiona i sudoku di giornali e riviste.
Scopri perché un numero va in una casella e continua da solo.
iPhone e Android / Download gratuito · Acquisti in-app
Schermate reali dell’app
Indizi spiegati
Lettura da immagine
Esercizi per tecnica
Note e modalità di prova
Temi confortevoli
Ti succede mentre giochi?
Vuoi sapere la risposta.
Ma vuoi risolverlo da solo.
«Dove dovrei guardare adesso?»
Controlli la griglia più e più volte,
ma resti bloccato nello stesso punto.
«La risposta da sola non mi spiega nulla.»
Perché quel numero va proprio lì?
Copiare la soluzione non ti basta.
«Inserire tutta la griglia richiede troppo tempo.»
Vuoi prendere il sudoku su carta che stai risolvendo
e continuarlo nell’app.
Da un ostacolo a un indizio
Funzionalità
Fotografa e inizia.
Leggi un sudoku di un giornale o una rivista da una foto, riducendo l’inserimento manuale dei numeri.
Comprendi il «perché».
Leggi il ragionamento dietro una mossa e usalo per trovare il passo successivo, invece di copiare solo la risposta.
Impara a risolvere.
Consulta spiegazioni ed esercizi dedicati alle tecniche e allenati a riconoscerle da solo.
Strumenti per ragionare con calma.
Temi di colore e modalità scura
Per chi ama trovare la soluzione da sé
A chi è rivolta?
Ti piacciono i sudoku di giornali e riviste
Importa la tua griglia e riprendi da dove eri rimasto.
Vuoi un indizio prima di vedere tutta la soluzione
Comprendi il passaggio difficile e poi continua da solo.
Vuoi imparare le tecniche del sudoku
Per principianti e per chi vuole imparare un’altra tecnica.
Leggi · Prova · Esercitati
Inizia dal browser.
Leggi una guida o gioca una griglia completa.
Dalle note sui candidati alle tecniche e agli esercizi.
Prova a completare una griglia con gli indizi quando servono.
Scopri le regole e il piacere di collegare gli indizi.
Vedi qui come funziona un indizio
Perché questa casella deve contenere 5?
Guarda la casella con il bordo blu e apri l’indizio.
Questo esempio web permette di provare una mossa. L’app ha una visualizzazione diversa.
Quando un sudoku ti blocca.
L’indizio giusto
per i tuoi sudoku preferiti.
Scarica {brand}
Download gratuito · Acquisti in-app
Domande frequenti
Posso usarla gratis?
L’app si scarica e si prova gratuitamente. Indizi, controlli e letture di immagini hanno limiti di utilizzo; alcune operazioni richiedono un annuncio video.
Premium è un abbonamento mensile o annuale. Rimuove gli annunci e include indizi e controlli illimitati. La lettura delle immagini resta limitata anche con Premium. Prezzi e condizioni sono indicati nell’app.
Posso usare griglie di giornali e riviste?
Importa una foto del sudoku. Controlla i numeri riconosciuti e correggi gli errori prima di iniziare. Sono supportati i sudoku classici di 9×9.
Posso giocare senza una mia griglia?
Puoi usare le griglie integrate, le spiegazioni e gli esercizi sulle tecniche. Alcune griglie e alcuni esercizi richiedono Premium.
Posso provare prima di installare?
Oltre a questa demo di una mossa, puoi giocare una griglia completa nel browser e consultare guide ed esercizi.''')

add('pt','''Leia com a câmera · Dicas com explicação
Travou no sudoku?
A dica de que você precisa.
Leia sudokus de jornais e revistas com a câmera.
Entenda por que um número se encaixa e continue resolvendo por conta própria.
iPhone e Android / Download grátis · Compras no app
Telas reais do app
Dicas com explicação
Leitura de imagem
Prática por técnica
Notas e modo de teste
Temas confortáveis
Isso acontece quando você joga?
Você quer saber a resposta.
Mas quer resolver por conta própria.
“Onde devo olhar agora?”
Você confere a grade várias vezes,
mas continua preso no mesmo ponto.
“Só a resposta não explica.”
Por que esse número vai nessa casa?
Copiar a solução não é suficiente.
“Digitar a grade inteira demora demais.”
Você quer pegar o sudoku em papel que está resolvendo
e continuar no app.
Transforme um bloqueio em uma pista
Recursos
Fotografe e comece.
Leia um sudoku de jornal ou revista a partir de uma foto e reduza a digitação de cada número.
Entenda o “porquê”.
Veja o raciocínio de uma jogada e use-o para pensar no próximo passo, em vez de apenas preencher a resposta.
Aprenda a resolver.
Explore explicações e exercícios de cada técnica e pratique reconhecê-las por conta própria.
Ferramentas para pensar com calma.
Temas de cores e modo escuro
Para quem gosta de encontrar a própria solução
Para quem é o app?
Você gosta dos sudokus de jornais e revistas
Importe sua grade habitual e continue de onde parou.
Você quer uma dica antes de ver a solução inteira
Entenda o ponto difícil e siga resolvendo por conta própria.
Você quer aprender técnicas de sudoku
Para iniciantes e quem quer aprender mais uma técnica.
Leia · Experimente · Pratique
Comece pelo navegador.
Leia um guia ou jogue um sudoku completo.
Das notas de candidatos às técnicas e aos exercícios.
Tente completar uma grade com dicas quando precisar.
Conheça as regras e a diversão de conectar as pistas.
Veja aqui como uma dica funciona
Por que esta casa precisa ser 5?
Observe a casa com borda azul e abra a dica.
Este exemplo web permite experimentar uma jogada. A apresentação do app é diferente.
Quando o sudoku travar.
A dica certa
para seus sudokus favoritos.
Baixar {brand}
Download grátis · Compras no app
Perguntas frequentes
Posso usar de graça?
O download e a experimentação são gratuitos. Dicas, verificações e leituras de imagens têm limites; alguns usos exigem assistir a um anúncio em vídeo.
Premium é uma assinatura mensal ou anual. Remove anúncios e inclui dicas e verificações ilimitadas. A leitura de imagens continua limitada mesmo com Premium. Veja os preços e condições no app.
Posso usar sudokus de jornais e revistas?
Importe uma foto do sudoku. Confira os números reconhecidos e corrija possíveis erros antes de começar. São aceitos sudokus tradicionais de 9×9.
Posso jogar sem uma grade própria?
Você pode jogar as grades incluídas e usar explicações e exercícios por técnica. Algumas grades e exercícios exigem Premium.
Posso experimentar antes de instalar?
Além desta demonstração de uma jogada, você pode jogar um sudoku completo no navegador e explorar guias e exercícios.''')

add('nl','''Scannen met de camera · Hints met uitleg
Vastgelopen met sudoku?
Precies de hint die je nodig hebt.
Scan puzzels uit kranten en tijdschriften.
Begrijp waarom een cijfer past en puzzel daarna zelf verder.
iPhone en Android / Gratis downloaden · In-appaankopen
Echte appschermen
Hints met uitleg
Een afbeelding inlezen
Technieken oefenen
Notities en proefmodus
Prettige thema’s
Herken je dit tijdens het puzzelen?
Je wilt het antwoord weten.
Maar je wilt het zelf oplossen.
“Waar moet ik nu kijken?”
Je controleert het rooster steeds opnieuw,
maar blijft op hetzelfde punt steken.
“Het antwoord alleen legt niets uit.”
Waarom hoort dat cijfer daar?
De oplossing overschrijven is niet genoeg.
“De hele puzzel overtypen duurt te lang.”
Je wilt de papieren sudoku waaraan je werkt
gewoon in de app voortzetten.
Maak van een struikelblok een aanwijzing
Functies
Maak een foto en begin.
Lees een sudoku uit een krant of tijdschrift in via een foto en typ minder cijfers met de hand.
Begrijp het “waarom”.
Lees de redenering achter een zet en gebruik die voor je volgende stap, in plaats van alleen het antwoord in te vullen.
Leer oplossen.
Bekijk uitleg en oefeningen per techniek en oefen om ze zelf te herkennen.
Ook hulpmiddelen om rustig na te denken.
Kleurthema’s en donkere modus
Voor wie graag zelf de oplossing vindt
Voor wie is de app?
Je houdt van sudoku’s in kranten en tijdschriften
Importeer je eigen puzzel en ga verder waar je gebleven was.
Je wilt een hint voordat je de hele oplossing ziet
Begrijp het lastige punt en puzzel daarna zelf verder.
Je wilt sudokutechnieken leren
Voor beginners en iedereen die een volgende techniek wil leren.
Lezen · Proberen · Oefenen
Begin in je browser.
Lees een handleiding of speel een volledige puzzel.
Van kandidaatnotities tot uitleg en oefeningen per techniek.
Probeer een hele puzzel met hints wanneer je die nodig hebt.
Ontdek de regels en het plezier van samenhangende aanwijzingen.
Bekijk hier hoe een hint werkt
Waarom moet deze cel een 5 zijn?
Kijk naar de blauw omrande cel en open de hint.
Dit webvoorbeeld laat je één zet proberen. De weergave in de app is anders.
Als je vastloopt met sudoku.
De juiste hint
voor je favoriete sudoku’s.
Download {brand}
Gratis downloaden · In-appaankopen
Veelgestelde vragen
Kan ik de app gratis gebruiken?
Downloaden en uitproberen is gratis. Hints, antwoordcontroles en afbeeldingsscans hebben gebruikslimieten; soms moet je een videoadvertentie bekijken.
Premium is een maand- of jaarabonnement. Het verwijdert advertenties en biedt onbeperkte hints en antwoordcontroles. Ook met Premium geldt een limiet voor afbeeldingsscans. Prijzen en voorwaarden staan in de app.
Kan ik puzzels uit kranten en tijdschriften gebruiken?
Importeer een foto van je sudoku. Controleer de herkende cijfers en verbeter fouten voordat je begint. Klassieke 9×9-sudoku’s worden ondersteund.
Kan ik zonder eigen puzzel spelen?
Je kunt ingebouwde puzzels spelen en uitleg en oefeningen per techniek gebruiken. Sommige puzzels en oefeningen vereisen Premium.
Kan ik proberen voordat ik installeer?
Naast deze demo van één zet kun je een volledige puzzel in je browser spelen en handleidingen en oefeningen bekijken.''')

add('da','''Scan med kameraet · Tips med forklaring
Sidder du fast i sudoku?
Lige det tip, du har brug for.
Scan opgaver fra aviser og blade.
Forstå, hvorfor et tal passer, og løs derefter videre selv.
iPhone og Android / Gratis download · Køb i appen
Rigtige skærmbilleder fra appen
Tips med forklaring
Læs fra et billede
Øv teknikker
Noter og prøvetilstand
Behagelige temaer
Kender du det, når du spiller?
Du vil kende svaret.
Men du vil selv løse opgaven.
“Hvor skal jeg kigge nu?”
Du gennemgår feltet igen og igen,
men sidder fast det samme sted.
“Svaret alene forklarer det ikke.”
Hvorfor skal netop det tal stå der?
Det er ikke nok bare at kopiere løsningen.
“Det tager for lang tid at taste hele opgaven ind.”
Du vil tage den papiropgave, du er i gang med,
og fortsætte i appen.
Fra et stop til et nyt spor
Funktioner
Tag et billede og begynd.
Læs en sudoku fra en avis eller et blad ind fra et foto, og slip for at taste alle tallene enkeltvis.
Forstå “hvorfor”.
Læs begrundelsen for et træk, og brug den til at finde næste skridt i stedet for blot at udfylde svaret.
Lær at løse sudoku.
Se forklaringer og øvelser for de enkelte teknikker, og øv dig i selv at genkende dem.
Også værktøjer til at tænke i ro og mag.
Farvetemaer og mørk tilstand
Til dig, der nyder selv at finde løsningen
Hvem er appen til?
Du kan lide sudoku i aviser og blade
Importer din sædvanlige opgave, og fortsæt, hvor du slap.
Du vil have et tip før hele løsningen
Forstå det svære punkt, og fortsæt selv.
Du vil lære sudokuteknikker
Til begyndere og alle, der vil lære endnu en teknik.
Læs · Prøv · Øv
Begynd i din browser.
Læs en vejledning, eller spil en hel opgave.
Fra kandidatnoter til teknikforklaringer og øvelser.
Prøv en hel opgave med tips, når du har brug for dem.
Opdag reglerne og glæden ved at forbinde sporene.
Se her, hvordan et tip virker
Hvorfor skal dette felt være 5?
Se på feltet med blå ramme, og åbn tippet.
Dette webeksempel lader dig prøve ét træk. Appens visning er anderledes.
Når du sidder fast i sudoku.
Det rette tip
til dine yndlingssudokuer.
Download {brand}
Gratis download · Køb i appen
Ofte stillede spørgsmål
Kan jeg bruge appen gratis?
Appen kan downloades og prøves gratis. Tips, svarkontrol og billedscanning har forbrugsgrænser; nogle handlinger kræver, at du ser en videoannonce.
Premium er et måneds- eller årsabonnement. Det fjerner annoncer og giver ubegrænsede tips og svarkontrol. Billedscanning er stadig begrænset med Premium. Se priser og betingelser i appen.
Kan jeg bruge opgaver fra aviser og blade?
Importer et foto af din sudoku. Kontroller de genkendte tal, og ret eventuelle fejl, før du begynder. Almindelige 9×9-sudokuer understøttes.
Kan jeg spille uden min egen opgave?
Du kan spille appens indbyggede opgaver og bruge forklaringer og øvelser til teknikker. Nogle opgaver og øvelser kræver Premium.
Kan jeg prøve før installation?
Ud over denne demo med ét træk kan du spille en hel opgave i browseren og se vejledninger og øvelser.''')

add('sv','''Skanna med kameran · Tips med förklaringar
Fastnat i ett sudoku?
Precis det tips du behöver.
Skanna sudoku från tidningar och tidskrifter.
Förstå varför en siffra passar och fortsätt sedan själv.
iPhone och Android / Gratis nedladdning · Köp i appen
Riktiga skärmbilder från appen
Tips med förklaringar
Läs in från en bild
Öva tekniker
Anteckningar och provläge
Behagliga teman
Känner du igen det här?
Du vill veta svaret.
Men du vill lösa det själv.
“Var ska jag titta nu?”
Du går igenom rutnätet om och om igen,
men fastnar på samma ställe.
“Bara svaret förklarar ingenting.”
Varför ska just den siffran stå där?
Att skriva av lösningen räcker inte.
“Att mata in hela pusslet tar för lång tid.”
Du vill ta papperssudokut du håller på med
och fortsätta i appen.
Gör ett hinder till en ledtråd
Funktioner
Fota och börja.
Läs in ett sudoku från en tidning eller tidskrift med ett foto och slipp mata in alla siffror för hand.
Förstå “varför”.
Läs resonemanget bakom ett drag och använd det för att hitta nästa steg, i stället för att bara fylla i svaret.
Lär dig att lösa.
Utforska förklaringar och övningar för varje teknik och träna på att känna igen dem själv.
Verktyg för att tänka i lugn och ro.
Färgteman och mörkt läge
För dig som gillar att hitta lösningen själv
Vem passar appen för?
Du gillar sudoku i tidningar och tidskrifter
Importera ditt vanliga pussel och fortsätt där du slutade.
Du vill ha ett tips före hela lösningen
Förstå det svåra stället och fortsätt sedan själv.
Du vill lära dig sudokutekniker
För nybörjare och alla som vill lära sig ännu en teknik.
Läs · Prova · Öva
Börja i webbläsaren.
Läs en guide eller spela ett helt pussel.
Från kandidatanteckningar till teknikförklaringar och övningar.
Prova ett helt pussel med tips när du behöver dem.
Upptäck reglerna och glädjen i att koppla ihop ledtrådar.
Se här hur ett tips fungerar
Varför måste den här rutan vara 5?
Titta på rutan med blå ram och öppna tipset.
Det här webbexemplet låter dig prova ett drag. Appens utseende skiljer sig.
När du fastnar i sudoku.
Rätt tips
för dina favoritsudokun.
Ladda ner {brand}
Gratis nedladdning · Köp i appen
Vanliga frågor
Kan jag använda appen gratis?
Appen kan laddas ner och provas gratis. Tips, svarkontroller och bildskanning har användningsgränser; vissa användningar kräver en videoannons.
Premium är en månads- eller årsprenumeration. Den tar bort annonser och ger obegränsade tips och svarkontroller. Bildskanning har fortfarande en gräns även med Premium. Priser och villkor finns i appen.
Kan jag använda pussel från tidningar?
Importera ett foto av ditt sudoku. Kontrollera de tolkade siffrorna och rätta eventuella fel innan du börjar. Vanliga 9×9-sudokun stöds.
Kan jag spela utan ett eget pussel?
Du kan spela inbyggda pussel och använda förklaringar och teknikövningar. Vissa pussel och övningar kräver Premium.
Kan jag prova innan jag installerar?
Utöver den här demon av ett drag kan du spela ett helt pussel i webbläsaren och utforska guider och övningar.''')

add('pl','''Skanowanie aparatem · Wskazówki z wyjaśnieniem
Utknąłeś przy sudoku?
Wskazówka w sam raz.
Skanuj sudoku z gazet i czasopism.
Zrozum, dlaczego cyfra pasuje, i rozwiązuj dalej samodzielnie.
iPhone i Android / Pobierz bezpłatnie · Zakupy w aplikacji
Rzeczywiste ekrany aplikacji
Wskazówki z wyjaśnieniem
Odczyt ze zdjęcia
Ćwiczenie technik
Notatki i tryb próbny
Wygodne motywy
Zdarza Ci się to podczas gry?
Chcesz znać odpowiedź.
Ale chcesz rozwiązać samodzielnie.
„Gdzie mam teraz spojrzeć?”
Sprawdzasz planszę raz za razem,
ale wciąż stoisz w tym samym miejscu.
„Sama odpowiedź niczego nie wyjaśnia.”
Dlaczego właśnie ta cyfra ma być tutaj?
Przepisywanie rozwiązania nie wystarcza.
„Wpisanie całej planszy trwa zbyt długo.”
Chcesz przenieść rozwiązywane papierowe sudoku
i kontynuować w aplikacji.
Zamień trudny moment w punkt zaczepienia
Funkcje
Zrób zdjęcie i zacznij.
Odczytaj sudoku z gazety lub czasopisma ze zdjęcia i ogranicz ręczne wpisywanie cyfr.
Zrozum „dlaczego”.
Poznaj uzasadnienie ruchu i użyj go do znalezienia kolejnego kroku zamiast tylko wpisywać odpowiedź.
Naucz się rozwiązywać.
Przeglądaj wyjaśnienia i ćwiczenia poszczególnych technik, a potem ucz się samodzielnie je dostrzegać.
Narzędzia do spokojnego myślenia.
Motywy kolorów i tryb ciemny
Dla tych, którzy lubią samodzielnie znajdować rozwiązania
Dla kogo jest aplikacja?
Lubisz sudoku z gazet i czasopism
Zaimportuj swoją planszę i kontynuuj od miejsca, w którym skończyłeś.
Chcesz wskazówki przed zobaczeniem całego rozwiązania
Zrozum trudny fragment, a potem rozwiązuj dalej samodzielnie.
Chcesz poznać techniki sudoku
Dla początkujących i osób chcących nauczyć się kolejnej techniki.
Czytaj · Wypróbuj · Ćwicz
Zacznij w przeglądarce.
Przeczytaj poradnik lub rozwiąż całą planszę.
Od notatek kandydatów po wyjaśnienia technik i ćwiczenia.
Spróbuj rozwiązać całą planszę, korzystając ze wskazówek w razie potrzeby.
Poznaj zasady i przyjemność łączenia kolejnych tropów.
Zobacz tutaj, jak działa wskazówka
Dlaczego w tej komórce musi być 5?
Spójrz na komórkę z niebieską ramką i otwórz wskazówkę.
To internetowy przykład jednego ruchu. Wygląd aplikacji jest inny.
Gdy utkniesz przy sudoku.
Właściwa wskazówka
do Twojego ulubionego sudoku.
Pobierz {brand}
Pobierz bezpłatnie · Zakupy w aplikacji
Często zadawane pytania
Czy mogę korzystać bezpłatnie?
Aplikację można bezpłatnie pobrać i wypróbować. Wskazówki, sprawdzanie odpowiedzi i skanowanie zdjęć mają limity; część użyć wymaga obejrzenia reklamy wideo.
Premium to subskrypcja miesięczna lub roczna. Usuwa reklamy i zapewnia nieograniczone wskazówki oraz sprawdzanie odpowiedzi. Skanowanie zdjęć pozostaje limitowane także w Premium. Ceny i warunki znajdziesz w aplikacji.
Czy mogę używać sudoku z gazet i czasopism?
Zaimportuj zdjęcie sudoku. Sprawdź rozpoznane cyfry i popraw błędy przed rozpoczęciem. Obsługiwane jest klasyczne sudoku 9×9.
Czy mogę grać bez własnej planszy?
Możesz rozwiązywać wbudowane plansze oraz korzystać z wyjaśnień i ćwiczeń technik. Część plansz i ćwiczeń wymaga Premium.
Czy mogę wypróbować przed instalacją?
Oprócz demonstracji jednego ruchu możesz rozwiązać całą planszę w przeglądarce oraz skorzystać z poradników i ćwiczeń.''')

add('tr','''Kamerayla tara · Açıklamalı ipuçları
Sudokuda takıldınız mı?
Tam ihtiyacınız olan ipucu.
Gazete ve dergilerdeki bulmacaları tarayın.
Bir rakamın neden uyduğunu anlayın, sonra kendiniz çözmeye devam edin.
iPhone ve Android / Ücretsiz indirme · Uygulama içi satın alımlar
Gerçek uygulama ekranları
Açıklamalı ipuçları
Görselden okuma
Teknik alıştırmaları
Notlar ve deneme modu
Rahat temalar
Oynarken bunlar oluyor mu?
Cevabı bilmek istiyorsunuz.
Ama kendiniz çözmek istiyorsunuz.
“Şimdi nereye bakmalıyım?”
Tabloyu tekrar tekrar inceliyorsunuz,
ama aynı yerde takılı kalıyorsunuz.
“Sadece cevap olması açıklamaya yetmiyor.”
O rakam neden oraya geliyor?
Çözümü kopyalamak yeterli değil.
“Bütün bulmacayı girmek çok uzun sürüyor.”
Çözdüğünüz kâğıt bulmacayı alıp
uygulamada devam etmek istiyorsunuz.
Takıldığınız yeri bir ipucuna dönüştürün
Özellikler
Fotoğraf çekin ve başlayın.
Gazete veya dergideki sudokuyu fotoğraftan okuyun ve rakamları tek tek girme işini azaltın.
“Neden”ini anlayın.
Bir hamlenin gerekçesini okuyup yalnızca cevabı doldurmak yerine sonraki adımınızı düşünmek için kullanın.
Çözmeyi öğrenin.
Tekniklere özel açıklama ve alıştırmaları keşfedin, sonra bu teknikleri kendiniz fark etmeyi çalışın.
Rahatça düşünmek için araçlar da var.
Renk temaları ve karanlık mod
Kendi çözümünü bulmaktan hoşlananlar için
Kimler için uygun?
Gazete ve dergilerdeki sudokuları seviyorsunuz
Alıştığınız bulmacayı içe aktarın ve kaldığınız yerden devam edin.
Tüm çözümü görmeden önce bir ipucu istiyorsunuz
Takıldığınız yerin nedenini anlayın ve kendiniz ilerleyin.
Sudoku tekniklerini öğrenmek istiyorsunuz
Yeni başlayanlar ve başka bir teknik öğrenmek isteyenler için.
Oku · Dene · Alıştırma yap
Tarayıcınızda başlayın.
Bir rehber okuyun veya tam bir bulmaca oynayın.
Aday notlarından teknik açıklamalarına ve alıştırmalara.
Gerektiğinde ipucu alarak bulmacanın tamamını çözmeyi deneyin.
Kuralları ve ipuçlarını birleştirmenin keyfini keşfedin.
Bir ipucunun nasıl çalıştığını burada görün
Bu hücre neden 5 olmalı?
Mavi çerçeveli hücreye bakın ve ipucunu açın.
Bu web örneği tek bir hamleyi denemenizi sağlar. Uygulamanın görünümü farklıdır.
Sudokuda takıldığınızda.
Doğru ipucu,
sevdiğiniz sudokular için.
{brand} uygulamasını indirin
Ücretsiz indirme · Uygulama içi satın alımlar
Sık sorulan sorular
Ücretsiz kullanabilir miyim?
Uygulama ücretsiz indirilip denenebilir. İpuçları, cevap kontrolleri ve görsel taramanın kullanım sınırları vardır; bazı kullanımlar video reklam izlemeyi gerektirir.
Premium aylık veya yıllık aboneliktir. Reklamları kaldırır, sınırsız ipucu ve cevap kontrolü sağlar. Görsel tarama Premium’da da sınırlıdır. Fiyat ve koşulları uygulamada görebilirsiniz.
Gazete veya dergi bulmacalarını kullanabilir miyim?
Sudokunun fotoğrafını içe aktarın. Başlamadan önce tanınan rakamları kontrol edip hataları düzeltin. Standart 9×9 sudokular desteklenir.
Kendi bulmacam olmadan oynayabilir miyim?
Uygulamadaki bulmacaları oynayabilir, teknik açıklamaları ve alıştırmaları kullanabilirsiniz. Bazı bulmaca ve alıştırmalar Premium gerektirir.
Yüklemeden önce deneyebilir miyim?
Bu tek hamlelik demoya ek olarak tarayıcıda tam bir bulmaca oynayabilir, teknik rehberlerini ve alıştırmaları inceleyebilirsiniz.''')

add('ru','''Сканирование камерой · Подсказки с объяснением
Застряли в судоку?
Подсказка в нужный момент.
Сканируйте судоку из газет и журналов.
Поймите, почему подходит цифра, и продолжайте решать самостоятельно.
iPhone и Android / Бесплатная загрузка · Покупки в приложении
Настоящие экраны приложения
Подсказки с объяснением
Распознавание по фото
Тренировка приёмов
Заметки и пробный режим
Удобные темы
Вам это знакомо?
Хочется узнать ответ.
Но решить хочется самому.
«Куда смотреть дальше?»
Вы снова и снова проверяете сетку,
но всё равно не можете сдвинуться с места.
«Сам ответ ничего не объясняет.»
Почему именно эта цифра должна стоять здесь?
Просто переписать решение недостаточно.
«Вводить всю головоломку слишком долго.»
Хочется взять судоку, которое решаете на бумаге,
и продолжить в приложении.
Превратите затруднение в зацепку
Возможности
Сфотографируйте и начинайте.
Распознайте судоку из газеты или журнала по фотографии и сократите ручной ввод цифр.
Поймите «почему».
Прочитайте обоснование хода и используйте его для следующего шага, а не просто вписывайте ответ.
Учитесь решать.
Изучайте объяснения и упражнения по отдельным приёмам, затем тренируйтесь замечать их самостоятельно.
Инструменты для спокойного решения.
Цветовые темы и тёмный режим
Для тех, кому нравится находить решение самому
Кому подойдёт приложение?
Вы любите судоку из газет и журналов
Импортируйте привычную головоломку и продолжите с того места, где остановились.
Вам нужна подсказка до просмотра всего решения
Разберитесь в сложном месте и продолжайте самостоятельно.
Вы хотите освоить приёмы судоку
Для новичков и тех, кто готов изучить ещё один приём.
Читайте · Пробуйте · Тренируйтесь
Начните в браузере.
Прочитайте руководство или решите целую головоломку.
От заметок о кандидатах до объяснений приёмов и упражнений.
Попробуйте решить всю сетку, обращаясь к подсказкам при необходимости.
Узнайте правила и почувствуйте удовольствие от связи подсказок.
Посмотрите здесь, как работает подсказка
Почему в этой клетке должна быть 5?
Посмотрите на клетку в синей рамке и откройте подсказку.
Этот веб-пример позволяет попробовать один ход. В приложении отображение отличается.
Когда судоку ставит в тупик.
Нужная подсказка
для любимого судоку.
Скачать {brand}
Бесплатная загрузка · Покупки в приложении
Частые вопросы
Можно пользоваться бесплатно?
Приложение можно бесплатно скачать и попробовать. Подсказки, проверка ответов и сканирование изображений ограничены; для некоторых действий нужно посмотреть видеорекламу.
Premium — месячная или годовая подписка. Она убирает рекламу и даёт неограниченные подсказки и проверки ответов. Сканирование изображений ограничено и в Premium. Цены и условия указаны в приложении.
Подойдут головоломки из газет и журналов?
Импортируйте фотографию судоку. Проверьте распознанные цифры и исправьте ошибки до начала игры. Поддерживается классическое судоку 9×9.
Можно играть без собственной головоломки?
В приложении есть встроенные головоломки, объяснения и упражнения по приёмам. Для некоторых головоломок и упражнений нужен Premium.
Можно попробовать до установки?
Кроме демонстрации одного хода, в браузере можно решить целую головоломку и изучить руководства и упражнения.''')

add('uk','''Сканування камерою · Підказки з поясненням
Застрягли в судоку?
Саме та підказка, що потрібна.
Скануйте судоку з газет і журналів.
Зрозумійте, чому підходить цифра, і розв’язуйте далі самостійно.
iPhone та Android / Безкоштовне завантаження · Покупки в застосунку
Справжні екрани застосунку
Підказки з поясненням
Розпізнавання з фото
Вправи з технік
Нотатки й пробний режим
Зручні теми
Вам це знайомо?
Хочеться знати відповідь.
Але розв’язати хочеться самому.
«Куди дивитися далі?»
Ви знову й знову перевіряєте сітку,
але досі стоїте на тому самому місці.
«Сама відповідь нічого не пояснює.»
Чому саме ця цифра має бути тут?
Просто переписати розв’язок недостатньо.
«Вводити всю головоломку надто довго.»
Хочеться взяти паперове судоку, яке розв’язуєте,
і продовжити в застосунку.
Перетворіть складний момент на зачіпку
Можливості
Сфотографуйте й починайте.
Розпізнайте судоку з газети чи журналу за фотографією та зменште ручне введення цифр.
Зрозумійте «чому».
Прочитайте обґрунтування ходу й використайте його для наступного кроку, а не просто вписуйте відповідь.
Вчіться розв’язувати.
Переглядайте пояснення та вправи з окремих технік і тренуйтеся знаходити їх самостійно.
Інструменти для спокійного розв’язування.
Колірні теми й темний режим
Для тих, хто любить знаходити розв’язок самостійно
Кому підійде застосунок?
Ви любите судоку з газет і журналів
Імпортуйте звичну головоломку й продовжте з місця, де зупинилися.
Вам потрібна підказка до перегляду всього розв’язку
Зрозумійте складне місце й рухайтеся далі самостійно.
Ви хочете опанувати техніки судоку
Для початківців і тих, хто хоче вивчити ще одну техніку.
Читайте · Пробуйте · Тренуйтеся
Почніть у браузері.
Прочитайте посібник або розв’яжіть цілу головоломку.
Від нотаток кандидатів до пояснень технік і вправ.
Спробуйте розв’язати всю сітку з підказками за потреби.
Дізнайтеся правила й відчуйте задоволення від поєднання підказок.
Подивіться тут, як працює підказка
Чому в цій клітинці має бути 5?
Подивіться на клітинку в синій рамці й відкрийте підказку.
Цей вебприклад дозволяє спробувати один хід. Вигляд застосунку відрізняється.
Коли застрягли в судоку.
Потрібна підказка
для улюбленого судоку.
Завантажити {brand}
Безкоштовне завантаження · Покупки в застосунку
Поширені запитання
Чи можна користуватися безкоштовно?
Застосунок можна безкоштовно завантажити й спробувати. Підказки, перевірки відповідей і сканування зображень мають обмеження; деякі дії потребують перегляду відеореклами.
Premium — місячна або річна підписка. Вона прибирає рекламу й надає необмежені підказки та перевірки відповідей. Сканування зображень залишається обмеженим і в Premium. Ціни й умови вказано в застосунку.
Чи можна використовувати судоку з газет і журналів?
Імпортуйте фото судоку. Перевірте розпізнані цифри й виправте помилки перед початком. Підтримується класичне судоку 9×9.
Чи можна грати без власної головоломки?
Можна розв’язувати вбудовані головоломки та користуватися поясненнями й вправами з технік. Деякі головоломки та вправи потребують Premium.
Чи можна спробувати до встановлення?
Крім демонстрації одного ходу, у браузері можна розв’язати цілу головоломку й переглянути посібники та вправи.''')

add('ar','''امسح بالكاميرا · تلميحات مع الشرح
هل تعثرت في السودوكو؟
التلميح المناسب لك.
امسح ألغاز الصحف والمجلات بالكاميرا.
افهم سبب ملاءمة الرقم، ثم واصل الحل بنفسك.
iPhone وAndroid / تنزيل مجاني · مشتريات داخل التطبيق
شاشات فعلية من التطبيق
تلميحات مع الشرح
قراءة من صورة
تدريب على التقنيات
ملاحظات ووضع التجربة
سمات مريحة
هل يحدث لك هذا أثناء اللعب؟
تريد معرفة الإجابة.
لكنك تريد الوصول إليها بنفسك.
«أين ينبغي أن أبحث الآن؟»
تراجع الشبكة مرارًا وتكرارًا،
لكنك تبقى عالقًا في الموضع نفسه.
«الإجابة وحدها لا تشرح السبب.»
لماذا يجب وضع هذا الرقم هنا؟
نسخ الحل ليس كافيًا.
«إدخال اللغز كله يدويًا يستغرق وقتًا طويلًا.»
تريد نقل لغز الورق الذي تحله
ومتابعته في التطبيق.
حوّل موضع التعثر إلى دليل
الميزات
التقط صورة وابدأ.
اقرأ لغز سودوكو من صحيفة أو مجلة عبر صورة، وقلّل إدخال الأرقام يدويًا.
افهم «لماذا».
اقرأ منطق الخطوة واستخدمه للتفكير في الخطوة التالية، بدلًا من مجرد إدخال الإجابة.
تعلّم طرق الحل.
استكشف شروح التقنيات وتمارينها، ثم تدرّب على اكتشافها بنفسك.
أدوات للتفكير على مهل أيضًا.
سمات الألوان والوضع الداكن
لمن يستمتع بالوصول إلى الحل بنفسه
لمن يناسب التطبيق؟
تحب ألغاز السودوكو في الصحف والمجلات
استورد لغزك المعتاد وتابع من حيث توقفت.
تريد تلميحًا قبل رؤية الحل كاملًا
افهم سبب الخطوة الصعبة، ثم تابع الحل بنفسك.
تريد تعلّم تقنيات السودوكو
للمبتدئين ولكل من يريد تعلّم تقنية جديدة.
اقرأ · جرّب · تدرّب
ابدأ في المتصفح.
اقرأ دليلًا أو العب لغزًا كاملًا.
من ملاحظات المرشحين إلى شروح التقنيات والتدريب.
حاول إكمال لغز كامل مع التلميحات عند الحاجة.
اكتشف القواعد ومتعة الربط بين الأدلة.
شاهد هنا كيف يعمل التلميح
لماذا يجب أن تحتوي هذه الخانة على 5؟
انظر إلى الخانة ذات الإطار الأزرق وافتح التلميح.
هذا مثال ويب لتجربة خطوة واحدة. يختلف العرض في التطبيق.
عندما تتعثر في السودوكو.
التلميح المناسب
لألغاز السودوكو التي تحبها.
نزّل {brand}
تنزيل مجاني · مشتريات داخل التطبيق
الأسئلة الشائعة
هل يمكنني استخدامه مجانًا؟
يمكن تنزيل التطبيق وتجربته مجانًا. توجد حدود لاستخدام التلميحات وفحص الإجابات وقراءة الصور؛ وتتطلب بعض الاستخدامات مشاهدة إعلان فيديو.
Premium اشتراك شهري أو سنوي يزيل الإعلانات ويتيح تلميحات وفحص إجابات بلا حدود. تبقى قراءة الصور محدودة حتى مع Premium. راجع الأسعار والشروط داخل التطبيق.
هل يمكنني استخدام ألغاز الصحف والمجلات؟
استورد صورة للغز السودوكو. تحقّق من الأرقام المقروءة وصحّح الأخطاء قبل البدء. يدعم التطبيق السودوكو التقليدي بحجم 9×9.
هل يمكنني اللعب دون لغز خاص بي؟
يمكنك لعب الألغاز المضمنة واستخدام شروح التقنيات وتمارينها. تتطلب بعض الألغاز والتمارين Premium.
هل يمكنني التجربة قبل التثبيت؟
إلى جانب عرض الخطوة الواحدة هنا، يمكنك لعب لغز كامل في المتصفح واستكشاف أدلة التقنيات وتمارينها.''')

add('hi','''कैमरे से स्कैन करें · कारण सहित संकेत
सुडोकू में अटक गए?
बस उतना संकेत, जितना चाहिए।
अख़बार और पत्रिकाओं की पहेलियाँ स्कैन करें।
समझें कि कोई अंक क्यों सही है, फिर खुद हल करना जारी रखें।
iPhone और Android / मुफ़्त डाउनलोड · ऐप में खरीदारी
ऐप की वास्तविक स्क्रीन
कारण सहित संकेत
तस्वीर से पढ़ें
तकनीकों का अभ्यास
नोट्स और परीक्षण मोड
आरामदायक थीम
क्या खेलते समय ऐसा होता है?
जवाब जानना चाहते हैं।
लेकिन खुद हल भी करना चाहते हैं।
“अब कहाँ देखूँ?”
बार-बार ग्रिड जाँचते हैं,
पर उसी जगह अटके रहते हैं।
“सिर्फ जवाब से कारण नहीं समझ आता।”
वही अंक उस जगह क्यों आएगा?
हल की नकल करना काफ़ी नहीं लगता।
“पूरी पहेली दर्ज करने में बहुत समय लगता है।”
कागज़ पर हल कर रहे सुडोकू को
ऐप में आगे जारी रखना चाहते हैं।
अटकाव को अगले सुराग में बदलें
सुविधाएँ
फ़ोटो लें और शुरू करें।
अख़बार या पत्रिका के सुडोकू को तस्वीर से पढ़ें और एक-एक अंक हाथ से दर्ज करने का काम कम करें।
“क्यों” समझें।
किसी चाल का तर्क पढ़ें और सिर्फ जवाब भरने के बजाय अगले कदम के लिए उसका उपयोग करें।
हल करने की तकनीक सीखें।
अलग-अलग तकनीकों की व्याख्या और अभ्यास देखें, फिर उन्हें खुद पहचानने का अभ्यास करें।
आराम से सोचने के लिए साधन भी।
रंग थीम और डार्क मोड
उनके लिए जिन्हें खुद हल खोजने में मज़ा आता है
यह ऐप किसके लिए है?
आपको अख़बार और पत्रिकाओं के सुडोकू पसंद हैं
अपनी पहेली आयात करें और वहीं से आगे बढ़ें जहाँ रुके थे।
पूरा हल देखने से पहले एक संकेत चाहते हैं
मुश्किल जगह का तर्क समझें और खुद आगे बढ़ें।
सुडोकू की तकनीक सीखना चाहते हैं
शुरुआती खिलाड़ियों और अगली तकनीक सीखने वालों के लिए।
पढ़ें · आज़माएँ · अभ्यास करें
ब्राउज़र में शुरू करें।
गाइड पढ़ें या पूरी पहेली खेलें।
संभावित अंकों के नोट्स से तकनीकों की व्याख्या और अभ्यास तक।
ज़रूरत पड़ने पर संकेत लेकर पूरी पहेली हल करने की कोशिश करें।
नियम और सुरागों को जोड़ने का आनंद जानें।
यहीं देखें कि संकेत कैसे काम करता है
इस खाने में 5 ही क्यों आएगा?
नीली सीमा वाले खाने को देखें और संकेत खोलें।
यह एक चाल आज़माने का वेब उदाहरण है। ऐप का प्रदर्शन अलग है।
जब सुडोकू में अटक जाएँ।
सही संकेत,
आपके पसंदीदा सुडोकू के लिए।
{brand} डाउनलोड करें
मुफ़्त डाउनलोड · ऐप में खरीदारी
अक्सर पूछे जाने वाले सवाल
क्या इसे मुफ़्त इस्तेमाल कर सकते हैं?
ऐप को मुफ़्त डाउनलोड करके आज़मा सकते हैं। संकेत, उत्तर की जाँच और तस्वीर पढ़ने की उपयोग सीमाएँ हैं; कुछ उपयोगों के लिए वीडियो विज्ञापन देखना होता है।
Premium मासिक या वार्षिक सदस्यता है। इससे विज्ञापन हटते हैं और असीमित संकेत तथा उत्तर जाँच मिलती है। Premium में भी तस्वीर पढ़ने की सीमा रहती है। कीमतें और शर्तें ऐप में देखें।
क्या अख़बार या पत्रिका की पहेलियाँ इस्तेमाल कर सकते हैं?
सुडोकू की तस्वीर आयात करें। शुरू करने से पहले पहचाने गए अंक जाँचें और गलतियाँ सुधारें। सामान्य 9×9 सुडोकू समर्थित है।
क्या अपनी पहेली के बिना खेल सकते हैं?
ऐप में शामिल पहेलियाँ खेल सकते हैं और तकनीकों की व्याख्या तथा अभ्यास इस्तेमाल कर सकते हैं। कुछ पहेलियों और अभ्यासों के लिए Premium चाहिए।
क्या इंस्टॉल करने से पहले आज़मा सकते हैं?
यहाँ एक चाल के डेमो के अलावा ब्राउज़र में पूरी पहेली खेल सकते हैं और तकनीकों की गाइड तथा अभ्यास देख सकते हैं।''')

add('id','''Pindai dengan kamera · Petunjuk dengan penjelasan
Buntu saat bermain sudoku?
Petunjuk yang pas untukmu.
Pindai teka-teki dari koran dan majalah.
Pahami mengapa suatu angka cocok, lalu lanjutkan sendiri.
iPhone & Android / Unduh gratis · Pembelian dalam aplikasi
Tampilan asli aplikasi
Petunjuk dengan penjelasan
Baca dari gambar
Latihan teknik
Catatan & mode uji coba
Tema yang nyaman
Pernah mengalami ini saat bermain?
Ingin tahu jawabannya.
Tapi ingin menyelesaikannya sendiri.
“Harus melihat ke mana lagi?”
Kamu memeriksa kotak berulang kali,
tetapi tetap buntu di bagian yang sama.
“Jawaban saja tidak menjelaskan alasannya.”
Mengapa angka itu harus di sana?
Menyalin solusi saja tidak cukup.
“Memasukkan seluruh teka-teki terlalu lama.”
Kamu ingin mengambil sudoku kertas yang sedang dikerjakan
dan melanjutkannya di aplikasi.
Ubah kebuntuan menjadi petunjuk
Fitur
Foto dan mulai.
Baca sudoku koran atau majalah dari foto dan kurangi pekerjaan memasukkan angka satu per satu.
Pahami “mengapa”.
Baca alasan di balik langkah dan gunakan untuk memikirkan langkah berikutnya, bukan sekadar mengisi jawaban.
Pelajari cara menyelesaikan.
Jelajahi penjelasan dan latihan tiap teknik, lalu berlatih menemukannya sendiri.
Alat untuk berpikir dengan santai juga.
Tema warna & mode gelap
Untuk yang senang menemukan solusi sendiri
Cocok untuk siapa?
Kamu suka sudoku di koran dan majalah
Impor teka-teki yang biasa kamu mainkan dan lanjutkan dari posisi terakhir.
Kamu ingin petunjuk sebelum melihat seluruh solusi
Pahami alasan di bagian sulit, lalu lanjutkan sendiri.
Kamu ingin mempelajari teknik sudoku
Untuk pemula dan siapa pun yang ingin belajar teknik berikutnya.
Baca · Coba · Berlatih
Mulai dari browser.
Baca panduan atau mainkan satu teka-teki lengkap.
Dari catatan kandidat hingga penjelasan teknik dan latihan.
Coba selesaikan satu teka-teki dengan petunjuk saat dibutuhkan.
Temukan aturan dan keseruan menghubungkan petunjuk.
Lihat cara kerja petunjuk di halaman ini
Mengapa sel ini harus berisi 5?
Perhatikan sel berbingkai biru dan buka petunjuknya.
Ini contoh web untuk mencoba satu langkah. Tampilan aplikasi berbeda.
Saat buntu dalam sudoku.
Petunjuk yang tepat
untuk sudoku favoritmu.
Unduh {brand}
Unduh gratis · Pembelian dalam aplikasi
Pertanyaan umum
Apakah bisa digunakan gratis?
Aplikasi dapat diunduh dan dicoba gratis. Petunjuk, pemeriksaan jawaban, dan pemindaian gambar memiliki batas penggunaan; beberapa penggunaan memerlukan iklan video.
Premium adalah langganan bulanan atau tahunan. Iklan dihapus dan petunjuk serta pemeriksaan jawaban tidak dibatasi. Pemindaian gambar tetap memiliki batas meskipun dengan Premium. Lihat harga dan ketentuan di aplikasi.
Bisa memakai teka-teki koran dan majalah?
Impor foto sudoku. Periksa angka yang dikenali dan perbaiki kesalahan sebelum mulai. Sudoku standar 9×9 didukung.
Bisa bermain tanpa teka-teki sendiri?
Kamu dapat memainkan teka-teki bawaan serta menggunakan penjelasan dan latihan teknik. Sebagian teka-teki dan latihan memerlukan Premium.
Bisa mencoba sebelum menginstal?
Selain demo satu langkah ini, kamu dapat memainkan satu teka-teki lengkap di browser serta menjelajahi panduan dan latihan teknik.''')

add('ko','''카메라로 스캔 · 이유를 알려 주는 힌트
스도쿠를 풀다가 막혔나요?
지금 필요한 만큼의 힌트를.
신문과 잡지의 문제도 카메라로 가져오세요.
숫자가 들어가는 이유를 이해하고, 다시 스스로 풀어 보세요.
iPhone·Android 지원 / 무료 다운로드 · 앱 내 구입
실제 앱 화면
이유를 알려 주는 힌트
이미지에서 읽기
기법별 연습
메모·가정 모드
편안한 테마
풀다 보면 이런 적 없나요?
답은 알고 싶어요.
하지만 직접 풀고 싶어요.
“다음에는 어디를 봐야 할까?”
몇 번이나 다시 살펴봐도 숫자를 넣지 못하고,
같은 곳에서 계속 막혀요.
“답만 봐서는 이해가 안 돼요.”
왜 그 숫자가 들어가는 걸까요?
정답을 옮겨 적는 것만으로는 부족해요.
“문제를 전부 입력하기는 번거로워요.”
지금 종이로 풀고 있는 문제를
앱에서도 이어서 풀고 싶어요.
막힌 순간을 다음 단서로
주요 기능
찍어서 가져오세요.
신문이나 잡지의 스도쿠를 사진에서 읽어 들여 숫자를 하나씩 입력하는 수고를 줄일 수 있어요.
“왜”인지 이해하세요.
힌트로 숫자가 들어가는 이유를 확인하세요. 정답을 채우는 데 그치지 않고 다음 수를 생각하는 단서로 삼을 수 있어요.
풀이 기법을 익히세요.
기법별 설명과 연습으로 궁금한 풀이를 확인하고, 배운 기법을 스스로 찾는 연습을 할 수 있어요.
차분하게 생각할 수 있는 기능도.
색상 테마·다크 모드
직접 푸는 즐거움을 소중히 여기는 분께
이런 분께 추천해요
신문과 잡지의 스도쿠를 즐기는 분
평소 풀던 문제를 가져와 멈춘 곳부터 이어서 풀고 싶어요.
전체 정답을 보기 전에 힌트가 필요한 분
막힌 부분의 이유를 이해하고 스스로 풀어 나가고 싶어요.
스도쿠 풀이 기법을 배우고 싶은 분
처음 시작하는 분도, 새로운 기법을 배우려는 분도.
읽기 · 체험 · 연습
먼저 브라우저에서 시작하세요.
설명을 읽거나 문제 하나를 끝까지 풀 수 있어요.
후보 메모부터 풀이 기법의 설명과 연습까지.
필요할 때 힌트를 사용하며 끝까지 도전하세요.
규칙과 단서가 이어지는 재미를 소개해요.
이 페이지에서 힌트가 작동하는 방식 보기
이 칸에는 왜 5가 들어갈까요?
파란 테두리의 칸을 보고 힌트를 열어 보세요.
한 수를 체험하는 웹 예제이며, 앱과 화면 구성이 달라요.
스도쿠를 풀다가 막혔다면.
딱 필요한 힌트를,
평소 즐기는 스도쿠에.
{brand} 다운로드
무료 다운로드 · 앱 내 구입
자주 묻는 질문
무료로 사용할 수 있나요?
무료로 다운로드해 체험할 수 있어요. 힌트·정답 확인·이미지 읽기 등에는 이용 횟수 제한이 있으며, 일부 이용 시 동영상 광고를 시청해야 해요.
Premium은 월간 또는 연간 구독이에요. 광고 제거와 무제한 힌트·정답 확인 등을 제공해요. 이미지 읽기는 Premium에도 제한이 있어요. 요금과 이용 조건은 앱에서 확인하세요.
신문과 잡지의 문제도 사용할 수 있나요?
스도쿠를 촬영한 이미지를 가져올 수 있어요. 읽어 들인 숫자를 확인하고 틀린 부분을 수정한 뒤 시작하세요. 일반적인 9×9 스도쿠를 지원해요.
문제가 없어도 플레이할 수 있나요?
앱에 포함된 문제와 기법별 설명·연습을 이용할 수 있어요. 일부 문제와 연습은 Premium 전용이에요.
설치하기 전에 체험할 수 있나요?
이 페이지의 한 수 데모 외에 브라우저에서 문제 하나를 끝까지 풀고 기법 설명과 연습을 살펴볼 수 있어요.''')

add('th','''สแกนด้วยกล้อง · คำใบ้พร้อมคำอธิบาย
ติดขัดกับซูโดกุอยู่ไหม?
คำใบ้ที่พอดีกับคุณ
สแกนโจทย์จากหนังสือพิมพ์และนิตยสารได้
เข้าใจว่าทำไมตัวเลขจึงลงช่องนั้น แล้วกลับไปแก้ต่อด้วยตัวเอง
iPhone และ Android / ดาวน์โหลดฟรี · การซื้อภายในแอป
หน้าจอจริงของแอป
คำใบ้พร้อมคำอธิบาย
อ่านจากรูปภาพ
ฝึกเทคนิค
จดตัวเลือกและโหมดทดลอง
ธีมที่สบายตา
เคยเจอแบบนี้ระหว่างเล่นไหม?
อยากรู้คำตอบ
แต่ก็อยากแก้ด้วยตัวเอง
“ต่อไปควรดูตรงไหน?”
ตรวจตารางซ้ำแล้วซ้ำเล่า
แต่ก็ยังติดอยู่ที่เดิม
“เห็นคำตอบอย่างเดียวก็ยังไม่เข้าใจ”
ทำไมตัวเลขนั้นต้องอยู่ช่องนี้?
แค่ลอกเฉลยยังไม่ตอบโจทย์
“กรอกโจทย์ทั้งตารางใช้เวลานานเกินไป”
อยากนำซูโดกุบนกระดาษที่กำลังแก้
มาเล่นต่อในแอป
เปลี่ยนจุดที่ติดให้เป็นเบาะแส
ฟีเจอร์
ถ่ายรูปแล้วเริ่มได้เลย
อ่านซูโดกุจากหนังสือพิมพ์หรือนิตยสารผ่านรูปถ่าย ลดการกรอกตัวเลขทีละช่อง
เข้าใจว่า “ทำไม”
อ่านเหตุผลของแต่ละก้าว แล้วนำไปคิดหาก้าวต่อไป แทนการเติมคำตอบอย่างเดียว
เรียนรู้วิธีแก้
ดูคำอธิบายและแบบฝึกแยกตามเทคนิค แล้วฝึกสังเกตเทคนิคเหล่านั้นด้วยตัวเอง
มีเครื่องมือให้คิดอย่างใจเย็นด้วย
ธีมสีและโหมดมืด
สำหรับคนที่สนุกกับการหาคำตอบด้วยตัวเอง
เหมาะกับใคร?
ชอบซูโดกุในหนังสือพิมพ์และนิตยสาร
นำเข้าโจทย์ที่เล่นอยู่ แล้วแก้ต่อจากจุดเดิม
อยากได้คำใบ้ก่อนดูเฉลยทั้งหมด
เข้าใจเหตุผลในจุดที่ติด แล้วแก้ต่อด้วยตัวเอง
อยากเรียนรู้เทคนิคซูโดกุ
สำหรับผู้เริ่มต้นและคนที่อยากเรียนเทคนิคถัดไป
อ่าน · ทดลอง · ฝึกฝน
เริ่มในเบราว์เซอร์ได้เลย
อ่านคู่มือหรือลองเล่นโจทย์เต็มหนึ่งข้อ
ตั้งแต่การจดตัวเลือก ไปจนถึงคำอธิบายเทคนิคและแบบฝึก
ลองแก้จนจบ โดยใช้คำใบ้เมื่อจำเป็น
เรียนรู้กติกาและความสนุกของการเชื่อมโยงเบาะแส
ดูการทำงานของคำใบ้ได้ในหน้านี้
ทำไมช่องนี้ต้องเป็นเลข 5?
ดูช่องที่มีกรอบสีน้ำเงิน แล้วเปิดคำใบ้
นี่คือตัวอย่างบนเว็บสำหรับทดลองหนึ่งก้าว หน้าจอในแอปจะแตกต่างกัน
เมื่อติดขัดกับซูโดกุ
คำใบ้ที่เหมาะสม
สำหรับซูโดกุที่คุณชอบ
ดาวน์โหลด {brand}
ดาวน์โหลดฟรี · การซื้อภายในแอป
คำถามที่พบบ่อย
ใช้งานฟรีได้ไหม?
ดาวน์โหลดและทดลองได้ฟรี คำใบ้ การตรวจคำตอบ และการอ่านภาพมีข้อจำกัดจำนวนครั้ง บางการใช้งานต้องรับชมโฆษณาวิดีโอ
Premium เป็นการสมัครสมาชิกรายเดือนหรือรายปี ช่วยลบโฆษณาและใช้คำใบ้กับการตรวจคำตอบได้ไม่จำกัด การอ่านภาพยังมีขีดจำกัดแม้ใช้ Premium ดูราคาและเงื่อนไขได้ในแอป
ใช้โจทย์จากหนังสือพิมพ์และนิตยสารได้ไหม?
นำเข้ารูปถ่ายซูโดกุ ตรวจสอบตัวเลขที่อ่านได้และแก้ไขข้อผิดพลาดก่อนเริ่ม รองรับซูโดกุมาตรฐานขนาด 9×9
เล่นได้ไหมถ้าไม่มีโจทย์ของตัวเอง?
เล่นโจทย์ที่มีในแอป พร้อมดูคำอธิบายและฝึกเทคนิคได้ โจทย์และแบบฝึกบางส่วนต้องใช้ Premium
ทดลองก่อนติดตั้งได้ไหม?
นอกจากเดโมหนึ่งก้าวในหน้านี้ ยังเล่นโจทย์เต็มหนึ่งข้อในเบราว์เซอร์ พร้อมอ่านคู่มือและฝึกเทคนิคได้ด้วย''')

add('vi','''Quét bằng máy ảnh · Gợi ý có giải thích
Bạn đang bí Sudoku?
Gợi ý vừa đủ cho bạn.
Quét câu đố từ báo và tạp chí.
Hiểu vì sao một số phù hợp, rồi tiếp tục tự giải.
iPhone và Android / Tải miễn phí · Mua trong ứng dụng
Màn hình thật của ứng dụng
Gợi ý có giải thích
Đọc từ hình ảnh
Luyện từng kỹ thuật
Ghi chú và chế độ thử
Giao diện dễ nhìn
Bạn có gặp những lúc này không?
Bạn muốn biết đáp án.
Nhưng vẫn muốn tự giải.
“Tiếp theo nên nhìn vào đâu?”
Bạn kiểm tra bảng hết lần này đến lần khác,
nhưng vẫn mắc ở cùng một chỗ.
“Chỉ có đáp án thì chưa hiểu được.”
Tại sao số đó lại nằm ở đây?
Chép lời giải thôi là chưa đủ.
“Nhập cả câu đố mất quá nhiều thời gian.”
Bạn muốn lấy Sudoku trên giấy đang giải
và tiếp tục trong ứng dụng.
Biến chỗ bế tắc thành một manh mối
Tính năng
Chụp ảnh và bắt đầu.
Đọc Sudoku từ ảnh báo hoặc tạp chí, giảm việc nhập từng số bằng tay.
Hiểu được “vì sao”.
Đọc lập luận của một nước đi và dùng nó để nghĩ bước tiếp theo, thay vì chỉ điền đáp án.
Học cách giải.
Xem giải thích và bài luyện cho từng kỹ thuật, rồi tập tự nhận ra chúng.
Công cụ để thong thả suy nghĩ.
Chủ đề màu và chế độ tối
Dành cho người thích tự tìm lời giải
Ứng dụng phù hợp với ai?
Bạn thích Sudoku trên báo và tạp chí
Nhập câu đố quen thuộc và tiếp tục từ chỗ đang dở.
Bạn muốn gợi ý trước khi xem toàn bộ lời giải
Hiểu lý do ở chỗ khó, rồi tự giải tiếp.
Bạn muốn học kỹ thuật Sudoku
Cho người mới bắt đầu và người muốn học thêm kỹ thuật.
Đọc · Thử · Luyện tập
Bắt đầu ngay trên trình duyệt.
Đọc hướng dẫn hoặc chơi trọn một câu đố.
Từ ghi chú ứng viên đến giải thích kỹ thuật và bài luyện.
Thử giải đến cuối với gợi ý khi cần.
Khám phá luật chơi và niềm vui khi kết nối manh mối.
Xem cách gợi ý hoạt động ngay tại đây
Vì sao ô này phải là 5?
Nhìn ô có viền xanh và mở gợi ý.
Đây là ví dụ trên web để thử một nước đi. Giao diện ứng dụng khác với ví dụ này.
Khi bạn bí Sudoku.
Gợi ý phù hợp
cho Sudoku bạn yêu thích.
Tải {brand}
Tải miễn phí · Mua trong ứng dụng
Câu hỏi thường gặp
Có thể dùng miễn phí không?
Ứng dụng được tải và dùng thử miễn phí. Gợi ý, kiểm tra đáp án và đọc ảnh có giới hạn lượt dùng; một số lượt cần xem quảng cáo video.
Premium là gói đăng ký tháng hoặc năm. Gói này bỏ quảng cáo và cho dùng gợi ý, kiểm tra đáp án không giới hạn. Việc đọc ảnh vẫn có giới hạn dù dùng Premium. Xem giá và điều kiện trong ứng dụng.
Có dùng câu đố trên báo và tạp chí được không?
Nhập ảnh chụp Sudoku. Kiểm tra các số được nhận dạng và sửa lỗi trước khi bắt đầu. Hỗ trợ Sudoku chuẩn 9×9.
Không có câu đố riêng thì có chơi được không?
Bạn có thể chơi các câu đố có sẵn và dùng phần giải thích, luyện kỹ thuật. Một số câu đố và bài luyện cần Premium.
Có thể thử trước khi cài đặt không?
Ngoài bản minh họa một nước đi, bạn có thể chơi trọn một câu đố trên trình duyệt và xem hướng dẫn cùng bài luyện kỹ thuật.''')

add('zh_CN','''相机识别 · 带理由的提示
数独卡住了？
给你恰到好处的提示。
报纸、杂志上的题目，也能拍照导入。
理解数字为何能填在这里，再继续自己解题。
iPhone、Android / 免费下载 · App 内购买
实际应用画面
带理由的提示
从图片识别
按技巧练习
候选笔记与假设模式
舒适的主题
解题时，你也遇到过这些情况吗？
想知道答案。
但更想自己解出来。
“接下来该看哪里？”
反复检查棋盘，还是填不出数字，
一直卡在同一个地方。
“只看答案，还是不明白。”
为什么这里一定是这个数字？
照着答案填，并不能满足好奇心。
“手动输入整道题太麻烦。”
想把手头正在做的纸上数独，
直接放到应用里继续解。
把卡住的地方，变成下一条线索
主要功能
拍下来，导入题目。
从报纸或杂志的照片中识别数独，减少逐个输入数字的麻烦。
看懂“为什么”。
通过提示了解数字能填入的理由。不只是补上答案，也为下一步思考提供线索。
学会解题技巧。
查看各类技巧的讲解和练习，再练习自己找出学过的技巧。
还有帮你慢慢思考的功能。
颜色主题与深色模式
献给享受独立解题乐趣的你
适合这些用户
喜欢报纸和杂志上的数独
导入平时在做的题目，从停下的地方继续。
想在看完整答案前，先获得一点提示
理解卡住之处的理由，再自己往下解。
想学习数独解题技巧
无论刚入门，还是想学下一个技巧。
阅读 · 体验 · 练习
先在浏览器里试试。
阅读讲解，或完整挑战一道题。
从候选笔记，到解题技巧的讲解和练习。
需要时使用提示，试着把一道题解到最后。
了解规则，感受线索相连的乐趣。
在本页看看提示如何起作用
为什么这个格子一定是 5？
注意蓝框格子，打开提示看看。
这是用于体验一步解法的网页示例，与应用中的显示不同。
数独卡住时。
让恰到好处的提示，
陪你解平时喜欢的数独。
下载 {brand}
免费下载 · App 内购买
常见问题
可以免费使用吗？
可以免费下载和体验。提示、答案检查、图片识别等有使用次数限制；部分使用需要观看视频广告。
Premium 为按月或按年订阅，可移除广告，并无限使用提示和答案检查等功能。即使订阅 Premium，图片识别仍有上限。价格及使用条件请在应用内确认。
可以使用报纸、杂志上的题目吗？
可以导入数独的照片。开始前请检查识别出的数字，并修正错误。支持标准的 9×9 数独。
没有自己的题目也能玩吗？
可以挑战应用内的题目，也能查看技巧讲解并练习。部分题目和练习需要 Premium。
安装前可以先体验吗？
除了本页的一步演示，还能在浏览器中完整挑战一道题，并阅读技巧讲解、进行练习。''')

add('zh_TW','''相機辨識 · 附理由的提示
數獨卡住了？
給你恰到好處的提示。
報紙、雜誌上的題目，也能拍照匯入。
理解數字為何能填在這裡，再繼續自己解題。
iPhone、Android / 免費下載 · App 內購買
實際應用程式畫面
附理由的提示
從圖片辨識
依技巧練習
候選筆記與假設模式
舒適的主題
解題時，你也遇過這些情況嗎？
想知道答案。
但更想自己解出來。
「接下來該看哪裡？」
反覆檢查盤面，還是填不出數字，
一直卡在同一個地方。
「只看答案，還是不明白。」
為什麼這裡一定是這個數字？
照著答案填，並不能滿足好奇心。
「手動輸入整道題太麻煩。」
想把手邊正在做的紙本數獨，
直接放進 App 裡繼續解。
把卡住的地方，變成下一條線索
主要功能
拍下來，匯入題目。
從報紙或雜誌的照片中辨識數獨，減少逐一輸入數字的麻煩。
看懂「為什麼」。
透過提示了解數字能填入的理由。不只是補上答案，也為下一步思考提供線索。
學會解題技巧。
查看各類技巧的講解與練習，再練習自己找出學過的技巧。
還有幫你慢慢思考的功能。
色彩主題與深色模式
獻給享受獨立解題樂趣的你
適合這些使用者
喜歡報紙和雜誌上的數獨
匯入平常在做的題目，從停下的地方繼續。
想在看完整答案前，先得到一點提示
理解卡住之處的理由，再自己往下解。
想學習數獨解題技巧
不論剛入門，還是想學下一個技巧。
閱讀 · 體驗 · 練習
先在瀏覽器裡試試。
閱讀講解，或完整挑戰一道題。
從候選筆記，到解題技巧的講解與練習。
需要時使用提示，試著把一道題解到最後。
了解規則，感受線索相連的樂趣。
在本頁看看提示如何發揮作用
為什麼這一格一定是 5？
注意藍框的格子，打開提示看看。
這是體驗一步解法的網頁範例，與 App 中的顯示不同。
數獨卡住時。
讓恰到好處的提示，
陪你解平常喜歡的數獨。
下載 {brand}
免費下載 · App 內購買
常見問題
可以免費使用嗎？
可以免費下載及體驗。提示、答案檢查、圖片辨識等有使用次數限制；部分使用需要觀看影片廣告。
Premium 為按月或按年訂閱，可移除廣告，並無限使用提示及答案檢查等功能。即使訂閱 Premium，圖片辨識仍有上限。價格與使用條件請在 App 內確認。
可以使用報紙、雜誌上的題目嗎？
可以匯入數獨的照片。開始前請檢查辨識出的數字，並修正錯誤。支援標準的 9×9 數獨。
沒有自己的題目也能玩嗎？
可以挑戰 App 內的題目，也能查看技巧講解並練習。部分題目與練習需要 Premium。
安裝前可以先體驗嗎？
除了本頁的一步示範，還能在瀏覽器中完整挑戰一道題，並閱讀技巧講解、進行練習。''')
