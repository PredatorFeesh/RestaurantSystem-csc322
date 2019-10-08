# Online Restaurant System Project

## Fall, 2019, CSc 32200, Professor Jie Wei

Our specification document can be viewed [here](https://github.com/PredatorFeesh/RestaurantSystem-csc322/blob/master/proj_req_f19.pdf).

### Quick Overview

This service links customers with different food options from local restaurants with different choices. Also acts as a mini-restaurant management system allowing managers, salespeople, delivery members, customers and cooks to interact. More information of the specifications below.

### Given Specification

The 5 user types:

- [ ] Managers/Superusers :
  - [ ] Decide commissions of salespeople dealing with supplies
  - [ ] Pays of cooks and delivery people
  - [ ] Handles Complaints and Management of Customers
  - [ ] Can approve/deny customers
- [ ] Salespeople
  - [ ] Deal with suppliers maximizing best food supplies and prices
  - [ ] Each store has at least two
- [ ] Cooks
  - [ ] Determines the supplies quantities, menus, and prices of different food items.
  - [ ] Each store has at least two cooks.
- [ ] Delivery People
  - [ ] Bid on deliveries
  - [ ] Decide route to and from the restaurant

- [ ] Customers
  - [ ] Can order, and pay.
  - [ ] Evaluate food
  - [ ] Evaluate Delivery People
  - [ ] Can be blacklisted from stores
  - [ ] Store history of purchases
  - [ ] Customer Types per Store (determines price):
    - [ ] Visitors
    - [ ] Registered Customers
    - [ ] VIPs

On Visit

- [ ] Customer first asked to login.
- [ ] If not logged in, treated as visitor. Can always log in.
- [ ] Store manager must approve registered customer (the manager can check the customer record of the restaurant to decide if this customer should be approved).
- [ ] Blacklisted should be automatically declined.

On ordering

- [ ] Restaurant Lists most relevant 3 food choices based on order history for VIPs and Registered Customer.
- [ ] Customer can choose food.
- [ ] Registered Customers recieve discounted prices.
- [ ] VIPs are registered and get an additional food item for free.
- [ ] Visitors can read but not post ratings.

On order submit

- [ ] After customer submits choice, manager starts a bidding procedure for delivery people to big.
- [ ] Accept lowest asking price bidder
  - [ ] The winning delivery person then decides which route to go for this transaction based on traffic on the road: s/he can use any scheduling algorithm to decide the optimal route, assuming each segment of street can be randomly assigned to be of type good, busy, and closed.

After order finished, customer can:

- [ ] Rate food/cook from 1-5.
- [ ] Rate delivery person from 1-5.
- [ ] If rating < 3, then views as a complaint and should be asked to provide reason.
- [ ] Delivery person can rate the customer as well right after delivery **EXCEPT** if seen customer rating already.

Registered Customer Conditions

- [ ] A registered customer who made more than 3 orders with an average rate > 4 is automatically promoted to VIP.
- [ ] A registered customer making more than 3 orders with an average rating < 2 but > 1 is demoted to a visitor.
- [ ] If average rating is 1, then the customer is put in customer blacklist who can never be a registered user.

Delivery Person Conditions

- [ ] When given an average rating < 2 for last 3 deliveries, recieves a warning which can be erased by manager.
- [ ] More than 3 warnings leads to layoff.

Food/Cook Condition

- [ ] A food item recieving average rating < 2 in last 3 orders is dropped.
- [ ] The cook whose food was dropped twice will be warned.
- [ ] A cook with 3 warnings will be laid off.

Sales Person Condition

- [ ] When recieving 3 straight 5's, recieve 10% raise.
- [ ] If the supplies ordered complained by cooks 3 times, sales person recieve a warning and 10% commission reduction.
- [ ] Laid off after 3 warnings.

Special Requirement

- [ ] Voice-based order feature should be avaliable.

OUR CHOSEN EXTRA FEATURE:

- [ ] TBD

### System Outlook

1) Provide consistent GUI, different users will have different/personalized outlooks.
2) Choose 1 creative feature for this sytem (10% of the score). Creativity Rewarded.
3) Any system details not provided left for us to choose.


## Current Plan (Subject to change)

Technologies:
- Python3 Flask (Gunicorn for more than 1 user support)
- Amazon Buckets 
- SQLite or MySql
- More to be added

Schema: To be added. Aim: Minimum (Hopefully 0) deletions. Tables done to support such.

*Possible Addition*: Suppliers, Supplier_Item are another type in our system, which communicate with sales people. "Communicate" meaning placing orders.
