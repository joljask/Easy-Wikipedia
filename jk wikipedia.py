from tkinter import *
import wikipedia

jkwiki = Tk()

def wikisearch():
    tvalue = txtsearch.get()
    displaydetail.delete(1.0,END)
    try:
        detail_value = wikipedia.summary(tvalue)
        displaydetail.insert(INSERT,detail_value)
    except:
        displaydetail.insert(INSERT, "MotherFucker check your internet connection or input correct keyword ")


def wikisuggest(*args):
    tvalue = txtsearch.get()
    suggest_value = wikipedia.suggest(tvalue)
    displaydetail.delete(1.0, END)
    displaydetail.insert(INSERT,suggest_value)


 #top frame    
topframe = Frame(jkwiki, width = 400, height = 100, background = "powder blue" )
txtsearch = Entry(topframe)
txtsearch.focus()
txtsearch.pack(side = LEFT, padx = 10, pady = 5,fill = X)

txtsearch.bind('<Return>', wikisearch)




btnsearch = Button(topframe, text = "SEARCH", command = wikisearch)

btnsearch.pack(side = LEFT)


topframe.pack(side = TOP, fill = BOTH)



#middle frame
middleframe = Frame(jkwiki, bg = "cyan")
display_suggest = Text(middleframe, width = 15, height = 1)
display_suggest.pack(side = LEFT,padx = 10, pady = 5,fill = X)
display_suggest.config(state=DISABLED)





btnsuggest = Button(middleframe, text = "SUGGEST", command = wikisuggest)
btnsuggest.pack(side = LEFT)

middleframe.pack(side =TOP,fill = BOTH)




#bottom frame

bottomframe = Frame(jkwiki, padx = 20, pady = 10)
lblinfo = Label(bottomframe, text = "WIKI INFORMATION", bg = "#60aeb5") 
lblinfo.pack(side = TOP)

scrolldetail  = Scrollbar(bottomframe)
scrolldetail.pack(side = RIGHT, fill = Y)

displaydetail = Text(bottomframe, width = 250, yscrollcommand = scrolldetail.set, wrap = WORD)
displaydetail.pack()

scrolldetail.config(command = displaydetail.yview)
bottomframe.pack()




jkwiki.geometry("400x600+500+100")
jkwiki.mainloop()