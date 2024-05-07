box_of_clothes = [int(number) for number in input().split()]

rack_capacity = int(input())
rack_count = 1
current_rack_capacity = rack_capacity

while box_of_clothes:
    clothe = box_of_clothes.pop()
    if current_rack_capacity >= clothe:
        current_rack_capacity -= clothe
    else:
        rack_count += 1
        current_rack_capacity = rack_capacity - clothe

print(rack_count)