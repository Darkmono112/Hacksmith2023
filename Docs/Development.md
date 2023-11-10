# Development Phase 1

## Security
This section is to make up for documention backlog from previous sprints.

The majority of security concerns will be handled by the Django Framework, but we as developers will 
always be looking for more ways to increase security of thr application. Throughout this sprint, we have collectively
been working on keeping security tight and looking for potential holes.

### Database
Like with any application, the data this program will store it it's database is very important and needs to be protected.
As developers, we must take steps to ensure that our users data and our data is safe.
We will do this by correctly storing sensitive information within our database, 
as well as correctly storing keys and tokens that our application will use to interact with other services. 
We will do this by utilizing Djangos built in Hashing features and environment variable storage systems. 

### HTML Forms
HTML forms are a fundamental part of web development, enabling user interaction and data submission. 
However, they also introduce various security risks that developers need to be aware of to ensure the safety of their applications.

#### 1. **Cross-Site Scripting (XSS):**

   HTML forms are susceptible to XSS attacks when user input is not properly validated or sanitized. 
   Malicious scripts can be injected into form fields, and if not properly handled on the server side, 
   these scripts can be executed in the context of other users' browsers, leading to data theft or unauthorized actions.

#### 2. **Cross-Site Request Forgery (CSRF):**

   CSRF attacks occur when a malicious site tricks a user's browser into making unintended requests to a different site where the user is authenticated.
   If forms lack adequate anti-CSRF tokens, attackers can submit malicious requests on behalf of authenticated users, leading to unauthorized actions.
   This should be adequately handled by Django, but deserves further testing. 

#### 3. **Injection Attacks:**

   Poorly validated or sanitized input can result in injection attacks. 
   For example, SQL injection can occur if user input is directly incorporated into database queries, leading to unauthorized access or data manipulation.
   This could be a huge issue if someone were to access the admin panel, where the inventory can be manipulated via input from the user. 

#### 4. **Data Validation and Sanitization:**

   Inadequate validation and sanitization of form data can open doors to various security issues. 
   Developers should validate input on both the client and server sides to prevent malicious data from reaching the application.

#### 5. **File Upload Vulnerabilities:**

   File upload forms are particularly susceptible to security risks. Without proper validation and restrictions,
   attackers might upload malicious files, leading to potential security breaches or the execution of harmful scripts on the server.
   This could be an issue if we allow the admin to submit image files for new inventory items, such as a new ice cream flavor. 

#### 6. **Insecure Transmission:**

   If form data is transmitted over insecure channels (HTTP instead of HTTPS), it can be intercepted and manipulated by attackers, 
   compromising sensitive information such as login credentials or personal data. We need to make sure that all traffic is handled
   through HTTPS.

#### 7. **Client-Side Security:**

   Relying solely on client-side validation is risky, as malicious users can manipulate or bypass it. 
   This will be tested heavily during the Testing and Debugging phase. 

#### 8. **Sensitive Information Exposure:**

   Inappropriately handling sensitive information in forms, such as passwords or personal details, can lead to data leaks. 
   We need to make sure that passwords, emails, and addresses are stored securely without access from the front-end.

## Work Distribution:
Below is a summary of work distribution according to group member. 

* Porter Ellis:
  - Finished FAQ/Contact page css, which allows a user to submit a help request
  - Finished database population migration to add FAQ and starting inventory items
  - Helped with pull requests and merge conflict resolution
  
* Rob Gordon:
  - Worked on refactoring file structure into more manageable subdirectories, including all javascript and css files
  - Started compiling documentation for the app
  - Helped with pull request and merge conflict resolution
  - Helped with drawing and javascripting images for inventory items (on order page)
  
* Paige M:
  - Built the flyer signup page, including ability to add/remove drones
  - Worked on order tracking tickets 
  - Helped with pull request and merge conflict resolution
  - Had medical issues, therefore excused from a portion of the work
  
* Zane Hirning:
  - Aided Ben Smith in order flow completion, including adding/removing items from order and submitting an order
  - Got a jump on debugging orders, including incorrect subtotals, wrong order items in final order, etc 
  - Helped with pull request and merge conflict resolution
  
* Ben Smith:
  - Aided Zane Hirning in order flow completion and all above-mentioned tasks
  - Completed javascript/css of order building for nice look and feel
  - Helped with pull request and merge conflict resolution

* Ben Hamner:
  - Admin panel css and adding/removing items from inventory
  - Earnings for all drone owners/drones individually
  - Helped with pull request and merge conflict resolution


## Sprint Difficulties:
**Problem:** 
Communication going into the start of this sprint was sorely lacking.  We were meeting less than once
per week and never updating group members on work completed. This created major issues with pull requests and work 
being done twice.

**Resolution:** 
We started meeting twice a week. Once over zoom and once in person. We also became much more active 
in the Discord, updating each other on how our work was going and what we needed help with. This significantly 
streamlined the work flow and reduced merge conflicts.  

**Problem:**

**Resolution:**

**Problem:**

**Resolution:**

**Problem:**

**Resolution:**

