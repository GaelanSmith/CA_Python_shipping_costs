'''
This script defines three shipping methods
and determines which method is the cheapeast
based on the weight of the package.
'''

def ground_shipping(weight):

  ground_flat_rate = 20
  
  if weight <= 2:
    ppp = 1.50
  elif weight <= 6:
    ppp = 3.00
  elif weight <= 10:
    ppp = 4.00
  elif weight > 10:
    ppp = 4.75
  cost = ground_flat_rate + ppp*weight
  return cost

premium_ground = 125.00
'''Standard flat rate for premium ground shipping.
  Does not change based on weight.
'''

def drone_shipping(weight):

  if weight <= 2:
    ppp = 4.50
  elif weight <= 6:
    ppp = 9.00
  elif weight <= 10:
    ppp = 12.00
  elif weight > 10:
    ppp = 14.25
  cost = ppp*weight
  return cost

# First method to determine and print the cheapest shipping method.

def cheapest(weight):

  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground:
    return "The cheapest option is ground shipping, which will cost $" + str(ground_shipping(weight)) + " for a package that weighs " + str(weight) + " lb."
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground:
    return "The cheapest option is drone shipping, which will cost $" + str(drone_shipping(weight)) + " for a package that weighs " + str(weight) + " lb."
  else:
    return "The cheapest option is premium ground shipping, which will cost $" + str(premium_ground) + " for a package that weighs " + str(weight) + " lb."
  
print(cheapest(4.8))
print(cheapest(41.5))

# Second method to determine and print the cheapest shipping method.

def print_cheapest(weight):

  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground
  
  if ground < drone and ground < premium:
    method = "ground"
    cost = ground
  elif drone < ground and drone < premium:
    method = "drone"
    cost = drone
  else:
    method = "premium ground"
    cost = premium
    
  print(
    "The cheapest option is %s shipping, which will cost $%.2f for a package that weighs %.2f lb."
    % (method, cost, weight)
  )
  
print_cheapest(4.8)
print_cheapest(41.5)
