'''
    Navigates and monitors transactions with customers.
    [1] Makes sure we don't go over our "allowed purchase per day limit"
    [2] Keep a count of total money / purchases throughout day
    [3] For every purchase, tell the employee how much each drink is,
    [4] and help them through the calculations for making change for the customer
'''


# we start out with no purchases and no money
purchases_made = 0
total_money_made = 0.0

# Let's pretend we are only allowed to make two purchases a day
# after we make two purchases, jump out of the code in the loop below.
while purchases_made < 2:
    
    print '\n' # a blank line
    print '--Purchase', purchases_made
    print '\n' # a blank line
    
    # log what the custumer ordered
    drink_name  = raw_input('Customer drink: ')
    drink_size = raw_input('Size: ')
    
    if drink_name == 'Mocha':
        cost = 3.50
    elif drink_name == 'Drip' or drink_name == 'Water':
        # in this case, a drip coffee and a water are the same price
        cost = 1.50
    elif drink_name == 'Tea':
        cost = 2.50
    else:
        print 'You did not enter a valid drink! Redoing purchase...'
        continue
    
    # Increase the size for larger drinks
    if drink_size == 'Large':
        added_cost = 1.50
    elif drink_size == 'Medium':
        added_cost = 1.00
    elif drink_size == 'Small':
        added_cost = 0.0
    else:
        # we didn't hit any of the cases above!
        # "continue" means "skip to the next loop cycle"
        print 'You did not enter a valid size! Redoing purchase...'
        continue
    
    # cost now equals what it used to equal, plus the added cost of drink size
    cost = cost + added_cost
    
    # add sales tax
    print 'Cost before tax: ', cost, 'dollars'
    cost_with_tax = cost + (cost * .08)
    print 'Customer owes (with tax): ', cost_with_tax, 'dollars'
    
    # get money from customer
    money_given = raw_input('Customer gave how much: ')
    
    # the "try" block here means "try to do the this next bit of code"
    try:
        # try to  turn the string response into a real 0.00 number
        money_given = float(money_given)
    # the "except" block here means "what we tried to do failed!"
    except:
        # this means turning the text into a 0.0 broke
        # this is probably because you typed a word like "Mocha"
        # into the input, which cannot be a 0.0 number.
        print 'Invalid value ' +  money_given, 'Skipping purchase...'
        continue
    
    # Even if you typed in the wrong thing, the customer could have
    # given us too little money.
    if money_given < cost_with_tax:
        print 'Customer did not give enough money. Skipping purchase...'
        continue
    else:
        # give the customer change!
        customer_change = money_given - cost_with_tax
        print 'Give the customer change: ', customer_change, 'dollars'
    
    # Update our totals. We have made one whole new purchase
    # and have made more money!
    # the "+=" means "add the new value to the existing variable"
    purchases_made +=1
    total_money_made += cost_with_tax
    

# All of our loops are done, and now we have a running record
# of what we did that day
print '\n\n' # blank lines
print 'Total purchases for today: ', purchases_made
print 'Total money made for today: ', total_money_made
    
    
    