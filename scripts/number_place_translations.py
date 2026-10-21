"""Reviewed website copy. Technique explanations are read from the app ARB files."""
LABEL_KEYS='guide learn playTrial aboutApp language skip enjoy brain demoCaption play pause step reset style speed slow normal fast effects notes standard sparkle neon zen check clearSelection retry reveal nextExample hint erase undo privacy terms operator contents how example mistakes related practice question'.split()
TEXT_KEYS='hero intro rulesHeading enjoyIntro chainHeading chainText progressHeading progressText brainIntro researchHeading researchText limitsHeading limitsText habitText appHeading appText premium playIntro keyboard practiceIntro demoFoot gameFoot notesWarning singleWarning hiddenWarning pairWarning lockedWarning'.split()
MESSAGE_KEYS='cell empty given entered candidateLabel nextDigit placed progress completeDemo resetDemo motionPaused selected chooseCell wrong remaining gameComplete erasePrompt erased undoEmpty undone resetGame hintFallback practiceLocked placePrompt eliminatePrompt answerCount answerChosen digitToggle noAnswer practiceCorrect practiceWrong revealShown nakedPrompt pairPrompt clearedSelection placeReason placeEffect pairReason pairEffect elimination solutionLegend loadingFailure solutionTitle gameBoard practiceBoard answerDigits boardHelp'.split()
PACKS={}
def add(code,labels,texts,messages):
 chunks=[labels.split('|'),texts.split('\n'),messages.split('\n')]
 for keys,values in zip([LABEL_KEYS,TEXT_KEYS,MESSAGE_KEYS],chunks):
  assert len(keys)==len(values),(code,len(keys),len(values),list(zip(keys,values))[-3:])
  assert all(values),code
 PACKS[code]=dict(zip(LABEL_KEYS+TEXT_KEYS+MESSAGE_KEYS,sum(chunks,[])))

add('en',
'Sudoku guide|Learn techniques|Play one puzzle|About the app|Choose language|Skip to content|Why Sudoku is fun|Sudoku and brain training|Fill in the numbers like this|Play demo|Pause|One step|Start again|Effects|Speed|Slow|Normal|Fast|Show effects|Show candidates|Standard|Sparkle|Neon|Zen|Check answer|Clear selection|Try again|Show explanation|Next example|Hint for the next move|Erase number|Undo|Privacy policy|Terms of use|About the developer|On this page|How it works|Example|Common mistakes|Related guides|Practice|Question',
'''Play Sudoku and learn how to solve it.
Compare rows, columns and blocks to find where a number belongs. Watch the puzzle being solved, then try one yourself.
What is Sudoku?
Sudoku uses a 9×9 grid. Each row, column and 3×3 block must contain 1–9 exactly once. The given numbers are your clues.
One number can lead to the next.
If a cell has candidates 2 and 7 and a 2 is placed elsewhere in its row, it must be 7. That 7 can help narrow down other cells too.
Find techniques you have learned.
With practice, you start spotting singles and pairs yourself. A step that once needed a hint can become one you find on your own.
Sudoku asks you to compare positions, keep track of possibilities and check your reasoning. It can be an enjoyable way to spend time thinking.
What has research found?
A 2019 observational study compared self-reported number-puzzle frequency with cognitive test performance in 19,078 adults aged 50–93. More frequent puzzle use was associated with better performance on several measures of attention, reasoning and memory.
What the findings do not prove
The study did not establish that Sudoku caused the differences, prevented dementia or improved everyday thinking. People already good at these tasks may be more likely to play. It did not test this app.
Choose a difficulty you enjoy, use notes or hints when needed, and take breaks. Try the puzzle to see whether you enjoy the process rather than aiming for a promised health benefit.
Have more fun with Sudoku in the app!
Practise specific techniques or mixed exercises and save your progress. You can also scan a paper puzzle with the camera and read hints that explain the next move.
Free to try. Some exercises and hints require Premium.
Solve this fixed beginner puzzle from start to finish. Select a cell, then use the number buttons or keyboard. Each entry is checked immediately.
Use arrow keys to move between editable cells, 1–9 to enter a number, and Delete or Backspace to erase. Progress is not saved.
Two examples let you practise just one technique without solving a whole puzzle.
Choose from four effect styles for placing numbers and completing groups. The demo is silent.
One fixed puzzle, with candidates and logical hints. No account is needed.
Candidate notes are possibilities, not confirmed numbers. Check the row, column and block and update notes after each placement.
A lone note is reliable only if no candidates have been left out. Check the notes before confirming the number.
Check every empty cell in the chosen row, column or block. A number must have only one possible position there.
Both cells must have exactly the same two candidates. A pair such as {2,7} and {2,7,9} does not qualify. Do not erase the pair itself.
Check where all candidates for the number occur. Pointing removes candidates outside the block; claiming removes them elsewhere inside it.''',
'''row {row}, column {col}
empty cell
given number
entered number
candidates {digits}
{reason} Next, place {value}.
Place {value} in {cell}.
{reason} Placed {value}. ({count}/{total} cells)
All {total} cells are filled. During autoplay, the demo starts again after a short pause.
Back at the starting grid. The empty cells will be filled in order.
Autoplay is off. Use Play demo or One step to watch.
Selected {cell}. Choose a number.
Select an empty cell first.
{value} in {cell} does not match the solution. Check the other candidates.
{cell}: placed {value}. {count} cells remain.
Correct! The whole grid is complete.
Select an entered number to erase.
Erased the number in {cell}.
There is no entry to undo yet.
Returned to the previous move.
The starting puzzle has been restored. Undo returns to your previous position.
Check the candidates in an empty cell.
The explanation is open. Choose Try again to answer once more.
Choose the number to place.
Choose candidates to remove. Press a number again to deselect it.
Selected: {count}
Answer selected. Choose Check answer.
Select or deselect {value}
No answer selected yet. Select a cell and then a number.
Correct. Read the explanation below to see why.
That is not the answer for this technique. Check the cell, number, and any missing or extra eliminations.
Explanation shown. Choose Try again to attempt the same question.
Find a cell with just one candidate.
Find two cells with the same two candidates, then select what can be removed elsewhere.
All answer selections have been cleared.
{cell} has only candidate {value}, so that number can be placed there.
Answer: place {value} in {cell}.
{cells} each have only {digits}. Those two numbers occupy the pair, so remove them from other cells in {unit}.
Remove: {eliminations}. The order of the two numbers in the pair is still unknown.
{value} in {cell}
Outlined cells show the reason. Crossed-out candidates can be removed.
The exercise could not be loaded. Reload the page and try again.
Why this move works
Sudoku trial grid, 9 rows and 9 columns
Practice grid, 9 rows and 9 columns
Answer numbers
Rows are counted from top to bottom and columns from left to right. Select a cell and use the number buttons or arrow keys and 1–9.''')
add('fr',
'Guide du sudoku|Apprendre les techniques|Jouer une grille|À propos de l’application|Choisir la langue|Aller au contenu|Le plaisir du sudoku|Sudoku et entraînement cérébral|Voici comment remplir la grille|Lire la démo|Pause|Un coup|Recommencer|Effets|Vitesse|Lente|Normale|Rapide|Afficher les effets|Afficher les candidats|Standard|Étincelles|Néon|Zen|Vérifier|Effacer la sélection|Réessayer|Voir l’explication|Exemple suivant|Indice pour le prochain coup|Effacer le chiffre|Annuler|Confidentialité|Conditions d’utilisation|À propos du développeur|Sur cette page|Principe|Exemple|Erreurs fréquentes|Autres guides|S’entraîner|Question',
'''Jouez au sudoku et apprenez à le résoudre.
Comparez les lignes, colonnes et blocs pour trouver la place de chaque chiffre. Regardez la démo, puis essayez une grille.
Qu’est-ce que le sudoku ?
Une grille de 9×9 cases doit contenir les chiffres de 1 à 9 une seule fois par ligne, colonne et bloc de 3×3. Les chiffres déjà inscrits sont vos indices.
Un chiffre peut débloquer le suivant.
Une case a pour candidats 2 et 7 : si un 2 est placé ailleurs sur sa ligne, elle vaut 7. Ce 7 peut à son tour aider à résoudre d’autres cases.
Repérez les techniques que vous connaissez.
Avec l’habitude, vous reconnaissez les singles et les paires. Vous pouvez alors trouver seul un coup qui nécessitait auparavant un indice.
Le sudoku invite à comparer les positions, organiser les possibilités et vérifier un raisonnement. C’est une façon de prendre plaisir à réfléchir.
Que montrent les recherches ?
Une étude observationnelle de 2019 a comparé la fréquence déclarée des jeux de chiffres et les résultats cognitifs de 19 078 personnes de 50 à 93 ans. Une pratique plus fréquente était associée à de meilleurs résultats dans plusieurs tâches d’attention, de raisonnement et de mémoire.
Ce que l’étude ne prouve pas
Cette association ne démontre pas que le sudoku améliore les capacités quotidiennes ou prévient la démence. Les personnes déjà à l’aise avec ces tâches jouent peut-être davantage. L’étude n’évaluait pas cette application.
Choisissez une difficulté agréable, utilisez les notes ou les indices et faites des pauses. Essayez surtout pour voir si vous aimez chercher, sans viser un bénéfice de santé garanti.
Amusez-vous encore plus dans l’application !
Entraînez-vous par technique ou avec des exercices mixtes et enregistrez votre progression. Vous pouvez aussi scanner une grille papier et lire des indices expliqués.
Essai gratuit. Certains exercices et indices nécessitent Premium.
Résolvez cette grille fixe pour débutants. Sélectionnez une case et saisissez un chiffre avec les boutons ou le clavier. Chaque saisie est vérifiée.
Flèches : changer de case ; 1–9 : saisir ; Suppr ou Retour arrière : effacer. La progression n’est pas enregistrée.
Deux exemples permettent de travailler une seule technique sans résoudre toute une grille.
Quatre styles animent la saisie et les groupes complétés. La démo est silencieuse.
Une grille fixe avec candidats et indices logiques, sans compte.
Les notes indiquent des possibilités. Vérifiez ligne, colonne et bloc, puis actualisez-les après chaque chiffre confirmé.
Un seul candidat ne suffit que si aucun n’a été oublié. Vérifiez vos notes avant de confirmer.
Examinez toutes les cases vides du groupe : le chiffre doit n’y avoir qu’une seule position possible.
Les deux cases doivent avoir exactement les mêmes deux candidats. {2,7} et {2,7,9} ne forment pas une paire nue. N’effacez pas les candidats de la paire.
Vérifiez toutes les positions du candidat. Pointing supprime hors du bloc ; Claiming supprime ailleurs dans ce bloc.''',
'''ligne {row}, colonne {col}
case vide
chiffre donné
chiffre saisi
candidats {digits}
{reason} Placez ensuite {value}.
Placez {value} en {cell}.
{reason} {value} placé. ({count}/{total} cases)
Les {total} cases sont remplies. La lecture automatique reprend après une courte pause.
Retour à la grille de départ. Les cases seront remplies dans l’ordre.
La lecture automatique est arrêtée. Utilisez Lire la démo ou Un coup.
{cell} sélectionnée. Choisissez un chiffre.
Sélectionnez d’abord une case vide.
{value} en {cell} ne correspond pas à la solution. Vérifiez les autres candidats.
{cell} : {value} placé. Il reste {count} cases.
Bravo ! La grille est terminée.
Sélectionnez un chiffre saisi à effacer.
Le chiffre en {cell} a été effacé.
Aucune saisie à annuler pour le moment.
Retour au coup précédent.
La grille initiale est rétablie. Annuler restaure votre position précédente.
Examinez les candidats d’une case vide.
L’explication est affichée. Réessayer permet de répondre à nouveau.
Choisissez le chiffre à placer.
Choisissez les candidats à supprimer. Appuyez à nouveau pour désélectionner.
Sélection : {count}
Réponse sélectionnée. Appuyez sur Vérifier.
Sélectionner ou désélectionner {value}
Aucune réponse. Sélectionnez une case puis un chiffre.
Correct. L’explication ci-dessous indique pourquoi.
Ce n’est pas la réponse pour cette technique. Vérifiez les cases, chiffres et suppressions en trop ou manquantes.
Explication affichée. Appuyez sur Réessayer pour reprendre la même question.
Cherchez une case avec un seul candidat.
Cherchez deux cases aux deux mêmes candidats, puis ce qui peut être supprimé ailleurs.
Toutes les sélections sont effacées.
{cell} n’a que le candidat {value} : ce chiffre peut donc y être placé.
Réponse : placer {value} en {cell}.
{cells} n’ont que {digits}. Ces chiffres occupent la paire : supprimez-les des autres cases de {unit}.
Supprimer : {eliminations}. La répartition des deux chiffres de la paire reste inconnue.
{value} en {cell}
Les cases encadrées montrent la raison. Les candidats barrés peuvent être supprimés.
Impossible de charger l’exercice. Rechargez la page.
Pourquoi ce coup fonctionne
Grille d’essai, 9 lignes et 9 colonnes
Grille d’exercice, 9 lignes et 9 colonnes
Chiffres de réponse
Les lignes se comptent du haut vers le bas et les colonnes de gauche à droite. Sélectionnez une case puis utilisez les boutons ou le clavier.''')
add('de',
'Sudoku-Ratgeber|Techniken lernen|Ein Rätsel spielen|Über die App|Sprache wählen|Zum Inhalt|Was Sudoku spannend macht|Sudoku und Gehirntraining|So füllt sich das Sudoku|Demo starten|Pause|Ein Schritt|Neu beginnen|Effekte|Tempo|Langsam|Normal|Schnell|Effekte anzeigen|Kandidaten anzeigen|Standard|Funkeln|Neon|Zen|Antwort prüfen|Auswahl löschen|Erneut versuchen|Erklärung anzeigen|Nächstes Beispiel|Hinweis zum nächsten Zug|Zahl löschen|Rückgängig|Datenschutz|Nutzungsbedingungen|Über den Entwickler|Auf dieser Seite|So funktioniert es|Beispiel|Häufige Fehler|Weitere Anleitungen|Üben|Aufgabe',
'''Spiele Sudoku und lerne die Lösungswege kennen.
Vergleiche Zeilen, Spalten und Blöcke, um den Platz einer Zahl zu finden. Sieh der Demo zu und probiere dann selbst ein Rätsel.
Was ist Sudoku?
In einem 9×9-Raster muss jede Zeile, Spalte und jeder 3×3-Block die Zahlen 1 bis 9 genau einmal enthalten. Die vorgegebenen Zahlen sind deine Hinweise.
Eine Zahl kann die nächste ermöglichen.
Hat ein Feld die Kandidaten 2 und 7 und wird in seiner Zeile eine 2 gesetzt, bleibt die 7. Diese kann weitere Felder eingrenzen.
Erkenne gelernte Techniken selbst.
Mit der Zeit fallen dir Singles und Paare leichter auf. Einen Zug, für den du früher einen Hinweis brauchtest, findest du vielleicht selbst.
Beim Sudoku vergleichst du Positionen, ordnest Möglichkeiten und prüfst Schlussfolgerungen. Das kann eine unterhaltsame Beschäftigung zum Nachdenken sein.
Was zeigt die Forschung?
Eine Beobachtungsstudie von 2019 verglich selbst berichtete Zahlenrätsel-Häufigkeit mit kognitiven Tests bei 19.078 Menschen zwischen 50 und 93 Jahren. Häufigeres Rätseln hing mit besseren Ergebnissen bei mehreren Aufmerksamkeits-, Denk- und Gedächtnisaufgaben zusammen.
Was daraus nicht folgt
Die Studie beweist nicht, dass Sudoku die Unterschiede verursacht, Demenz verhindert oder das Denken im Alltag verbessert. Bereits leistungsfähigere Menschen spielen womöglich häufiger. Diese App wurde nicht untersucht.
Wähle eine angenehme Schwierigkeit, nutze Notizen oder Hinweise und mache Pausen. Probiere aus, ob dir das Lösen Spaß macht, ohne einen garantierten Gesundheitseffekt zu erwarten.
Mit der App macht Sudoku noch mehr Spaß!
Übe einzelne Techniken oder gemischte Aufgaben und speichere deinen Fortschritt. Du kannst auch ein Papierrätsel scannen und erklärende Hinweise lesen.
Kostenlos ausprobieren. Einige Übungen und Hinweise erfordern Premium.
Löse dieses feste Einsteigerrätsel vollständig. Wähle ein Feld und gib eine Zahl per Schaltfläche oder Tastatur ein. Jede Eingabe wird sofort geprüft.
Pfeiltasten wechseln das Feld, 1–9 geben Zahlen ein, Entf und Rücktaste löschen. Dein Zwischenstand wird nicht gespeichert.
Zwei Beispiele üben jeweils eine Technik, ohne ein ganzes Rätsel lösen zu müssen.
Vier Effektstile begleiten Eingaben und vollständige Gruppen. Die Demo bleibt lautlos.
Ein festes Rätsel mit Kandidaten und logischen Hinweisen, ohne Konto.
Notizen sind Möglichkeiten, keine bestätigten Zahlen. Prüfe Zeile, Spalte und Block und aktualisiere sie nach jeder Eingabe.
Ein einzelner Kandidat ist nur verlässlich, wenn keiner vergessen wurde. Prüfe die Notizen vor dem Bestätigen.
Prüfe alle leeren Felder der gewählten Gruppe. Die Zahl darf dort nur eine mögliche Position haben.
Beide Felder müssen genau dieselben zwei Kandidaten haben. {2,7} und {2,7,9} bilden kein nacktes Paar. Lösche nicht die Kandidaten des Paares selbst.
Prüfe alle Positionen eines Kandidaten. Pointing entfernt außerhalb des Blocks, Claiming an anderen Stellen innerhalb des Blocks.''',
'''Zeile {row}, Spalte {col}
leeres Feld
vorgegebene Zahl
eingetragene Zahl
Kandidaten {digits}
{reason} Als Nächstes wird {value} gesetzt.
Setze {value} in {cell}.
{reason} {value} gesetzt. ({count}/{total} Felder)
Alle {total} Felder sind gefüllt. Die automatische Demo beginnt nach einer kurzen Pause von vorn.
Zurück zum Ausgangsraster. Die leeren Felder werden nacheinander gefüllt.
Automatische Wiedergabe ist aus. Nutze Demo starten oder Ein Schritt.
{cell} ausgewählt. Wähle eine Zahl.
Wähle zuerst ein leeres Feld.
{value} in {cell} stimmt nicht mit der Lösung überein. Prüfe die übrigen Kandidaten.
{cell}: {value} gesetzt. Noch {count} Felder.
Richtig! Das ganze Raster ist gelöst.
Wähle eine eingetragene Zahl zum Löschen.
Die Zahl in {cell} wurde gelöscht.
Es gibt noch keine Eingabe zum Rückgängigmachen.
Zum vorherigen Zug zurückgekehrt.
Das Ausgangsrätsel wurde wiederhergestellt. Rückgängig bringt den vorherigen Stand zurück.
Prüfe die Kandidaten eines leeren Feldes.
Die Erklärung ist geöffnet. Mit Erneut versuchen kannst du noch einmal antworten.
Wähle die einzutragende Zahl.
Wähle Kandidaten zum Entfernen. Erneutes Drücken hebt die Auswahl auf.
Ausgewählt: {count}
Antwort ausgewählt. Drücke Antwort prüfen.
{value} auswählen oder abwählen
Noch keine Antwort. Wähle ein Feld und anschließend eine Zahl.
Richtig. Die Erklärung unten zeigt den Grund.
Das ist nicht die Antwort für diese Technik. Prüfe Feld, Zahl sowie fehlende oder zusätzliche Streichungen.
Erklärung angezeigt. Mit Erneut versuchen startest du dieselbe Aufgabe erneut.
Suche ein Feld mit genau einem Kandidaten.
Suche zwei Felder mit denselben zwei Kandidaten und wähle die anderswo entfernbaren Kandidaten.
Alle Antwortauswahlen wurden gelöscht.
{cell} hat nur den Kandidaten {value}; diese Zahl kann dort gesetzt werden.
Antwort: {value} in {cell} setzen.
{cells} haben nur {digits}. Diese Zahlen belegen das Paar und können aus anderen Feldern von {unit} entfernt werden.
Entfernen: {eliminations}. Die Reihenfolge der beiden Zahlen im Paar ist noch offen.
{value} in {cell}
Umrandete Felder zeigen die Begründung. Durchgestrichene Kandidaten können entfernt werden.
Die Übung konnte nicht geladen werden. Lade die Seite neu.
Warum dieser Zug möglich ist
Sudoku-Testraster mit 9 Zeilen und 9 Spalten
Übungsraster mit 9 Zeilen und 9 Spalten
Antwortzahlen
Zeilen zählen von oben nach unten, Spalten von links nach rechts. Wähle ein Feld und nutze die Zahlentasten oder die Tastatur.''')
add('es',
'Guía de sudoku|Aprender técnicas|Jugar un sudoku|Sobre la app|Elegir idioma|Ir al contenido|El encanto del sudoku|Sudoku y entrenamiento mental|Así puedes completar la cuadrícula|Reproducir demo|Pausa|Un paso|Reiniciar|Efectos|Velocidad|Lenta|Normal|Rápida|Mostrar efectos|Mostrar candidatos|Estándar|Destellos|Neón|Zen|Comprobar respuesta|Borrar selección|Reintentar|Ver explicación|Siguiente ejemplo|Pista para el próximo paso|Borrar número|Deshacer|Privacidad|Condiciones de uso|Sobre el desarrollador|En esta página|Cómo funciona|Ejemplo|Errores habituales|Otras guías|Practicar|Pregunta',
'''Juega al sudoku y aprende a resolverlo.
Compara filas, columnas y bloques para encontrar dónde va cada número. Mira la demo y prueba un sudoku.
¿Qué es el sudoku?
En una cuadrícula de 9×9, cada fila, columna y bloque de 3×3 debe contener del 1 al 9 una sola vez. Los números iniciales son tus pistas.
Un número puede llevarte al siguiente.
Si una casilla tiene los candidatos 2 y 7 y aparece un 2 en su fila, debe ser 7. Ese 7 también puede aclarar otras casillas.
Reconoce las técnicas que has aprendido.
Con práctica empezarás a ver singles y parejas por tu cuenta. Un paso que antes requería una pista puede convertirse en uno que encuentres tú.
El sudoku invita a comparar posiciones, ordenar posibilidades y comprobar el razonamiento. Puede ser una forma entretenida de dedicar tiempo a pensar.
¿Qué dicen los estudios?
Un estudio observacional de 2019 comparó la frecuencia declarada de pasatiempos numéricos y pruebas cognitivas de 19.078 personas de 50 a 93 años. Una mayor frecuencia se asoció con mejores resultados en varias tareas de atención, razonamiento y memoria.
Lo que el estudio no demuestra
No prueba que el sudoku causara esas diferencias, prevenga la demencia ni mejore las capacidades cotidianas. Quienes ya tienen más facilidad quizá jueguen más. Tampoco estudió esta app.
Elige una dificultad que disfrutes, usa notas o pistas y descansa. Prueba si te gusta resolverlo, sin esperar un beneficio de salud garantizado.
¡Disfruta aún más del sudoku con la app!
Practica técnicas concretas o ejercicios mixtos y guarda tu progreso. También puedes escanear un sudoku en papel y consultar pistas explicadas.
Puedes probarla gratis. Algunos ejercicios y pistas requieren Premium.
Resuelve este sudoku fijo para principiantes. Selecciona una casilla e introduce un número con los botones o el teclado. Cada entrada se comprueba al instante.
Usa las flechas para moverte, 1–9 para escribir y Supr o Retroceso para borrar. El progreso no se guarda.
Dos ejemplos permiten practicar una técnica sin resolver una cuadrícula entera.
Cuatro estilos animan las entradas y los grupos completados. La demo no tiene sonido.
Un sudoku fijo con candidatos y pistas lógicas, sin cuenta.
Las notas son posibilidades, no números confirmados. Revisa fila, columna y bloque y actualízalas después de cada colocación.
Un único candidato solo es fiable si no has olvidado ninguno. Revisa las notas antes de confirmar.
Revisa todas las casillas vacías del grupo. El número debe tener una sola posición posible.
Ambas casillas deben tener exactamente los mismos dos candidatos. {2,7} y {2,7,9} no forman una pareja desnuda. No borres los candidatos de la pareja.
Comprueba todas las posiciones del candidato. Pointing elimina fuera del bloque; Claiming, en otras casillas de su interior.''',
'''fila {row}, columna {col}
casilla vacía
número inicial
número introducido
candidatos {digits}
{reason} A continuación se coloca {value}.
Coloca {value} en {cell}.
{reason} Se ha colocado {value}. ({count}/{total} casillas)
Las {total} casillas están completas. La demo automática se reinicia tras una breve pausa.
Se ha vuelto a la cuadrícula inicial. Las casillas se rellenarán en orden.
La reproducción automática está desactivada. Pulsa Reproducir demo o Un paso.
Has seleccionado {cell}. Elige un número.
Selecciona primero una casilla vacía.
{value} en {cell} no coincide con la solución. Revisa los otros candidatos.
{cell}: se ha colocado {value}. Quedan {count} casillas.
¡Correcto! Has completado el sudoku.
Selecciona un número introducido para borrarlo.
Se ha borrado el número de {cell}.
Todavía no hay entradas que deshacer.
Se ha vuelto al paso anterior.
Se ha restaurado el sudoku inicial. Deshacer recupera la posición anterior.
Revisa los candidatos de una casilla vacía.
La explicación está abierta. Pulsa Reintentar para volver a responder.
Elige el número que quieres colocar.
Elige los candidatos que se pueden eliminar. Vuelve a pulsar para quitar la selección.
Seleccionados: {count}
Respuesta seleccionada. Pulsa Comprobar respuesta.
Seleccionar o deseleccionar {value}
No has elegido una respuesta. Selecciona una casilla y un número.
Correcto. La explicación de abajo muestra por qué.
No es la respuesta de esta técnica. Revisa la casilla, el número y las eliminaciones que falten o sobren.
Explicación mostrada. Pulsa Reintentar para repetir la pregunta.
Busca una casilla con un solo candidato.
Busca dos casillas con los mismos dos candidatos y selecciona qué se elimina en las demás.
Se han borrado todas las selecciones.
{cell} solo tiene el candidato {value}, por lo que puedes colocarlo ahí.
Respuesta: coloca {value} en {cell}.
{cells} solo tienen {digits}. Esos números ocupan la pareja y se eliminan de las otras casillas de {unit}.
Eliminar: {eliminations}. Todavía no sabemos el orden de los dos números de la pareja.
{value} en {cell}
Las casillas enmarcadas muestran el motivo. Los candidatos tachados se pueden eliminar.
No se pudo cargar el ejercicio. Recarga la página.
Por qué funciona este paso
Cuadrícula de prueba, 9 filas y 9 columnas
Cuadrícula de práctica, 9 filas y 9 columnas
Números de respuesta
Las filas se cuentan de arriba abajo y las columnas de izquierda a derecha. Selecciona una casilla y usa los botones o el teclado.''')
add('it',
'Guida al sudoku|Impara le tecniche|Gioca una griglia|Informazioni sull’app|Scegli lingua|Vai al contenuto|Il bello del sudoku|Sudoku e allenamento mentale|Ecco come riempire la griglia|Avvia demo|Pausa|Una mossa|Ricomincia|Effetti|Velocità|Lenta|Normale|Veloce|Mostra effetti|Mostra candidati|Standard|Scintille|Neon|Zen|Controlla risposta|Cancella selezione|Riprova|Mostra spiegazione|Esempio successivo|Indizio per la prossima mossa|Cancella numero|Annulla|Privacy|Condizioni d’uso|Informazioni sullo sviluppatore|In questa pagina|Come funziona|Esempio|Errori comuni|Altre guide|Esercitati|Domanda',
'''Gioca a sudoku e impara a risolverlo.
Confronta righe, colonne e blocchi per trovare il posto di ogni numero. Guarda la demo e prova una griglia.
Che cos’è il sudoku?
In una griglia 9×9, ogni riga, colonna e blocco 3×3 deve contenere i numeri da 1 a 9 una sola volta. I numeri già presenti sono gli indizi.
Un numero può sbloccare il successivo.
Se una casella ha i candidati 2 e 7 e nella sua riga viene inserito un 2, resta il 7. Quel 7 può aiutare a risolvere altre caselle.
Riconosci le tecniche che hai imparato.
Con la pratica noterai singoli e coppie da solo. Una mossa per cui serviva un indizio può diventare una scoperta tua.
Nel sudoku confronti posizioni, organizzi possibilità e verifichi il ragionamento. Può essere un modo piacevole di dedicare tempo a pensare.
Che cosa dice la ricerca?
Uno studio osservazionale del 2019 ha confrontato frequenza dichiarata di giochi numerici e test cognitivi di 19.078 persone tra 50 e 93 anni. Una frequenza maggiore era associata a risultati migliori in varie prove di attenzione, ragionamento e memoria.
Che cosa non dimostra lo studio
Non dimostra che il sudoku abbia causato le differenze, prevenga la demenza o migliori le capacità quotidiane. Chi è già abile potrebbe giocare di più. Questa app non è stata studiata.
Scegli una difficoltà piacevole, usa note o indizi e fai delle pause. Prova per capire se ti diverte cercare la soluzione, senza aspettarti benefici di salute garantiti.
Divertiti ancora di più con l’app!
Esercitati su singole tecniche o esercizi misti e salva i progressi. Puoi anche scansionare una griglia su carta e leggere indizi spiegati.
Provala gratis. Alcuni esercizi e indizi richiedono Premium.
Risolvi questa griglia fissa per principianti. Seleziona una casella e inserisci un numero con i pulsanti o la tastiera. Ogni inserimento viene verificato.
Le frecce cambiano casella; 1–9 inseriscono i numeri; Canc o Backspace cancellano. I progressi non vengono salvati.
Due esempi permettono di esercitare una tecnica senza risolvere tutta la griglia.
Quattro stili animano gli inserimenti e i gruppi completati. La demo è senza audio.
Una griglia fissa con candidati e indizi logici, senza account.
Le note indicano possibilità, non numeri certi. Controlla riga, colonna e blocco e aggiornale dopo ogni inserimento confermato.
Un solo candidato è affidabile soltanto se non ne hai dimenticati altri. Controlla le note prima di confermare.
Controlla tutte le caselle vuote del gruppo: il numero deve avere un’unica posizione possibile.
Le due caselle devono avere esattamente gli stessi due candidati. {2,7} e {2,7,9} non sono una coppia nuda. Non cancellare i candidati della coppia.
Controlla tutte le posizioni del candidato. Pointing elimina fuori dal blocco; Claiming elimina altrove al suo interno.''',
'''riga {row}, colonna {col}
casella vuota
numero iniziale
numero inserito
candidati {digits}
{reason} Ora inserisci {value}.
Inserisci {value} in {cell}.
{reason} Inserito {value}. ({count}/{total} caselle)
Tutte le {total} caselle sono complete. La demo automatica ricomincia dopo una breve pausa.
Ritorno alla griglia iniziale. Le caselle verranno riempite in ordine.
Riproduzione automatica disattivata. Usa Avvia demo o Una mossa.
Hai selezionato {cell}. Scegli un numero.
Seleziona prima una casella vuota.
{value} in {cell} non corrisponde alla soluzione. Controlla gli altri candidati.
{cell}: inserito {value}. Restano {count} caselle.
Corretto! Hai completato la griglia.
Seleziona un numero inserito da cancellare.
Il numero in {cell} è stato cancellato.
Non ci sono ancora inserimenti da annullare.
Ritorno alla mossa precedente.
Griglia iniziale ripristinata. Annulla recupera la posizione precedente.
Controlla i candidati di una casella vuota.
La spiegazione è aperta. Premi Riprova per rispondere ancora.
Scegli il numero da inserire.
Scegli i candidati da eliminare. Premi di nuovo per deselezionare.
Selezionati: {count}
Risposta selezionata. Premi Controlla risposta.
Seleziona o deseleziona {value}
Non hai scelto una risposta. Seleziona una casella e un numero.
Corretto. La spiegazione qui sotto mostra il motivo.
Non è la risposta per questa tecnica. Controlla casella, numero ed eliminazioni mancanti o in eccesso.
Spiegazione mostrata. Premi Riprova per ripetere la domanda.
Cerca una casella con un solo candidato.
Cerca due caselle con gli stessi due candidati e seleziona cosa eliminare nelle altre.
Tutte le selezioni sono state cancellate.
{cell} ha solo il candidato {value}, quindi puoi inserirlo lì.
Risposta: inserisci {value} in {cell}.
{cells} hanno solo {digits}. Questi numeri occupano la coppia: eliminali dalle altre caselle di {unit}.
Elimina: {eliminations}. L’ordine dei due numeri della coppia resta sconosciuto.
{value} in {cell}
Le caselle contornate mostrano il motivo. I candidati barrati si possono eliminare.
Impossibile caricare l’esercizio. Ricarica la pagina.
Perché questa mossa funziona
Griglia di prova, 9 righe e 9 colonne
Griglia di esercizio, 9 righe e 9 colonne
Numeri di risposta
Le righe si contano dall’alto e le colonne da sinistra. Seleziona una casella e usa i pulsanti o la tastiera.''')
add('pt',
'Guia de sudoku|Aprender técnicas|Jogar um sudoku|Sobre o aplicativo|Escolher idioma|Ir para o conteúdo|A diversão do sudoku|Sudoku e treino mental|Veja como preencher os números|Reproduzir demo|Pausar|Uma jogada|Recomeçar|Efeitos|Velocidade|Lenta|Normal|Rápida|Mostrar efeitos|Mostrar candidatos|Padrão|Brilho|Neon|Zen|Verificar resposta|Limpar seleção|Tentar novamente|Ver explicação|Próximo exemplo|Dica para a próxima jogada|Apagar número|Desfazer|Privacidade|Termos de uso|Sobre o desenvolvedor|Nesta página|Como funciona|Exemplo|Erros comuns|Outros guias|Praticar|Questão',
'''Jogue sudoku e aprenda a resolver.
Compare linhas, colunas e blocos para descobrir onde cada número entra. Veja a demonstração e tente um sudoku.
O que é sudoku?
Em uma grade 9×9, cada linha, coluna e bloco 3×3 deve conter os números de 1 a 9 uma única vez. Os números iniciais são suas pistas.
Um número pode revelar o próximo.
Se uma célula tem os candidatos 2 e 7 e um 2 aparece na mesma linha, ela só pode ser 7. Esse 7 também pode ajudar em outras células.
Encontre as técnicas que aprendeu.
Com a prática, você começa a reconhecer singles e pares. Uma jogada que antes precisava de uma dica pode ser encontrada por você.
O sudoku envolve comparar posições, organizar possibilidades e conferir o raciocínio. Pode ser uma forma divertida de passar um tempo pensando.
O que mostram as pesquisas?
Um estudo observacional de 2019 comparou a frequência declarada de jogos numéricos e testes cognitivos de 19.078 pessoas de 50 a 93 anos. Maior frequência esteve associada a melhores resultados em várias tarefas de atenção, raciocínio e memória.
O que o estudo não demonstra
Não demonstra que o sudoku causou essas diferenças, previne demência ou melhora capacidades do dia a dia. Pessoas que já têm facilidade podem jogar mais. O estudo não avaliou este aplicativo.
Escolha uma dificuldade agradável, use notas ou dicas e faça pausas. Experimente para descobrir se gosta de resolver, sem esperar um benefício de saúde garantido.
Divirta-se ainda mais no aplicativo!
Pratique técnicas específicas ou exercícios mistos e salve seu progresso. Você também pode escanear um sudoku em papel e ler dicas explicadas.
Experimente grátis. Alguns exercícios e dicas exigem Premium.
Resolva este sudoku fixo para iniciantes. Selecione uma célula e use os botões ou o teclado. Cada entrada é verificada na hora.
As setas mudam a célula; 1–9 inserem números; Delete ou Backspace apagam. O progresso não é salvo.
Dois exemplos permitem praticar uma técnica sem resolver a grade inteira.
Quatro estilos animam as entradas e os grupos completos. A demonstração não tem som.
Um sudoku fixo com candidatos e dicas lógicas, sem conta.
As notas são possibilidades, não números confirmados. Confira linha, coluna e bloco e atualize-as a cada confirmação.
Um único candidato só é confiável se nenhum tiver sido esquecido. Confira as notas antes de confirmar.
Verifique todas as células vazias do grupo. O número precisa ter uma única posição possível.
As duas células devem ter exatamente os mesmos dois candidatos. {2,7} e {2,7,9} não formam um par nu. Não apague os candidatos do próprio par.
Confira todas as posições do candidato. Pointing elimina fora do bloco; Claiming elimina em outras células dentro dele.''',
'''linha {row}, coluna {col}
célula vazia
número inicial
número inserido
candidatos {digits}
{reason} Em seguida, coloque {value}.
Coloque {value} em {cell}.
{reason} {value} colocado. ({count}/{total} células)
Todas as {total} células estão preenchidas. A reprodução automática recomeça após uma breve pausa.
De volta à grade inicial. As células serão preenchidas em ordem.
A reprodução automática está desligada. Use Reproduzir demo ou Uma jogada.
{cell} selecionada. Escolha um número.
Selecione primeiro uma célula vazia.
{value} em {cell} não corresponde à solução. Confira os outros candidatos.
{cell}: {value} colocado. Restam {count} células.
Correto! A grade está completa.
Selecione um número inserido para apagar.
O número em {cell} foi apagado.
Ainda não há entradas para desfazer.
Retornou à jogada anterior.
A grade inicial foi restaurada. Desfazer recupera a posição anterior.
Confira os candidatos de uma célula vazia.
A explicação está aberta. Use Tentar novamente para responder outra vez.
Escolha o número a colocar.
Escolha os candidatos a remover. Aperte novamente para desmarcar.
Selecionados: {count}
Resposta selecionada. Use Verificar resposta.
Selecionar ou desmarcar {value}
Nenhuma resposta selecionada. Escolha uma célula e um número.
Correto. A explicação abaixo mostra o motivo.
Essa não é a resposta desta técnica. Confira célula, número e remoções em falta ou em excesso.
Explicação exibida. Use Tentar novamente para repetir a questão.
Procure uma célula com apenas um candidato.
Procure duas células com os mesmos dois candidatos e selecione o que pode ser removido das outras.
Todas as seleções foram apagadas.
{cell} tem apenas o candidato {value}, então esse número pode ser colocado ali.
Resposta: coloque {value} em {cell}.
{cells} só têm {digits}. Esses números ocupam o par e podem ser removidos das outras células de {unit}.
Remover: {eliminations}. A ordem dos dois números no par ainda não é conhecida.
{value} em {cell}
As células contornadas mostram o motivo. Os candidatos riscados podem ser removidos.
Não foi possível carregar o exercício. Recarregue a página.
Por que esta jogada funciona
Grade de teste, 9 linhas e 9 colunas
Grade de prática, 9 linhas e 9 colunas
Números de resposta
Conte as linhas de cima para baixo e as colunas da esquerda para a direita. Selecione uma célula e use os botões ou o teclado.''')
add('nl',
'Sudoku-uitleg|Technieken leren|Eén sudoku spelen|Over de app|Taal kiezen|Naar de inhoud|Het plezier van sudoku|Sudoku en hersentraining|Zo vul je de cijfers in|Demo afspelen|Pauze|Eén stap|Opnieuw beginnen|Effecten|Snelheid|Langzaam|Normaal|Snel|Effecten tonen|Kandidaten tonen|Standaard|Schittering|Neon|Zen|Antwoord controleren|Selectie wissen|Opnieuw proberen|Uitleg tonen|Volgend voorbeeld|Hint voor de volgende zet|Cijfer wissen|Ongedaan maken|Privacy|Gebruiksvoorwaarden|Over de ontwikkelaar|Op deze pagina|Zo werkt het|Voorbeeld|Veelgemaakte fouten|Andere uitleg|Oefenen|Vraag',
'''Speel sudoku en leer hoe je de puzzel oplost.
Vergelijk rijen, kolommen en blokken om de juiste plek te vinden. Bekijk de demo en probeer zelf een sudoku.
Wat is sudoku?
Een rooster van 9×9 vakjes moet in elke rij, kolom en elk blok van 3×3 de cijfers 1–9 precies één keer bevatten. De gegeven cijfers zijn je aanwijzingen.
Eén cijfer kan het volgende mogelijk maken.
Heeft een vakje de kandidaten 2 en 7 en komt er een 2 in dezelfde rij, dan blijft 7 over. Die 7 kan ook andere vakjes verduidelijken.
Herken technieken die je hebt geleerd.
Door te oefenen ga je singles en paren zelf herkennen. Een zet waarvoor je eerst een hint nodig had, vind je later misschien zelf.
Sudoku vraagt om posities vergelijken, mogelijkheden ordenen en redeneringen controleren. Dat kan een prettige manier zijn om even na te denken.
Wat blijkt uit onderzoek?
Een observationeel onderzoek uit 2019 vergeleek zelfgerapporteerde cijferpuzzelfrequentie met cognitieve tests bij 19.078 mensen van 50–93 jaar. Vaker puzzelen hing samen met betere prestaties op verschillende aandachts-, redeneer- en geheugentaken.
Wat dit niet bewijst
Het bewijst niet dat sudoku deze verschillen veroorzaakt, dementie voorkomt of het dagelijks denken verbetert. Mensen die al vaardig zijn, puzzelen mogelijk vaker. Deze app is niet onderzocht.
Kies een leuk niveau, gebruik notities of hints en neem pauzes. Probeer of je plezier hebt in het oplossen, zonder een gegarandeerd gezondheidseffect te verwachten.
Beleef nog meer sudokuplezier in de app!
Oefen losse technieken of gemengde opgaven en bewaar je voortgang. Je kunt ook een papieren puzzel scannen en uitgelegde hints lezen.
Gratis proberen. Sommige oefeningen en hints vereisen Premium.
Los deze vaste beginnerspuzzel helemaal op. Kies een vakje en voer een cijfer in met de knoppen of het toetsenbord. Elke invoer wordt direct gecontroleerd.
Pijltjestoetsen verplaatsen de selectie, 1–9 voeren cijfers in en Delete of Backspace wist ze. Voortgang wordt niet opgeslagen.
Met twee voorbeelden oefen je één techniek zonder een hele puzzel op te lossen.
Vier effectstijlen begeleiden invoer en voltooide groepen. De demo heeft geen geluid.
Eén vaste puzzel met kandidaten en logische hints, zonder account.
Notities zijn mogelijkheden, geen vaststaande cijfers. Controleer rij, kolom en blok en werk ze na elke plaatsing bij.
Eén kandidaat is alleen betrouwbaar als je er geen hebt vergeten. Controleer de notities voor je bevestigt.
Bekijk alle lege vakjes in de groep. Het cijfer mag daar maar één mogelijke plek hebben.
Beide vakjes moeten precies dezelfde twee kandidaten hebben. {2,7} en {2,7,9} vormen geen naakt paar. Wis niet de kandidaten van het paar zelf.
Controleer alle posities van de kandidaat. Pointing schrapt buiten het blok; Claiming op andere plekken binnen het blok.''',
'''rij {row}, kolom {col}
leeg vakje
gegeven cijfer
ingevuld cijfer
kandidaten {digits}
{reason} Vul vervolgens {value} in.
Vul {value} in op {cell}.
{reason} {value} ingevuld. ({count}/{total} vakjes)
Alle {total} vakjes zijn gevuld. De automatische demo begint na een korte pauze opnieuw.
Terug bij het beginrooster. De lege vakjes worden achtereenvolgens ingevuld.
Automatisch afspelen staat uit. Gebruik Demo afspelen of Eén stap.
{cell} geselecteerd. Kies een cijfer.
Kies eerst een leeg vakje.
{value} op {cell} klopt niet met de oplossing. Bekijk de andere kandidaten.
{cell}: {value} ingevuld. Nog {count} vakjes.
Goed! De hele puzzel is opgelost.
Selecteer een ingevuld cijfer om te wissen.
Het cijfer op {cell} is gewist.
Er is nog geen invoer om terug te draaien.
Terug naar de vorige zet.
De beginpuzzel is hersteld. Ongedaan maken brengt je vorige stand terug.
Bekijk de kandidaten van een leeg vakje.
De uitleg staat open. Kies Opnieuw proberen om nogmaals te antwoorden.
Kies het cijfer om in te vullen.
Kies kandidaten om te schrappen. Nogmaals drukken heft de selectie op.
Geselecteerd: {count}
Antwoord geselecteerd. Kies Antwoord controleren.
{value} selecteren of deselecteren
Nog geen antwoord gekozen. Kies een vakje en daarna een cijfer.
Goed. De uitleg hieronder laat zien waarom.
Dit is niet het antwoord voor deze techniek. Controleer vakje, cijfer en ontbrekende of extra schrappingen.
Uitleg getoond. Kies Opnieuw proberen voor dezelfde vraag.
Zoek een vakje met maar één kandidaat.
Zoek twee vakjes met dezelfde twee kandidaten en selecteer wat elders kan worden geschrapt.
Alle antwoordselecties zijn gewist.
{cell} heeft alleen kandidaat {value}, dus dat cijfer kan daar staan.
Antwoord: vul {value} in op {cell}.
{cells} hebben alleen {digits}. Die cijfers bezetten het paar en kunnen uit andere vakjes van {unit} worden geschrapt.
Schrap: {eliminations}. De volgorde van de twee cijfers in het paar is nog onbekend.
{value} op {cell}
Omlijnde vakjes tonen de reden. Doorgestreepte kandidaten kunnen weg.
De oefening kon niet laden. Vernieuw de pagina.
Waarom deze zet werkt
Proefrooster met 9 rijen en 9 kolommen
Oefenrooster met 9 rijen en 9 kolommen
Antwoordcijfers
Rijen tellen van boven naar beneden, kolommen van links naar rechts. Kies een vakje en gebruik de knoppen of het toetsenbord.''')
add('da',
'Sudoku-guide|Lær teknikker|Spil en sudoku|Om appen|Vælg sprog|Gå til indhold|Glæden ved sudoku|Sudoku og hjernetræning|Sådan udfylder du tallene|Afspil demo|Pause|Ét træk|Start forfra|Effekter|Hastighed|Langsom|Normal|Hurtig|Vis effekter|Vis kandidater|Standard|Glimt|Neon|Zen|Tjek svar|Ryd valg|Prøv igen|Vis forklaring|Næste eksempel|Hint til næste træk|Slet tal|Fortryd|Privatlivspolitik|Brugsvilkår|Om udvikleren|På denne side|Sådan virker det|Eksempel|Typiske fejl|Andre guider|Øv dig|Opgave',
'''Spil sudoku, og lær at løse det.
Sammenlign rækker, kolonner og blokke for at finde tallenes plads. Se demoen, og prøv en sudoku selv.
Hvad er sudoku?
Et 9×9-felt skal have tallene 1–9 præcis én gang i hver række, kolonne og 3×3-blok. De givne tal er dine ledetråde.
Ét tal kan åbne for det næste.
Har et felt kandidaterne 2 og 7, og sættes 2 et andet sted i rækken, må feltet være 7. Det kan hjælpe videre i andre felter.
Genkend de teknikker, du har lært.
Med øvelse opdager du selv singler og par. Et træk, der før krævede et hint, kan du senere finde på egen hånd.
Sudoku får dig til at sammenligne placeringer, holde styr på muligheder og kontrollere din logik. Det kan være en hyggelig måde at bruge tankerne på.
Hvad viser forskningen?
Et observationsstudie fra 2019 sammenlignede selvrapporteret brug af talopgaver og kognitive tests hos 19.078 personer på 50–93 år. Hyppigere brug hang sammen med bedre resultater i flere opmærksomheds-, ræsonnements- og hukommelsesopgaver.
Hvad studiet ikke viser
Det beviser ikke, at sudoku skabte forskellene, forebygger demens eller forbedrer evner i hverdagen. Personer, som allerede klarer sig godt, spiller måske oftere. Appen blev ikke undersøgt.
Vælg et niveau, du kan lide, brug noter eller hints, og hold pauser. Prøv, om du nyder at løse opgaven, uden at forvente en garanteret sundhedseffekt.
Få endnu mere glæde af sudoku i appen!
Øv bestemte teknikker eller blandede opgaver, og gem dine fremskridt. Du kan også scanne en papiropgave og læse hints med forklaringer.
Prøv gratis. Nogle øvelser og hints kræver Premium.
Løs denne faste begynderopgave helt. Vælg et felt, og brug talknapperne eller tastaturet. Hver indtastning kontrolleres straks.
Piletaster skifter felt, 1–9 indtaster tal, og Delete eller Backspace sletter. Fremskridt gemmes ikke.
To eksempler lader dig øve én teknik uden at løse en hel sudoku.
Fire effektstile viser indtastninger og færdige grupper. Demoen er uden lyd.
Én fast opgave med kandidater og logiske hints, uden konto.
Noter er muligheder, ikke sikre tal. Tjek række, kolonne og blok, og opdater efter hvert bekræftet tal.
Én kandidat er kun sikker, hvis ingen er glemt. Tjek noterne, før du bekræfter.
Undersøg alle tomme felter i gruppen. Tallet må kun have én mulig placering.
Begge felter skal have præcis de samme to kandidater. {2,7} og {2,7,9} er ikke et nøgent par. Slet ikke parrets egne kandidater.
Tjek alle kandidatens placeringer. Pointing fjerner uden for blokken; Claiming andre steder inden for blokken.''',
'''række {row}, kolonne {col}
tomt felt
givet tal
indtastet tal
kandidater {digits}
{reason} Sæt derefter {value}.
Sæt {value} i {cell}.
{reason} {value} sat. ({count}/{total} felter)
Alle {total} felter er udfyldt. Automatisk afspilning starter forfra efter en kort pause.
Tilbage ved startfeltet. De tomme felter udfyldes ét ad gangen.
Automatisk afspilning er slået fra. Brug Afspil demo eller Ét træk.
{cell} er valgt. Vælg et tal.
Vælg først et tomt felt.
{value} i {cell} stemmer ikke med løsningen. Tjek de andre kandidater.
{cell}: {value} sat. {count} felter tilbage.
Korrekt! Hele opgaven er løst.
Vælg et indtastet tal, der skal slettes.
Tallet i {cell} er slettet.
Der er endnu ingen indtastning at fortryde.
Tilbage til det forrige træk.
Startopgaven er gendannet. Fortryd gendanner din forrige stilling.
Tjek kandidaterne i et tomt felt.
Forklaringen er åben. Vælg Prøv igen for at svare igen.
Vælg tallet, der skal sættes.
Vælg kandidater, der skal fjernes. Tryk igen for at fravælge.
Valgt: {count}
Svar valgt. Tryk på Tjek svar.
Vælg eller fravælg {value}
Intet svar valgt. Vælg et felt og derefter et tal.
Korrekt. Forklaringen nedenfor viser hvorfor.
Det er ikke svaret for denne teknik. Tjek felt, tal og manglende eller ekstra fjernelser.
Forklaring vist. Vælg Prøv igen for samme opgave.
Find et felt med kun én kandidat.
Find to felter med de samme to kandidater, og vælg det, der kan fjernes andre steder.
Alle svarvalg er ryddet.
{cell} har kun kandidaten {value}, så tallet kan sættes dér.
Svar: sæt {value} i {cell}.
{cells} har kun {digits}. Tallene optager parret og kan fjernes fra andre felter i {unit}.
Fjern: {eliminations}. Rækkefølgen af parrets tal er stadig ukendt.
{value} i {cell}
Indrammede felter viser begrundelsen. Overstregede kandidater kan fjernes.
Øvelsen kunne ikke indlæses. Genindlæs siden.
Hvorfor dette træk virker
Prøvefelt med 9 rækker og 9 kolonner
Øvefelt med 9 rækker og 9 kolonner
Svartal
Rækker tælles oppefra og kolonner fra venstre. Vælg et felt, og brug knapperne eller tastaturet.''')
add('sv',
'Sudokuguide|Lär dig tekniker|Spela ett sudoku|Om appen|Välj språk|Till innehållet|Det roliga med sudoku|Sudoku och hjärnträning|Så här fyller du i siffrorna|Spela demo|Paus|Ett steg|Börja om|Effekter|Hastighet|Långsam|Normal|Snabb|Visa effekter|Visa kandidater|Standard|Glitter|Neon|Zen|Kontrollera svar|Rensa val|Försök igen|Visa förklaring|Nästa exempel|Ledtråd till nästa drag|Radera siffra|Ångra|Integritetspolicy|Användarvillkor|Om utvecklaren|På den här sidan|Så fungerar det|Exempel|Vanliga misstag|Fler guider|Öva|Uppgift',
'''Spela sudoku och lär dig lösa det.
Jämför rader, kolumner och block för att hitta rätt plats för siffrorna. Se demonstrationen och prova ett sudoku själv.
Vad är sudoku?
I ett rutnät på 9×9 ska varje rad, kolumn och 3×3-block innehålla 1–9 exakt en gång. De givna siffrorna är dina ledtrådar.
En siffra kan leda till nästa.
Har en ruta kandidaterna 2 och 7 och en 2:a placeras på samma rad återstår 7. Den kan i sin tur hjälpa dig med andra rutor.
Känn igen tekniker du har lärt dig.
Med övning börjar du se singlar och par själv. Ett drag som tidigare behövde en ledtråd kan du så småningom hitta på egen hand.
Sudoku innebär att jämföra lägen, ordna möjligheter och kontrollera resonemang. Det kan vara ett roligt sätt att ägna en stund åt att tänka.
Vad visar forskningen?
En observationsstudie från 2019 jämförde självrapporterad användning av sifferpussel och kognitiva tester hos 19 078 personer i åldern 50–93 år. Oftare pusslande hade samband med bättre resultat på flera uppgifter om uppmärksamhet, resonemang och minne.
Vad studien inte bevisar
Det bevisar inte att sudoku orsakade skillnaderna, förebygger demens eller förbättrar vardagsförmågor. De som redan är bra på uppgifterna kanske spelar oftare. Appen undersöktes inte.
Välj en lagom svår nivå, använd anteckningar eller ledtrådar och ta pauser. Prova om du tycker om själva lösandet, utan att vänta dig en garanterad hälsoeffekt.
Ha ännu roligare med sudoku i appen!
Öva särskilda tekniker eller blandade uppgifter och spara dina framsteg. Du kan också skanna ett papperssudoku och läsa förklarande ledtrådar.
Prova gratis. Vissa övningar och ledtrådar kräver Premium.
Lös detta fasta nybörjarsudoku. Välj en ruta och ange siffran med knapparna eller tangentbordet. Varje inmatning kontrolleras direkt.
Piltangenter flyttar mellan rutor, 1–9 matar in siffror och Delete eller Backsteg raderar. Framsteg sparas inte.
Två exempel låter dig öva en teknik utan att lösa ett helt sudoku.
Fyra effektstilar visar inmatningar och färdiga grupper. Demonstrationen är ljudlös.
Ett fast sudoku med kandidater och logiska ledtrådar, utan konto.
Anteckningar är möjligheter, inte bekräftade siffror. Kontrollera rad, kolumn och block och uppdatera efter varje placering.
En ensam kandidat är bara säker om ingen har glömts bort. Kontrollera anteckningarna före bekräftelsen.
Kontrollera alla tomma rutor i gruppen. Siffran måste ha exakt en möjlig plats.
Båda rutorna måste ha exakt samma två kandidater. {2,7} och {2,7,9} är inte ett naket par. Radera inte parets egna kandidater.
Kontrollera alla kandidatpositioner. Pointing tar bort utanför blocket; Claiming på andra platser inuti blocket.''',
'''rad {row}, kolumn {col}
tom ruta
given siffra
inmatad siffra
kandidater {digits}
{reason} Placera sedan {value}.
Placera {value} i {cell}.
{reason} {value} placerad. ({count}/{total} rutor)
Alla {total} rutor är fyllda. Automatisk uppspelning börjar om efter en kort paus.
Tillbaka vid startrutnätet. De tomma rutorna fylls i tur och ordning.
Automatisk uppspelning är av. Använd Spela demo eller Ett steg.
{cell} är vald. Välj en siffra.
Välj först en tom ruta.
{value} i {cell} stämmer inte med lösningen. Kontrollera övriga kandidater.
{cell}: {value} placerad. {count} rutor återstår.
Rätt! Hela sudokut är klart.
Välj en inmatad siffra att radera.
Siffran i {cell} har raderats.
Det finns ännu ingen inmatning att ångra.
Återgick till föregående drag.
Startpusslet har återställts. Ångra tar dig tillbaka till föregående läge.
Kontrollera kandidaterna i en tom ruta.
Förklaringen är öppen. Välj Försök igen för att svara en gång till.
Välj siffran som ska placeras.
Välj kandidater att ta bort. Tryck igen för att avmarkera.
Valda: {count}
Svar valt. Tryck på Kontrollera svar.
Välj eller avmarkera {value}
Inget svar valt. Välj en ruta och sedan en siffra.
Rätt. Förklaringen nedan visar varför.
Det är inte svaret för den här tekniken. Kontrollera ruta, siffra samt saknade eller extra borttagningar.
Förklaring visad. Välj Försök igen för samma uppgift.
Hitta en ruta med bara en kandidat.
Hitta två rutor med samma två kandidater och välj vad som kan tas bort på andra ställen.
Alla svarsalternativ har rensats.
{cell} har bara kandidaten {value}, så den siffran kan placeras där.
Svar: placera {value} i {cell}.
{cells} har bara {digits}. Dessa siffror upptar paret och kan tas bort från andra rutor i {unit}.
Ta bort: {eliminations}. Ordningen på parets två siffror är fortfarande okänd.
{value} i {cell}
Inramade rutor visar orsaken. Överstrukna kandidater kan tas bort.
Övningen kunde inte laddas. Ladda om sidan.
Varför draget fungerar
Provrutnät med 9 rader och 9 kolumner
Övningsrutnät med 9 rader och 9 kolumner
Svarssiffror
Rader räknas uppifrån och kolumner från vänster. Välj en ruta och använd knapparna eller tangentbordet.''')
add('ko',
'스도쿠 가이드|풀이 기법 배우기|한 문제 풀기|앱 소개|언어 선택|본문으로 이동|스도쿠의 재미|스도쿠와 두뇌 활동|이렇게 숫자를 채워 보세요|데모 재생|일시 정지|한 수 진행|처음부터|효과|속도|느리게|보통|빠르게|효과 표시|후보 표시|기본|반짝임|네온|젠|답 확인|선택 지우기|다시 풀기|해설 보기|다음 예제|다음 수 힌트|숫자 지우기|되돌리기|개인정보 처리방침|이용약관|개발자 소개|이 페이지의 내용|원리|예제|자주 하는 실수|다른 해설|연습|문제',
'''스도쿠를 즐기며 풀이 방법을 배워 보세요.
행·열·블록을 비교해 숫자가 들어갈 자리를 찾습니다. 자동 풀이를 살펴본 뒤 직접 한 문제 풀어 보세요.
스도쿠는 어떤 퍼즐인가요?
9×9 칸에 1~9를 채우는 퍼즐입니다. 각 행·열·3×3 블록에 같은 숫자가 중복되지 않아야 합니다. 처음 주어진 숫자가 단서입니다.
숫자 하나가 다음 단서가 됩니다.
후보가 2와 7인 칸과 같은 행에 2가 들어가면 그 칸은 7로 정해집니다. 이 7이 다른 칸의 후보를 줄일 수도 있습니다.
배운 기법을 직접 찾아보세요.
연습하면 싱글이나 페어가 눈에 들어오기 시작합니다. 예전에는 힌트가 필요했던 수를 스스로 찾는 재미가 있습니다.
스도쿠에서는 위치를 비교하고 가능성을 정리하며 추론을 확인합니다. 생각하는 시간을 즐길 수 있는 놀이입니다.
연구에서는 무엇을 알아냈나요?
2019년 관찰 연구는 50~93세 19,078명의 숫자 퍼즐 이용 빈도 자기보고와 인지 과제 성적을 비교했습니다. 자주 푸는 것과 주의·추론·기억 과제의 높은 성적 사이에 관련성이 보고됐습니다.
이 연구로 단정할 수 없는 점
스도쿠 때문에 성적이 좋아졌거나 치매를 예방하고 일상 능력이 향상된다고 입증한 연구는 아닙니다. 원래 과제에 능숙한 사람이 더 자주 즐길 수도 있습니다. 이 앱의 효과를 조사한 것도 아닙니다.
재미를 느끼는 난이도를 고르고 메모와 힌트를 이용하며 쉬어 가세요. 건강 효과를 기대하기보다 푸는 과정이 즐거운지 체험해 보세요.
앱에서 스도쿠를 더 즐겨 보세요!
기법별 연습과 혼합 연습을 하고 진행 상황을 저장할 수 있습니다. 종이 문제를 카메라로 읽어 풀이 이유를 알려 주는 힌트도 확인할 수 있습니다.
무료로 체험할 수 있습니다. 일부 연습과 힌트는 프리미엄 기능입니다.
초보자용 고정 문제 한 개를 끝까지 풀 수 있습니다. 칸을 고른 뒤 숫자 버튼이나 키보드로 입력하세요. 입력 즉시 정답을 확인합니다.
방향키로 이동하고 1~9로 입력합니다. Delete나 Backspace로 지울 수 있습니다. 진행 상황은 저장되지 않습니다.
전체 문제를 처음부터 풀지 않고 두 예제로 한 가지 기법만 연습합니다.
숫자 입력과 행·열·블록 완성 효과를 네 가지 스타일로 고를 수 있습니다. 데모에는 소리가 없습니다.
가입 없이 후보 표시와 논리 힌트를 이용해 고정 문제 한 개를 풉니다.
후보 메모는 가능성이며 확정 숫자가 아닙니다. 행·열·블록을 확인하고 숫자가 정해질 때마다 갱신하세요.
후보를 빠뜨리지 않았을 때만 하나 남은 후보를 확정할 수 있습니다. 먼저 메모를 확인하세요.
선택한 행·열·블록의 빈칸을 모두 확인하세요. 그 숫자가 들어갈 곳이 한 칸뿐이어야 합니다.
두 칸에 정확히 같은 두 후보만 있어야 합니다. {2,7}과 {2,7,9}는 네이키드 페어가 아닙니다. 페어 자체의 후보를 지우지 마세요.
그 숫자의 후보 위치를 모두 확인하세요. Pointing은 블록 밖에서, Claiming은 같은 블록의 다른 칸에서 후보를 지웁니다.''',
'''{row}행 {col}열
빈칸
주어진 숫자
입력한 숫자
후보 {digits}
{reason} 다음으로 {value}를 입력합니다.
{cell}에 {value}를 입력합니다.
{reason} {value}를 입력했습니다. ({count}/{total}칸)
{total}칸을 모두 채웠습니다. 자동 재생 중에는 잠시 후 처음부터 반복합니다.
처음 판으로 돌아왔습니다. 빈칸을 차례대로 채웁니다.
자동 재생이 꺼져 있습니다. 데모 재생이나 한 수 진행을 누르세요.
{cell}을 선택했습니다. 숫자를 고르세요.
먼저 빈칸을 선택하세요.
{cell}의 {value}는 정답과 다릅니다. 다른 후보를 살펴보세요.
{cell}에 {value}를 입력했습니다. {count}칸 남았습니다.
정답입니다! 모든 칸을 채웠습니다.
지울 숫자를 입력한 칸을 고르세요.
{cell}의 숫자를 지웠습니다.
아직 되돌릴 입력이 없습니다.
한 수 전으로 돌아갔습니다.
처음 문제로 돌아왔습니다. 되돌리기를 누르면 이전 상태를 복원합니다.
빈칸의 후보를 확인하세요.
해설을 보고 있습니다. 다시 풀기를 누르면 재도전할 수 있습니다.
입력할 숫자를 하나 고르세요.
지울 후보를 고르세요. 다시 누르면 선택이 취소됩니다.
선택: {count}개
답을 골랐습니다. 답 확인을 누르세요.
{value} 선택 또는 해제
답을 고르지 않았습니다. 칸을 선택한 뒤 숫자를 고르세요.
정답입니다. 아래 해설에서 이유를 확인하세요.
이 기법의 답과 다릅니다. 칸·숫자와 후보를 빠뜨리거나 더 고르지 않았는지 확인하세요.
해설을 표시했습니다. 다시 풀기로 같은 문제에 도전할 수 있습니다.
후보가 하나뿐인 칸을 찾으세요.
같은 두 후보만 있는 두 칸을 찾고 다른 칸에서 지울 후보를 고르세요.
선택한 답을 모두 지웠습니다.
{cell}의 후보는 {value}뿐이므로 이 숫자를 넣을 수 있습니다.
답: {cell}에 {value}를 넣습니다.
{cells}에는 {digits}만 있습니다. 이 숫자들이 두 칸을 차지하므로 {unit}의 다른 칸에서 지울 수 있습니다.
지울 후보: {eliminations}. 페어에서 어느 칸에 어느 숫자가 들어갈지는 아직 모릅니다.
{cell}의 {value}
테두리로 표시한 칸이 근거입니다. 취소선을 그은 후보는 지울 수 있습니다.
연습 문제를 불러오지 못했습니다. 페이지를 새로고침하세요.
이 수를 둘 수 있는 이유
체험용 스도쿠 판, 9행 9열
연습용 스도쿠 판, 9행 9열
답으로 고를 숫자
행은 위에서 아래로, 열은 왼쪽에서 오른쪽으로 셉니다. 칸을 선택하고 숫자 버튼이나 키보드를 사용하세요.''')
add('zh_CN',
'数独指南|学习解题技巧|玩一道数独|应用介绍|选择语言|跳到正文|数独的乐趣|数独与脑力活动|像这样逐步填入数字|播放演示|暂停|前进一步|重新开始|特效|速度|慢速|正常|快速|显示特效|显示候选数|标准|闪光|霓虹|禅意|检查答案|清除选择|重试|查看讲解|下一个例题|下一步提示|擦除数字|撤销|隐私政策|使用条款|开发者介绍|本页内容|解题原理|示例|常见错误|其他讲解|练习|题目',
'''边玩数独，边学习解题方法。
对照行、列和宫，找出数字能放在哪里。先看看自动解题演示，再自己试一道题。
数独是什么？
数独是在9×9的格子中填入1~9的游戏。每一行、每一列和每个3×3宫内，同一个数字都只能出现一次。题目给出的数字就是线索。
填入一个数字，可能带来下一个线索。
一个格子的候选数是2和7，如果同一行的其他位置填入2，这个格子就只能是7。这个7也可能帮助缩小其他格子的候选范围。
自己发现学过的技巧。
练习后，你会更容易发现单数和数对。以前需要提示的一步，也能逐渐自己找出来。
解数独时，需要比较位置、整理可能性并检查推理。它可以是一种享受思考过程的游戏。
研究发现了什么？
2019年的一项观察性研究比较了19,078名50~93岁参与者自报的数字谜题使用频率与认知任务成绩。更常玩谜题与多项注意、推理和记忆任务的较好成绩有关。
研究不能证明什么？
这不能证明是数独导致成绩提高，也不能证明能预防痴呆或改善日常能力。原本擅长这些任务的人也可能更爱玩谜题。研究并未评估本应用。
选择自己觉得有趣的难度，适当使用笔记和提示，也可以休息。先体验解题过程是否有趣，不必追求有保证的健康效果。
在应用里玩得更开心！
可按技巧练习、进行混合练习并保存进度。也可以用相机扫描纸上题目，查看解释解题理由的提示。
可以免费体验。部分练习和提示需要高级版。
这道固定的入门题可以一直解到完成。选中格子后，用数字按钮或键盘输入，系统会立即检查正误。
方向键移动，1~9输入数字，Delete或Backspace擦除。不会保存中途进度。
通过两道例题，只练习一种技巧，不必从头解完整道题。
填入数字和完成行列宫时的特效可选择四种风格。演示没有声音。
无需注册，即可体验带候选数和逻辑提示的一道固定题目。
候选笔记表示可能性，不是已经确定的数字。请检查行、列和宫，并在每次确定数字后更新。
只有在没有漏写其他候选数时，唯一候选才可靠。确定前请检查笔记。
检查所选行、列或宫中的全部空格。该数字必须只剩一个可放的位置。
两个格子必须恰好只有相同的两个候选数。{2,7}和{2,7,9}不构成裸数对。不要删除数对本身的候选数。
检查该数字的全部候选位置。Pointing删除宫外的候选数；Claiming删除同一宫内其他位置的候选数。''',
'''第{row}行第{col}列
空格
题目数字
已填数字
候选数{digits}
{reason}接下来填入{value}。
在{cell}填入{value}。
{reason}已填入{value}。（{count}/{total}格）
{total}格已全部填好。自动播放时，稍后会从头重复。
已返回初始盘面，将依次填入空格。
自动播放已关闭。可点击播放演示或前进一步。
已选择{cell}，请选择数字。
请先选择一个空格。
{cell}的{value}与答案不符，请检查其他候选数。
已在{cell}填入{value}，还剩{count}格。
正确！所有格子都填好了。
请选择要擦除的已填数字。
已擦除{cell}的数字。
还没有可撤销的输入。
已返回上一步。
已恢复初始题目，点击撤销可回到之前的状态。
请检查空格中的候选数。
正在显示讲解，点击重试可再次作答。
请选择要填入的数字。
请选择可删除的候选数，再次点击可取消选择。
已选择：{count}个
已选择答案，请点击检查答案。
选择或取消{value}
尚未选择答案，请先选择格子，再选择数字。
正确，可在下方讲解中查看原因。
这不是该技巧的答案，请检查格子、数字及是否多选或漏选了候选数。
已显示讲解，点击重试可重新回答本题。
寻找只剩一个候选数的格子。
找出只有相同两个候选数的两个格子，再选择其他格子中可删除的候选数。
已清除所有答案选择。
{cell}只剩候选数{value}，因此可以填入这个数字。
答案：在{cell}填入{value}。
{cells}的候选数都只有{digits}，这两个数字会占据数对，因此可从{unit}的其他格子中删除。
可删除：{eliminations}。数对中的两个数字分别在哪个格子里仍未确定。
{cell}中的{value}
带边框的格子是依据，带删除线的候选数可以删除。
无法加载练习，请刷新页面重试。
这一步的依据
体验数独盘面，9行9列
练习数独盘面，9行9列
答案数字
行从上往下数，列从左往右数。请选择格子后使用数字按钮或键盘。''')
add('zh_TW',
'數獨指南|學習解題技巧|玩一道數獨|應用程式介紹|選擇語言|跳到正文|數獨的樂趣|數獨與腦力活動|像這樣逐步填入數字|播放示範|暫停|前進一步|重新開始|特效|速度|慢速|一般|快速|顯示特效|顯示候選數|標準|閃光|霓虹|禪意|檢查答案|清除選擇|重試|查看解說|下一個例題|下一步提示|擦除數字|復原|隱私權政策|使用條款|開發者介紹|本頁內容|解題原理|範例|常見錯誤|其他解說|練習|題目',
'''邊玩數獨，邊學習解題方法。
對照列、欄與宮，找出數字能放在哪裡。先看看自動解題示範，再自己試一道題。
數獨是什麼？
數獨是在9×9的格子中填入1～9的遊戲。每一橫列、每一直欄及每個3×3宮內，相同數字都只能出現一次。題目給出的數字就是線索。
填入一個數字，可能帶來下一個線索。
某個格子的候選數是2和7，若同一橫列的其他位置填入2，這格就只能是7。這個7也可能幫助縮小其他格子的候選範圍。
自己發現學過的技巧。
練習後，會更容易發現單數和數對。以前需要提示的一步，也能逐漸自己找出來。
解數獨時，需要比較位置、整理可能性並檢查推理。它可以是一種享受思考過程的遊戲。
研究發現了什麼？
2019年的一項觀察性研究，比較19,078名50～93歲參與者自述的數字謎題使用頻率與認知作業成績。較常玩謎題，與多項注意、推理及記憶作業的較好成績有關。
研究不能證明什麼？
這不能證明是數獨使成績進步，也不能證明能預防失智症或改善日常能力。原本擅長這些作業的人，也可能更常玩謎題。研究並未評估本應用程式。
選擇自己覺得有趣的難度，適時使用筆記和提示，也可以休息。先體驗是否喜歡解題過程，不必追求有保證的健康效果。
在應用程式裡玩得更開心！
可按技巧練習、進行混合練習並儲存進度。也能用相機掃描紙上題目，查看說明解題理由的提示。
可免費體驗。部分練習和提示需要進階版。
這道固定的入門題可以一路解到完成。選取格子後，用數字按鈕或鍵盤輸入，系統會立即檢查正誤。
方向鍵移動，1～9輸入數字，Delete或Backspace擦除。不會儲存中途進度。
透過兩道例題，只練習一種技巧，不必從頭解完整道題。
填入數字及完成列、欄或宮時的特效，可選擇四種風格。示範沒有聲音。
不必註冊，即可體驗附候選數和邏輯提示的一道固定題目。
候選筆記表示可能性，不是已確定的數字。請檢查列、欄與宮，並在每次確定數字後更新。
只有在未漏寫其他候選數時，唯一候選才可靠。確定前請檢查筆記。
檢查所選列、欄或宮中的所有空格。該數字必須只剩一個可放的位置。
兩個格子必須恰好只有相同的兩個候選數。{2,7}和{2,7,9}不構成裸數對。不要刪除數對本身的候選數。
檢查該數字的所有候選位置。Pointing刪除宮外的候選數；Claiming刪除同一宮內其他位置的候選數。''',
'''第{row}列第{col}欄
空格
題目數字
已填數字
候選數{digits}
{reason}接著填入{value}。
在{cell}填入{value}。
{reason}已填入{value}。（{count}/{total}格）
{total}格已全部填好。自動播放時，稍後會從頭重複。
已回到初始盤面，將依序填入空格。
自動播放已關閉。可按播放示範或前進一步。
已選取{cell}，請選擇數字。
請先選取一個空格。
{cell}的{value}與答案不符，請檢查其他候選數。
已在{cell}填入{value}，還剩{count}格。
正確！所有格子都填好了。
請選取要擦除的已填數字。
已擦除{cell}的數字。
還沒有可復原的輸入。
已回到上一步。
已還原初始題目，按復原可回到先前狀態。
請檢查空格中的候選數。
正在顯示解說，按重試可再次作答。
請選擇要填入的數字。
請選擇可刪除的候選數，再按一次可取消選取。
已選取：{count}個
已選擇答案，請按檢查答案。
選取或取消{value}
尚未選擇答案，請先選取格子，再選擇數字。
正確，可在下方解說查看原因。
這不是該技巧的答案，請檢查格子、數字及是否多選或漏選候選數。
已顯示解說，按重試可重新回答本題。
尋找只剩一個候選數的格子。
找出只有相同兩個候選數的兩個格子，再選擇其他格子中可刪除的候選數。
已清除所有答案選擇。
{cell}只剩候選數{value}，因此可以填入這個數字。
答案：在{cell}填入{value}。
{cells}的候選數都只有{digits}，這兩個數字會佔據數對，因此可從{unit}的其他格子中刪除。
可刪除：{eliminations}。數對中的兩個數字分別在哪個格子仍未確定。
{cell}中的{value}
加框格子是依據，加刪除線的候選數可以刪除。
無法載入練習，請重新整理頁面。
這一步的依據
體驗數獨盤面，9列9欄
練習數獨盤面，9列9欄
答案數字
列由上往下數，欄由左往右數。請選取格子，再用數字按鈕或鍵盤操作。''')
add('pl',
'Poradnik sudoku|Poznaj techniki|Rozwiąż jedno sudoku|O aplikacji|Wybierz język|Przejdź do treści|Przyjemność z sudoku|Sudoku i trening umysłu|Tak możesz wypełniać pola|Odtwórz demo|Pauza|Jeden ruch|Od początku|Efekty|Szybkość|Wolno|Normalnie|Szybko|Pokaż efekty|Pokaż kandydatów|Standardowy|Iskry|Neon|Zen|Sprawdź odpowiedź|Wyczyść wybór|Spróbuj ponownie|Pokaż wyjaśnienie|Następny przykład|Wskazówka do następnego ruchu|Usuń cyfrę|Cofnij|Prywatność|Warunki korzystania|O twórcy|Na tej stronie|Jak to działa|Przykład|Częste błędy|Inne poradniki|Ćwiczenia|Zadanie',
'''Graj w sudoku i poznawaj sposoby rozwiązywania.
Porównuj wiersze, kolumny i bloki, aby znaleźć miejsce dla cyfry. Obejrzyj demo, a potem spróbuj samodzielnie.
Czym jest sudoku?
W siatce 9×9 każdy wiersz, kolumna i blok 3×3 musi zawierać cyfry 1–9 dokładnie raz. Wpisane na początku cyfry są wskazówkami.
Jedna cyfra może pomóc znaleźć kolejną.
Jeśli pole ma kandydatów 2 i 7, a w tym samym wierszu pojawi się 2, pozostaje 7. Ta siódemka może zawęzić możliwości w innych polach.
Rozpoznawaj poznane techniki.
Z czasem zaczniesz samodzielnie zauważać single i pary. Ruch, do którego dawniej była potrzebna wskazówka, możesz znaleźć sam.
Sudoku wymaga porównywania pozycji, porządkowania możliwości i sprawdzania rozumowania. Może być przyjemną okazją do myślenia.
Co pokazują badania?
Badanie obserwacyjne z 2019 r. porównało deklarowaną częstotliwość łamigłówek liczbowych i testy poznawcze 19 078 osób w wieku 50–93 lat. Częstsze rozwiązywanie wiązało się z lepszymi wynikami w części zadań uwagi, rozumowania i pamięci.
Czego badanie nie dowodzi?
Nie dowodzi, że to sudoku spowodowało różnice, zapobiega demencji lub poprawia codzienne zdolności. Osoby już sprawne mogą częściej wybierać łamigłówki. Nie badano tej aplikacji.
Wybierz przyjemny poziom trudności, korzystaj z notatek i wskazówek oraz rób przerwy. Sprawdź, czy lubisz samo rozwiązywanie, bez oczekiwania gwarantowanych korzyści zdrowotnych.
Baw się jeszcze lepiej w aplikacji!
Ćwicz pojedyncze techniki lub zadania mieszane i zapisuj postępy. Możesz też zeskanować sudoku z papieru i czytać objaśnione wskazówki.
Wypróbuj bezpłatnie. Część ćwiczeń i wskazówek wymaga Premium.
Rozwiąż to stałe zadanie dla początkujących. Wybierz pole i wpisz cyfrę przyciskiem lub klawiaturą. Każdy wpis jest od razu sprawdzany.
Strzałki zmieniają pole, 1–9 wpisują cyfry, Delete lub Backspace je usuwają. Postęp nie jest zapisywany.
Dwa przykłady pozwalają ćwiczyć jedną technikę bez rozwiązywania całej planszy.
Cztery style efektów towarzyszą wpisywaniu i ukończeniu grup. Demo nie ma dźwięku.
Jedno stałe zadanie z kandydatami i logicznymi wskazówkami, bez konta.
Notatki to możliwości, nie potwierdzone cyfry. Sprawdzaj wiersz, kolumnę i blok oraz aktualizuj je po każdym wpisie.
Jeden kandydat jest pewny tylko wtedy, gdy żadnego nie pominięto. Sprawdź notatki przed potwierdzeniem.
Sprawdź wszystkie puste pola wybranej grupy. Cyfra musi mieć dokładnie jedno możliwe miejsce.
Oba pola muszą mieć dokładnie tych samych dwóch kandydatów. {2,7} i {2,7,9} nie tworzą nagiej pary. Nie usuwaj kandydatów samej pary.
Sprawdź wszystkie pozycje kandydata. Pointing usuwa poza blokiem, a Claiming w innych polach tego bloku.''',
'''wiersz {row}, kolumna {col}
puste pole
cyfra początkowa
wpisana cyfra
kandydaci {digits}
{reason} Następnie wpisz {value}.
Wpisz {value} w {cell}.
{reason} Wpisano {value}. ({count}/{total} pól)
Wypełniono wszystkie pola: {total}. Automatyczne demo po chwili zacznie się od nowa.
Powrót do początkowej planszy. Puste pola będą kolejno wypełniane.
Autoodtwarzanie jest wyłączone. Wybierz Odtwórz demo lub Jeden ruch.
Wybrano {cell}. Wybierz cyfrę.
Najpierw wybierz puste pole.
{value} w {cell} nie pasuje do rozwiązania. Sprawdź innych kandydatów.
{cell}: wpisano {value}. Pozostałe pola: {count}.
Dobrze! Cała plansza jest rozwiązana.
Wybierz wpisaną cyfrę do usunięcia.
Usunięto cyfrę z {cell}.
Nie ma jeszcze wpisu do cofnięcia.
Powrót do poprzedniego ruchu.
Przywrócono początkowe zadanie. Cofnij przywraca poprzedni stan.
Sprawdź kandydatów pustego pola.
Wyjaśnienie jest otwarte. Spróbuj ponownie pozwala odpowiedzieć jeszcze raz.
Wybierz cyfrę do wpisania.
Wybierz kandydatów do usunięcia. Naciśnij ponownie, aby odznaczyć.
Wybrano: {count}
Wybrano odpowiedź. Naciśnij Sprawdź odpowiedź.
Zaznacz lub odznacz {value}
Nie wybrano odpowiedzi. Wybierz pole, a potem cyfrę.
Dobrze. Wyjaśnienie poniżej podaje powód.
To nie jest odpowiedź dla tej techniki. Sprawdź pole, cyfrę oraz brakujące lub nadmiarowe skreślenia.
Pokazano wyjaśnienie. Spróbuj ponownie, aby wrócić do tego zadania.
Znajdź pole z tylko jednym kandydatem.
Znajdź dwa pola z tymi samymi dwoma kandydatami i zaznacz, co można usunąć z innych pól.
Wyczyszczono wszystkie wybrane odpowiedzi.
{cell} ma tylko kandydata {value}, więc można tam wpisać tę cyfrę.
Odpowiedź: wpisz {value} w {cell}.
{cells} mają tylko {digits}. Te cyfry zajmują parę i można je usunąć z innych pól grupy {unit}.
Usuń: {eliminations}. Kolejność cyfr w parze jest nadal nieznana.
{value} w {cell}
Obramowane pola pokazują uzasadnienie. Przekreślonych kandydatów można usunąć.
Nie udało się wczytać ćwiczenia. Odśwież stronę.
Dlaczego ten ruch działa
Plansza próbna, 9 wierszy i 9 kolumn
Plansza ćwiczeniowa, 9 wierszy i 9 kolumn
Cyfry odpowiedzi
Wiersze liczymy od góry, kolumny od lewej. Wybierz pole i użyj przycisków lub klawiatury.''')
add('ru',
'Руководство по судоку|Изучить приёмы|Решить одно судоку|О приложении|Выбрать язык|К содержимому|Чем интересно судоку|Судоку и тренировка ума|Вот так можно заполнять клетки|Запустить демо|Пауза|Один ход|Сначала|Эффекты|Скорость|Медленно|Обычно|Быстро|Показывать эффекты|Показывать кандидатов|Стандарт|Искры|Неон|Дзен|Проверить ответ|Сбросить выбор|Попробовать снова|Показать объяснение|Следующий пример|Подсказка к следующему ходу|Стереть цифру|Отменить|Конфиденциальность|Условия использования|О разработчике|На этой странице|Как это работает|Пример|Частые ошибки|Другие объяснения|Практика|Задание',
'''Играйте в судоку и изучайте способы решения.
Сравнивайте строки, столбцы и блоки, чтобы найти место для цифры. Посмотрите демонстрацию и попробуйте решить задачу сами.
Что такое судоку?
В сетке 9×9 каждая строка, столбец и блок 3×3 должны содержать цифры 1–9 ровно по одному разу. Начальные цифры служат подсказками.
Одна цифра может подсказать следующую.
Если в клетке кандидаты 2 и 7, а в той же строке появилась 2, остаётся 7. Эта семёрка может помочь сузить выбор в других клетках.
Находите изученные приёмы самостоятельно.
С практикой вы начнёте замечать одиночки и пары. Ход, для которого раньше требовалась подсказка, получится найти самому.
Судоку требует сравнивать позиции, упорядочивать варианты и проверять рассуждения. Это может быть приятным способом провести время за размышлением.
Что показали исследования?
Наблюдательное исследование 2019 года сравнило заявленную частоту решения числовых головоломок и когнитивные тесты 19 078 человек в возрасте 50–93 лет. Более частое решение было связано с лучшими результатами ряда заданий на внимание, рассуждение и память.
Чего исследование не доказывает
Оно не доказывает, что различия вызваны судоку, что игра предотвращает деменцию или улучшает повседневные способности. Уже успешные в этих заданиях люди могут играть чаще. Это приложение не исследовалось.
Выбирайте интересную сложность, используйте заметки и подсказки, делайте перерывы. Попробуйте понять, нравится ли вам процесс решения, без ожидания гарантированной пользы для здоровья.
В приложении играть ещё интереснее!
Тренируйте отдельные приёмы или смешанные задания и сохраняйте прогресс. Можно также отсканировать бумажное судоку и читать подсказки с объяснениями.
Можно попробовать бесплатно. Часть упражнений и подсказок требует Premium.
Решите эту фиксированную задачу для начинающих. Выберите клетку и введите цифру кнопками или с клавиатуры. Каждый ввод проверяется сразу.
Стрелки перемещают между клетками, 1–9 вводят цифры, Delete и Backspace стирают. Промежуточный результат не сохраняется.
Два примера позволяют отработать один приём, не решая всю задачу с начала.
Четыре стиля эффектов сопровождают ввод и завершение групп. Демонстрация без звука.
Одна фиксированная задача с кандидатами и логическими подсказками, без регистрации.
Заметки обозначают варианты, а не подтверждённые цифры. Проверяйте строку, столбец и блок и обновляйте их после каждого хода.
Единственный кандидат надёжен, только если другие не пропущены. Перед подтверждением проверьте заметки.
Проверьте все пустые клетки выбранной группы. У цифры должно быть лишь одно возможное место.
Обе клетки должны иметь ровно двух одинаковых кандидатов. {2,7} и {2,7,9} не образуют голую пару. Не стирайте кандидатов самой пары.
Проверьте все позиции кандидата. Pointing удаляет вне блока, Claiming — в других клетках внутри него.''',
'''строка {row}, столбец {col}
пустая клетка
начальная цифра
введённая цифра
кандидаты {digits}
{reason} Затем ставим {value}.
Поставьте {value} в {cell}.
{reason} Поставлено {value}. ({count}/{total} клеток)
Все клетки заполнены: {total}. Автоматическое демо начнётся заново после короткой паузы.
Возврат к начальной сетке. Пустые клетки будут заполнены по порядку.
Автовоспроизведение выключено. Нажмите «Запустить демо» или «Один ход».
Выбрано: {cell}. Выберите цифру.
Сначала выберите пустую клетку.
{value} в {cell} не совпадает с решением. Проверьте другие варианты.
{cell}: поставлено {value}. Осталось клеток: {count}.
Верно! Всё судоку решено.
Выберите введённую цифру для удаления.
Цифра в {cell} стёрта.
Пока нечего отменять.
Возврат к предыдущему ходу.
Начальная задача восстановлена. «Отменить» вернёт предыдущее положение.
Проверьте кандидатов пустой клетки.
Объяснение открыто. Нажмите «Попробовать снова», чтобы ответить ещё раз.
Выберите цифру для ввода.
Выберите кандидатов для удаления. Повторное нажатие снимает выбор.
Выбрано: {count}
Ответ выбран. Нажмите «Проверить ответ».
Выбрать или отменить выбор {value}
Ответ не выбран. Сначала выберите клетку, затем цифру.
Верно. Ниже объясняется причина.
Это не ответ для данного приёма. Проверьте клетку, цифру и лишние или пропущенные удаления.
Объяснение показано. Нажмите «Попробовать снова» для того же задания.
Найдите клетку с единственным кандидатом.
Найдите две клетки с одинаковыми двумя кандидатами и выберите, что можно удалить в других местах.
Все выбранные ответы сброшены.
У {cell} остался только кандидат {value}, поэтому можно поставить эту цифру.
Ответ: поставить {value} в {cell}.
У {cells} есть только {digits}. Эти цифры занимают пару, поэтому их можно удалить из других клеток группы {unit}.
Удалить: {eliminations}. Порядок двух цифр в паре пока неизвестен.
{value} в {cell}
Обведённые клетки показывают основание. Зачёркнутых кандидатов можно удалить.
Не удалось загрузить упражнение. Обновите страницу.
Почему этот ход возможен
Пробная сетка судоку, 9 строк и 9 столбцов
Учебная сетка, 9 строк и 9 столбцов
Цифры ответа
Строки считаются сверху вниз, столбцы — слева направо. Выберите клетку и используйте кнопки или клавиатуру.''')
add('uk',
'Посібник із судоку|Вивчити прийоми|Розв’язати одне судоку|Про застосунок|Вибрати мову|До вмісту|Чим цікаве судоку|Судоку й тренування мислення|Ось так можна заповнювати клітинки|Запустити демо|Пауза|Один хід|Спочатку|Ефекти|Швидкість|Повільно|Звичайно|Швидко|Показувати ефекти|Показувати кандидатів|Стандарт|Іскри|Неон|Дзен|Перевірити відповідь|Скинути вибір|Спробувати знову|Показати пояснення|Наступний приклад|Підказка для наступного ходу|Стерти цифру|Скасувати|Конфіденційність|Умови використання|Про розробника|На цій сторінці|Як це працює|Приклад|Поширені помилки|Інші пояснення|Практика|Завдання',
'''Грайте в судоку й вивчайте способи розв’язання.
Порівнюйте рядки, стовпці та блоки, щоб знайти місце для цифри. Подивіться демонстрацію й спробуйте самі.
Що таке судоку?
У сітці 9×9 кожен рядок, стовпець і блок 3×3 має містити цифри 1–9 рівно по одному разу. Початкові цифри є підказками.
Одна цифра може підказати наступну.
Якщо клітинка має кандидатів 2 і 7, а в тому самому рядку з’явиться 2, залишається 7. Ця сімка може звузити вибір в інших клітинках.
Знаходьте вивчені прийоми самостійно.
З практикою ви помічатимете одиночки й пари. Хід, для якого раніше потрібна була підказка, зможете знайти самі.
Судоку спонукає порівнювати позиції, упорядковувати можливості й перевіряти міркування. Це може бути приємною нагодою подумати.
Що показують дослідження?
Спостережне дослідження 2019 року порівняло заявлену частоту числових головоломок і когнітивні тести 19 078 людей віком 50–93 роки. Частіше розв’язування було пов’язане з кращими результатами низки завдань на увагу, міркування й пам’ять.
Чого дослідження не доводить
Воно не доводить, що саме судоку спричинило відмінності, запобігає деменції чи покращує повсякденні здібності. Люди, які вже вправні, можуть грати частіше. Цей застосунок не досліджували.
Оберіть цікаву складність, користуйтеся нотатками й підказками та робіть перерви. Спробуйте, чи подобається процес, не очікуючи гарантованої користі для здоров’я.
У застосунку грати ще цікавіше!
Тренуйте окремі прийоми або змішані завдання й зберігайте поступ. Можна також відсканувати паперове судоку та читати підказки з поясненнями.
Можна спробувати безкоштовно. Деякі вправи й підказки потребують Premium.
Розв’яжіть це фіксоване завдання для початківців. Оберіть клітинку та введіть цифру кнопками або з клавіатури. Кожне введення перевіряється одразу.
Стрілки переміщують між клітинками, 1–9 вводять цифри, Delete і Backspace стирають. Проміжний стан не зберігається.
Два приклади дозволяють відпрацювати один прийом без розв’язування всієї сітки.
Чотири стилі ефектів супроводжують введення та завершення груп. Демо без звуку.
Одне фіксоване завдання з кандидатами й логічними підказками, без реєстрації.
Нотатки — це можливості, а не підтверджені цифри. Перевіряйте рядок, стовпець і блок та оновлюйте після кожного ходу.
Єдиний кандидат надійний, лише якщо інших не пропущено. Перед підтвердженням перевірте нотатки.
Перевірте всі порожні клітинки групи. Цифра повинна мати лише одне можливе місце.
Обидві клітинки мають містити рівно двох однакових кандидатів. {2,7} і {2,7,9} не є голою парою. Не стирайте кандидатів самої пари.
Перевірте всі позиції кандидата. Pointing видаляє поза блоком, Claiming — в інших клітинках усередині нього.''',
'''рядок {row}, стовпець {col}
порожня клітинка
початкова цифра
введена цифра
кандидати {digits}
{reason} Далі поставте {value}.
Поставте {value} у {cell}.
{reason} Поставлено {value}. ({count}/{total} клітинок)
Усі клітинки заповнено: {total}. Автоматичне демо почнеться знову після короткої паузи.
Повернення до початкової сітки. Порожні клітинки заповнюватимуться по черзі.
Автовідтворення вимкнено. Натисніть «Запустити демо» або «Один хід».
Обрано {cell}. Оберіть цифру.
Спершу оберіть порожню клітинку.
{value} у {cell} не відповідає розв’язку. Перевірте інші можливості.
{cell}: поставлено {value}. Залишилося клітинок: {count}.
Правильно! Усе судоку розв’язано.
Оберіть введену цифру, яку потрібно стерти.
Цифру у {cell} стерто.
Поки немає введень для скасування.
Повернення до попереднього ходу.
Початкове завдання відновлено. «Скасувати» поверне попередній стан.
Перевірте кандидатів порожньої клітинки.
Пояснення відкрите. Натисніть «Спробувати знову», щоб відповісти ще раз.
Оберіть цифру для введення.
Оберіть кандидатів для видалення. Повторне натискання скасовує вибір.
Обрано: {count}
Відповідь обрано. Натисніть «Перевірити відповідь».
Обрати або скасувати вибір {value}
Відповідь не обрано. Спочатку оберіть клітинку, потім цифру.
Правильно. Нижче наведено пояснення.
Це не відповідь для цього прийому. Перевірте клітинку, цифру та зайві або пропущені видалення.
Пояснення показано. Натисніть «Спробувати знову» для цього ж завдання.
Знайдіть клітинку з єдиним кандидатом.
Знайдіть дві клітинки з однаковими двома кандидатами й оберіть, що видалити в інших місцях.
Усі вибрані відповіді скинуто.
У {cell} лише кандидат {value}, тому можна поставити цю цифру.
Відповідь: поставити {value} у {cell}.
У {cells} лише {digits}. Ці цифри займають пару, тож їх можна видалити з інших клітинок групи {unit}.
Видалити: {eliminations}. Порядок двох цифр у парі ще невідомий.
{value} у {cell}
Обведені клітинки показують підставу. Закреслених кандидатів можна видалити.
Не вдалося завантажити вправу. Оновіть сторінку.
Чому цей хід можливий
Пробна сітка судоку, 9 рядків і 9 стовпців
Навчальна сітка, 9 рядків і 9 стовпців
Цифри відповіді
Рядки рахуються згори вниз, стовпці — зліва направо. Оберіть клітинку й скористайтеся кнопками або клавіатурою.''')
add('id',
'Panduan sudoku|Pelajari teknik|Main satu sudoku|Tentang aplikasi|Pilih bahasa|Ke isi utama|Serunya sudoku|Sudoku dan latihan otak|Isi angka seperti ini|Putar demo|Jeda|Satu langkah|Mulai lagi|Efek|Kecepatan|Lambat|Normal|Cepat|Tampilkan efek|Tampilkan kandidat|Standar|Kilau|Neon|Zen|Periksa jawaban|Hapus pilihan|Coba lagi|Lihat penjelasan|Contoh berikutnya|Petunjuk langkah berikutnya|Hapus angka|Urungkan|Privasi|Ketentuan penggunaan|Tentang pengembang|Di halaman ini|Cara kerja|Contoh|Kesalahan umum|Panduan lain|Latihan|Soal',
'''Main sudoku sambil mempelajari cara menyelesaikannya.
Bandingkan baris, kolom, dan kotak untuk menemukan tempat angka. Lihat demo lalu coba satu sudoku sendiri.
Apa itu sudoku?
Pada kisi 9×9, setiap baris, kolom, dan kotak 3×3 harus berisi angka 1–9 masing-masing satu kali. Angka awal menjadi petunjuk.
Satu angka bisa membuka langkah berikutnya.
Jika kandidat sebuah sel adalah 2 dan 7 lalu angka 2 diisi di baris yang sama, sel itu harus berisi 7. Angka 7 ini dapat membantu mempersempit sel lain.
Temukan sendiri teknik yang sudah dipelajari.
Dengan latihan, single dan pasangan mulai lebih mudah terlihat. Langkah yang dahulu perlu petunjuk bisa kamu temukan sendiri.
Sudoku mengajak kita membandingkan posisi, menyusun kemungkinan, dan memeriksa penalaran. Ini bisa menjadi cara menyenangkan untuk meluangkan waktu berpikir.
Apa temuan penelitian?
Studi observasional tahun 2019 membandingkan frekuensi bermain teka-teki angka yang dilaporkan sendiri dengan tes kognitif pada 19.078 orang usia 50–93 tahun. Frekuensi lebih tinggi berkaitan dengan hasil lebih baik pada sejumlah tugas perhatian, penalaran, dan ingatan.
Apa yang belum terbukti?
Studi itu tidak membuktikan sudoku menyebabkan perbedaan, mencegah demensia, atau meningkatkan kemampuan sehari-hari. Orang yang sudah terampil mungkin lebih sering bermain. Aplikasi ini tidak diuji.
Pilih tingkat yang menyenangkan, gunakan catatan atau petunjuk, dan beristirahatlah. Coba untuk mengetahui apakah kamu menyukai prosesnya, tanpa mengharapkan manfaat kesehatan yang dijamin.
Nikmati lebih banyak sudoku di aplikasi!
Latih teknik tertentu atau soal campuran dan simpan kemajuan. Kamu juga bisa memindai soal kertas dan membaca petunjuk beserta alasannya.
Bisa dicoba gratis. Sebagian latihan dan petunjuk memerlukan Premium.
Selesaikan satu soal pemula tetap ini. Pilih sel lalu masukkan angka dengan tombol atau papan ketik. Setiap masukan langsung diperiksa.
Tombol panah berpindah sel, 1–9 memasukkan angka, Delete atau Backspace menghapus. Kemajuan tidak disimpan.
Dua contoh memungkinkan latihan satu teknik tanpa menyelesaikan seluruh teka-teki.
Empat gaya efek untuk pengisian dan kelompok yang lengkap. Demo tidak bersuara.
Satu soal tetap dengan kandidat dan petunjuk logis, tanpa akun.
Catatan adalah kemungkinan, bukan angka pasti. Periksa baris, kolom, dan kotak lalu perbarui setelah angka dipastikan.
Kandidat tunggal hanya dapat dipercaya jika tidak ada yang terlewat. Periksa catatan sebelum memastikan.
Periksa semua sel kosong dalam kelompok. Angka tersebut harus memiliki tepat satu posisi yang mungkin.
Kedua sel harus memiliki tepat dua kandidat yang sama. {2,7} dan {2,7,9} bukan pasangan telanjang. Jangan hapus kandidat pasangan itu sendiri.
Periksa semua posisi kandidat. Pointing menghapus di luar kotak; Claiming menghapus di bagian lain dalam kotak.''',
'''baris {row}, kolom {col}
sel kosong
angka awal
angka yang dimasukkan
kandidat {digits}
{reason} Berikutnya isi {value}.
Isi {value} di {cell}.
{reason} {value} diisi. ({count}/{total} sel)
Semua {total} sel terisi. Demo otomatis dimulai lagi setelah jeda singkat.
Kembali ke kisi awal. Sel kosong akan diisi berurutan.
Putar otomatis nonaktif. Gunakan Putar demo atau Satu langkah.
{cell} dipilih. Pilih angka.
Pilih sel kosong terlebih dahulu.
{value} di {cell} tidak cocok dengan solusi. Periksa kandidat lainnya.
{cell}: {value} diisi. Tersisa {count} sel.
Benar! Seluruh kisi selesai.
Pilih angka yang dimasukkan untuk dihapus.
Angka di {cell} dihapus.
Belum ada masukan yang bisa diurungkan.
Kembali ke langkah sebelumnya.
Soal awal dipulihkan. Urungkan mengembalikan posisi sebelumnya.
Periksa kandidat pada sel kosong.
Penjelasan terbuka. Pilih Coba lagi untuk menjawab kembali.
Pilih angka yang akan diisi.
Pilih kandidat yang dihapus. Tekan lagi untuk membatalkan pilihan.
Dipilih: {count}
Jawaban dipilih. Tekan Periksa jawaban.
Pilih atau batalkan {value}
Belum ada jawaban. Pilih sel lalu angka.
Benar. Penjelasan di bawah menunjukkan alasannya.
Itu bukan jawaban teknik ini. Periksa sel, angka, dan kandidat yang kurang atau berlebihan dipilih.
Penjelasan ditampilkan. Pilih Coba lagi untuk soal yang sama.
Cari sel dengan satu kandidat saja.
Cari dua sel dengan dua kandidat yang sama, lalu pilih yang dapat dihapus di sel lain.
Semua pilihan jawaban dihapus.
{cell} hanya memiliki kandidat {value}, jadi angka itu dapat diisi di sana.
Jawaban: isi {value} di {cell}.
{cells} hanya memiliki {digits}. Angka itu menempati pasangan dan dapat dihapus dari sel lain dalam {unit}.
Hapus: {eliminations}. Urutan dua angka pada pasangan masih belum diketahui.
{value} di {cell}
Sel berbingkai menunjukkan alasannya. Kandidat yang dicoret bisa dihapus.
Latihan tidak dapat dimuat. Muat ulang halaman.
Alasan langkah ini benar
Kisi sudoku percobaan, 9 baris dan 9 kolom
Kisi latihan, 9 baris dan 9 kolom
Angka jawaban
Baris dihitung dari atas, kolom dari kiri. Pilih sel lalu gunakan tombol angka atau papan ketik.''')
add('tr',
'Sudoku rehberi|Teknikleri öğren|Bir sudoku oyna|Uygulama hakkında|Dil seçin|İçeriğe geç|Sudokunun keyfi|Sudoku ve zihin egzersizi|Sayıları böyle yerleştirebilirsiniz|Demoyu oynat|Duraklat|Bir adım|Baştan başla|Efektler|Hız|Yavaş|Normal|Hızlı|Efektleri göster|Adayları göster|Standart|Parıltı|Neon|Zen|Yanıtı kontrol et|Seçimi temizle|Yeniden dene|Açıklamayı göster|Sonraki örnek|Sonraki hamle için ipucu|Sayıyı sil|Geri al|Gizlilik|Kullanım koşulları|Geliştirici hakkında|Bu sayfada|Nasıl çalışır|Örnek|Sık yapılan hatalar|Diğer rehberler|Alıştırma|Soru',
'''Sudoku oynayın, çözüm yollarını öğrenin.
Sayıların yerini bulmak için satır, sütun ve blokları karşılaştırın. Demoyu izleyin, sonra bir sudoku deneyin.
Sudoku nedir?
9×9 karelik tabloda her satır, sütun ve 3×3 blok 1–9 sayılarını birer kez içermelidir. Başlangıç sayıları ipuçlarınızdır.
Bir sayı sonraki adımı açabilir.
Bir hücrenin adayları 2 ve 7 iken aynı satıra 2 yerleşirse o hücre 7 olur. Bu 7 başka hücrelerdeki olasılıkları da azaltabilir.
Öğrendiğiniz teknikleri kendiniz bulun.
Alıştırmayla tek adayları ve çiftleri daha kolay fark edersiniz. Önceden ipucu gerektiren bir hamleyi kendiniz bulabilirsiniz.
Sudoku konumları karşılaştırmayı, olasılıkları düzenlemeyi ve akıl yürütmeyi kontrol etmeyi gerektirir. Düşünerek vakit geçirmenin keyifli bir yolu olabilir.
Araştırmalar ne buldu?
2019 tarihli gözlemsel çalışma, 50–93 yaşındaki 19.078 kişinin bildirdiği sayı bulmacası sıklığını bilişsel testlerle karşılaştırdı. Daha sık bulmaca çözmek bazı dikkat, akıl yürütme ve bellek görevlerinde daha iyi sonuçlarla ilişkiliydi.
Araştırma neyi kanıtlamıyor?
Bu, farklara sudokunun neden olduğunu, demansı önlediğini veya günlük becerileri geliştirdiğini kanıtlamaz. Zaten başarılı kişiler daha sık oynuyor olabilir. Bu uygulama araştırılmadı.
Keyif aldığınız zorluğu seçin, not ve ipucu kullanın, mola verin. Garantili bir sağlık yararı beklemek yerine çözme sürecini sevip sevmediğinizi deneyin.
Uygulamada sudokunun keyfini daha çok çıkarın!
Belirli teknikleri veya karma soruları çalışın, ilerlemenizi kaydedin. Kâğıttaki sudokuyu tarayıp açıklamalı ipuçlarına da bakabilirsiniz.
Ücretsiz deneyebilirsiniz. Bazı alıştırmalar ve ipuçları Premium gerektirir.
Yeni başlayanlar için bu sabit soruyu tamamlayın. Hücre seçip düğmelerle veya klavyeyle sayı girin. Her giriş anında kontrol edilir.
Ok tuşları hücre değiştirir, 1–9 sayı girer, Delete veya Backspace siler. İlerleme kaydedilmez.
İki örnek, tüm bulmacayı çözmeden tek bir tekniği çalışmanızı sağlar.
Giriş ve tamamlanan gruplar için dört efekt stili vardır. Demo sessizdir.
Hesap gerektirmeyen, adaylar ve mantıksal ipuçları içeren tek bir sabit soru.
Notlar kesin sayılar değil, olasılıklardır. Satır, sütun ve bloğu kontrol edip her yerleştirmeden sonra güncelleyin.
Tek aday ancak başka aday unutulmamışsa güvenilirdir. Onaylamadan önce notları kontrol edin.
Seçilen gruptaki bütün boş hücreleri kontrol edin. Sayının yalnız bir olası yeri olmalıdır.
İki hücre tam olarak aynı iki adayı içermelidir. {2,7} ve {2,7,9} çıplak çift değildir. Çiftin kendi adaylarını silmeyin.
Adayın tüm konumlarını kontrol edin. Pointing blok dışından, Claiming ise aynı bloğun diğer hücrelerinden aday siler.''',
'''satır {row}, sütun {col}
boş hücre
başlangıç sayısı
girilen sayı
adaylar {digits}
{reason} Ardından {value} yerleştirilir.
{cell} konumuna {value} yerleştirin.
{reason} {value} yerleştirildi. ({count}/{total} hücre)
{total} hücrenin tamamı doldu. Otomatik demo kısa bir aradan sonra yeniden başlar.
Başlangıç tablosuna dönüldü. Boş hücreler sırayla doldurulacak.
Otomatik oynatma kapalı. Demoyu oynat veya Bir adım düğmesini kullanın.
{cell} seçildi. Bir sayı seçin.
Önce boş bir hücre seçin.
{cell} içindeki {value} çözümle eşleşmiyor. Diğer adayları kontrol edin.
{cell}: {value} yerleştirildi. {count} hücre kaldı.
Doğru! Tüm tablo tamamlandı.
Silmek için girilmiş bir sayı seçin.
{cell} içindeki sayı silindi.
Henüz geri alınacak giriş yok.
Önceki hamleye dönüldü.
Başlangıç sorusu geri yüklendi. Geri al önceki konumunuzu geri getirir.
Boş bir hücrenin adaylarını kontrol edin.
Açıklama açık. Tekrar yanıtlamak için Yeniden dene seçeneğini kullanın.
Yerleştirilecek sayıyı seçin.
Silinecek adayları seçin. Seçimi kaldırmak için tekrar basın.
Seçilen: {count}
Yanıt seçildi. Yanıtı kontrol et düğmesine basın.
{value} seç veya seçimini kaldır
Henüz yanıt yok. Önce hücre, sonra sayı seçin.
Doğru. Aşağıdaki açıklama nedenini gösterir.
Bu tekniğin yanıtı bu değil. Hücreyi, sayıyı ve eksik veya fazla elemeleri kontrol edin.
Açıklama gösterildi. Aynı soru için Yeniden dene seçeneğini kullanın.
Yalnızca tek adayı olan bir hücre bulun.
Aynı iki adayı içeren iki hücre bulun, sonra diğer yerlerden silinebilecek adayları seçin.
Tüm yanıt seçimleri temizlendi.
{cell} yalnızca {value} adayını içerir, bu yüzden sayı buraya yerleşir.
Yanıt: {cell} konumuna {value} yerleştirin.
{cells} yalnızca {digits} içerir. Bu sayılar çifti doldurur; {unit} içindeki diğer hücrelerden silinebilir.
Silinecekler: {eliminations}. Çiftteki sayıların sırası henüz belli değildir.
{cell} içindeki {value}
Çerçeveli hücreler gerekçeyi gösterir. Üstü çizilen adaylar silinebilir.
Alıştırma yüklenemedi. Sayfayı yenileyin.
Bu hamlenin gerekçesi
Deneme sudoku tablosu, 9 satır ve 9 sütun
Alıştırma tablosu, 9 satır ve 9 sütun
Yanıt sayıları
Satırlar yukarıdan aşağıya, sütunlar soldan sağa sayılır. Hücre seçip sayı düğmelerini veya klavyeyi kullanın.''')
add('vi',
'Hướng dẫn sudoku|Học kỹ thuật|Chơi một câu đố|Giới thiệu ứng dụng|Chọn ngôn ngữ|Đến nội dung|Niềm vui của sudoku|Sudoku và rèn luyện trí óc|Điền các số như thế này|Phát bản mẫu|Tạm dừng|Đi một bước|Bắt đầu lại|Hiệu ứng|Tốc độ|Chậm|Bình thường|Nhanh|Hiện hiệu ứng|Hiện ứng viên|Tiêu chuẩn|Lấp lánh|Neon|Thiền|Kiểm tra đáp án|Xóa lựa chọn|Thử lại|Xem giải thích|Ví dụ tiếp theo|Gợi ý bước tiếp theo|Xóa số|Hoàn tác|Quyền riêng tư|Điều khoản sử dụng|Về nhà phát triển|Trong trang này|Cách hoạt động|Ví dụ|Lỗi thường gặp|Hướng dẫn khác|Luyện tập|Câu hỏi',
'''Chơi sudoku và học cách giải.
So sánh hàng, cột và khối để tìm vị trí của số. Xem bản giải mẫu rồi tự thử một câu đố.
Sudoku là gì?
Trong bảng 9×9, mỗi hàng, cột và khối 3×3 phải có các số 1–9 đúng một lần. Các số có sẵn là manh mối.
Một số có thể mở ra bước tiếp theo.
Nếu một ô có ứng viên 2 và 7, khi số 2 được điền ở ô khác cùng hàng thì ô đó phải là 7. Số 7 này có thể thu hẹp lựa chọn ở các ô khác.
Tự nhận ra kỹ thuật đã học.
Qua luyện tập, bạn sẽ dễ nhận ra số đơn và cặp số hơn. Một bước từng cần gợi ý có thể trở thành bước bạn tự tìm được.
Sudoku yêu cầu so sánh vị trí, sắp xếp các khả năng và kiểm tra suy luận. Đây có thể là cách thú vị để dành thời gian suy nghĩ.
Nghiên cứu cho thấy điều gì?
Một nghiên cứu quan sát năm 2019 so sánh tần suất chơi đố số tự báo cáo và bài kiểm tra nhận thức của 19.078 người từ 50–93 tuổi. Tần suất cao hơn có liên quan đến kết quả tốt hơn ở nhiều nhiệm vụ chú ý, suy luận và trí nhớ.
Nghiên cứu chưa chứng minh điều gì?
Không thể kết luận sudoku gây ra khác biệt, ngăn sa sút trí tuệ hay cải thiện năng lực hằng ngày. Người vốn làm tốt có thể chơi thường xuyên hơn. Nghiên cứu không đánh giá ứng dụng này.
Chọn độ khó bạn thích, dùng ghi chú hoặc gợi ý và nghỉ khi cần. Hãy thử xem bạn có thích quá trình giải không, thay vì kỳ vọng lợi ích sức khỏe được bảo đảm.
Chơi sudoku vui hơn nữa trong ứng dụng!
Luyện từng kỹ thuật hoặc bài tập tổng hợp và lưu tiến độ. Bạn cũng có thể quét câu đố trên giấy rồi xem gợi ý có giải thích.
Có thể dùng thử miễn phí. Một số bài tập và gợi ý cần Premium.
Giải trọn câu đố cố định dành cho người mới này. Chọn ô rồi dùng nút số hoặc bàn phím. Mỗi số nhập được kiểm tra ngay.
Dùng phím mũi tên để di chuyển, 1–9 để nhập và Delete hoặc Backspace để xóa. Tiến độ không được lưu.
Hai ví dụ giúp luyện một kỹ thuật mà không cần giải cả câu đố.
Có bốn kiểu hiệu ứng cho số được điền và nhóm hoàn thành. Bản mẫu không có âm thanh.
Một câu đố cố định có ứng viên và gợi ý logic, không cần tài khoản.
Ghi chú là khả năng, không phải số đã xác định. Kiểm tra hàng, cột, khối và cập nhật sau mỗi lần điền đúng.
Một ứng viên duy nhất chỉ đáng tin khi không bỏ sót ứng viên khác. Hãy kiểm tra ghi chú trước khi xác nhận.
Kiểm tra mọi ô trống trong nhóm. Số đó chỉ được có một vị trí có thể điền.
Hai ô phải có đúng hai ứng viên giống nhau. {2,7} và {2,7,9} không tạo thành cặp trần. Đừng xóa ứng viên của chính cặp đó.
Kiểm tra mọi vị trí ứng viên. Pointing loại ở ngoài khối; Claiming loại tại các vị trí khác trong khối.''',
'''hàng {row}, cột {col}
ô trống
số cho sẵn
số đã nhập
ứng viên {digits}
{reason} Tiếp theo điền {value}.
Điền {value} vào {cell}.
{reason} Đã điền {value}. ({count}/{total} ô)
Đã điền đủ {total} ô. Khi phát tự động, bản mẫu sẽ chạy lại sau một lát.
Đã trở lại bảng ban đầu. Các ô trống sẽ được điền lần lượt.
Đã tắt phát tự động. Dùng Phát bản mẫu hoặc Đi một bước.
Đã chọn {cell}. Hãy chọn số.
Trước tiên hãy chọn một ô trống.
{value} ở {cell} không khớp đáp án. Hãy kiểm tra ứng viên khác.
{cell}: đã điền {value}. Còn {count} ô.
Chính xác! Đã hoàn thành cả bảng.
Chọn một số đã nhập để xóa.
Đã xóa số ở {cell}.
Chưa có thao tác nào để hoàn tác.
Đã quay về bước trước.
Đã khôi phục câu đố ban đầu. Hoàn tác sẽ đưa về trạng thái trước đó.
Kiểm tra ứng viên của một ô trống.
Đang xem giải thích. Chọn Thử lại để trả lời lại.
Chọn số cần điền.
Chọn các ứng viên cần loại. Nhấn lần nữa để bỏ chọn.
Đã chọn: {count}
Đã chọn câu trả lời. Nhấn Kiểm tra đáp án.
Chọn hoặc bỏ chọn {value}
Chưa chọn câu trả lời. Hãy chọn ô rồi chọn số.
Chính xác. Xem lý do trong phần giải thích bên dưới.
Chưa đúng với kỹ thuật này. Kiểm tra ô, số và ứng viên bị chọn thừa hoặc thiếu.
Đã hiện giải thích. Chọn Thử lại để làm lại câu này.
Tìm ô chỉ có một ứng viên.
Tìm hai ô chỉ có cùng hai ứng viên rồi chọn những ứng viên có thể loại ở ô khác.
Đã xóa mọi lựa chọn trả lời.
{cell} chỉ có ứng viên {value}, nên có thể điền số đó.
Đáp án: điền {value} vào {cell}.
{cells} chỉ có {digits}. Hai số này chiếm cặp ô, nên có thể loại khỏi các ô khác trong {unit}.
Loại: {eliminations}. Thứ tự hai số trong cặp vẫn chưa xác định.
{value} ở {cell}
Ô có viền chỉ ra căn cứ. Ứng viên bị gạch ngang có thể loại.
Không tải được bài tập. Hãy tải lại trang.
Vì sao đi được bước này
Bảng sudoku dùng thử, 9 hàng và 9 cột
Bảng luyện tập, 9 hàng và 9 cột
Các số trả lời
Đếm hàng từ trên xuống, cột từ trái sang phải. Chọn ô rồi dùng nút số hoặc bàn phím.''')
add('th',
'คู่มือซูโดกุ|เรียนรู้เทคนิค|เล่นซูโดกุหนึ่งข้อ|เกี่ยวกับแอป|เลือกภาษา|ไปยังเนื้อหา|ความสนุกของซูโดกุ|ซูโดกุกับการใช้ความคิด|ค่อย ๆ เติมตัวเลขแบบนี้|เล่นตัวอย่าง|หยุดชั่วคราว|เดินหนึ่งก้าว|เริ่มใหม่|เอฟเฟกต์|ความเร็ว|ช้า|ปกติ|เร็ว|แสดงเอฟเฟกต์|แสดงตัวเลือก|มาตรฐาน|ประกาย|นีออน|เซน|ตรวจคำตอบ|ล้างการเลือก|ลองอีกครั้ง|ดูคำอธิบาย|ตัวอย่างถัดไป|คำใบ้ก้าวถัดไป|ลบตัวเลข|ย้อนกลับ|ความเป็นส่วนตัว|เงื่อนไขการใช้งาน|เกี่ยวกับผู้พัฒนา|เนื้อหาในหน้านี้|หลักการ|ตัวอย่าง|ข้อผิดพลาดที่พบบ่อย|คู่มืออื่น|ฝึกฝน|โจทย์',
'''เล่นซูโดกุไปพร้อมกับเรียนรู้วิธีแก้โจทย์
เปรียบเทียบแถว คอลัมน์ และบล็อกเพื่อหาตำแหน่งของตัวเลข ดูตัวอย่างการแก้แล้วลองเล่นเองหนึ่งข้อ
ซูโดกุคืออะไร?
เติมเลข 1–9 ในตาราง 9×9 โดยแต่ละแถว คอลัมน์ และบล็อก 3×3 ต้องมีตัวเลขแต่ละตัวเพียงครั้งเดียว ตัวเลขที่ให้มาคือเบาะแส
ตัวเลขหนึ่งตัวอาจช่วยให้พบตัวถัดไป
หากช่องหนึ่งมีตัวเลือก 2 กับ 7 แล้วใส่ 2 ในช่องอื่นของแถวเดียวกัน ช่องนั้นต้องเป็น 7 เลข 7 นี้อาจช่วยลดตัวเลือกในช่องอื่นได้อีก
ค้นพบเทคนิคที่เรียนมาด้วยตัวเอง
เมื่อฝึกบ่อยขึ้น คุณจะมองเห็นซิงเกิลและคู่ได้ง่ายขึ้น ก้าวที่เคยต้องใช้คำใบ้อาจกลายเป็นก้าวที่หาได้เอง
ซูโดกุให้เราเปรียบเทียบตำแหน่ง จัดระเบียบความเป็นไปได้ และตรวจเหตุผล จึงเป็นการใช้เวลาคิดที่สนุกได้
งานวิจัยพบอะไร?
งานศึกษาเชิงสังเกตในปี 2019 เปรียบเทียบความถี่การเล่นปริศนาตัวเลขที่รายงานเองกับแบบทดสอบการรู้คิดของคน 19,078 คน อายุ 50–93 ปี การเล่นบ่อยมีความสัมพันธ์กับผลที่ดีกว่าในงานด้านความสนใจ การใช้เหตุผล และความจำหลายรายการ
สิ่งที่งานวิจัยยังพิสูจน์ไม่ได้
งานนี้ไม่ได้พิสูจน์ว่าซูโดกุทำให้ผลดีขึ้น ป้องกันภาวะสมองเสื่อม หรือเพิ่มความสามารถในชีวิตประจำวัน คนที่ทำได้ดีอยู่แล้วอาจเล่นบ่อยกว่า และไม่ได้ศึกษาผลของแอปนี้
เลือกระดับที่สนุก ใช้บันทึกหรือคำใบ้ และพักได้ ลองดูว่าคุณชอบกระบวนการแก้โจทย์หรือไม่ โดยไม่คาดหวังผลด้านสุขภาพที่รับประกัน
สนุกกับซูโดกุได้มากขึ้นในแอป!
ฝึกเทคนิคเฉพาะหรือแบบผสมและบันทึกความคืบหน้าได้ อีกทั้งสแกนโจทย์บนกระดาษเพื่ออ่านคำใบ้พร้อมเหตุผล
ทดลองได้ฟรี แบบฝึกและคำใบ้บางส่วนต้องใช้ Premium
แก้โจทย์สำหรับผู้เริ่มต้นข้อนี้จนจบ เลือกช่องแล้วใช้ปุ่มตัวเลขหรือแป้นพิมพ์ ระบบจะตรวจทุกครั้งที่ใส่เลข
ใช้ปุ่มลูกศรย้ายช่อง 1–9 ใส่เลข และ Delete หรือ Backspace ลบ ระบบไม่บันทึกความคืบหน้า
ตัวอย่างสองข้อช่วยฝึกหนึ่งเทคนิคโดยไม่ต้องแก้ทั้งตาราง
เลือกเอฟเฟกต์ได้สี่แบบสำหรับการใส่เลขและการเติมกลุ่มครบ ตัวอย่างไม่มีเสียง
โจทย์คงที่หนึ่งข้อพร้อมตัวเลือกและคำใบ้ตามเหตุผล ไม่ต้องมีบัญชี
บันทึกคือตัวเลขที่อาจเป็นไปได้ ไม่ใช่คำตอบที่ยืนยันแล้ว ตรวจแถว คอลัมน์ บล็อก และอัปเดตเมื่อใส่เลขแน่นอน
ตัวเลือกเดียวเชื่อถือได้เมื่อไม่ได้ตกหล่นตัวอื่น ตรวจบันทึกก่อนยืนยัน
ตรวจทุกช่องว่างในกลุ่มที่เลือก ตัวเลขนั้นต้องมีตำแหน่งที่ใส่ได้เพียงแห่งเดียว
สองช่องต้องมีตัวเลือกเหมือนกันสองตัวเท่านั้น {2,7} กับ {2,7,9} ไม่ใช่คู่เปลือย อย่าลบตัวเลือกของคู่เอง
ตรวจตำแหน่งตัวเลือกทั้งหมด Pointing ลบนอกบล็อก ส่วน Claiming ลบตำแหน่งอื่นภายในบล็อก''',
'''แถว {row} คอลัมน์ {col}
ช่องว่าง
ตัวเลขที่โจทย์ให้
ตัวเลขที่ใส่
ตัวเลือก {digits}
{reason} ต่อไปใส่ {value}
ใส่ {value} ที่ {cell}
{reason} ใส่ {value} แล้ว ({count}/{total} ช่อง)
เติมครบ {total} ช่องแล้ว เมื่อเล่นอัตโนมัติจะเริ่มใหม่หลังพักสักครู่
กลับสู่ตารางเริ่มต้นแล้ว จะเติมช่องว่างตามลำดับ
ปิดการเล่นอัตโนมัติอยู่ ใช้เล่นตัวอย่างหรือเดินหนึ่งก้าว
เลือก {cell} แล้ว โปรดเลือกตัวเลข
เลือกช่องว่างก่อน
{value} ที่ {cell} ไม่ตรงกับคำตอบ ลองตรวจตัวเลือกอื่น
{cell}: ใส่ {value} แล้ว เหลือ {count} ช่อง
ถูกต้อง! เติมครบทั้งตารางแล้ว
เลือกตัวเลขที่ใส่ไว้เพื่อลบ
ลบตัวเลขที่ {cell} แล้ว
ยังไม่มีการใส่เลขให้ย้อนกลับ
กลับไปก้าวก่อนหน้าแล้ว
คืนค่าโจทย์เริ่มต้นแล้ว กดย้อนกลับเพื่อคืนสถานะก่อนหน้า
ตรวจตัวเลือกในช่องว่าง
กำลังแสดงคำอธิบาย กดลองอีกครั้งเพื่อตอบใหม่
เลือกตัวเลขที่จะใส่
เลือกตัวเลือกที่จะลบ กดซ้ำเพื่อยกเลิกการเลือก
เลือกแล้ว: {count}
เลือกคำตอบแล้ว กดตรวจคำตอบ
เลือกหรือยกเลิก {value}
ยังไม่ได้เลือกคำตอบ โปรดเลือกช่องแล้วเลือกตัวเลข
ถูกต้อง อ่านเหตุผลในคำอธิบายด้านล่าง
ยังไม่ใช่คำตอบของเทคนิคนี้ ตรวจช่อง ตัวเลข และตัวเลือกที่เลือกเกินหรือตกหล่น
แสดงคำอธิบายแล้ว กดลองอีกครั้งเพื่อทำข้อเดิม
หาช่องที่มีตัวเลือกเดียว
หาสองช่องที่มีตัวเลือกเหมือนกันสองตัว แล้วเลือกตัวเลือกที่ลบจากช่องอื่นได้
ล้างคำตอบที่เลือกทั้งหมดแล้ว
{cell} มีตัวเลือกเพียง {value} จึงใส่เลขนี้ได้
คำตอบ: ใส่ {value} ที่ {cell}
{cells} มีเพียง {digits} ตัวเลขสองตัวนี้อยู่ในคู่ จึงลบจากช่องอื่นใน {unit} ได้
ลบ: {eliminations} ยังไม่รู้ลำดับของตัวเลขสองตัวในคู่
{value} ที่ {cell}
ช่องที่มีกรอบคือเหตุผล ตัวเลือกที่ขีดฆ่าสามารถลบได้
โหลดแบบฝึกไม่สำเร็จ โปรดโหลดหน้าใหม่
เหตุผลของก้าวนี้
ตารางซูโดกุทดลอง 9 แถว 9 คอลัมน์
ตารางฝึก 9 แถว 9 คอลัมน์
ตัวเลขสำหรับคำตอบ
นับแถวจากบนลงล่างและคอลัมน์จากซ้ายไปขวา เลือกช่องแล้วใช้ปุ่มตัวเลขหรือแป้นพิมพ์''')
add('hi',
'सुडोकू मार्गदर्शिका|तकनीक सीखें|एक पहेली खेलें|ऐप के बारे में|भाषा चुनें|मुख्य सामग्री पर जाएँ|सुडोकू का आनंद|सुडोकू और मानसिक अभ्यास|इस तरह अंक भरते जाएँ|डेमो चलाएँ|रोकें|एक चाल|फिर से शुरू करें|प्रभाव|गति|धीमी|सामान्य|तेज़|प्रभाव दिखाएँ|संभावित अंक दिखाएँ|मानक|चमक|निऑन|ज़ेन|उत्तर जाँचें|चयन मिटाएँ|फिर प्रयास करें|व्याख्या देखें|अगला उदाहरण|अगली चाल का संकेत|अंक मिटाएँ|पूर्ववत करें|गोपनीयता|उपयोग की शर्तें|डेवलपर के बारे में|इस पृष्ठ पर|यह कैसे काम करता है|उदाहरण|आम गलतियाँ|अन्य मार्गदर्शिकाएँ|अभ्यास|प्रश्न',
'''सुडोकू खेलें और उसे हल करना सीखें।
पंक्तियों, स्तंभों और खंडों की तुलना करके अंक की जगह खोजें। पहले डेमो देखें, फिर स्वयं एक पहेली आज़माएँ।
सुडोकू क्या है?
9×9 की ग्रिड में हर पंक्ति, स्तंभ और 3×3 खंड में 1–9 का हर अंक ठीक एक बार आना चाहिए। शुरुआत में दिए अंक आपके संकेत हैं।
एक अंक अगली चाल का रास्ता खोल सकता है।
किसी खाने में 2 और 7 की संभावना हो और उसी पंक्ति में दूसरी जगह 2 भर जाए, तो उस खाने में 7 होगा। यह 7 दूसरे खानों की संभावनाएँ भी घटा सकता है।
सीखी हुई तकनीक स्वयं पहचानें।
अभ्यास से सिंगल और जोड़े पहचानना आसान होता है। जिस चाल के लिए पहले संकेत चाहिए था, उसे आप स्वयं खोज सकते हैं।
सुडोकू में स्थानों की तुलना, संभावनाओं को व्यवस्थित करना और तर्क जाँचना शामिल है। यह सोचने में समय बिताने का आनंददायक तरीका हो सकता है।
शोध में क्या मिला?
2019 के एक अवलोकन अध्ययन में 50–93 वर्ष के 19,078 लोगों द्वारा बताई गई संख्या-पहेलियों की आवृत्ति और संज्ञानात्मक परीक्षणों की तुलना की गई। अधिक बार खेलने का संबंध ध्यान, तर्क और स्मृति के कई कार्यों में बेहतर परिणामों से था।
शोध क्या सिद्ध नहीं करता?
इससे यह सिद्ध नहीं होता कि सुडोकू ने अंतर पैदा किया, मनोभ्रंश रोकता है या दैनिक क्षमताएँ बढ़ाता है। पहले से कुशल लोग शायद अधिक खेलते हों। इस ऐप का परीक्षण नहीं किया गया था।
पसंद की कठिनाई चुनें, नोट या संकेत लें और विराम करें। स्वास्थ्य लाभ की गारंटी की अपेक्षा के बजाय देखें कि हल करने की प्रक्रिया आपको अच्छी लगती है या नहीं।
ऐप में सुडोकू का और आनंद लें!
अलग तकनीकों या मिश्रित प्रश्नों का अभ्यास करें और प्रगति सहेजें। कागज़ की पहेली स्कैन करके तर्क सहित संकेत भी पढ़ सकते हैं।
मुफ़्त में आज़माएँ। कुछ अभ्यासों और संकेतों के लिए Premium चाहिए।
शुरुआती लोगों के लिए इस तय पहेली को पूरा हल करें। खाना चुनकर अंक बटन या कीबोर्ड से भरें। हर प्रविष्टि तुरंत जाँची जाती है।
तीर कुंजियों से खाना बदलें, 1–9 से अंक भरें और Delete या Backspace से मिटाएँ। प्रगति सहेजी नहीं जाती।
दो उदाहरणों से पूरी पहेली हल किए बिना एक तकनीक का अभ्यास कर सकते हैं।
अंक भरने और समूह पूरे होने के लिए चार प्रभाव-शैलियाँ हैं। डेमो में आवाज़ नहीं है।
संभावित अंकों और तार्किक संकेतों के साथ एक तय पहेली, बिना खाते के।
नोट संभावनाएँ हैं, पक्के अंक नहीं। पंक्ति, स्तंभ और खंड जाँचें और हर निश्चित अंक के बाद नोट बदलें।
एक संभावित अंक तभी भरोसेमंद है जब कोई दूसरा छूटा न हो। पुष्टि से पहले नोट जाँचें।
चुने समूह के सभी खाली खाने जाँचें। उस अंक की केवल एक संभव जगह होनी चाहिए।
दोनों खानों में ठीक वही दो संभावित अंक होने चाहिए। {2,7} और {2,7,9} नेकेड पेयर नहीं हैं। जोड़े के अपने अंक न मिटाएँ।
संभावित अंक की सभी जगहें जाँचें। Pointing में खंड के बाहर और Claiming में उसी खंड की दूसरी जगहों से अंक हटाते हैं।''',
'''पंक्ति {row}, स्तंभ {col}
खाली खाना
दिया हुआ अंक
भरा हुआ अंक
संभावित अंक {digits}
{reason} अगला अंक {value} भरें।
{cell} में {value} भरें।
{reason} {value} भर दिया गया। ({count}/{total} खाने)
सभी {total} खाने भर गए। स्वतः चलने वाला डेमो थोड़े विराम के बाद फिर शुरू होगा।
शुरुआती ग्रिड पर लौट आए। खाली खाने क्रम से भरेंगे।
स्वतः चलना बंद है। डेमो चलाएँ या एक चाल चुनें।
{cell} चुना गया। अंक चुनें।
पहले खाली खाना चुनें।
{cell} का {value} समाधान से मेल नहीं खाता। दूसरे संभावित अंक जाँचें।
{cell} में {value} भरा। {count} खाने शेष हैं।
सही! पूरी पहेली हल हो गई।
मिटाने के लिए भरा हुआ अंक चुनें।
{cell} का अंक मिटा दिया।
अभी पूर्ववत करने के लिए कोई प्रविष्टि नहीं है।
पिछली चाल पर लौट आए।
शुरुआती पहेली वापस आ गई। पूर्ववत करने से पिछली स्थिति लौटेगी।
खाली खाने के संभावित अंक जाँचें।
व्याख्या खुली है। दोबारा उत्तर देने के लिए फिर प्रयास करें चुनें।
भरने वाला अंक चुनें।
हटाने वाले संभावित अंक चुनें। दोबारा दबाने पर चयन हटेगा।
चुने गए: {count}
उत्तर चुन लिया। उत्तर जाँचें दबाएँ।
{value} चुनें या चयन हटाएँ
अभी उत्तर नहीं चुना। पहले खाना, फिर अंक चुनें।
सही। नीचे की व्याख्या में कारण देखें।
यह इस तकनीक का उत्तर नहीं है। खाना, अंक और अधिक या कम चुने गए हटाव जाँचें।
व्याख्या दिखाई गई। वही प्रश्न दोहराने के लिए फिर प्रयास करें चुनें।
ऐसा खाना खोजें जिसमें केवल एक संभावित अंक हो।
एक जैसे दो संभावित अंकों वाले दो खाने खोजें, फिर दूसरी जगह से हटाए जा सकने वाले अंक चुनें।
उत्तर के सभी चयन मिटा दिए गए।
{cell} में केवल {value} संभव है, इसलिए यह अंक वहाँ भर सकते हैं।
उत्तर: {cell} में {value} भरें।
{cells} में केवल {digits} हैं। ये अंक जोड़े के दोनों खाने लेते हैं, इसलिए {unit} के अन्य खानों से हट सकते हैं।
हटाएँ: {eliminations}। जोड़े में दोनों अंकों का क्रम अभी ज्ञात नहीं है।
{cell} में {value}
घेरे वाले खाने कारण दिखाते हैं। काटे गए संभावित अंक हट सकते हैं।
अभ्यास लोड नहीं हुआ। पृष्ठ फिर लोड करें।
इस चाल का कारण
परीक्षण सुडोकू ग्रिड, 9 पंक्तियाँ और 9 स्तंभ
अभ्यास ग्रिड, 9 पंक्तियाँ और 9 स्तंभ
उत्तर के अंक
पंक्तियाँ ऊपर से नीचे और स्तंभ बाएँ से दाएँ गिने जाते हैं। खाना चुनकर अंक बटन या कीबोर्ड इस्तेमाल करें।''')
add('ar',
'دليل السودوكو|تعلّم التقنيات|العب لغزًا واحدًا|عن التطبيق|اختر اللغة|انتقل إلى المحتوى|متعة السودوكو|السودوكو والنشاط الذهني|املأ الأرقام بهذه الطريقة|تشغيل العرض|إيقاف مؤقت|خطوة واحدة|البدء من جديد|المؤثرات|السرعة|بطيئة|عادية|سريعة|إظهار المؤثرات|إظهار المرشحين|قياسي|بريق|نيون|زن|تحقق من الإجابة|مسح التحديد|حاول مجددًا|عرض الشرح|المثال التالي|تلميح للخطوة التالية|مسح الرقم|تراجع|الخصوصية|شروط الاستخدام|عن المطوّر|في هذه الصفحة|كيف تعمل|مثال|أخطاء شائعة|أدلة أخرى|تدرّب|السؤال',
'''العب السودوكو وتعلّم طرق حلها.
قارن الصفوف والأعمدة والمربعات لتجد موضع الرقم. شاهد العرض ثم جرّب حل لغز بنفسك.
ما هي السودوكو؟
في شبكة 9×9 يجب أن يحتوي كل صف وعمود ومربع 3×3 على الأرقام 1–9 مرة واحدة فقط. الأرقام المعطاة هي أدلتك.
قد يكشف رقم واحد الخطوة التالية.
إذا كان مرشحا خلية هما 2 و7 ووُضع 2 في موضع آخر من الصف نفسه، تصبح الخلية 7. وقد يساعد هذا الرقم في تضييق خيارات خلايا أخرى.
اكتشف التقنيات التي تعلّمتها بنفسك.
مع التدريب ستلاحظ الأرقام المنفردة والأزواج بسهولة أكبر. وقد تجد بنفسك خطوة كنت تحتاج إلى تلميح لاكتشافها.
تتطلب السودوكو مقارنة المواضع وتنظيم الاحتمالات والتحقق من الاستنتاجات. ويمكن أن تكون وسيلة ممتعة لقضاء وقت في التفكير.
ماذا وجدت الأبحاث؟
قارنت دراسة رصدية عام 2019 بين تكرار ألغاز الأرقام المبلّغ عنه ذاتيًا ونتائج اختبارات معرفية لدى 19,078 شخصًا بين 50 و93 عامًا. ارتبط التكرار الأعلى بأداء أفضل في عدة مهام للانتباه والاستدلال والذاكرة.
ما الذي لا تثبته الدراسة؟
لا تثبت أن السودوكو سببت الفروق أو تمنع الخرف أو تحسّن القدرات اليومية. ربما يلعب أصحاب القدرات الأفضل أصلًا أكثر. ولم تدرس هذا التطبيق.
اختر مستوى تستمتع به، واستخدم الملاحظات والتلميحات وخذ استراحة. جرّب لترى إن كنت تستمتع بالحل دون انتظار فائدة صحية مضمونة.
استمتع أكثر بالسودوكو في التطبيق!
تدرّب على تقنيات محددة أو تمارين مختلطة واحفظ تقدمك. ويمكنك أيضًا مسح لغز ورقي بالكاميرا وقراءة تلميحات تشرح السبب.
يمكن التجربة مجانًا. تتطلب بعض التمارين والتلميحات اشتراك Premium.
حل هذا اللغز الثابت للمبتدئين حتى النهاية. اختر خلية وأدخل الرقم بالأزرار أو لوحة المفاتيح. يُفحص كل إدخال فورًا.
استخدم الأسهم للتنقل، و1–9 للإدخال، وDelete أو Backspace للمسح. لا يُحفظ التقدم.
مثالان للتدرّب على تقنية واحدة دون حل اللغز كاملًا.
أربعة أنماط لمؤثرات إدخال الأرقام وإكمال المجموعات. العرض بلا صوت.
لغز ثابت واحد بمرشحين وتلميحات منطقية، دون حساب.
الملاحظات احتمالات وليست أرقامًا مؤكدة. افحص الصف والعمود والمربع وحدّثها بعد كل رقم مؤكد.
لا يُعتمد على المرشح الوحيد إلا إن لم تُنسَ مرشحات أخرى. راجع الملاحظات قبل التأكيد.
افحص كل الخلايا الفارغة في المجموعة. يجب أن يكون للرقم موضع ممكن واحد فقط.
يجب أن تحتوي الخليتان على المرشحين نفسيهما فقط. {2,7} و{2,7,9} لا تشكلان زوجًا عاريًا. لا تمسح مرشحي الزوج نفسه.
افحص كل مواضع المرشح. يحذف Pointing خارج المربع، ويحذف Claiming من المواضع الأخرى داخله.''',
'''الصف {row}، العمود {col}
خلية فارغة
رقم معطى
رقم مُدخل
المرشحون {digits}
{reason} بعد ذلك ضع {value}.
ضع {value} في {cell}.
{reason} وُضع {value}. ({count}/{total} خلية)
اكتملت الخلايا وعددها {total}. سيبدأ العرض التلقائي من جديد بعد توقف قصير.
عدنا إلى الشبكة الأولى. ستُملأ الخلايا الفارغة بالترتيب.
التشغيل التلقائي متوقف. استخدم تشغيل العرض أو خطوة واحدة.
تم اختيار {cell}. اختر رقمًا.
اختر خلية فارغة أولًا.
{value} في {cell} لا يطابق الحل. افحص المرشحين الآخرين.
{cell}: وُضع {value}. بقي {count} خلية.
صحيح! اكتمل حل الشبكة.
اختر رقمًا مُدخلًا لمسحه.
مُسح الرقم في {cell}.
لا يوجد إدخال للتراجع عنه بعد.
عدنا إلى الخطوة السابقة.
استُعيد اللغز الأول. يعيد التراجع الحالة السابقة.
افحص مرشحي خلية فارغة.
الشرح مفتوح. اختر حاول مجددًا للإجابة مرة أخرى.
اختر الرقم الذي تريد وضعه.
اختر المرشحين لحذفهم. اضغط مرة أخرى لإلغاء التحديد.
المحدد: {count}
تم اختيار الإجابة. اضغط تحقق من الإجابة.
اختيار {value} أو إلغاء اختياره
لم تختر إجابة. اختر خلية ثم رقمًا.
صحيح. اقرأ الشرح أدناه لمعرفة السبب.
ليست إجابة هذه التقنية. افحص الخلية والرقم والمرشحين الزائدين أو الناقصين.
ظهر الشرح. اختر حاول مجددًا لتكرار السؤال نفسه.
ابحث عن خلية لها مرشح واحد فقط.
ابحث عن خليتين لهما المرشحان نفسيهما، ثم حدد ما يمكن حذفه من الخلايا الأخرى.
مُسحت جميع اختيارات الإجابة.
ليس في {cell} سوى المرشح {value}، لذا يمكن وضعه فيها.
الإجابة: ضع {value} في {cell}.
ليس لدى {cells} سوى {digits}. يشغل الرقمان الزوج، لذا يمكن حذفهما من الخلايا الأخرى في {unit}.
احذف: {eliminations}. ترتيب الرقمين داخل الزوج لم يُعرف بعد.
{value} في {cell}
الخلايا المؤطّرة توضّح السبب. يمكن حذف المرشحين المشطوبين.
تعذّر تحميل التمرين. أعد تحميل الصفحة.
سبب صحة هذه الخطوة
شبكة سودوكو تجريبية، 9 صفوف و9 أعمدة
شبكة تدريب، 9 صفوف و9 أعمدة
أرقام الإجابة
تُعد الصفوف من الأعلى إلى الأسفل والأعمدة من اليسار إلى اليمين. اختر خلية واستخدم الأزرار أو لوحة المفاتيح.''')
