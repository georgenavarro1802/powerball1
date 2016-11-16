from collections import defaultdict
import operator


objects_list = []
general_numbers_list = []
general_powerball_ist = []


def get_input(question):
    return raw_input(question)


def get_element(elem, list, index):
    """
        Keep asking the user for an valid element until it is finally selected and valid.
    """
    if elem:
        # validate if elem is a number and is it in 1 to 69 range
        if not elem.isdigit():
            print("IT IS NOT A VALID NUMBER \n")
        elif int(elem) not in range(1, 70):
            print("OUT OF RANGE, Must be between 1 to 69 \n")
        elif elem in list:
            print("DUPLICATE NUMBER, the number is already on the list \n")
        else:
            return elem

    elem = get_input("{:>20}".format("Select {0} # (1 thru 69 {1}): ".format(index,
                                                                             "excluding: {0}".format(", ".join(list))
                                                                             if list else "")))
    return get_element(elem, list, index)


def get_element_powerball(elem=None):
    """ Keep asking the user for an valid element until it is finally selected and valid. """
    if elem:
        # validate if elem is a number and is it in 1 to 26 range
        if not elem.isdigit():
            print("IT IS NOT A VALID NUMBER \n")
        elif int(elem) not in range(1, 27):
            print("OUT OF RANGE, Must be between 1 to 26 \n")
        else:
            return elem

    elem = get_input("{:>20}".format("Select Power Ball # (1 thru 26): "))
    return get_element_powerball(elem)


def print_list_players():
    # better console style
    print "\n"
    LAYOUT = "{:<20} {:<20} {:4} {:4} {:4} {:4} {:4} {:14}"
    print LAYOUT.format("FirstName", "LastName", "N1", "N2", "N3", "N4", "N5", "Powerball")
    print LAYOUT.format("-" * 20, "-" * 20, "-" * 4, "-" * 4, "-" * 4, "-" * 4, "-" * 4, "-" * 10)
    for obj in objects_list:
        # list from objects (i did this, just to use OOP: creating instance and read attributes from it)
        print LAYOUT.format(obj.firstname, obj.lastname, obj.n1, obj.n2, obj.n3, obj.n4, obj.n5, obj.powb)
    print "\n"


def print_winning_numbers(num_dict, powb_dict):
    # Giving a better format
    print("\n")
    LAYOUT = "{:5} {:^40} {:5}"
    print LAYOUT.format("#" * 3, "Powerball Winning Number", "#" * 3)
    print LAYOUT.format("#" * 3, "#" * 40, "#" * 3)
    print LAYOUT.format("#" * 3, ' '.join(str(n) for n in num_dict.keys()) +
                        '  Powerball: {0}'.format(powb_dict.keys().pop()), "#" * 3)
    print LAYOUT.format("#" * 3, "#" * 40, "#" * 3)
    print("\n")


def generate_winning_numbers():
    # Ask if exists data entered
    if len(general_numbers_list):
        # used two dicts to write duplicates number and how many times it repeats (favorites and powerball numbers)
        appearances = defaultdict(int)
        appearances_powb = defaultdict(int)
        for curr in general_numbers_list:
            appearances[curr] += 1
        for curr in general_powerball_ist:
            appearances_powb[curr] += 1
        # get the first five numbers with more concurrence in a general list sorted by concurrences number
        favorites_numbers = dict(sorted(appearances.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
        favorite_powerball = dict(sorted(appearances_powb.iteritems(), key=operator.itemgetter(1), reverse=True)[:1])
        # print results
        print_winning_numbers(favorites_numbers, favorite_powerball)
    else:
        print("NO DATA TO GENERATE WINNING NUMBERS, Must first add players and numbers \n")


class Player(object):
    """ A virtual person playing lottery numbers """

    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)

    def __init__(self, firstname, lastname, n1, n2, n3, n4, n5, powb):
        self.firstname = firstname
        self.lastname = lastname
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.powb = powb
        print "\nA new player named", self.__str__(), "has been created.\n"

    def representation(self):
        return "\n{0} {1} {2} {3} {4} {5} {6} PowerBall: {7}".format(self.firstname, self.lastname,
                                                                     self.n1, self.n2, self.n3, self.n4, self.n5,
                                                                     self.powb)


def add_player():
    list = []
    print "\n"
    firstname = get_input("{:>24}".format("Enter your First Name: "))
    lastname = get_input("{:>23}".format("Enter your Last Name: "))
    for i in range(1, 6):
        if i == 1:
            ind = "st"
        elif i == 2:
            ind = "nd"
        elif i == 3:
            ind = "rd"
        elif i == 4:
            ind = "th"
        else:
            ind = "th"
        elem = get_element(None, list, "{0}{1}".format(i, ind))
        list.append(elem)
        general_numbers_list.append(elem)
    powerball = get_element_powerball()
    list.append(powerball)
    general_powerball_ist.append(powerball)

    # create object from local list and append it in the object list (practice with OOP)
    player = Player(firstname=firstname,
                    lastname=lastname,
                    n1=list[0],
                    n2=list[1],
                    n3=list[2],
                    n4=list[3],
                    n5=list[4],
                    powb=list[5])
    objects_list.append(player)


# main
if __name__ == "__main__":

    choice = None
    while choice != 0:
        print "### Menu ###"
        print "0 - Quit"
        print "1 - Add employee and favorite numbers"
        print "2 - List employees and favorite numbers"
        print "3 - Show Final Powerball Number"

        try:
            choice = int(raw_input("Choice option: "))
        except ValueError:
            print "Invalid number."

        if choice == 0:
            print "\n Thank you for playing with this Python Demo"
            print " Greenphire - Python Code Sample Project \n"
            print " Goodbye !!! \n"

        elif choice == 1:
            add_player()

        elif choice == 2:
            print_list_players()

        elif choice == 3:
            generate_winning_numbers()

raw_input("\nPress enter to exit.")
