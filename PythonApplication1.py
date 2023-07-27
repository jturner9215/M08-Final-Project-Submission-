import PySimpleGUI as sg




sg.theme('HotDogStand')
inventory = []

#for creating a card
class card:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def cardInfo(self):
        print("Card name: " + self.name + "\nColor: " + self.color + "\nPrice: " + self.price)



############################################## FUNCTIONS #############################################

#for seaching cards by name
def findCardName(name, list):
    
    inventory = list
    x = name
    counter = 0
    y = card(x, '', 0)
    

    for y in inventory:
        if y.name == x:
            counter += 1
            print("\n" + str(counter) + ".\nName: " + y.name + "\nColor: " + y.color + "\nPrice: $" + str(y.price))


    #print("\n" + str(counter) + " cards found.")

    text = "\n" + str(counter) + " cards found."

    return text










#for searching cards by color

def findCardColor(color, list):

    inventory = list
    x = color
    counter = 0
    y = card('', x, 0)

    for y in inventory:
        if y.color == x:
            counter += 1
            print("\n" + str(counter) + ".\nName: " + y.name + "\nColor: " + y.color + "\nPrice: $" + str(y.price))

    #print("\n" + str(counter) + " cards found.")

    text = "\n" + str(counter) + " cards found."

    return text








#for searching cards by price

def findCardPrice(price, list):

    inventory = list
    x = price
    counter = 0
    y = card('', '', x)
    

    for y in inventory:
        if y.price == x:
            counter += 1
         
            print("\n" + str(counter) + ".\nName: " + y.name + "\nColor: " + y.color + "\nPrice: $" + str(y.price))


    text = "\n" + str(counter) + " cards found."

    return text








#### CREATE A FUNCTION FOR SELLING CARDS


def findToSell(name, color, list):

    inventory = list
    x = name
    y = color
    counter = 1
    index = 0
    test = ''

    z = card(x, y, 0)

    while counter != 0:
        
        test = inventory[index]

        if (test.name == z.name) & (test.color == z.color):
            counter -= 1
            inventory.pop(index)
            
            return 1

        else:

            index += 1

            if (index >= len(inventory)):
                
                return 0
            


############################# LAYOUTS ########################################





#main window
def layout():

    layout = [
    
            [sg.Button('View cards'), sg.Button('Enter new card'), sg.Button('Sell card')]
    
    ]

    return layout



#View cards window - main
def layout2():

    layout2 = [
        
            [sg.Button('Search by name'), sg.Button('Search by color'), sg.Button('Back')]
    
    ]

    return layout2




#Search by name window
def  layout5():

    layout5 = [
    
                [sg.InputText()],
                [sg.Button('Search'), sg.Button('Back')]
    
    ]

    return layout5



#Search by color window
def layout6():

    layout6 = [
    
                [sg.InputText()],
                [sg.Button('Search'), sg.Button('Back')]
    
    ]
    return layout6



#Search by price window
"""def layout7():

    layout7 = [
    
                [sg.Text('$'), sg.InputText()],
                [sg.Button('Search'), sg.Button('Back')]
    
    ]
    return layout7"""





#enter cards window
def layout3():
    layout3 = [
    
            [sg.Text('Name: '), sg.InputText()],
            [sg.Text('Color: '), sg.InputText()],
            [sg.Text('Price: $'), sg.InputText()],
            [sg.Button('Enter'), sg.Button('Back')]
    
    ]
    return layout3




#sell cards window
def layout4():
    layout4 = [
    
            [sg.Text('Name: '), sg.InputText()],
            [sg.Text('Color: '), sg.InputText()],
            [sg.Button('Enter'), sg.Button('Back')]
    
    ]
    return layout4


#success
def layoutTest():
    layoutTest = [
    
                [sg.Text('Success')],
                [sg.Button('Okay')]
    
    ]
    return layoutTest




#error selling
def layoutTest2():
    layoutTest2 = [
    
                [sg.Text('Error. No card of this type to sell')],
                [sg.Button('Okay')]
    
    ]
    return layoutTest2




###### ADD RECURSIVE FUNCTIONS SO THAT APP CAN BE USED UNTIL USER EXITS ###################################

#function for main window
def mainWindow():

    window = sg.Window('Valkyries Vault', layout())

    event, values = window.Read()


    if event == 'View cards':

        window.close() 

        viewCards() #done


    if event == 'Enter new card':

        window.close()

        enterCards() #done



    if event == 'Sell card':

        window.close()

        sellCards() #done





#function for viewing cards - cancel, name, color, price

def viewCards():

    window = sg.Window('Find cards', layout2())

    event, values = window.Read()


    if event == 'Search by name':

        window.close()

        nameSearch() #done


    if event == 'Search by color':

        window.close()

        colorSearch() #done


    """if event == 'Search by price':

        window.close()

        priceSearch() #done"""


    if event == 'Back':

        window.close()

        mainWindow()



"""#function within card search to look up by price
def priceSearch():

    window = sg.Window('Enter price', layout7())

    event, values = window.read()

    price = values[0]

    text = findCardPrice(price, inventory)

    sg.popup(text)

    window.close()

    viewCards()
"""


#function within card search to look up by color
def colorSearch():

    window = sg.Window('Enter color', layout6())

    event, values = window.read()

    color = values[0]

    text = findCardColor(color, inventory)

    sg.popup(text)

    window.close()

    viewCards()




#function within card search to look up by name
def nameSearch():

    window = sg.Window('Enter name', layout5())

    event, values = window.read()

    name = values[0]

    text = findCardName(name, inventory)

    sg.popup(text)

    window.close()

    viewCards()


#function for entering cards - enter name & color & price || back - append to list || back


def enterCards():

    window = sg.Window('Entering new card', layout3())

    event, values = window.Read()


    if event == 'Enter':

        window.close()

        name = values[0]
        color = values[1]
        price = values[2]

        cardEnter = card(name, color, price)

        inventory.append(cardEnter)

        sg.popup('Success')

        #window.close()

        enterCards()


    if event == 'Back':

        window.close()

        mainWindow()



def sellCards():

    window = sg.Window('Lookup card', layout4())

    event, values = window.Read()


    if event == 'Enter':

        name = values[0]
        color = values[1]

        result = findToSell(name, color, inventory)

        if result == 1:

            window.close()

            window = sg.Window('Success', layoutTest())
            
            event, values = window.Read()

            if event == 'Okay':

                window.close()

                sellCards()

            else:

                window.close()

                sellCards()

        if result == 0:

            window.close()

            window = sg.Window('Failure', layoutTest2())
            
            event, values = window.Read()

            if event == 'Okay':

                window.close()

                sellCards()

            else:

                window.close()

                sellCards()



    if event == 'Back':

        window.close()

        mainWindow()












#############################################################################################################


card1 = card('Magic', 'Blue', 1.91)
card2 = card('Butterfly', 'Green', 3.64)
card3 = card('Magic', 'Green', 1.99)
card4 = card('Pop', 'Red', 1.76)
card5 = card('Marley', 'White', 100)
card6 = card('Dragon', 'White', 2)
card7 = card('Elf', 'Green', 0.30)
card8 = card('Dwarf', 'Black', 0.99)
card9 = card('Wyvern', 'Green', 0.50)
card10= card('Centaur', 'Blue', 1.00)
card11= card('Blob', 'Black', 0.12)
card12= card('Farm', 'Red', 0.01)
card13= card('Hills', 'Blue', 0.01)
card14= card('Fighter','Red', 0.46)
card15= card('Mage','Black', 1.50)




inventory.append(card1)
inventory.append(card2)
inventory.append(card3)
inventory.append(card4)
inventory.append(card5)
inventory.append(card6)
inventory.append(card7)
inventory.append(card8)
inventory.append(card9)
inventory.append(card10)
inventory.append(card11)
inventory.append(card12)
inventory.append(card13)
inventory.append(card14)
inventory.append(card15)






#showtime, baby

mainWindow()



