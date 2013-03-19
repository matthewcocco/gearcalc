gearcalc
========

Written as part of a class project.

**Objective: design a two-speed transmission**.
+ Pick 4 gears from the McMaster-Carr website [link](http://www.mcmaster.com/#standard-gears/)
+ Gears should provide transmission ratios of 0.5 and 1.5 between the two axles
+ Centers of axles should be 1" apart
+ Cost <= $15 *(I am not sure this condition is possible)*

This is a short script in python to:
+ read data about a gears from an INI file
+ find sets of gears that fit constraints

------------

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