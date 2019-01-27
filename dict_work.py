

import statistics

def get_nationality(something):
    value_arr=[]

    for item in something:
        value_arr.append(item[1])

    the_median=statistics.median(value_arr)

    new_arr=[]

    new_arr.append((something[0][0],int(100*something[0][1]/(something[0][1]+0.5*the_median))))
    new_arr.append((something[1][0],int(100*something[1][1]/(something[0][1]+the_median))))
    new_arr.append((something[2][0],int(100*something[2][1]/(something[0][1]+2*the_median))))

    return new_arr



something=[('ethiopia', 13.425), ('ephiopia', 13.425), ('westafrica', 13.24), ('russia', 12.505), ('saudiarabia', 12.500000000000002), ('africanamerican', 11.729999999999999), ('southafrica', 11.455000000000002), ('poland', 11.339999999999998), ('israel', 10.89), ('iraq', 10.66), ('germany', 10.514999999999999), ('austria', 10.4), ('czechrepublic', 10.015), ('southindia', 9.894999999999998), ('whiteamerican', 9.67), ('hungary', 9.604999999999999), ('spain', 9.379999999999997), ('france', 8.975000000000001), ('puertorico', 8.899999999999999), ('ukraine', 8.75), ('ireland', 8.405), ('afhganistan', 8.399999999999999), ('england', 8.32), ('india', 8.265), ('samoa', 8.24), ('argentina', 7.470000000000001), ('serbia', 7.295), ('greece', 7.215), ('tibet', 7.004999999999999), ('mexico', 6.955000000000001), ('japan', 6.495000000000001), ('shwitzerland', 6.119999999999999), ('cambodia', 6.0200000000000005), ('mongolia', 5.88), ('iran', 5.665), ('rumania', 5.425000000000001), ('brazilia', 5.210000000000001), ('peru', 4.705), ('italy', 4.49), ('uzbekistan', 4.465000000000001), ('philippines', 4.225000000000001), ('china', 3.3100000000000005), ('vietnam', 2.8200000000000003), ('burma', 2.495000000000001), ('thailand', 1.6199999999999997), ('taiwan', 1.5949999999999995), ('korea', 0.4349999999999996)]


print(get_nationality(something))