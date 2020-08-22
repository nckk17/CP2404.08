def lower_dict(d):
   new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
   return new_dict

color_code = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebud7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
              "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"
              , "aquamarine4": "#458b74", "azure1": "#f0ffff"}
new=(lower_dict(color_code))
print(new)

print (color_code)
color = str(input("Enter color name: "))
while color != "":

    if color in new:
        print(new[color])
    elif color in color_code:
        print(color_code[color])
    else:
        print("invalid")


    color = str(input("Enter color name: "))