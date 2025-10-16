class HotelFareCalc:
    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='', cindate='', coutdate='', rno=101):
        print("\n\n**WELCOME TO  TRANQUIL NEST INN**\n")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your name: ")
        self.address = input("Enter your address: ")
        self.cindate = input("Enter your check-in date: ")
        self.coutdate = input("Enter your checkout date: ")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):
        print("We have the following rooms for you:")
        print("1. Deluxe Suite ----> Rs 6000 PN")
        print("2. Executive Room ----> Rs 5000 PN")
        print("3. Classic Room ----> Rs 4000 PN")
        print("4. Budget Room ----> Rs 3000 PN")

        x = int(input("Enter your choice: "))
        n = int(input("How many nights did you stay? "))

        if x == 1:
            print("You have opted for Deluxe Suite.")
            self.s = 6000 * n
        elif x == 2:
            print("You have opted for Executive Room.")
            self.s = 5000 * n
        elif x == 3:
            print("You have opted for Classic Room.")
            self.s = 4000 * n
        elif x == 4:
            print("You have opted for Budget Room.")
            self.s = 3000 * n
        else:
            print("Invalid room choice.")
            self.s = 0

        print("Your room rent is = Rs", self.s, "\n")
        return self.s

    def restaurantbill(self):
        print("RESTAURANT MENU")
        print("1. Water --> Rs 20")
        print("2. Tea --> Rs 10")
        print("3. Breakfast Combo --> Rs 90")
        print("4. Lunch --> Rs 110")
        print("5. Dinner --> Rs 150")
        print("6. Exit")

        while True:
            c = int(input("Enter your choice: "))
            if c == 6:
                break
            d = int(input("Enter the quantity: "))
            if c == 1:
                self.r += 20 * d
            elif c == 2:
                self.r += 10 * d
            elif c == 3:
                self.r += 90 * d
            elif c == 4:
                self.r += 110 * d
            elif c == 5:
                self.r += 150 * d
            else:
                print("Invalid option")

        print("Total food cost = Rs", self.r, "\n")
        return self.r

    def laundrybill(self):
        print("LAUNDRY MENU")
        print("1. Shorts --> Rs 3")
        print("2. Trousers --> Rs 4")
        print("3. Shirt --> Rs 5")
        print("4. Jeans --> Rs 6")
        print("5. Girlsuit --> Rs 8")
        print("6. Exit")

        while True:
            e = int(input("Enter your choice: "))
            if e == 6:
                break
            f = int(input("Enter the quantity: "))
            if e == 1:
                self.t += 3 * f
            elif e == 2:
                self.t += 4 * f
            elif e == 3:
                self.t += 5 * f
            elif e == 4:
                self.t += 6 * f
            elif e == 5:
                self.t += 8 * f
            else:
                print("Invalid option")

        print("Total laundry cost = Rs", self.t, "\n")
        return self.t

    def gamebill(self):
        print("GAME MENU")
        print("1. Table Tennis --> Rs 60/hr")
        print("2. Bowling --> Rs 80/hr")
        print("3. Snooker --> Rs 70/hr")
        print("4. Video Games --> Rs 90/hr")
        print("5. Pool --> Rs 50/hr")
        print("6. Exit")

        while True:
            g = int(input("Enter your choice: "))
            if g == 6:
                break
            h = int(input("No. of hours: "))
            if g == 1:
                self.p += 60 * h
            elif g == 2:
                self.p += 80 * h
            elif g == 3:
                self.p += 70 * h
            elif g == 4:
                self.p += 90 * h
            elif g == 5:
                self.p += 50 * h
            else:
                print("Invalid option")

        print("Total game bill = Rs", self.p, "\n")
        return self.p

    def display(self):
        print("\n****** HOTEL BILL ******")
        print("Customer Details:")
        print("Name:", self.name)
        print("Address:", self.address)
        print("Check-in Date:", self.cindate)
        print("Check-out Date:", self.coutdate)
        print("Room No.:", self.rno)
        print("Room Rent: Rs", self.s)
        print("Food Bill: Rs", self.r)
        print("Laundry Bill: Rs", self.t)
        print("Game Bill: Rs", self.p)

        self.rt = self.s + self.t + self.p + self.r
        print("Subtotal: Rs", self.rt)
        print("Additional Service Charges: Rs", self.a)
        print("Grand Total: Rs", self.rt + self.a, "\n")

        self.rno += 1
        return self.rt + self.a


# Main Program
def main():
    a = HotelFareCalc()

    while True:
        print("1. Enter Customer Data")
        print("2. Calculate Room Rent")
        print("3. Calculate Restaurant Bill")
        print("4. Calculate Laundry Bill")
        print("5. Calculate Game Bill")
        print("6. Show Total Cost")
        print("7. Exit")

        b = int(input("Enter your choice: "))

        if b == 1:
            a.inputdata()
        elif b == 2:
            a.roomrent()
        elif b == 3:
            a.restaurantbill()
        elif b == 4:
            a.laundrybill()
        elif b == 5:
            a.gamebill()
        elif b == 6:
            a.display()
        elif b == 7:
            print("Thank you for visiting Tranquil nest inn.")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()
