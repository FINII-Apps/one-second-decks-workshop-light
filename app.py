import config as config

from pres import Deliverable
from ki import functions as ki_f

# pip3 install playsound==1.2.2
# pip3 install openai python-dotenv python-pptx



if __name__ == "__main__":

    try:

        config_list = []

        with open(f"{config.userfolder_path}config.py", "r") as file:
            lines = file.readlines()

        for line in lines:
            if "=" in line and "ki_request" in line:
                var_name = line.split("=")[0].strip()
                config_list.append(var_name)
                
        anzahl_eintraege = len(config_list)
        print(f"Die Anzahl der Einträge in der Liste beträgt: {anzahl_eintraege}")
        
        for config_variable in config_list:
            exec(f"{config_variable} = ki_f.initOpenAI(config.{config_variable})")

    finally: 
        
        print("KI done")
                
        report = Deliverable.OneSecondDeck(config.output_file, config.output_folder, config.input_file, config.input_folder)

    # SLIDE 1
    try:            
        slide = 1 # Titelfolie
        report.insertTextOnSlide(f"{config.workshop_ziel}", slide, "Titel 1")
        report.insertTextOnSlide(f"Mit dem Fokus auf {config.stichworte}", slide, "Untertitel 2") 
        
        report.insertImageOnSlide(f'https://images.unsplash.com/photo-1682917595484-41b62dc54320?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2487&q=80', slide, 'Titel 1', 1, 1, 3.3, 0.8)
        report.insertImageOnSlide(f'{config.img_folder}{config.title_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.title_fix == 1 else None
        
        report.writeNotes(f"Bildideen:\n{ki_request_002}", slide)

    finally: 
        print(f"#### Slide {slide} done ####")



    # SLIDE 2
    try: 
        slide = 2  # Verwendeter Master-Slide: Abschnittsüberschrift
        
        content = ki_request_003.splitlines()
        content = [element for element in content if element != '']
        content = [element for element in content if element != ':']
        content = [element for element in content if element != '.']
        content = [element for element in content if element != '.  ']

        print(content)

        report.insertTextOnSlide(f"PART I: {ki_request_004}", slide, "Titel 1")
        report.insertTextOnSlide(f"{content[0]}", slide, "Inhaltsplatzhalter 4")
        report.insertTextOnSlide(f"{content[1]}", slide, "Inhaltsplatzhalter 2")
        report.insertTextOnSlide(f"{content[2]}", slide, "Inhaltsplatzhalter 3")

        report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None
        report.writeNotes(f"Bildideen:\n{ki_request_002}", slide)

    finally: 
        print(f"#### Slide {slide} done ####")

    # SLIDE 3
    try: 
        slide = 3  # Verwendeter Master-Slide: Abschnittsüberschrift

        report.insertTextOnSlide(f"PART II: {ki_request_005}", slide, "Titel 1")
        report.insertTextOnSlide(f"{content[3]}", slide, "Inhaltsplatzhalter 4")
        report.insertTextOnSlide(f"{content[4]}", slide, "Inhaltsplatzhalter 2")
        report.insertTextOnSlide(f"{content[5]}", slide, "Inhaltsplatzhalter 3")

        report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None
        report.writeNotes(f"Bildideen:\n{ki_request_002}", slide)

    finally: 
        print(f"#### Slide {slide} done ####")

    report.createPres()
