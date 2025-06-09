import  pandas

squirrels = pandas.read_csv("squirrel_data.csv")
colors_gray = squirrels[squirrels["Primary Fur Color"]=="gray"].to_list()
colors_colonium = squirrels[squirrels["Primary Fur Color"]=="gray"].to_list()
for color in colors:
    color.name=color
    color.number=





print(colors)