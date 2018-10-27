dollarsForACupcake = int(input())
centsForACupcake = int(input())
numbersOfCupcakes = int(input())
allDollarsForAllCupcakes = dollarsForACupcake * numbersOfCupcakes + centsForACupcake * numbersOfCupcakes // 100
allCentsForAllCupcakes = centsForACupcake * numbersOfCupcakes % 100
print(allDollarsForAllCupcakes, allCentsForAllCupcakes)
