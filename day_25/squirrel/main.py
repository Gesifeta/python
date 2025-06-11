import  pandas

squirrels = pandas.read_csv("./squirrel_data.csv")

gray_squirrels = len(squirrels[squirrels["Primary Fur Color"]=="Gray"])
cinnamon_squirrels = len(squirrels[squirrels["Primary Fur Color"]=="Cinnamon"])
black_squirrels = len(squirrels[squirrels["Primary Fur Color"]=="Black"])

squirrels_dict ={
    "colors":["Gray","Cinnamon","Black"],
    "count":[gray_squirrels,cinnamon_squirrels,black_squirrels]
}
squirrels_data =pandas.DataFrame(squirrels_dict)
squirrels_data_from = pandas.read_csv("./squirrels_data_frame.csv")
print(squirrels_data)
print(squirrels_data_from)
print(squirrels_data.to_csv("squirrels_data_frame.csv"))
