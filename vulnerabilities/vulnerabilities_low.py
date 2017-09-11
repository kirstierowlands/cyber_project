import csv
import numpy as np

startx = 0
incx = 6
endx = 408

starty = 0
incy = 6
endy = 408

count = 0
leave_loop = False

data_count = np.zeros((79, 79))

# open csv and reader hours1 and hours 2 columns
with open('Vulnerabilities-SPSS_2006_2016_LOW.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for each_line in reader:

        # convert str into float
        h1 = (each_line['hours_until_next_1'])
        h1 = float(h1)
        h2 = (each_line['hours_until_next_2'])
        h2 = float(h2)

        leave_loop = False
        start_x_range = startx
        start_y_range = starty

# nested for loop, runs x then runs all y, then next x then all y, etc
        for x_range in range(startx, endx, incx):
            start_x_range += incx


            if leave_loop:
                break

            for y_range in range(starty, endy, incy):
                start_y_range += incy

                if leave_loop:
                    break

                # count according to conditionals
                print(h1, " ", start_x_range, " ", start_y_range, " ", y_range)
                if (h1 >= start_x_range) and (h1 < (start_x_range + incx)):
                    print("Reached the conditional")
                if (h2 >= start_y_range) and (h2 < (start_y_range + incy)):
                    if (start_x_range > 0) and (incx > 0):
                        xbox = start_x_range / incx
                else:
                    xbox = 0
                if (start_y_range > 0) and (incy > 0):

                    ybox = start_y_range / incy
                else:
                    ybox = 0

              #  data_count[xbox, ybox] += 1
                print("I put it in the box!!!")
                leave_loop = True
                break

# print count
print('the count is', count)
print(data_count)