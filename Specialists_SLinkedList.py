class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self,):
        self.headval = None

    def AtBegining(self, newdata):
        NewNode = Node(newdata)

        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # def RemoveNode(self, Removekey):
    #     headval = self.headval
    #     if (headval is not None):
    #         if (headval.dataval == Removekey):
    #             self.head = headval.next
    #             headval = None
    #             return
    #     while (headval is not None):
    #         if headval.dataval == Removekey:
    #             break
    #         prev = headval
    #         headval = headval.next
    #     if (headval == None):
    #         return
    #     prev.next = headval.next

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

# list = SLinkedList()
# print("Here is a list of our health specialists.")
# print("\n")
# list.headval = Node("General-Doctor")
# e2 = Node("Psychotherapist")
# e3 = Node("General Doctor")
#
# list.headval.nextval = e2
# e2.nextval = e3
#
# list.AtEnd("Neuropathalogist")
# list.AtBegining("Anesthesiologist Reanimatologist")
# # list.Inbetween(list.headval.nextval, "Radiologist ")
# # # list.RemoveNode("General Doctor")
# #
# list.listprint()