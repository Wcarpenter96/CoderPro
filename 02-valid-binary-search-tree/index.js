function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}


var isValidBST = function (root) {
    const nodeCheck = (node, lower, upper) => {
        if (!node)
            return true;

        if (node.val <= lower || node.val >= upper)
            return false;

        if (!nodeCheck(node.right, node.val, upper))
            return false;
        if (!nodeCheck(node.left, lower, node.val))
            return false

        return true
    }
    return nodeCheck(root, -Infinity, Infinity)
};

let node = new TreeNode(5)
node.left = new TreeNode(4)
node.right = new TreeNode(7)
console.log(node)
console.log(isValidBST(node))

