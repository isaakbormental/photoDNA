import json


the_obj=[('vietnam', 75), ('philippines', 55), ('china', 39)]


d = {}
d[the_obj[0][0]] = the_obj[0][1]
d[the_obj[1][0]] = the_obj[1][1]
d[the_obj[2][0]] = the_obj[2][1]

with open('data.json', 'w') as outfile:
    print('{',file=outfile)
    print('  "data": [', file=outfile)

    print('    {', file=outfile)
    print('      "nation": '+'"'+the_obj[0][0]+'"'+',',file=outfile)
    print('      "occuracy": ' + str(the_obj[0][1]),file=outfile)
    print('    },', file=outfile)

    print('    {', file=outfile)
    print('      "nation": ' +'"'+ the_obj[1][0]+'"' + ',', file=outfile)
    print('      "occuracy": ' + str(the_obj[1][1]), file=outfile)
    print('    },', file=outfile)

    print('    {', file=outfile)
    print('      "nation": '+'"' + the_obj[2][0]+'"' + ',', file=outfile)
    print('      "occuracy": ' + str(the_obj[2][1]), file=outfile)
    print('    }', file=outfile)



    print('  ]', file=outfile)

    print('}', file=outfile)


#print (json.dumps(d,ensure_ascii=False))