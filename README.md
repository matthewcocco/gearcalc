gearcalc
========

Written as part of a class project.

**Objective: design a simple two-speed transmission**. *(by picking 4 gears)*
+ Pick 4 gears from the [McMaster-Carr website](http://www.mcmaster.com/#standard-gears/)
+ Gears should provide transmission ratios of 0.5 and 1.5 between the two axles
+ Centers of axles should be 1" apart
+ Cost <= $15 *(impossible?)*
	- *("[Molded Nylon Plain Bore](http://www.mcmaster.com/#standard-gears/=ly6yze)" gears appear to be the cheapest.)*


This is a short script in python to:
+ read data about a gears from an INI file
+ find sets of gears that fit constraints

---------------------------------------

results
-------
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

---------------------------------------

values used:
------------
The gears.ini file was built by hand from the values on McMaster-Carr's [Molded Nylon Plain Bore](http://www.mcmaster.com/#standard-gears/=ly6yze) page.
converted them using [a table I found](http://www.seoconsultants.com/charts/inches-decimal/)

    # 12, 0.250, 3/16, 0.29, 5/16, 1/8, 3/32, "57655K11", 6.15
    # 14, 0.292, 1/4,  0.33, 5/16, 1/8, 3/32, "57655K12", 4.38
    # 16, 0.333, 1/4,  0.37, 5/16, 1/8, 1/8,  "57655K13", 4.66
    # 18, 0.375, 5/16, 0.41, 5/16, 1/8, 1/8,  "57655K14", 4.60
    # 20, 0.417, 3/8,  0.45, 3/8,  1/8, 1/8,  "57655K15", 4.09
    # 24, 0.500, 3/8,  0.54, 3/8,  1/8, 1/8,  "57655K16", 4.84
    # 28, 0.583, 1/2,  0.62, 3/8,  1/8, 1/8,  "57655K17", 4.93
    # 32, 0.667, 1/2,  0.70, 3/8,  1/8, 1/8,  "57655K18", 5.06
    # 36, 0.750, 5/8,  0.79, 3/8,  1/8, 3/16, "57655K19", 5.00
    # 40, 0.833, 5/8,  0.87, 3/8,  1/8, 3/16, "57655K21", 5.90
    # 42, 0.875, 7/16, 0.91, 3/8,  1/8, 1/4,  "57655K22", 4.12
    # 48, 1.000, 5/8,  1.04, 3/8,  1/8, 3/16, "57655K24", 5.69
    # 56, 1.167, 5/8,  1.20, 3/8,  1/8, 3/16, "57655K25", 6.64
    # 60, 1.250, 5/8,  1.29, 3/8,  1/8, 1/4,  "57655K26", 6.89
    # 64, 1.333, 5/8,  1.37, 3/8,  1/8, 1/4,  "57655K27", 7.05
    # 72, 1.500, 5/8,  1.54, 3/8,  1/8, 1/4,  "57655K28", 7.06
    # 80, 1.667, 5/8,  1.70, 3/8,  1/8, 1/4,  "57655K29", 7.28
    # 96, 2.000, 1,    2.04, 3/8,  1/8, 1/4,  "57655K31", 6.16
