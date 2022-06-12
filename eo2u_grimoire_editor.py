import eel

from save_file_manager import SaveFileManager

@eel.expose
def get_random_number():
    eel.prompt_alerts(7)

@eel.expose
def get_date():
    eel.prompt_alerts(SFM.current_time())


if __name__ == "__main__":
    SFM = SaveFileManager()

    eel.init('web')
    eel.start('index.html')