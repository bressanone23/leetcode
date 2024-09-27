class MyCalendar:

    def __init__(self):
        self.event = []

    def book(self, start: int, end: int) -> bool:
        if self.event != []:
            for x in self.event:
                if x[0] < end and start < x[1]:
                    return False

        self.event.append([start,end])
        #print(self.event)
        return True
        # print(self.event)
        # print(self.res)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

#[3,8],[8,13],[19,25][25,32],[33,41][47,50],
