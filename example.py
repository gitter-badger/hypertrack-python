import hypertrack


hypertrack.secret_key = 'c237rtyfeo9893u2t4ghoevslsd'

customer = hypertrack.Customer.create(
    name='John Doe',
    email='john@customer.com',
    phone='+15555555555',
)

print customer
