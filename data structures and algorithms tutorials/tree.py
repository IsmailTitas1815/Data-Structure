class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addd_child(self,child):
        child.parent = self   #jei object er maddhome jacche , shetai hocche child er parent. self bolte shei object ta mean korteche, like laptop, tv or root.
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * (self.get_level() * 2)
        prefix = spaces+'|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    laptop.addd_child(TreeNode('mac'))
    laptop.addd_child(TreeNode('surface'))
    laptop.addd_child(TreeNode('thinkpad'))

    cellphone = TreeNode('cell phone')
    cellphone.addd_child(TreeNode('iphone'))
    cellphone.addd_child(TreeNode('google pixel'))
    cellphone.addd_child(TreeNode('huawie'))

    tv = TreeNode('TV')
    tv.addd_child(TreeNode('Samsung'))
    tv.addd_child(TreeNode('LG'))
    tv.addd_child(TreeNode('Sony'))

    root.addd_child(laptop)
    root.addd_child(cellphone)
    root.addd_child(tv)
    
    return root

if __name__ =='__main__':
    root = build_product_tree()
    root.print_tree()
    pass