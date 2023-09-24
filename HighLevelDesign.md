# High Level Design

## Security Requirements
-- Note that not all these subgroups necessarily need to be addressed... also delete the question when addressing each subroup...
### Operating System
- How could a bad actor access interact with the operating system?
### Application
- How could a bad actor access interact with the application?
### Network
- How could a bad actor access interact with the network?
### Data
- How could a bad actor access interact with our data?
### Physical
- How could a bad actor access interact with the physical server?

## Target Platform
-- What is the target platform? Mobile phone, desktop, web?
## User Interface
-- At a basic level, what will the user interface look like?

### Screens
- Home screen 
- Login/sign-up page it 
    - account details 
        - Passwords, points, history 
- Apply Tab ( Flyer applications at minimum) ( Can be the flyer tab)  ( for now mark off a checkbox to immediately become a flyer)
- Form for complaints and questions 
- Order screen with options 
    - payment ( Instant, no qualifying)
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

## Programming Language/Framework
-- What programming language should we use? What libraries should we use? 
**Server Side:**
--Django
**UI Side:**
--Vue
--Javascript
--HTML
--CSS
## Data Architecture
-- What architecture should we use? 
- Monolithic,
- Client/Server,
- Component-Based,
- Service-Oriented, 
- Data-Centric,
- Event-Driven,
- Rule-Based,
- Distributed
## Database Tables:



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




[Definitions Here](https://gitlab.cs.usu.edu/erik.falor/fa23-cs3450-lecturenotes/-/tree/master/Module2/Lec09-Mon_Sep_18?ref_type=heads)
## 3rd Party Interfaces
-- What other interfaces should we use? (This might fit under the umbrella of programming language/framework)
- Google Maps API
