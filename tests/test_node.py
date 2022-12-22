'''
Name:
    test_node

Description:
    Module test_node is used for behavior verification of node.py module.

Tests:
    test_module_docstring
    test_version_module
    test_node_docstring
    test_help_valid_function
    test_help_valid_class
    test_node_invalid_instantization
    test_node_valid_instantization    
    test_node_empty_edges_lists_after_init
    test_node_add_valid_edge
    test_node_add_invalid_edge
    test_node_nonempty_edgelists_after_add
    test_node_nonempty_connectednodeslist_after_add
    test_this_node_nodeconnections_after_adding
    test_other_node_nodeconnections_after_adding
    test_this_node_edges_after_adding
    test_other_node_edges_after_adding
'''

import pytest
from graphs import node


def test_module_docstring():
    print(node.__doc__)
    assert True


def test_version_module():
    print(node.__version__)
    assert True


def test_node_docstring():
    print(node.Node.__doc__)
    assert True


def test_help_valid_function():
    test_term = node.__version__
    node.help(test_term)
    assert True


def test_help_valid_class():
    test_term = node.Node
    node.help(test_term)
    assert True


def test_node_invalid_instantization():
    with pytest.raises(Exception):
        n = node.Node()


def test_node_valid_instantization():
    data = "data"
    n = node.Node(data)
    assert True


def test_node_empty_edges_lists_after_init():
    data = "data"
    n = node.Node(data)
    assert len(n.edges) == 0


def test_node_add_valid_edge():
    data = "data"
    n = node.Node(data)
    assert len(n.connected_nodes) == 0


def test_node_add_invalid_edge():
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    with pytest.raises(Exception):
        n1.connect_node(n2)


def test_node_nonempty_edgelists_after_add():
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    n1.connect_node((n1, n2))
    assert len(n1.edges) == 1 and len(n2.edges) == 1


def test_node_nonempty_connectednodeslist_after_add():
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    n1.connect_node((n1, n2))
    assert len(n1.connected_nodes) == 1 and len(n2.connected_nodes) == 1


def test_this_node_nodeconnections_after_adding():
    n = node.Node(data="data")
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    n.connect_node((n, n1))
    n.connect_node((n2, n))
    assert n.connected_nodes == [n1, n2]


def test_other_node_nodeconnections_after_adding():
    n = node.Node(data="data")
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    n.connect_node((n, n1))
    n.connect_node((n2, n))
    assert n2.connected_nodes == [n]


def test_this_node_edges_after_adding():
    n = node.Node(data="data")
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    n.connect_node((n, n1))
    n.connect_node((n2, n))
    assert n.edges == [(n, n1), (n2, n)]


def test_other_node_edges_after_adding():
    n = node.Node(data="data")
    n1 = node.Node(data="data")
    n2 = node.Node(data="data")
    n.connect_node((n, n1))
    n.connect_node((n2, n))
    assert n1.edges == [(n, n1)]


#TODO:
#[ ] add test markings
#[ ] add test parametrization