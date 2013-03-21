gearcalc
========

Written as part of a class project.

**Objective: design a simple two-speed transmission**. *(by picking 4 gears)*
+ Pick 4 gears from the [McMaster-Carr website](http://www.mcmaster.com/#standard-gears/)
+ Gears should provide transmission ratios of 0.5 and 1.5 between the two axles (+/- 0.1)
+ Centers of axles should be 1" apart
+ Cost <= $25 *(totally possible; up from the initial pricing of $15)*

This is a short script in python to:
+ read data about a gears from an INI file (in this case, part of the Molded Nylon Plain Bore gears.)
+ find sets of gears that fit the constraints

---------------------------------------

usage
-----

1. clone the repo
2. edit **gearcalc.py** if you need to change:

	+ the names of the INI files
	+ ideal values
	+ tolerances
	+ price range

3. run gearcalc.py

---------------------------------------

results
-------

Combination found: $17.81 *(closest)*

    57655K36 and 57655K45
      ($4.03  +  $5.37)
           Ratio: 0.5
        Distance: 1.0 inch

and

    57655K43 and 57655K38
      ($4.48  +  $3.93)
           Ratio: 1.5
        Distance: 1.0 inch

see also [combinations.md](combinations.md)

---------------------------------------

values used:
------------
The gears*.ini files were built by hand from the values on McMaster-Carr's [Molded Nylon Plain Bore](http://www.mcmaster.com/#standard-gears/=ly7dov) page.

I converted them using [a table I found](http://www.seoconsultants.com/charts/inches-decimal/).
