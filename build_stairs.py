answer = input("Do you wanna build stairs?: ").lower()
if answer in ("y", "yes"):
    steps = int(input("This is going to be fun!!! \n" + "How many steps do you wanna build?: "))

    def build_stairs(steps):
        for i in range(steps):
            print("_" *(i==0) +  "__")
            print("   "*(i+1) + "|" , end="")
    build_stairs(steps)
elif answer in ("n", "no"):
    print("ohh! sorry to see you go, but you are missing the fun")
else:
    print("if you wanna build stairs try answering with on of these \n" + "y/yes/no/n")
