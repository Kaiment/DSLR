from helpers import dataToDict
import matplotlib.pyplot as plt
import copy

def main():
    coursesData = getDataByCoursesAndHomes()
    fig, axs = plt.subplots(13, 13)
    for i, course1 in enumerate(coursesData):
        for j, course2 in enumerate(coursesData):
            createPairPlot(coursesData, course1, course2, i, j, axs)
    plt.show()

def createPairPlot(coursesData, course1, course2, i, j, axs):
    #fig = plt.figure()
    #a = fig.add_axes([0,0,1,1])

    if (j == 0):
        #axs[i][j].set(ylabel = course1)
        axs[i][j].set_ylabel(course1, rotation=0)
    if (i == 12):
        axs[i][j].set(xlabel = course2)
    if (i != j):
        axs[i][j].scatter(coursesData[course1]['Gryffindor'], coursesData[course2]['Gryffindor'], color='r', s=1)
        axs[i][j].scatter(coursesData[course1]['Hufflepuff'], coursesData[course2]['Hufflepuff'], color='b', s=1)
        axs[i][j].scatter(coursesData[course1]['Slytherin'], coursesData[course2]['Slytherin'], color='g', s=1)
        axs[i][j].scatter(coursesData[course1]['Ravenclaw'], coursesData[course2]['Ravenclaw'], color='y', s=1)
    else:
        axs[i][j].hist(coursesData[course1]['Gryffindor'] + coursesData[course2]['Gryffindor'], color='r')
        axs[i][j].hist(coursesData[course1]['Hufflepuff'] + coursesData[course2]['Hufflepuff'], color='b')
        axs[i][j].hist(coursesData[course1]['Slytherin'] + coursesData[course2]['Slytherin'], color='g')
        axs[i][j].hist(coursesData[course1]['Ravenclaw'] + coursesData[course2]['Ravenclaw'], color='y')
    


def getDataByCoursesAndHomes():
    data = dataToDict("../datasets/dataset_train.csv", 1)
    del data['First Name'], data['Last Name'], data['Birthday'], data['Best Hand']
    coursesData = initCoursesData()
    for i, house in enumerate(data['Hogwarts House']):
        for course in data:
            if course != 'Hogwarts House':
                coursesData[course][house].append(data[course][i])
    return coursesData

def initCoursesData():
    houses = {
        'Gryffindor': [],
        'Ravenclaw': [],
        'Hufflepuff': [],
        'Slytherin': []
    }
    courses = {
        'Arithmancy': copy.deepcopy(houses),
        'Astronomy': copy.deepcopy(houses),
        'Herbology': copy.deepcopy(houses),
        'Defense Against the Dark Arts': copy.deepcopy(houses),
        'Divination': copy.deepcopy(houses),
        'Muggle Studies': copy.deepcopy(houses),
        'Ancient Runes': copy.deepcopy(houses),
        'History of Magic': copy.deepcopy(houses),
        'Transfiguration': copy.deepcopy(houses),
        'Potions': copy.deepcopy(houses),
        'Care of Magical Creatures': copy.deepcopy(houses),
        'Charms': copy.deepcopy(houses),
        'Flying': copy.deepcopy(houses)
    }
    return courses

if __name__ == "__main__":
    main()
