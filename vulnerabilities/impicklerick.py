x_inc = 6
y_inc = 6

x_start = 0
y_start = 0

xlower_range = x_start
xupper_range = xlower_range + x_inc

ylower_range = y_start
yupper_range = ylower_range + y_inc

while xlower_range <= 402:
    while xupper_range <= 408:
        print('x{0} - x{1}'.format(xlower_range, xupper_range))
        xlower_range += x_inc
        xupper_range += x_inc

while ylower_range <= 402:
    while yupper_range <= 408:
        print('y{0} - y{1}'.format(ylower_range, yupper_range))
        ylower_range += y_inc
        yupper_range += y_inc

