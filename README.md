# fullsafe
Windows application that makes it easy to record and maintain buisness's purchase receipts by automatically filling Seller Name, Address with `requests` and auto-displaying Tax Amount and Total with Sub Total Value.

<p align="center">
  <img alt="Light" src="https://github.com/hariprasath112/fullsafe/assets/96934076/5b708b26-1dfd-475a-9f7b-1b5c31e12698" width=50%" />
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Dark", src="https://github.com/hariprasath112/fullsafe/assets/96934076/d518f7e3-cfa4-442b-aa85-6ed14e9d117f" width=30% /> 
</p>

The above GIFs illustrate how the search and entry process is simplified. The Name and Address is got using `HTTP` `GET` and parsed with `BeautifulSoup4` then displayed in a windows built with `Tkinter` and saved as a spreadsheet using `openpyxl`.


<br></br>


|  Dark Mode | Light Mode  |
| ------------ | ------------ |
|   ![image](https://github.com/hariprasath112/fullsafe/assets/96934076/948c553c-549b-492a-9dcb-1a1dd52761ed) |![image](https://github.com/hariprasath112/fullsafe/assets/96934076/9ff2b0a1-4fd9-430c-bd61-63d97ff337c0)  |

## Getting Started
To dowload the latest version go to the[ releases page](https://github.com/hariprasath112/fullsafe/releases " releases page") or [click here to download windows installer](https://github.com/hariprasath112/fullsafe/releases/download/v2.1/fullsafeSetup.exe "click here to download windows installer") for the latest version. 

The releases are built for Windows operating system. For MacOS/Linux you can try running the python script in [/src/main.py](https://github.com/hariprasath112/fullsafe/blob/main/src/main.py "/src/main.py")

## Documentation
### Menu bar
| Menu Item  | Function  |
| ------------ | ------------ |
| `File`  | Open the Excel file that is currently being used. Current file is determined by `Entry Month` and `Entry Year` under the `Entry Configuration`  tab. If no entries were made for that particular month then error message pops up.
|  `Options` | Clicking this opens a message box to change Organization name  |
| `Font`  | Changes the font size of the windows (either small or large)  |
| `View`  | Change the color them of the window  |
| `Help`  | Opens this Github repository page  |

## Navigation in the application
The program allows clicking `Enter` key to jump to the next value, this also has the feature of triggering the functions associated with them. The default chain of navigation through `Enter` Key where each `-->` denotes a click of `Enter` key is given below

`Invoice Date` --> `Invoice Date` --> `GST No.` --> Generates Seller Name and Address from GST No. and autofills --> `Product Name` --> `HSN` --> `Sub Total` --> Generates Tax value and Total Value --> `Total` --> `Submit` --> Adds to Spreadsheet and clears all Fields --> `Invoice Date`

Just like using Microsoft Excel you can navigate the entire software with `Enter` key, thus saving time that is consumed with mannual navigation using a mouse.

## Entry Configuration
The `Entry Month` is always set to previous month. `Entry Year` is set to always display the current year, adjustments has been made to display previous year during the month of December (i.e. entry takes place on January).
### File naming
The details are automatically stored in an `.xlsx` file once `Submit` button is hit. The file is stored in the location `E:\fullsafe\{year}\{month}` and the file name is in the format `Purchase_{month}{year}.xlsx`. The `Month` and `year` is determined from the values of `Entry Month` and `Entry Year`.
### Accessing File
The `File` item in the menubar can be clicked to open the file immediately.

## Input Specifications
Inputs having special feature are listed below. Rest of the inputs are self-explanatory and hence omitted from long explanations. `Invoice Date` supports both alphanumerical characters.
### Invoice Date
Using `Enter` key navigation you can reach the box quickly, but unlike other input boxes this has a builtin calendar. Click the `V` to open the calendar and pick the date.

![image](https://github.com/hariprasath112/fullsafe/assets/96934076/2c2d139a-be2c-4a44-90a3-720c8e30ae99)

### GSTIN No
The `✔` button  can be used to request data to be filled, but with pressing `Enter` the process is automated and your cursor jumps to `Product Name`.
### Sub Total
After entering the subtotal, when you click `Enter` key the `Tax Amount` and `Total` are generated and the cursor jumps to `Total`. 
### Submit button
After confirming the `Total` value you can press `Enter` again, which leads you to the `Submit` button. The data will be uploaded only after you press `Enter` a second time. After that click, the data is added to Excel file and all columns are erased.
#### Submit & Reuse Button
This button does the same upload function as the `Submit` button but excludes clearing the `GST No`, `Business Name` and `Business Address` fields. It is suited for entering multiple receipts from the same seller. It has to be manually clicked before the second `Enter` click when the `Submit` button is highlighted, preferably right after the `Total` is generated.
#### Clear button
This clears all values. Only default values like `Entry Month`, `Entry Year` and `Invoice Date` remains.

## Changing Preferences
### Name of User's Organization
Click `Options`, a message box with a text field pops up. Enter your Organization name and click `OK`. To exit without changing click `Cancel`. Once changed the Organization name is updated only to the current Excel file and then saved for future use.

![image)](https://github.com/hariprasath112/fullsafe/assets/96934076/68ee1dc1-baac-4e5b-a28f-525af3b8ee77)

### Change font size of the application
By default, there is two font size groups - Large and Small. Click `Font` to trigger change. Note that the change from Small to Large is immediate but changing from Large to Small triggers a auto-restart of the app. Your size preference is saved permanently for the app to load next time.

| Dark mode  | Light mode  |
| ------------ | ------------ |
| ![image](https://github.com/hariprasath112/fullsafe/assets/96934076/686048d2-21f8-44eb-be23-82d07249b38e)  | ![image](https://github.com/hariprasath112/fullsafe/assets/96934076/f7418a9e-a547-46cb-910f-d067a7524c90)  |

### Changing theme of the application
Click `View` to trigger theme reversal. This causes the application to restart with desired theme. A error message also warns loss of current data, data submitted earlier is saved. 

## Tax Customizations
#### Additional
This text field's value is directly added to `Sub Total` although it may not reflect on the app input box, the `Tax Amount` and `Total` shows correct values. The sub total in the Excel file is a sum of `Additional` and `Sub Total` inputs. This can be utilized to include delivery/handling charges that are cometimes not mentioneted correctly by some sellers.

#### Tax Type Selection
There is an option to choose between `IGST` and `CGST\SGST` tax types. While either one is selected the other one is empty in the generated spreadsheet.

#### Tax Percentage Selection
You can choose between a range of values for the tax percentage. Note that the tax rate shown is the cummulative of CGST and SGST or the entire rate of IGST.

![image](https://github.com/hariprasath112/fullsafe/assets/96934076/90058969-e5fa-4c42-af23-e612f02ce7cf)

## Required Packages (for running main.py)
Python 3.11.4 was used in building this software. The libraries used are `tkinter`, `sv_ttk`, `ctypes`, `datetype`, `tkcalendar`, `openpyxl`, `os`, `sys`, `ntkutils`, `bs4` and `webbrowser`. Much of the feautures are tailored to Windows operating system. Hence, it is unlikely that the `main.py` is functional in other operating systems.

## Contributing
Any suggestions you make are greatly appreciated.

- If you have suggestions , feel free to [open an issue](https://github.com/hariprasath112/fullsafe/issues/new) to discuss it, or directly create a pull request after you edit the _main.py_ file with necessary changes.
- Create individual pull request for each suggestion.

## License

Distributed under License based off of MIT Lience. See [LICENSE](https://github.com/hariprasath112/fullsafe/blob/LICENSE) for more information.

### Author

**Hariprasath Senthil kumar**  - [LinkedIn](https://linkedin.com/in/hariprasath11) 
