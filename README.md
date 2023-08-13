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

## Entry Configuration
The `Entry Month` is always set to previous month. `Entry Year` is set to always display current year, adjustments has been made to display previous year during the month of December (i.e. entry takes place on January)
### File naming
The details are automatically stored in an `.xlsx` file once `Submit` button is hit
