import utils as utils
import configparser
import guifunctions as gfunc

class Requirments():

    def __init__(self):
        self.file = "options.properties"
        self.ffmpeg = "ffmpeg.exe"
        ## File configurazioni
        # Se non esiste il file di configurazione
        # ne crea uno nuovo 
        if not utils.isExistDir(self.file):
            with open(self.file,"w") as props:
                self.setDefaultOptions().write(props)
            

    def setDefaultOptions(self):
        config = configparser.ConfigParser()
        config['OPTIONS'] = {
            'language' : 'it',
            'theme' : 'light'
        }
        return config

    def setOption(self,option,value):
        config = configparser.ConfigParser()
        config.read(self.file)
        #Se non trova la sezione options
        if config.sections()[0] != "OPTIONS":
            print("File compromesso")
            self.errorRead()
            return
        try:
            config['OPTIONS'][option] = value
            with open(self.file,"w") as props:
                config.write(props)
        except:
            pass

    def getOption(self,option):
        config = configparser.ConfigParser()
        config.read(self.file)
        #Se non trova la sezione options
        if config.sections()[0] != "OPTIONS":
            print("File compromesso")
            self.errorRead()
            return
        try:
            return config['OPTIONS'][option]
        except:
            return None
            

    def errorRead(self):
        #Sovrascrive il file con le impostazioni di default
        with open(self.file,"w") as props:
            self.setDefaultOptions().write(props)
        return

    def checkFFmpeg(self):
        lang = self.getOption("language")
        #Se non esiste il file ffmpeg.exe
        if not utils.isExistDir(self.ffmpeg):
            gfunc.missingFFmpeg(lang)
            return False
        return True


