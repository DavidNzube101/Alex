import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import json
from ttkthemes import ThemedStyle


def ComboApp():
    from tkinter.font import Font
    comboWin = tk.Tk()
    comboWin.title("Combo - Bivid")
    comboWin.resizable(width=False, height=False)
    alexIcon = ("data\\alexlibs\\MEDIA\\alex-icon-new.ico")
    comboWin.iconbitmap(alexIcon)
    style = ThemedStyle(comboWin)
    style.set_theme("arc")

    def openAndSave():
        def saveCombo():
            with open("BDFILES\\combolist.bd", "a") as combofile:
                combofile.write("\n" + listLabel)

            a_c_n = str(app_combo_name.get())
            appDict = ("," + f'"{a_c_n}"' + ":" + (f'"{listLabel}"' + ",\n"))
            # jsonString = json.dumps(appDict)
            jsonFileR = open("BDFILES\\comboApps.json", "r")
            fileContent = jsonFileR.read()
            jsonFileW = open("BDFILES\\comboApps.json", "w")
            jsonFileW.write(fileContent.replace("}", ""))
            jsonFileW.close()
            jsonFileR.close()

            jsonFile = open("BDFILES\\comboApps.json", "a")

            toWrite = ((appDict.replace("{", "")).replace("}", "")).replace("\\", "\\\\")

            jsonFile.write(toWrite)
            jsonFile.close()

            tk.Label(comboWin, text="Saved as " + str(app_combo_name.get()) + "!", fg="green").pack()

            jsonFileR2 = open("BDFILES\\comboApps.json", "r")
            fileContent2 = jsonFileR2.read()
            jsonFileW2 = open("BDFILES\\comboApps.json", "w")
            jsonFileW2.write(fileContent2.replace(",\n", "}"))
            jsonFileW2.close()
            jsonFileR2.close()

        lists = filedialog.askopenfilenames(filetypes=[("Executables", "*.exe")])
        q = (str(lists))
        w = q.replace("('", "")
        w1 = w.replace('("', '')
        e = w.replace("', '", " ")
        e1 = e.replace('", "', ' ')
        r = e.replace("')", "")
        r1 = r.replace('")', '')
        j = r1.replace("/", "\\")
        listLabel = j.replace(".exe ", ".exe\n")
        # listLabel = lists.replace(" ", "\n")
        print(listLabel)
        listofapps.config(text=f"Apps to add to combo:\n\n{listLabel}")
        # listofapps.pack(pady=30)

        butt1.config(text=("Save Combo"), width=40, command=saveCombo)
        # butt2.pack(pady=30)


    tk.Label(comboWin, text="Combo allows you to open multiple apps just with a single click.\nSelect the apps you would wish to open from the future dialog,\nthen save it with name you'll use to reference it later.\nThat's all, easy peazy.", font=("Roboto", 10)).pack(pady=30)
    
    # engine.say(("Combo allows you to open multiple apps just with a single click. Select the apps you would wish to open from the future dialog, then save it with name you'll use to reference it later. That's all, easy peazy."))
    # engine.runAndWait()


    app_combo_name = ttk.Entry(comboWin, width=40)
    app_combo_name.insert(0, "My app combo")
    app_combo_name.pack(pady=30)

    listofapps = tk.Label(comboWin, text="Apps to add to combo:\n\n(None selected)")
    listofapps.pack(pady=30)

    boostOpen = ttk.Checkbutton(comboWin, text="Enable BoostOpen to open apps faster")
    boostOpen.pack(pady=20)

    butt1 = ttk.Button(comboWin, text="Open App(s)", width=40, command=openAndSave)
    butt1.pack(pady=30)

    comboWin.mainloop()

# ComboApp()