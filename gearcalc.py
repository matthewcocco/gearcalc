# gearcalculator.py

import ConfigParser

gearDataFile = "gears.ini"

# converted values by hand using http://www.seoconsultants.com/charts/inches-decimal/ 
# list taken from mcmaster.com

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
# 96, 2.000, 1,      2.04, 3/8,  1/8, 1/4,  "57655K31", 6.16

class Gear:
	def __init__(self, gearNumber): 
		cfp = ConfigParser.ConfigParser()
		cfp.readfp(open(gearDataFile))
		gearname = 'Gear' + str(gearNumber)
		self.teeth              = float(cfp.get(gearname, 'Teeth'))
		self.pitchDiameter      = float(cfp.get(gearname, 'PitchDiameter'))
		self.hubDiameter        = float(cfp.get(gearname, 'HubDiameter'))
		self.orthogonalDiameter = float(cfp.get(gearname, 'OrthogonalDiameter'))
		self.overallLength      = float(cfp.get(gearname, 'OverallLength'))
		self.faceWidth          = float(cfp.get(gearname, 'FaceWidth'))
		self.boreSize           = float(cfp.get(gearname, 'BoreSize'))
		self.partNumber         = cfp.get(gearname, 'PartNumber')
		self.price              = float(cfp.get(gearname, 'Price'))

gears = [ Gear(i) for i in range(1,19) ]

for gear1 in gears:
	for gear2 in gears:
		for gear3 in gears:
			for gear4 in gears:
				length_1_3 = (gear1.orthogonalDiameter / 2 + gear3.orthogonalDiameter / 2)
				length_2_4 = (gear2.orthogonalDiameter / 2 + gear4.orthogonalDiameter / 2)

				correctLength = (length_1_3 == length_2_4 and length_1_3 >= 1.0 and length_2_4 <= 2.0)

				ratio_1_3 = (gear1.teeth / gear3.teeth)
				ratio_2_4 = (gear2.teeth / gear4.teeth)

				correctRatio = ((0.4 <= ratio_1_3 <= 0.6) and (1.4 <= ratio_2_4 <= 1.6))

				total = gear1.price + gear2.price + gear3.price + gear4.price

				if correctLength and correctRatio:
					# print gear1.partNumber, gear2.partNumber, gear3.partNumber, gear4.partNumber, total_s
					print "Combination found: \n\tTotal cost = $" + str(total)
					print "\t\tRatio of 1 to 3 = " + str(ratio_1_3)
					print "\t\t\t(" + str(gear1.teeth) + " : " + str(gear3.teeth) + ")"
					print "\t\tRatio of 2 to 4 = " + str(ratio_2_4)
					print "\t\t\t(" + str(gear2.teeth) + " : " + str(gear4.teeth) + ")"
					print "\t\tAxle-distance   = " + str(length_1_3) + " inches"
					print "\tPart Numbers:"
					print "\t\tGear 1 :" + gear1.partNumber
					print "\t\tGear 2: " + gear2.partNumber
					print "\t\tGear 3: " + gear3.partNumber
					print "\t\tGear 4: " + gear4.partNumber