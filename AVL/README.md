# AVL
Bobby's implementation of AVL

## Update
when supplied a list of nodes which was touched during an insert or delete, we traverse through it and update the height of everything. Might insert fix/rebalancing inside instead of waiting till the end.

## Rotate Right/Left

1. If everything is present, cool, as per normal.
2. If there's no left subtree for x, we can just exit.
3. If x is the root, we need to update root too and when we update the left node's parent, make it none. since x got no parent too.
4. If left subtree got no right subtree that's OK, just attach nothing to x's left subtree.




