project = "workshop"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Design

background_fix = 1
background_picture = "Rainbow Blue.jpg"

title_fix = 1
title_picture = "Rainbow Blue.jpg"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# AI prompts

workshop_ziel = "produktseite"
stichworte = "texte"
zielgruppe = "data people"
anzahl_personen = "3"

ki_request_001 = f"Schreib mir 4 Sätze, warum es Sinn macht als {zielgruppe} in {workshop_ziel} zu investieren. Insgesamt maximal 40 Worte. Der Text soll sehr leicht lesbar sein, sodass ein 10-jähriger Schüler den Text verstehen könnte. Benutze klare und einfache Sprache, selbst beim Erklären von komplexen Sachverhalten. Schreibe eher kurze Sätze. Vermeide Fremdwörter, Fachbegriffe und Abkürzungen."
ki_request_002 = f"Gib mir fünf elegante und ungewöhnliche Bildideen um zu sagen, dass {workshop_ziel} in für {anzahl_personen} personen gut sind"
ki_request_003 = f"Du bist ein Workshop Spezialist. Überlege dir eine konkrete Workshop-Übung für die Dauer von 10 Minuten, die das Thema '{workshop_ziel}' spannend macht. Berücksichtige dabei, dass die Übung '{stichworte}' beinhalten sollte. Insgesamt soll der Workshop aus 6 Schritten bestehen (1., 2., 3., 4., 5., 6.). Füge für jeden Punkt in zwei Sätzen den Beispiel Outcome ein"
ki_request_004 = f"Schlage mir mir einen kreativen und kurzen Namen für den Workshop vor um {workshop_ziel} zu erreichen. Maximal 3 Worte"
ki_request_005 = f"Finde ein synonym für {workshop_ziel}. Schlage mir mir einen kreativen und kurzen Namen für den Workshop vor um das zu erreichen. Maximal 3 Worte."


# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# File Paths

title = "1 Second Deck – Powerpoint App"

userfolder_path = "" 

# Pfad zum Eingangsordner (masters) und zur Eingabe-Datei (Master.pptx)
input_folder = f"{userfolder_path}masters"
input_file = f"{project}.pptx"

# Pfad zum Ausgabeordner (output) und zum Ausgabe-Dateinamen
output_folder = f"{userfolder_path}output"
output_file = f"{project}_edited.pptx"

img_folder = f"{userfolder_path}img/"

