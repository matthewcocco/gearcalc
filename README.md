gearcalc
========

Written as part of a class project.

**Objective: design a simple two-speed transmission**. *(by picking 4 gears)*
+ Pick 4 gears from the [McMaster-Carr website](http://www.mcmaster.com/#standard-gears/)
+ Gears should provide transmission ratios of 0.5 and 1.5 between the two axles
+ Centers of axles should be 1" apart
+ Cost <= $15 *(impossible?)*

This is a short script in python to:
+ read data about a gears from an INI file (in this case, part of the Molded Nylon Plain Bore gears.)
+ find sets of gears that fit constraints

---------------------------------------

usage
-----

1. clone the repo
2. edit **gearcalc.py** if you need to change:
	+ the name of the INI file
	+ the number of gears in the INI file
3. run gearcalc.py

---------------------------------------

results
-------

(for 48 pitch)

Combination found:

    Total cost = $25.07
    	Ratio of 1 to 3 = 0.444444444444
    		(32.0 : 72.0)
    	Ratio of 2 to 4 = 1.6
    		(64.0 : 40.0)
    	Axle-distance   = 1.12 inches
    Part Numbers:
    	Gear 1 :"57655K18"
    	Gear 2: "57655K27"
    	Gear 3: "57655K28"
    	Gear 4: "57655K21"

Combination found:

    Total cost = $24.84
    	Ratio of 1 to 3 = 0.5625
    		(36.0 : 64.0)
    	Ratio of 2 to 4 = 1.5
    		(60.0 : 40.0)
    	Axle-distance   = 1.08 inches
    Part Numbers:
    	Gear 1 :"57655K19"
    	Gear 2: "57655K26"
    	Gear 3: "57655K27"
    	Gear 4: "57655K21"

(for 32 pitch)

Combination found: 

    Total cost = $17.81
    	Ratio of 1 to 3 = 0.5
    		(20.0 : 40.0)
    	Ratio of 2 to 4 = 1.5
    		(36.0 : 24.0)
    	Axle-distance   = 1.0 inches
    Part Numbers:
    	Gear 1 :57655K36
    	Gear 2: 57655K43
    	Gear 3: 57655K45
    	Gear 4: 57655K38

Combination found: 

    Total cost = $19.88
    	Ratio of 1 to 3 = 0.416666666667
    		(20.0 : 48.0)
    	Ratio of 2 to 4 = 1.42857142857
    		(40.0 : 28.0)
    	Axle-distance   = 1.125 inches
    Part Numbers:
    	Gear 1 :57655K36
    	Gear 2: 57655K45
    	Gear 3: 57655K47
    	Gear 4: 57655K41

Combination found: 

    Total cost = $19.41
    	Ratio of 1 to 3 = 0.545454545455
    		(24.0 : 44.0)
    	Ratio of 2 to 4 = 1.42857142857
    		(40.0 : 28.0)
    	Axle-distance   = 1.125 inches
    Part Numbers:
    	Gear 1 :57655K38
    	Gear 2: 57655K45
    	Gear 3: 57655K46
    	Gear 4: 57655K41

---------------------------------------

values used:
------------
The gears*.ini files were built by hand from the values on McMaster-Carr's [Molded Nylon Plain Bore](http://www.mcmaster.com/#standard-gears/=ly7dov) page.

I converted them using [a table I found](http://www.seoconsultants.com/charts/inches-decimal/).
