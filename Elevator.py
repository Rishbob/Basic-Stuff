elevator1level = 5
elevator2level = 2
total_levels = 5
desired_level = int(input("What level do you want to go to?"))
starting_level = int(input("What level are you on?"))
dist1 = abs(starting_level - elevator1level)
dist2 = abs(starting_level - elevator2level)

print ("The first elevator is", dist1, "floors away")
print ("The second elevator is", dist2, "floors away")

def preferred_elevator(dist1, dist2):
   if starting_level == desired_level:
       print ("No elevator required")
   elif dist2 == dist1:
    print("Take either elevator")
   elif dist1 < dist2:
        print ("Take the first elevator")
   elif dist1 > dist2:
       print ("Take the second elevator")


preferred_elevator(dist1,dist2)