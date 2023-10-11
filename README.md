# Dynamic stock sheet

This project makes it possible to take various information about actions and add them to a spreadsheet, it is also extremely flexible where you can use different information and in variable ways.

Dependencies:
- yfinance:
- - Version: 0.2.30
- pandas:
- - Version: 2.1.1

# Features
 It has basic functions such as reading a spreadsheet in .xlsx format with a specific structure and complete/updating the information in the columns referring to the actions.

# Modifications
If you want to add a function to get some information, follow these steps:
1. Add the function to the collector.py file.
2. Go to the organizer.py file and import the function you want to add.
3. In the same file, look for the update_columns_datatype function and in the dictionary called columns_datatype add the name of the column to which it will be filled with the information and its type. Ex: columns_datatypes={"name":type, "Price":float}
4. Staying in the same file, search for the function update_action and in the dictionary connector connect the name of the column with the function that gets the information. Ex: connector={"column_name":function, "Book value":get_book_value}
5. Save the modifications and the code is ready to run again. :)

