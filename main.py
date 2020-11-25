import kivy
from DES_Edited import DES, bin2hex, hex2bin
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button


def tripleDES(pt, key1, key2, key3, encr):
    if encr:
        c1 = bin2hex(DES(pt, key1, encr)["cipher"])
        c2 = bin2hex(DES(c1, key2, not encr)["cipher"])
        c3 = bin2hex(DES(c2, key3, encr)["cipher"])
        return (c1, c2, c3)
    else:
        p3 = bin2hex(DES(pt, key3, encr)["cipher"])
        p2 = bin2hex(DES(p3, key2, not encr)["cipher"])
        p1 = bin2hex(DES(p2, key1, encr)["cipher"])
        return (p3, p2, p1)

def dict2string(round):
    s = ''
    s += "Plaintext: "+bin2hex(round["initialLeft"])+bin2hex(round["initialRight"])+'\n'
    s += "Key: "+round["key"]+'\n'
    s += "Expansion of R: "+bin2hex(round["expandedRight"])+'\n'
    s += "xOr Output: "+bin2hex(round["keyxOr"])+'\n'
    s += "s-box Output: "+bin2hex(round["sboxOut"])+'\n'
    s += "Permutation: "+bin2hex(round["finPerm"])+'\n'
    s += "Output of round: " + bin2hex(round["finOut"]) + '\n'
    return s


def verifyInput(text, key):
    # check if plaintext is 16 and hexadecimal
    try:
        int(text, 16) # check if can be considered hexadecimal
        if len(text) != 16:
            return (False, "Input Text should be 16 letters long")
    except:
        return (False, "Input Text should be hexadecimal")
    newText = ""
    # capitalize lowercase letters
    for i in range(len(text)):
        if text[i].islower():
            newText += text[i].capitalize()
        else:
            newText += text[i]
    # check if key is 16 and hexadecimal
    try:
        int(key, 16)  # check if can be considered hexadecimal
        if len(key) != 16:
            return (False, "Input Key should be 16 letters long")
    except:
        return (False, "Input Key should be hexadecimal")
    newKey = ""
    # capitalize lowercase letters
    for i in range(len(key)):
        if key[i].islower():
            newKey += key[i].capitalize()
        else:
            newKey += key[i]
    return (newText, newKey)


#Main Window:
class MainWindow(Screen):
    def info(self):
        t = 'Welcome to the DES Encryptor/Decryptor!' + '\n'+'\n' + 'For better graphics, please use full screen' + '\n' + 'Here you can encrypt or decrypt any hexadecimal text using the DES algorithim' + '\n' + 'You can see the output of each round with all the steps!' + '\n' + 'To achieve a higher level of security, please use our Triple DES Encryptor/Decryptor!' + '\n' + 'If your inputs are in binary, you can use our convertor to convert form binary to hexadecimal and vice versa'
        pop = Popup(title='Information', title_size = 30,
                    content=Label(text= t, font_size = 20, pos_hint = {"x":0.05, "top":0.97}),
                    size_hint=(None, None), size=(1000, 400))
        pop.open()
        return


#Encrypt Window:
class EncWindow(Screen):
    plaintext = ObjectProperty(None)
    key = ObjectProperty(None)
    def enc(self):
        pt, key = verifyInput(self.plaintext.text, self.key.text)
        print(pt, key)
        if pt==False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(pt , key, True)
        pop = Popup(title='Ciphertext',
                      content=Label(text =  'Ciphertext: ' + bin2hex(des["cipher"])),
                      size_hint=(None, None), size=(400, 400))
        pop.open()
        return des

    def round14(self):
        pt, key = verifyInput(self.plaintext.text, self.key.text)
        if pt == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(pt, key, True)
        print(des, bin2hex(des["InitialPermutation"]))
        t = "Initial Permutation: "+ bin2hex(des["InitialPermutation"])+'\n' + "Key after PC1: "+bin2hex(des["PermutedChoiceOne"]) + '\n' + '\n' + 'Round 1:' + '\n' + dict2string(des["round1"]) +'\n' + 'Round 2:' + '\n' + dict2string(des["round2"]) +'\n' + 'Round 3:' + '\n' + dict2string(des["round3"]) +'\n'+'Round 4:' + '\n' + dict2string(des["round4"])
        pop = Popup(title='Round 1 - 4',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def round58(self):
        pt, key = verifyInput(self.plaintext.text, self.key.text)
        if pt == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(pt, key, True)
        t = 'Round 5:' + '\n' + dict2string(des["round5"]) +'\n'+'\n' + 'Round 6:' + '\n' + dict2string(des["round6"]) +'\n'+'\n' + 'Round 7:' + '\n' + dict2string(des["round7"]) +'\n'+'\n' +'Round 8:' + '\n' + dict2string(des["round8"])
        pop = Popup(title='Round 5 - 8',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def round912(self):
        pt, key = verifyInput(self.plaintext.text, self.key.text)
        if pt == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(pt, key, True)
        t = 'Round 9:' + '\n' + dict2string(des["round9"]) +'\n'+'\n' + 'Round 10:' + '\n' + dict2string(des["round10"]) +'\n'+'\n' + 'Round 11:' + '\n' + dict2string(des["round11"]) +'\n'+'\n' +'Round 12:' + '\n' + dict2string(des["round12"])
        pop = Popup(title='Round 9 - 12',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def round1316(self):
        pt, key = verifyInput(self.plaintext.text, self.key.text)
        if pt == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(pt, key, True)
        t = 'Round 13:' + '\n' + dict2string(des["round13"]) +'\n'+'\n' + 'Round 14:' + '\n' + dict2string(des["round14"]) +'\n'+'\n' + 'Round 15:' + '\n' + dict2string(des["round15"]) +'\n'+'\n' +'Round 16:' + '\n' + dict2string(des["round16"])
        pop = Popup(title='Round 13 - 16',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def clear(self):
        self.plaintext.text = ""
        self.key.text = ""
        return

#Decrypt Window:
class DecWindow(Screen):
    ciphertext = ObjectProperty(None)
    key = ObjectProperty(None)
    def dec(self):
        ct, key = verifyInput(self.ciphertext.text, self.key.text)
        if ct == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(ct, key, False)
        pop = Popup(title='Plaintext',
                    content=Label(text='Plaintext: ' + bin2hex(des["cipher"])),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
        return des

    def round14(self):
        ct, key = verifyInput(self.ciphertext.text, self.key.text)
        if ct == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(ct, key, False)
        t = "Initial Permutation: "+ bin2hex(des["InitialPermutation"])+'\n' + "Key after PC1: "+bin2hex(des["PermutedChoiceOne"]) + '\n'  + '\n'  + 'Round 1:' + '\n' + dict2string(des["round1"]) +'\n' + 'Round 2:' + '\n' + dict2string(des["round2"]) +'\n' + 'Round 3:' + '\n' + dict2string(des["round3"]) +'\n'+'Round 4:' + '\n' + dict2string(des["round4"])
        pop = Popup(title='Round 1 - 4',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def round58(self):
        ct, key = verifyInput(self.ciphertext.text, self.key.text)
        if ct == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(ct, key, False)
        t = 'Round 5:' + '\n' + dict2string(des["round5"]) +'\n'+'\n' + 'Round 6:' + '\n' + dict2string(des["round6"]) +'\n'+'\n' + 'Round 7:' + '\n' + dict2string(des["round7"]) +'\n'+'\n' +'Round 8:' + '\n' + dict2string(des["round8"])
        pop = Popup(title='Round 5 - 8',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def round912(self):
        ct, key = verifyInput(self.ciphertext.text, self.key.text)
        if ct == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(ct, key, False)
        t = 'Round 9:' + '\n' + dict2string(des["round9"]) +'\n'+'\n' + 'Round 10:' + '\n' + dict2string(des["round10"]) +'\n'+'\n' + 'Round 11:' + '\n' + dict2string(des["round11"]) +'\n'+'\n' +'Round 12:' + '\n' + dict2string(des["round12"])
        pop = Popup(title='Round 9 - 12',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def round1316(self):
        ct, key = verifyInput(self.ciphertext.text, self.key.text)
        if ct == False:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + key),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return
        des = DES(ct, key, False)
        t = 'Round 13:' + '\n' + dict2string(des["round13"]) +'\n'+'\n' + 'Round 14:' + '\n' + dict2string(des["round14"]) +'\n'+'\n' + 'Round 15:' + '\n' + dict2string(des["round15"]) +'\n'+'\n' +'Round 16:' + '\n' + dict2string(des["round16"])
        pop = Popup(title='Round 13 - 16',
                      content=Label(text=t),
                      size_hint=(None, None), size=(600, 800))
        pop.open()

    def clear(self):
            self.ciphertext.text = ""
            self.key.text = ""
            return


class ConvertWindow(Screen):
    hexInput = ObjectProperty(None)
    binInput = ObjectProperty(None)
    def converter2bin(self):
        try:
            int(self.hexInput.text, 16) # check if can be considered hexadecimal
            newText =''
            for i in range(len(self.hexInput.text)):
                if self.hexInput.text[i].islower():
                    newText += self.hexInput.text[i].capitalize()
                else:
                    newText += self.hexInput.text[i]
            bin = hex2bin(newText)
            pop = Popup(title='Binary',
                         content=Label(text='Binary: ' + bin),
                         size_hint=(None, None), size=(600, 400))
            pop.open()
        except:
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: Input must be a hexadecimal'),
                        size_hint=(None, None), size=(400, 400))
            pop.open()

        self.hexInput.text = ""
        self.binInput.text = ""

    def converter2hex(self):
        try:

            int(self.binInput.text, 2) # check if can be considered hexadecimal
            c = len(self.binInput.text) % 4
            newText = ((4-c)%4)*'0' + self.binInput.text # take care of invalid number of bits
            print(newText)
            hex = bin2hex(newText)
            pop = Popup(title='Hexadecimal',
                         content=Label(text='Hexadecimal: ' + hex),
                         size_hint=(None, None), size=(600, 400))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: Input must be binary'),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
        self.binInput.text = ""
        self.hexInput.text = ""

class TripleDESWindow(Screen):
    des_text = ObjectProperty(None)
    key1 = ObjectProperty(None)
    key2 = ObjectProperty(None)
    key3 = ObjectProperty(None)
    def TripleDESencryption(self):
        ct1, key1 = verifyInput(self.des_text.text, self.key1.text)
        ct2, key2 = verifyInput(self.des_text.text, self.key2.text)
        ct3, key3 = verifyInput(self.des_text.text, self.key3.text)

        if not ct1 or not ct2 or not ct3:
            msg = key1 if not ct1 else key2 if not ct2 else key3
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + msg),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return

        cipher1, cipher2, cipher3 = tripleDES(ct1, key1, key2, key3, True)
        t = 'Encryption with Key1: '+str(cipher1)+'\n'+'\n'+ 'Decryption with Key2: '+str(cipher2)+'\n'+'\n'+ 'Result - Encryption with Key3: '+str(cipher3)
        pop = Popup(title='Results Triple DES Encryption',
                    content=Label(text= t),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
        self.des_text.text = ""
        self.key1.text = ""
        self.key2.text = ""
        self.key3.text = ""


    def TripleDESdecryption(self):
        pt1, key1 = verifyInput(self.des_text.text, self.key1.text)
        pt2, key2 = verifyInput(self.des_text.text, self.key2.text)
        pt3, key3 = verifyInput(self.des_text.text, self.key3.text)

        if not pt1 or not pt2 or not pt3:
            msg = key1 if not pt1 else key2 if not pt2 else key3
            pop = Popup(title='ERROR',
                        content=Label(text='ERROR: ' + msg),
                        size_hint=(None, None), size=(400, 400))
            pop.open()
            return

        text3, text2, text1 = tripleDES(pt1, key1, key2, key3, False)
        t = 'Decryption with Key3: ' + str(text3) + '\n' + '\n' + 'Encryption with Key2: ' + str(
            text2) + '\n' + '\n' + 'Result(Dec with Key1): ' + str(text1)
        pop = Popup(title='Results Triple DES Encryption',
                    content=Label(text=t),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
        self.des_text.text = ""
        self.key1.text = ""
        self.key2.text = ""
        self.key3.text = ""


#Window Manager
class WindowManager(ScreenManager):
    Window.size = (1280, 720)
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv




if __name__ == "__main__":
    MyApp().run()
