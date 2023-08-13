# fullsafe
Windows application that makes it easy to record and maintain buisness's purchase receipts by automatically filling Seller Name, Address with `requests` and auto-displaying Tax Amount and Total with Sub Total Value.

|  Dark Mode | Light Mode  |
| ------------ | ------------ |
|   ![image](https://github.com/hariprasath112/fullsafe/assets/96934076/948c553c-549b-492a-9dcb-1a1dd52761ed) |![image](https://github.com/hariprasath112/fullsafe/assets/96934076/9ff2b0a1-4fd9-430c-bd61-63d97ff337c0)  |

## Getting Started
To dowload the latest version go to the[ releases page](https://github.com/hariprasath112/fullsafe/releases " releases page") or [click here to download windows installer](https://github.com/hariprasath112/fullsafe/releases/download/v2.1/fullsafeSetup.exe "click here to download windows installer") for the latest version. 

The release are built for Windows operating system. For MacOS/Linux you can try running the python script in [/src/main.py](https://github.com/hariprasath112/fullsafe/blob/main/src/main.py "/src/main.py")

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
The program allows clicking `Enter` key to jump to the next value, this also has the feature of triggering the functions associated with them. The default chain of navigation through `Enter` Key where each `-->` denotes a click of `Enter` key

`Invoice Date` --> `Invoice Date` --> `GST No.` --> Generates Seller Name and Address from GST No. and autofills --> `Product Name` --> `HSN` --> `Sub Total` --> Generates Tax value and Total Value --> `Total` --> `Submit` --> Adds to Spreadsheet and clear all Fields --> `Invoice Date`

Just like using Microsoft Excel you can navigate the entire software with `Enter` keys, thus saving time that is consumed with mannual navigation using a mouse.

## Entry Configuration
The `Entry Month` is always set to previous month. `Entry Year` is set to always display current year, adjustments has been made to display previous year during the month of December (i.e. entry takes place on January)
### File naming
The details are automatically stored in an `.xlsx` file once `Submit` button is hit. The file is stored in the location `E:\fullsafe\{year}\{month}` and the file name is in the format `Purchase_{month}{year}.xlsx`. The `Month` and `year` is determined from the values of `Entry Month` and `Entry Year`.
### Accessing File
The `File` item in the menubar can be clicked to open the file immediately.

## Invoice Details
### Invoice Number
Invoice number can be of any alphanumberical character. 
