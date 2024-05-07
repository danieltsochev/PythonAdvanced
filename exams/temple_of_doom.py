from collections import deque

tools = deque([int(x) for x in input().split()])
substance = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substance and challenges:

    current_tool = tools.popleft()
    current_substance = substance.pop()
    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)

    else:
        tools.append(current_tool + 1)
        checked_substance = current_substance -1
        if checked_substance > 0:
            substance.append(checked_substance)


if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print(f"Tools: {', '.join([str(x) for x in tools])}")
    if substance:
        print(f"Substances: {', '.join([str(x) for x in substance])}")

else:
    print("Harry is lost in the temple. Oblivion awaits him.")
    if tools:
        print(f"Tools: {', '.join([str(x) for x in tools])}")
    if substance:
        print(f"Substances: {', '.join([str(x) for x in substance])}")
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")