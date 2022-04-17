## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login
2. Logout
3. Create Account
4. Delete Account
5. Search Items
6. Post Items
7. Delete Item
8. Purchase/Bid on Item
9. User Profile
10. Ratings
11. Add pictures
12. Sorting

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


Use Case Description

Name: Sell Item

Summary: User who has logged in can sell item on the website

Actor(s): The customer and buyers

Trigger: Customer select "Post item" option




### 1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...
  
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

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
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
###4. User profile
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

- **Alternate Sequence <optional>:**
  1. User edit information
     1. System will pop up message verify each changing, (Yes or No)
     2. User needs select(click) "save" button to save changed

### 5. 5
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
