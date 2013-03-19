# gearcalculator.py

import ConfigParser

# config values

gearDataFile = "gears32_15.ini"
numGears = 15 # this is the number after the underscore ( _ )

ideal_ratio_1_3 = 0.5
tolerance_1_3   = 0.1

ideal_ratio_2_4 = 1.5
tolerance_2_4   = 0.1

min_distance = 1.0 # in inches
max_distance = 2.0 # also in inches

# a few calculations before we begin

minr_1_3 = ideal_ratio_1_3 - tolerance_1_3
maxr_1_3 = ideal_ratio_1_3 + tolerance_1_3

minr_2_4 = ideal_ratio_2_4 - tolerance_2_4
maxr_2_4 = ideal_ratio_2_4 + tolerance_2_4

# open file to parse

cfp = ConfigParser.ConfigParser()
cfp.readfp(open(gearDataFile))

class Gear:
    def __init__(self, gearNumber): 
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

gears = [ Gear(i) for i in range(1,numGears) ] # make a list, gears, of objects starting at Gear(1) and ending at Gear(18)

for gear1 in gears:
    for gear2 in gears:
        for gear3 in gears:
            for gear4 in gears:
                dist_1_3 = (gear1.orthogonalDiameter / 2 + gear3.orthogonalDiameter / 2)
                dist_2_4 = (gear2.orthogonalDiameter / 2 + gear4.orthogonalDiameter / 2)

                correctDistance = (dist_1_3 == dist_2_4 and dist_1_3 >= min_distance and dist_1_3 <= max_distance)

                ratio_1_3 = (gear1.teeth / gear3.teeth)
                ratio_2_4 = (gear2.teeth / gear4.teeth)

                correctRatio = ((minr_1_3 <= ratio_1_3 <= maxr_1_3) and (minr_2_4 <= ratio_2_4 <= maxr_2_4))

                total = gear1.price + gear2.price + gear3.price + gear4.price

                if correctDistance and correctRatio:
                    # print gear1.partNumber, gear2.partNumber, gear3.partNumber, gear4.partNumber, total_s
                    print "Combination found: \n\tTotal cost = $" + str(total)
                    print "\t\tRatio of 1 to 3 = " + str(ratio_1_3)
                    print "\t\t\t(" + str(gear1.teeth) + " : " + str(gear3.teeth) + ")"
                    print "\t\tRatio of 2 to 4 = " + str(ratio_2_4)
                    print "\t\t\t(" + str(gear2.teeth) + " : " + str(gear4.teeth) + ")"
                    print "\t\tAxle-distance   = " + str(dist_1_3) + " inches"
                    print "\tPart Numbers:"
                    print "\t\tGear 1 :" + gear1.partNumber
                    print "\t\tGear 2: " + gear2.partNumber
                    print "\t\tGear 3: " + gear3.partNumber
                    print "\t\tGear 4: " + gear4.partNumber
