def describeDisplay(data):
    display = []
    display.append("")
    display[0] += "{:10}".format("")
    for c in data:
        if len(c) > 14:
            c = c[:15]
            c += ".."
        display[0] += "{:>20}".format(c)
    for i, featureData in enumerate(data["Ancient Runes"].keys()):
        display.append("")
        display[i + 1] += "{:10}".format(featureData.capitalize())
        for feature in data:
            display[i + 1] += "{:20.6f}".format(data[feature][featureData])
    for line in display:
        print(line)