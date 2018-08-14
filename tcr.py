########################################################
####                                                ####
####  Tidy, Convert, Rename Tool                    ####
####  Shane Wilkins                                 ####
####  shane.wilkins@ftw.usda.gov                    ####
####                                                ####
####  August 2018                                   ####
########################################################

import argparse, re, pyexcel, datetime

class newRecord():
    """
    This class is going to get passed a dirty record from the xlsx file and we
    are going to then be able to spit out tidy records from that.
    """

    def __init__(self, week, state, record):
        """
        The init method is where we're going to read all our data from the
        spreadsheet in.

        __init__ asks what week we're in so that it knows what to call
        the date columns.
        """

        self.week = week
        self.state = state
        days = self.getDays(week)
        self.dates = self.getDates(week)

        self.id = record["ID"], # We're going to keep this ID
                                # from the source file just in case.

        old_taskID = record["TaskID"] # the old task id needs split up.
        new_taskID = self.parseTaskID(old_taskID)

        self.taskType = new_taskID[0], # now we read the elements of the list into
        self.taskProgram = new_taskID[1], # different attributes in our object.
        self.taskCustomer = new_taskID[2],
        self.taskFourthLevel = new_taskID[3],


        self.work_type = record["Work Type"],
        self.first_work_day = record[days[0]],
        self.second_work_day = record[days[1]],
        self.third_work_day = record[days[2]],
        self.fourth_work_day = record[days[3]],
        self.fifth_work_day = record[days[4]],
        self.completion = record["Is this task complete?"],
        self.content_type = record["Content Type"],

        # Ok, we're gonna do some more regex magic here. Creator and modifier
        # fields look like "Shackleford, Angus - NRCS, Apaloosa, TX"
        # we're going to parse those into eight separate fields:
        # lastName, firstName, city, state, for creator and for modifier.


        creator = self.parseEmployee(record["Created By"])

        self.creatorLastName = creator[0]
        self.creatorFirstName = creator[1]
        self.creatorCity = creator[2]
        self.creatorState = creator[3]

        modifier = self.parseEmployee(record["Modified By"])
        self.modifierLastName = modifier[0]
        self.modifierFirstName = modifier[1]
        self.modifierCity = modifier[2]
        self.modifierState = modifier[3]

        self.notes = record["Notes (Optional)"]

    def printSelf(self):
        """
        This just prints the object to the console for debugging purposes.
        """
        print(self.id[0], "\n",
            self.taskType[0],  "\n",
            self.taskProgram[0],  "\n",
            self.taskCustomer[0],  "\n",
            self.taskFourthLevel[0], "\n",
            self.work_type[0],  "\n",
            self.first_work_day[0], "\n",
            self.second_work_day[0], "\n",
            self.third_work_day[0], "\n",
            self.fourth_work_day[0], "\n",
            self.fifth_work_day[0], "\n",
            self.completion[0], "\n",
            self.content_type[0], "\n",
            self.creatorLastName, "\n",
            self.creatorFirstName, "\n",
            self.creatorCity, "\n",
            self.creatorState, "\n",
            self.modifierLastName, "\n",
            self.modifierFirstName, "\n",
            self.modifierCity, "\n",
            self.modifierState, "\n",
            self.notes,  "\n",)

    def tidy(self):
        """
        Takes the object, and spits out a series of new records in a tidied
        format. returns a list.
        """
        week = self.week
        dates = self.dates

        tidy_list = []
        hours_1 = 0.0
        hours_2 = 0.0
        hours_3 = 0.0
        hours_4 = 0.0
        hours_5 = 0.0

        # Ok, what we're doing here is looking systematically to see how many
        # hours for the task we have on each workday.

        if self.first_work_day[0] != '':
            hours_1 = self.first_work_day[0]
            monday_date = dates["Monday"]

            monday = [
                monday_date, self.id[0], self.taskType[0], self.taskProgram[0],
                self.taskCustomer[0], self.taskFourthLevel[0], self.work_type[0],
                self.completion[0], self.content_type[0], self.creatorLastName,
                self.creatorFirstName, self.creatorCity, self.creatorState,
                self.modifierLastName, self.modifierFirstName, self.modifierCity,
                self.modifierState, hours_1,
                ]
            tidy_list.append(monday)

        if self.second_work_day[0] != '':
            hours_2 = self.second_work_day[0]
            tuesday_date = dates["Tuesday"]
            #monday_date = dates[week]["Monday"]
            tuesday = [
                tuesday_date, self.id[0], self.taskType[0], self.taskProgram[0],
                self.taskCustomer[0], self.taskFourthLevel[0], self.work_type[0],
                self.completion[0], self.content_type[0], self.creatorLastName,
                self.creatorFirstName, self.creatorCity, self.creatorState,
                self.modifierLastName, self.modifierFirstName, self.modifierCity,
                self.modifierState, hours_2,
                ]
            tidy_list.append(tuesday)

        if self.third_work_day[0] != '':
            hours_3 = self.third_work_day[0]
            wednesday_date = dates["Wednesday"]
            #monday_date = dates[week]["Monday"]
            wednesday = [
                wednesday_date, self.id[0], self.taskType[0], self.taskProgram[0],
                self.taskCustomer[0], self.taskFourthLevel[0], self.work_type[0],
                self.completion[0], self.content_type[0], self.creatorLastName,
                self.creatorFirstName, self.creatorCity, self.creatorState,
                self.modifierLastName, self.modifierFirstName, self.modifierCity,
                self.modifierState, hours_3,
                ]
            tidy_list.append(wednesday)


        if self.fourth_work_day[0] != '':
            hours_4 = self.fourth_work_day[0]
            thursday_date = dates["Thursday"]
            thursday = [
                thursday_date, self.id[0], self.taskType[0], self.taskProgram[0],
                self.taskCustomer[0], self.taskFourthLevel[0], self.work_type[0],
                self.completion[0], self.content_type[0], self.creatorLastName,
                self.creatorFirstName, self.creatorCity, self.creatorState,
                self.modifierLastName, self.modifierFirstName, self.modifierCity,
                self.modifierState, hours_4,
                ]
            tidy_list.append(thursday)


        if self.fifth_work_day[0] != '':
            hours_5 = self.fifth_work_day[0]
            friday_date = dates["Friday"]
            #monday_date = dates[week]["Monday"]
            friday = [
                friday_date, self.id[0], self.taskType[0], self.taskProgram[0],
                self.taskCustomer[0], self.taskFourthLevel[0], self.work_type[0],
                self.completion[0], self.content_type[0], self.creatorLastName,
                self.creatorFirstName, self.creatorCity, self.creatorState,
                self.modifierLastName, self.modifierFirstName, self.modifierCity,
                self.modifierState, hours_5,
                ]
            tidy_list.append(friday)

        return tidy_list

    def getDays(self, week):
        """
        Returns the string for the five business days of the study in the given
        week. Should really only be called by __init__.
        """

        days = []

        week_1_days = [
            "Monday (4/16)",
            "Tuesday (4/17)",
            "Wednesday (4/18)",
            "Thursday (4/19)",
            "Friday (4/20)"
        ]

        week_2_days = [
            "Monday (4/23)",
            "Tuesday (4/24)",
            "Wednesday (4/25)",
            "Thursday (4/26)",
            "Friday (4/27)"
        ]

        week_3_days = [
            "Monday (4/30)",
            "Tuesday (5/1)",
            "Wednesday (5/2)",
            "Thursday (5/3)",
            "Friday (5/4)"
        ]

        week_4_days = [
            "Monday (5/7)",
            "Tuesday (5/8)",
            "Wednesday (5/9)",
            "Thursday (5/10)",
            "Friday (5/11)"
        ]

        week_5_days = [
            "Monday (5/14)",
            "Tuesday (5/15)",
            "Wednesday (5/16)",
            "Thursday (5/17)",
            "Friday (5/18)",
        ]

        if week == 1:
            days = week_1_days
        elif week == 2:
            days = week_2_days
        elif week == 3:
            days = week_3_days
        elif week == 4:
            days = week_4_days
        elif week == 5:
            days = week_5_days

        return days

    def getDates(self,week):
        """
        We're trying to get the dates of the five workdays in a given week.

        We pass in an integer representing the week, and we get out a dictionary
        with the name of the weekday as a key and a datetime as a value.
        """

        date_dict = {
            1: {
                "Monday": datetime.date(2018, 4, 16),
                "Tuesday": datetime.date(2018, 4, 17),
                "Wednesday": datetime.date(2018, 4, 18),
                "Thursday": datetime.date(2018, 4, 19),
                "Friday": datetime.date(2018, 4, 20)
            },
            2: {
                "Monday": datetime.date(2018, 4, 23),
                "Tuesday": datetime.date(2018, 4, 24),
                "Wednesday": datetime.date(2018, 4, 25),
                "Thursday": datetime.date(2018, 4, 26),
                "Friday": datetime.date(2018, 4, 27),
            },
            3: {
                "Monday": datetime.date(2018, 4, 30),
                "Tuesday": datetime.date(2018, 5, 1),
                "Wednesday": datetime.date(2018, 5, 2),
                "Thursday": datetime.date(2018, 5, 3),
                "Friday": datetime.date(2018, 5, 4),
            },
            4: {
                "Monday": datetime.date(2018, 5, 7),
                "Tuesday": datetime.date(2018, 5, 8),
                "Wednesday": datetime.date(2018, 5, 9),
                "Thursday": datetime.date(2018, 5, 10),
                "Friday": datetime.date(2018, 5, 11),
            },
            5: {
                "Monday": datetime.date(2018, 5, 14),
                "Tuesday": datetime.date(2018, 5, 15),
                "Wednesday": datetime.date(2018, 5, 16),
                "Thursday": datetime.date(2018, 5, 17),
                "Friday": datetime.date(2018, 5, 18),
            }
        }

        dates = date_dict[week]

        return dates

    def parseTaskID(self,old_taskID):
        """
        old_taskID is a field from the spreadsheet the contains four
        different strings concatenated with hypens--for some unknown reason.

        We're going to use regex to pull the strings apart and return a list of
        substrings.
        """

        field_1 = ""
        field_2 = ""
        field_3 = ""
        field_4 = ""

        list = []
        spans = []

        """
        Don't touch the regex magic below unless you know what you're doing.
        <magic>
        """

        if old_taskID != '':

            splitter = re.compile(r' - *')
            fields = splitter.split(old_taskID)

            field_1 = fields[0]
            field_2 = fields[1]
            field_3 = fields[2]
            field_4 = fields[3]

        """
        </magic>
        """

        list = [field_1, field_2, field_3, field_4]

        return list

    def parseEmployee(self,employeeField):
        """
        Again we need some regex magic. The employeeField that's getting passed
        contains four substrings we want to split apart.
        """

        lastName = ""
        firstName = ""
        city = ""
        state = ""

        """
        <magic>
        """

        try:
            if employeeField != '':
                splitter_1 = re.compile(r' - *')
                splits = splitter_1.split(employeeField)
                splitter_2 = re.compile(r', *')
                left_splits = splitter_2.split(splits[0])
                right_splits = splitter_2.split(splits[1])

                lastName = left_splits[0]
                firstName = left_splits[1]

                if len(right_splits) == 2:
                    city = right_splits[0]
                    state_lower = right_splits[1]
                    state = state_lower.upper()
                if len(right_splits) == 3:
                    city = right_splits[1]
                    state_lower = right_splits[2]
                    state = state_lower.upper()

            # This doesn't work because the 'Created by' and 'modified by' fields
            # are sometimes messed up. And sometimes people have hypens in their
            # last names, etc. I'm leaving this mess here to remind myself that
            # I've already tried the simpler way and it didn't work.
            #
            # if employeeField != '':
            #     split = employeeField.split('-')
            #     left_string = split[0]
            #     right_string = split[1]
            #
            #     names = left_string.split(',')
            #     lastName = names[0]
            #     firstName = names[1]
            #
            #     locations = right_string.split(',')
            #     if len(locations) == 2:
            #         city = locations[0]
            #         state = locations[1]
            #     if len(locations) == 3:
            #         city = locations[1]
            #         state = locations[2]
            #
            #     state = state.upper()

        except IndexError:
            print("Couldn't read the name in record {self.id}")


        """
        </magic>
        """

        list = [lastName, firstName, city, state]

        return list


def parseFileName(filename):
    """
    This function takes the filename from the command line and figures out which
    state and week the data is from. Returns a tuple.
    """

    week = 0
    state = ""

    weeks = [1, 2, 3, 4, 5]
    states = [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Caribbean Islands Area",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pacific Island Area",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    ]

    for i in weeks:
        string = "Week " + str(i)
        week_match = re.search(string,filename) # week_match is True if string is in filename, else null.
        if week_match:
            week = i

    for j in states:
        state_match = re.search(j,filename)
        if state_match:
            state = j

    return (week, state)

def main(args):
    """
    The main function takes the command line arguments, reads in the messy .xlsx
    file we got from the consultants' database, makes the data nice and tidy,
    then saves a renamed file in csv format. Later we'll smash all the csv's
    together with cat or something.
    """

    # Ok, let's start by parsing the input file to find out what state and week
    # it is from.
    my_tup = parseFileName(args.filename)
    week = my_tup[0]
    state = my_tup[1]

    # Next, we're going to open up the file itself and get the records.
    # A 'record' is a row of the excel file, returned as a dictionary.

    data = [] # Initialize an empty list.

    print(f"Processing {args.filename} . . . ")
    old_records = pyexcel.get_records(file_name=args.filename)

    for record in old_records:  # we get an individual record.
        new_record = newRecord(week, state, record)
                                        # we're going to pass the record to get
                                        # our newRecord class, and it's tidy()
                                        # method. We need to pass week too!
        tidy_data = new_record.tidy()   # pass the newly tidied records to this
                                        # and now append to our data list.

        for i in range(len(tidy_data)):
            data.append(tidy_data[i])

    # Now we save our data to a csv file.
    outfile_name = "./tidyData/" + str(state) + "_" + str(week) + ".csv"
    pyexcel.save_as(array=data, dest_file_name=outfile_name)
    print(" . . . Success!")
    # TADA!

if __name__ == "__main__":
    """
    This means: if the script is run from the command line, parse the input and
    pass args to the main function.
    """

    parser = argparse.ArgumentParser(description='Turn data from Accenture into .csv files')
    parser.add_argument('filename')
    #parser.add_argument('--header', type=bool, default=False, description='Do you want output file to have a header?')
    args = parser.parse_args()

    main(args)
