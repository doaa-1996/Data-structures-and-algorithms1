from linked_list import __version__
import linked_list
from linked_list.linked_list import LinkedList, Node
def test_version():
    assert __version__ == '0.1.0'
def test_Node():
    a = Node(5)
    assert a.value is 5
    assert a.next is None
def test_append_1():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value is 1
    ll.append(2)
    assert ll.head.next.value is 2
    assert ll.head.next.next is None
def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value is 5
    assert ll.head.next is None
    ll.insert('s')
    assert ll.head.value is 's'
    assert ll.head.next.value is 5
    ll.append('i')
    assert ll.head.value is 's'
    assert ll.head.next.value is 5
    ll.insert(17)
    assert ll.head.value is 17
    assert ll.head.next.value is 's'
def test_include():
    ll = LinkedList()
    assert ll.include(4) is False
    ll.append(5)
    assert ll.include(1) is False
    assert ll.include(5) is True
    ll.append(4)
    ll.insert(3)
    assert ll.include(1) is False
    assert ll.include(5) is True
    assert ll.include(4) is True
    assert ll.include(3) is True
    ll.insert(2)
    ll.append(1)
    assert ll.include(5) is True
    assert ll.include(1) is True
    assert ll.include(6) is False
def test_str():
    ll=LinkedList()
    assert str(ll) is 'None'
    ll.append(5)
    assert str(ll) == '{ 5 } -> None'
    ll.append(5)
    assert str(ll) == '{ 5 } -> { 5 } -> None'
    ll.append(4)
    ll.insert(3)
    ll.append(2)
    assert str(ll) == '{ 3 } -> { 5 } -> { 5 } -> { 4 } -> { 2 } -> None'