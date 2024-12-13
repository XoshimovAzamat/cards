import json
import os.path


def create_data(data:None, file_name:str, status:str):
    with open(f"{file_name}", f"{status}") as file:
        if status == "w":
           json.dump(data, file, indent=4)
           return "Qo`shildi."
        else:
            if os.path.exists(f"{file_name}"):
                try:
                    s = json.load(file)
                    return s
                except:
                    return "\nMa`lumot topilmadi."