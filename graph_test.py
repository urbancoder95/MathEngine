from graph.nodes import Node, DataNode
from graph.tensor import Tensor


def main():
    # Node test
    print("\nNode TEST\n")
    # print("Creating Node object with name \"ex_node\"\n")
    node = Node(name="ex_node")
    # print("Print Node(name=\"ex_node\"): ", node)
    if "<class:{} name:\"{}\">".format("Node", "ex_node") == repr(node):
        print("Node class PASSING.")
    else:
        print("Node class FAILING.")

    # DataNode test
    print("\nDataNode TEST\n")
    node = DataNode(value=54, name="ex_data_node")
    if "<class:{} value:{} name:\"{}\">".format("DataNode", 54, "ex_data_node") == repr(node):
        print("DataNode class PASSING.")
    else:
        print("DataNode class FAILING. {}".format(node))

    # Tensor test
    print("\nTensor TEST\n")
    value = [1, 2, 3]
    t = Tensor(value, name="ex_tensor_node")
    # print(t)
    if "<class:{} value:{} name:\"{}\">".format("Tensor", value, "ex_tensor_node") != repr(t):
        print("Tensor class FAILING at \"{}\" creation.".format("t = Tensor(value, name=\"ex_tensor_node\")"))

    if t[2] != 3:
        print("Tensor class FAILING. Value mismatch during indexing. t[2] != 3")
    elif t[0:2] != [1, 2]:
        print("Tensor class FAILING. Value mismatch during indexing t[0:3] != [1, 2]")
    else:
        print("Tensor class PASSING.")
    value = [[1, 2], [3, 4], [5, 6]]
    t2 = Tensor([[1, 2], [3, 4], [5, 6]], name="ex_tensor_node2")
    if "<class:{} value:{} name:\"{}\">".format("Tensor", value, "ex_tensor_node2") != repr(t2) :
        print("Tensor class FAILING at \"{}\" creation.".format("t = Tensor(value, name=\"ex_tensor_node2\")"))
    if t2[2] != [5, 6]:
        print("Tensor class FAILING. Value mismatch during indexing. t2[2] != [5, 6]")
    elif t2[0:2] != [[1, 2], [3, 4]]:
        print("Tensor class FAILING. Value mismatch during indexing. t2[0:2] != [[1, 2], [3, 4]]")
    elif t2[0:, 1] != [2, 4, 6]:
        print("Tensor class FAILING. Value mismatch during indexing. t2[0: 1] != [2, 4, 6].")
        print(t2[0:, 1])
    else:
        print("Tensor class PASSING.")
    try:
        a = t2[0:, 1, 2]
        print("Tensor class FAILING. Too many indices which should be caught.")
    except IndexError:
        print("Tensor class PASSING.")


if __name__ == '__main__':
    main()
