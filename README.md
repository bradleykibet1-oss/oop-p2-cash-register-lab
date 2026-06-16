# Object Oriented Programming (OOP) Part 2 - Cash Register Lab

Now that we’ve discussed more about object oriented design philosophies and techniques like decorators we will be looking at building more complex objects. In this case we will be building a cash register object to simulate different functions of a cash register for an e-commerce site. 

## Tools & Resources
* [GitHub Repo](https://github.com/learn-co-curriculum/oop-p2-cash-register-lab)
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 
* Fork and Clone: For this lesson, you will need the following GitHub Repo:
  * Go to the provided GitHub repository link.
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Open and Run File
  * Open the project in VSCode.
  * Run npm install to install all necessary dependencies.

### Task 1: Define the Problem

Build a model for a cash register
* Build a cash register object
* Add items
* Apply discounts
* Void previous transactions

### Task 2: Determine the Design

Cash Register
* Attributes
  * discount
  * total
  * items
  * previous_transactions
* Methods
  * add_item(item, price, quantity)
  * apply_discount()
  * void_last_transaction()

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Git Feature Branch

* Create a feature branch for your work using git.

#### Step 2: Create a CashRegister class

* ```__init__```:
  * discount
  * Allow for user to input
  * If no input initialize as 0
  * Note that discount is a percentage off of the total cash register price (e.g. a discount of 20 means the customer receives 20% off of their total price)
* ```total```
  * Initialize as 0
* ```items```
  * Initialize as empty array
* ```previous_transactions```
  * Initialize as empty array

#### Step 3: Properties

* Discount:
  * Ensure discount is an integer
  * Ensure that discount is between 0-100 inclusive
  * If not print “Not valid discount”

#### Step 4: Methods

* add_item(item, price, quantity)
  * Add price to total
  * Add item to the items array
  * Add an object to the previous transactions with the item, price and quantity.
* apply_discount()
  * Apply discount as percentage off from total
  * Remove the last item of previous_transaction from array
    * Ensure price reflects correctly
    * Ensure items reflects correctly
  * If no transactions in array print “There is no discount to apply.”
* void_last_transaction()
  * Remove the last item of previous_transaction from the array.
    * Ensure the price reflects correctly.
    * Ensure items reflect correctly.
  * If no transactions are in the array, print “There is no transaction to void.”

#### Step 5: Push feature branch and open a PR on GitHub

* Save, commit, and push your code to GitHub.
* Open a PR on the main branch of your own repo (be sure not to open a PR on the learn-co-curriculum repo).

#### Step 6: Merge to main

* Review the PR and merge your finished code into the main branch.

### Task 4: Document and Maintain

Best Practice documentation steps:

* Add comments to code to explain purpose and logic
  * Clarify intent / functionality of code to other developers
  * Add screenshot of completed work included in Markdown in README.
  * Update README text to reflect the functionality of the application following https://makeareadme.com. 
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Implementation Details

### CashRegister Class

The CashRegister class provides a complete solution for managing a cash register system. It handles item tracking, total calculation, discount application, and transaction history.

#### Features

- **Item Management**: Add items with price and optional quantity
- **Discount Support**: Apply percentage-based discounts (0-100%)
- **Transaction Tracking**: Maintain a history of all transactions
- **Void Operations**: Remove the last transaction and update totals accordingly

#### Usage Example

```python
from cash_register import CashRegister

# Create a cash register with no discount
register = CashRegister()

# Add items
register.add_item("eggs", 0.98)
register.add_item("book", 5.00, 3)  # Quantity: 3
print(f"Total: ${register.total}")  # Total: $15.98

# Create a register with 20% discount
discounted_register = CashRegister(20)
discounted_register.add_item("macbook air", 1000)
discounted_register.apply_discount()  # Prints: "After the discount, the total comes to $800."
print(f"Total: ${discounted_register.total}")  # Total: $800.0

# Void last transaction
register.add_item("tomato", 1.76)
register.void_last_transaction()
print(f"Items: {register.items}")  # Only eggs and 3 books remain
```

#### Class Methods

- `__init__(discount=0)`: Initialize register with optional discount
- `add_item(item, price, quantity=1)`: Add item to register
- `apply_discount()`: Apply discount percentage to total
- `void_last_transaction()`: Remove last transaction from register

#### Testing

All functionality has been tested and verified to pass 14 unit tests:
- Initialization tests
- Item addition tests
- Discount application tests
- Transaction void tests

Run tests with:
```bash
python3 -m pytest lib/testing/cash_register_test.py -v
```

## Save your work and push to GitHub

Before you submit your solution, you need to save your progress with git.
1. Add your changes to the staging area by executing git add .
2. Create a commit by executing git commit -m "Your commit message"
3. Push your commits to GitHub by executing git push origin main or git push origin master , depending on the name of your branch (use git branch to check on which branch you are).

## Submission and Grading Criteria

1. Use the rubric in Canvas as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade, using the most recent commit. Remember to make sure you have pushed your commit to GitHub before submitting your assignment. 
3. You can review your submission in CodeGrade and see your final score in your Canvas gradebook.
4. When you are ready to submit, click the ***Load Lab: Object Oriented Programming (OOP)- Part 2- Cash Register*** button in Canvas to launch CodeGrade.
  * Click on + Create Submission. Connect your repository for this lab.
  * For additional information on submitting assignments in CodeGrade: [Getting Started in Canvas](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas).
