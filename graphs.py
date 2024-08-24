from collections import deque

s_to_f_nodes = {
    "s": ["top", "bottom"],
    "top": ["middle", "f"],
    "bottom": ["middle", "bottom_right"],
    "middle": [],
    "bottom_right": ["f"],
}

cab_to_bat_nodes = {
    "cab": ["cat", "car"],
    "car": ["bar", "cat"],
    "cat": ["mat", "bat"],
    "bar": ["bat"],
    "mat": ["bat"],
}


def breadth_first_search(nodes, start, end):
    if end in nodes[start]:
        return

    queue = deque(item for item in nodes[start])
    checked = set()

    print(start)

    while queue:
        traverse_next = queue.popleft()
        checked.add(traverse_next)
        print(traverse_next)

        for node in nodes[traverse_next]:
            if node in checked:
                continue
            if node == end:
                print(end)
                return

            queue.append(node)


breadth_first_search(cab_to_bat_nodes, "cab", "bat")

print("----")

breadth_first_search(s_to_f_nodes, "s", "f")
