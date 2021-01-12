n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
a.sort() 
print("\nSorted List is - ", a)
