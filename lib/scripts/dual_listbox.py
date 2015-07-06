'''
Created on 31/01/2012

Dual listbox widget implementation (Gtk+3).

@author: Edorta Garcia
'''
# TODO
# Implement exceptions
# Use Gtk.SelectionMode.MULTIPLE

from gi.repository import Gtk


class DualListBox(Gtk.Box):
    def __init__(self, columnNameLeft=None, columnNameRight=None):
        ''''columnNameLeft' -> str (showed in the top of the left list)
        'columnNameRight' -> str (showed in the top of the right list)'''
        #Extend Gtk.Box
        Gtk.Box.__init__(self)

        #Assign values from received parameters
        self._columnNameLeft = columnNameLeft
        self._columnNameRight = columnNameRight

        #Set some properties
        self.set_property("orientation", Gtk.Orientation.HORIZONTAL)
        self.set_property("homogeneous", True)

        #CREATE BOTH MODELS AND VIEW NECCESARY FOR DUAL LIST
        #Create the models
        self._storeRight = Gtk.ListStore(str)
        self._storeLeft = Gtk.ListStore(str)

        #Create the views and associate it with proper models
        self._viewLeft = Gtk.TreeView(self._storeLeft)
        self._viewRight = Gtk.TreeView(self._storeRight)

        #Add proper columns to the views
        self._rendererTextLeft = Gtk.CellRendererText()
        self._rendererTextRight = Gtk.CellRendererText()
        self._columnLeft = Gtk.TreeViewColumn(self._columnNameLeft, self._rendererTextLeft, text=0)
        self._columnRight = Gtk.TreeViewColumn(self._columnNameRight, self._rendererTextRight, text=0)
        self._viewLeft.append_column(self._columnLeft)
        self._viewRight.append_column(self._columnRight)

        #Set TreeViewColumn 'alignment' property
        self._columnLeft.set_property("alignment", 0.5)
        self._columnRight.set_property("alignment", 0.5)

        #CREATE NEEDED BUTTONS
        #button to pass SELECTED ITEM FROM LEFT LIST TO RIGHT ONE
        self._buttonMoveRight = Gtk.Button()
        self._iconMoveRight = Gtk.Image()
        self._iconMoveRight.set_from_stock(Gtk.STOCK_GO_FORWARD, 1)
        self._buttonMoveRight.set_image(self._iconMoveRight)

        #button to pass SELECTED ITEM FROM RIGHT LIST TO LEFT ONE
        self._buttonMoveLeft = Gtk.Button()
        self._iconMoveLeft = Gtk.Image()
        self._iconMoveLeft.set_from_stock(Gtk.STOCK_GO_BACK, 1)
        self._buttonMoveLeft.set_image(self._iconMoveLeft)

        #button to pass ALL ITEMS FROM LEFT LIST TO RIGHT ONE
        self._buttonMoveAllRight = Gtk.Button()
        self._iconMoveAllRight = Gtk.Image()
        self._iconMoveAllRight.set_from_stock(Gtk.STOCK_GOTO_LAST, 1)
        self._buttonMoveAllRight.set_image(self._iconMoveAllRight)

        #button to pass ALL ITEMS FROM RIGHT LIST TO LEFT ONE
        self._buttonMoveAllLeft = Gtk.Button()
        self._iconMoveAllLeft = Gtk.Image()
        self._iconMoveAllLeft.set_from_stock(Gtk.STOCK_GOTO_FIRST, 1)
        self._buttonMoveAllLeft.set_image(self._iconMoveAllLeft)

        #Set button CONNECTORS
        self._buttonMoveAllLeft.connect("clicked", self._move_all_to, "left")
        self._buttonMoveAllRight.connect("clicked", self._move_all_to, "right")
        self._buttonMoveLeft.connect("clicked", self._move_to, "left")
        self._buttonMoveRight.connect("clicked", self._move_to, "right")

        #Create a box to contain buttons in proper way
        self._buttonBox = Gtk.VButtonBox()

        #Set some properties
        self._buttonBox.set_layout(5) #5 = center layout

        #Packing widgets
        self._buttonBox.add(self._buttonMoveRight)
        self._buttonBox.add(self._buttonMoveAllRight)
        self._buttonBox.add(Gtk.Separator()) #Adds also a nice separator
        self._buttonBox.add(self._buttonMoveLeft)
        self._buttonBox.add(self._buttonMoveAllLeft)

        #DO LIST SCROLLABLES
        #Create scrolledwindow
        self._scrollLeft = Gtk.ScrolledWindow()
        self._scrollRight = Gtk.ScrolledWindow()

        #Set AUTOMATIC POLICY for both scrolls vertical and horizontal
        self._scrollLeft.set_policy(1,1)
        self._scrollRight.set_policy(1,1)

        #Add view to proper scrolledwindow
        self._scrollLeft.add_with_viewport(self._viewLeft)
        self._scrollRight.add_with_viewport(self._viewRight)

        #Add lists and buttons in proper order
        self.add(self._scrollLeft)
        self.add(self._buttonBox)
        self.add(self._scrollRight)

    def _is_side_correct(self, side):
        '''Returns True if 'side' parameter is 'left' or 'right'.
        (str, no case sensitive)'''
        if side.lower() == "left" or side.lower() == "right":
            return True
        else:
            return False

    def _move_all_to(self, button, side):
        '''Move all items from original list to indicated one.
        'side' -> 'left' or 'right' (str, no case sensitive)'''
        if side == "left":
            tempIter = self._storeRight.get_iter_first()

            while tempIter != None:
                self.append_to("left",self._storeRight.get_value(tempIter,0))
                self._storeRight.remove(tempIter)
                tempIter = self._storeRight.get_iter_first()
        else:
            tempIter = self._storeLeft.get_iter_first()

            while tempIter != None:
                self.append_to("right",self._storeLeft.get_value(tempIter,0))
                self._storeLeft.remove(tempIter)
                tempIter = self._storeLeft.get_iter_first()

    def _move_to(self, button, side):
        '''Move selected item to the other list.
        'side' -> 'left' or 'right' (str, no case sensitive)'''
        if side == 'left':
            tempStore, tempIter = self._viewRight.get_selection().get_selected()

            if tempIter != None:
                self.append_to(side, tempStore.get_value(tempIter, 0))
                self._storeRight.remove(tempIter)
        else:
            tempStore, tempIter = self._viewLeft.get_selection().get_selected()

            if tempIter != None:
                self.append_to(side, tempStore.get_value(tempIter, 0))
                self._storeLeft.remove(tempIter)

    def append_to(self, side, item):
        '''Add item/s to one of the lists.
        'side' -> str ('left' or 'right' (no case sensitive))
        'item' -> list, tuple or str'''
        if self._is_side_correct(side):
            #TODO Check type(item) and handle exceptions

            #If 'side' is str type, convert it to list type,
            #since Gtk.ListStore.append() only admits list or tuples
            if type(item) == type(str()):
                tempList = list()
                tempList.append(item)
                item = tempList

                if side.lower() == "left":
                    self._storeLeft.append(item)
                else:
                    self._storeRight.append(item)

            elif type(item) == type(list()) or type(item) == type(tuple()):
                if side.lower() == "left":
                    for element in item:
                        tempList = list()
                        tempList.append(element)
                        element = tempList

                        self._storeLeft.append(element)
                else:
                    for element in item:
                        tempList = list()
                        tempList.append(element)
                        element = tempList

                        self._storeRight.append(element)
        else:
            pass #TODO handle exception

    def get_items_from(self, side):
        '''Returns a list that contains all items from indicated list.
        'side' -> 'left' or 'right' (str, no case sensitive)'''
        tempList = list()

        if self._is_side_correct(side):
            if side.lower() == "left":
                tempIter = self._storeLeft.get_iter_first()
                while tempIter != None:
                    tempList.append(self._storeLeft.get_value(tempIter,0))
                    tempIter = self._storeLeft.iter_next(tempIter)
            else:
                tempIter = self._storeRight.get_iter_first()
                while tempIter != None:
                    tempList.append(self._storeRight.get_value(tempIter,0))
                    tempIter = self._storeRight.iter_next(tempIter)

            return tempList
        else:
            pass #TODO handle exception

    def clear_list(self, side):
        '''Remove all items from indicated list.
        'side' -> str ('left' or 'right', no case sensitive)'''
        if self._is_side_correct(side):
            if side.lower() == "left":
                self._storeLeft.clear()
            else:
                self._storeRight.clear()
        else:
            pass #TODO handle exception

    def set_new_content_to(self, side, content):
        '''Clear indicated list and sets 'content' as the new items in list.
        'side' -> 'left' or 'right' (str, no case sensitive)
        'content' -> list, tuple or str'''
        if self._is_side_correct(side):
                self.clear_list(side)
                self.append_to(side, content)
        else:
            pass #TODO handle exception