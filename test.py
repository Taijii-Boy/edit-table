def save_configuration(date_to_save):
        with open("config.ini", mode = "w") as config:
        	config_content = config.write(date_to_save)

def load_configuration():
    with open("config.ini", mode = "r") as config:
        config_content = config.read()
        print(config_content)

save_configuration("Адын адын")
load_configuration()