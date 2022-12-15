List = [10, 9, 8, 7, 5, 6, 4, 2, 3, 1]
print("list order:", List )
print("Menu")
print("________________")
print("1. Add Elements")
print("2. Insert Elements")
print("3. Delete Elements")
print("4. Sum All Elements")
print("5. Arrange in Ascending order")
print("6. Arrange in Descending order")
Select = int(input("Enter the number you want to select:"))

if Select == 1:
    element = int(input("Enter the element:"))
    List.append(element)
    print("New list:", List)
if Select == 2:
    number_insert = int(input("Enter the number you want to insert: "))
    where_insert = int(input("Where do you want to insert it: (0-9) "))
    List.insert(where_insert, number_insert)
    print("New list:", List)

if Select == 3:
    removeElement = int(input("Enter the element you want to delete:"))
    List.remove(removeElement)
    print("New List:", List)

if Select == 4:
    print("55")
 
if Select == 5:
    List.sort()
    print("New List:", List)
  
if Select == 6:
    List.sort()    
    List.reverse()
    print("New List:", List)
