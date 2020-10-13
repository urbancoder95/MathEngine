from graph.nodes import Node, DataNode


def main():
    # Node test
    print("Node test\n")
    print("Creating Node object with name \"ex_node\"\n")
    node = Node(name="ex_node")
    print("Print Node(name=\"ex_node\"): ", node)
    # DataNode test
    print("DataNode test\n")
    print("Creating DataNode object with name \"ex_data_node\"\n")
    node = DataNode(value=54, name="ex_data_node")
    print("Print DataNode(value=54, name=\"ex_node\"): ", node)


if __name__ == '__main__':
    main()
