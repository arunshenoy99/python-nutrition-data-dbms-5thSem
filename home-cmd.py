from utils import food,calories,fat,mineral,vitamin
choice = 999
while choice != 10:
    print("_________NUTRITION DATABASE___________")
    print("1.GET NUTRITION DATA FOR FOOD NAME")
    print("2.MAKE YOUR OWN NUTRITION ENTRY")
    print("3.GET FOOD ITEMS WITH GIVEN CALORIES")
    print("4.GET FOODS WITH LOW FAT CONTENT")
    print("5.GET THE FAT DATA OF A PARTICULAR FOOD")
    print("6.GET THE MINERAL DATA OF A PARTICULAR FOOD")
    print("7.GET THE VITAMIN DATA OF A GIVEN FOOD")
    print("8.DETERMINE IF A PARTICULAR FOOD IS HEALTHY OR NOT")
    print("9.GET FOODS RICH IN WATER")
    print("10.EXIT")
    choice = int(input("ENTER YOUR CHOICE:"))
    if choice == 1:
        food_name = input("ENTER THE NAME OF THE FOOD:")
        food_list = food.get_food(food_name)
        print("FOOD_ID\t\t\tNAME\t\t\tSERVING_SIZE\t\t\tCALORIES\t\t\t")
        for x in food_list:
            print(str(x[0])+'\t\t\t'+str(x[1])+'\t\t\t10'+str(x[2])+'\t\t\t'+str(x[3]))
    elif choice == 2:
        
