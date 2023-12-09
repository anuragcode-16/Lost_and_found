# Lost and Found Application

This is a simple Lost and Found desktop application built with Python and Tkinter. It allows you to keep track of lost and found items, search for items, and mark items as found when they are returned.

## Overview

The application has two listboxes to display lost and found items separately. Users can add new lost items which get added to the database (CSV file) and displayed in the lost items listbox. When an item is returned, it can be marked as found, which moves it from the lost to the found list.

The main features include:

- Add new lost items 
- Mark items as found when returned
- Search for items 
- Clear lost items list 
- Clear found items list
- Display items in separate Lost and Found listboxes
- Save data to a CSV file

## Code Overview

The application is built using:

- **Tkinter** for the graphical user interface
- **CSV file** for storing the item data

The main class is `LostAndFoundApp` which handles initializing the GUI, CSV file, and button functions to add/edit items.

Key methods include:

- `add_lost_item()` - Add new lost item entries 
- `mark_item_as_found()` - Move item from lost to found
- `search_items()` - Search for items based on name  
- `clear_lost_items()` - Clear all lost items
- `refresh_lists()` - Refresh the listbox displays

Validation is implemented where applicable, e.g. checking for duplicate items or missing fields.

## Usage

To run the app:

```
python lost_and_found.py
```

The GUI provides an intuitive interface to:

- Enter item, owner, contact details
- Choose actions like Add Lost Item, Mark As Found, Search
- View Lost and Found item listboxes
- Clear or refresh item lists as needed

The data is saved to `lost_and_found.csv` file, which serves as the database.

Let me know if you have any other questions!
