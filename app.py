from graphs.graph import Graph
from graphs.node import Node

def main():
    node_bery = Node("Bery", None)
    node_marie = Node("Marie", None)
    node_duck = Node("Duck", None)

    rn = Node("bery", [Node("Marie", None), Node('Duck', None)])
    g = Graph(rn)
    print(g.root.data)
    for child in g.root.children:
        print(child.data)

if __name__ == "__main__":
    main()

#TODO:
# [ ] vytvorit tridu pro graf
# [ ] vytvorit tridu pro hru
# [ ] vytvorit tridu pro dependabilni graf

#FIXME:
# [ ]

#HACK:
# [ ]

#BUG:
# [ ] 

#XXX:
# [ ] mozna pouzit navrhovy vzor kompozit