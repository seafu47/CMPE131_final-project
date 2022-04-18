
## Functional Requirements

1. Login - Xiyuan Zhou
2. Logout - Rommel Aquino Jr
3. Create Account - Jiaheng Fang
4. Delete Account - Jiaheng Fang
5. Search Items - Rommel Aquino Jr 
6. Post Items - Rommel Aquino Jr 
7. Delete Item - Xiyuan Zhou
8. Purchase/Bid on Item - Ahmet Mutlugun
9. User Profile - Xiyuan Zhou
10. Ratings - Ahmet Mutlugun
11. Add pictures - Jiaheng Fang
12. Sorting - Ahmet Mutlugun

## Non-functional Requirements

1. Chinese Language
2. Turkish Language
3. Dark Mode
4. Smooth interface

## Use Cases
1. Sell items
2. Post items
3. Delete items 
4. User profile
5. Adding pictures
6. Sorting

@Jiaheng
### 1. Sell Items
- Pre-condition: User must be logged into their account
- Trigger: User selects the "Sell item" button
- Primary Sequence:
    1. User log into their account
    2. Select "Sell item" button
    3. User enter description of item
    4. User select bid or sell at a fix price
    5. User enter bid price or item pirce
    6. Select confirm
- Primary Postconditions:The user must be registered and have a valid profile
- Alternate Sequence:
  1. User Enter the wrong price
     1. Have the option to confirm the price to see if the value exists. if the value is valid but customer enter the value by mistake have the delete button.
  
### 2. Post items

- **Pre-condition:** User must be logged into their account.

- **Trigger:** User selects the "Post Item" button

- **Primary Sequence:**
  
  1. User logs into their account
  2. Select "Post Item" button
  3. User imports image of item by clicking the image box
  4. User fills in the description box of the item
  5. User inputs the price of the item in the price box
  6. Submit post

- **Primary Postconditions:** The account of the user who posted the item must still exist and not be deleted.

- **Alternate Sequence:** 
  
  1. User logs into their account
  2. Select "Post Item" button
  3. User imports image of item by clicking the image box
  4. User fills in the description box of the item
  5. User inputs the price of the item in the price box
  6. Submit post
  7. If user leaves any input box empty, post won't be submitted
  8. User continues from where they left off to complete post
  9. Submit post

@xiyuanzhuo
### 3. Delete items
- **Pre-condition:** User(customer) need to login

- **Trigger:** User click the "Post Item" button then click "delete" button for specify one

- **Primary Sequence:**
  1. User(customer) login first
  2. User select and click "Post Item" button to view
  3. User look for the item to delete
  4. User(customer) choice and Click "delete" button
  5. User(customer) back to the main page

- **Primary Postconditions:** User delete items successfully for the chosen one and the rest of items still exist

- **Alternate Sequence:**
  1. User(customer) click the "delete" items button does not execute right away
     1. The system will pop up message to verify the user again, (Yes or No)
     
@xiyuanzhou
### 4. User profile
- **Pre-condition:** User(customer) has logged in

- **Trigger:** User click(select) "user's name" button first to see the "profile" button

- **Primary Sequence:**
  1. User(customer) has logged in first
  2. User need to select(click) user's name button show on the top
  3. User see the "profile" button then select
  4. System will show user's information
  5. User can select "edit" button 
  6. System shows edit options for information

- **Primary Postconditions:** User(customer) profile information successfully show or options ("edit successfully")

- **Alternate Sequence:**
  1. User(customer) profile should not show all the information
     1. The system will not show password
     2. The system will not show security information (if any security info)

- **Alternate Sequence:**
  1. User edit information
     1. System will pop up message verify each changing, (Yes or No)
     2. User needs select(click) "save" button to save changed

@Jiaheng
### 5. Adding Pictures
- **Pre-condition:** User must be logged in, and must be a seller

- **Trigger:** User click on "Add Image" button

- **Primary Sequence:**
  1. User(customer) has logged in first
  2. User need to click on adding picture option 
  3. User must select an image file type .jpg
  4. System will show confirmation text
  5. User can select "edit" button to resize picture
  6. User click on confirmation to add the picture.

- **Primary Postconditions:** User must be logged in, and must be selling an item or have a valid profile picture to upload.

- **Alternate Sequence:**
  1. User upload the wrong file type
     1. The system will prompt a message showing "Invalid File Type please upload a picture of .jpg type"
     2. System will check file type again to confirm 

- **Alternate Sequence:**
  1. User edit information
     1. System will pop up message verify each changing, (Yes or No)
     2. User needs select(click) "save" button to save changed
  
### 6. **Sorting** 
- **Pre-condition:** Sort listings by conditions.

- **Trigger:** Sorts the posted items in the main page by price, reviews and listing date. 

- **Primary Sequence:**
  
  1. Be in the main page
  2. Click the sort icon
  3. Pick sort option from "price", "date" or "reviews".

- **Primary Postconditions:** The items listed in the page will be ordered accordingly. 

- **Alternate Sequence:** Uncheck sorting
  
  1. Be in the main page
  2. Click the sort icon
  3. Click the selected sort again to undo the sorting.
