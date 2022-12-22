'''
Name:
    node

Description:
    Module node is used for creating graphs with oriented edges. Nodes can hold any data (even other objects).

Classes:
    Node

Functions:
    version(None) -> None
    help(Callable | type) -> None

Misc variables:
    __version__
'''


__version__ = "0.0.1"


from typing import Callable


class Node:
    '''
    A class to represent a Node of Graph.
    ...

    Attributes
    ----------
        data: any
            Data content of node.
        connected_nodes: list(Node)
            List of connected nodes to this node.
        edges: list(tuple(Node, Node))
            List of directional edges in which this node is starting or ending node.

    Methods
    -------
        connect_node(tuple(Node, Node))
            Connects node to another node.
    '''

    def __init__(self, data: any):
        '''
        Constructs node with given node data. Initial lists of connected nodes and edges between connected nodes are empty. Nodes are connected to lists via connect_node methods.

        Parameters:
        -----------
            data: any
                Content of node.

        Returns:
        --------
            obj: Node 
                Constructed Node object.
        '''
        self._data = data
        self._connected_nodes = []
        self._edges = []

    @property
    def data(self) -> any:
        return self._data

    @data.setter
    def data(self, value: any) -> None:
        self._data = value

    @property
    def connected_nodes(self) -> list:
        return self._connected_nodes

    @property
    def edges(self) -> list:
        return self._edges

    def connect_node(self, connection: tuple) -> None:
        '''
        Connects node to another node. Connection is always directional. Tuple of tail and head nodes is appended to edges list and other Node is appened to connected_nodes to this Node.

        Parameters:
        -----------
            connections: tuple(Node, Node)
                List of directional edges in which this node is starting or ending node. First Node object is tail (start) of directional edge and second Node object is head (end) of directional edge. If neither of nodes is this node then methods calls exception ValueError.

        Returns:
        --------
            None
        '''
        tail, head = connection
        if tail is not self and head is not self:
            raise ValueError('One of the Nodes in directional edge must be "this" Node.')
        
        other = head if head is not self else tail
        
        self._connected_nodes.append(other)
        other.connected_nodes.append(self)

        self._edges.append(connection)
        other.edges.append(connection)


def version():
    '''
    Prints current version od module.

    Parameters:
    -----------
        None

    Returns:
    --------
        None
    '''
    print(__version__)


def help(term: Callable | type) -> None:
    '''
        Prints docstring for given term. Term should be function (Callable) or class (type)

        Parameters:
        -----------
            term: tuple(Node, Node)
                Term of which docstring should be printed.

        Returns:
        --------
            None
        '''
    print(term.__doc__)


def main():
    '''
    Main procedure of module. Prints module documentation.

    Parameters:
    -----------
        None

    Returns:
    --------
        None
    '''
    print(__doc__)


if __name__ == '__main__':
    main()

#TODO:
# [ ] implement deleters ... is it necessary?

#FIXME:
# [ ]

#HACK:
# [ ]

#BUG:
# [ ] 

#XXX:
# [ ] is it possible or useful to use design pattern composit?