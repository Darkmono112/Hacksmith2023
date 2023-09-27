# Low Level Design

### Screens - TODO: add the rest of the screens
- Home screen 
- Login/sign-up page it 
    - account details 
        - Passwords, points, history 
- Apply Tab ( Flyer applications at minimum) ( Can be the flyer tab)  ( for now mark off a checkbox to immediately become a flyer)
- Form for complaints and questions 
- Order screen with options 
    - payment ( Instant, no qualifying)
#### Overall Flowchart
![Overall Flowchart](md_images/Figma_Diagram.png)
#### Checkout Screen
![Checkout Screen](md_images/checkout_screen.png)
- Manager 
    - Inventory with editable values 
    - History???
#### Inventory Screen
![Inventory Screen](md_images/inventory_screen.jpg)
- Flyer 
    - Drone management ( Managers have access ) create new drone 
    - Order cue 
#### optional 
- About 
-   Track your order 

### Models 
**User Table**
- Email
- ID 
- Password
- User role (Consumer, Flyer, Admin)

**Price Table**
- Item  ( IE 1 scoop 2 scoop )
- Price 

**Order History Table**
( Max history size in testing)
- Keeps track of orders and users via foreign keys
- (Track 5 previous orders)
- Order number 
- User ID 
- Sale price 
- Drone ID

**Drone Table**
- Email or User ID 
- size 
- Drone ID
- Active status ( Like are you on vacation?)
- On order / in use or free 
- Orders carried / flight time  ( Compensation for our app )
- Max Battery / max mileage ( Ask about how we measure battery life )

**Inventory Table:**
- Inventory with 'type' column
- Item name 
- Amount 
- units ( stored as servings) 
- cost per unit (maybe )

### Templates 
- TODO psudocode (( the data and returns speciffically))

### Routes
- TODO psudocode

### CSS
 - TODO baseline (( fonts and colors and stuff))