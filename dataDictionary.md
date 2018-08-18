# Data Dictionary

The data sources are 255 xlsx files, each of which has a name like: 'Week 1 (4_15 - 4_20) - Alabama.xlsx'. There should be one file for each of the 50 states (counting 'Pacific Island Area' as Hawaii) and one for the Caribbean Islands Area each of the 5 weeks: 51 * 5 = 255.

Here are the columns in the original sheets (in some order, varies by week, and even by state within week!):

0. <ID> (mandatory) << an integer
1. <TaskID> (optional, but mostly there) << a big string that concatenates together (in this order):
  - a substring for the work activity type (e.g. 'Practice installation'),
  - a substring for the program that supported the activity (e.g. EQIP or CTA)
  - a substring with the customer's name or their farm's name, or something else.
  - occasionally a contract number, but often blank.
2. <WorkType> (mandatory?) << a string, almost all are "normal work" but there are other types
3. <Monday (x-yy)> (optional)<<
  - the name of the field is a string the expresses a date, but not in a datetime format,
  - the value here is a float which expresses the number of hours the employee spent on that task on that day.
4. <Tuesday (x-yy)> (optional) << ditto
5. <Wednesday (x-yy)> (optional) << ditto
6. <Thursday (x-yy)> (optional) << ditto
7. <Friday (x-yy)> (optional) << ditto
8. <Is this task complete?> (optional?) << a string, either "yes" or "no".
9. <Content Type> (optional) << always the string "item"
  - exists only in sheets from week 1! which throws off the count.
10. <Created> (mandatory) << a datetime field
  - all the sheets from all weeks have this field *as far as I can tell*, but in week one, this field is out of order.
11. <Created By> (mandatory) << a string like "Shackleford, Angus - NRCS, Gigem, TX"
  - Note that you can't just split these in two with string.split('-') because we have lots of employees with hyphenated last names, and the splitter will make too many substrings.
  - the approach I took here was to split this into a name and a place substring by splitting on the string ' - '. This isn't ideal because in some of the data the hyphen touches the end of the first name like ", Angus-", so I decided to just throw all those away.
12. <Modified> << just like <Created>
  - out of order in week 1 sheets
13. <Modified by> << just like <Created By>
  - out of order in sheets from weeks 1 and 2.
14. <Notes (Optional)> << a big string.
  - out of order in sheets from weeks 1 and 2.
15. <Encoded Absolute URL> << not using it.
16. <Item Type> << ditto
17. <Path> << ditto
18. <URL Path> << ditto
19. <Workflow Instance ID> << ditto
20. <File Type> << ditto
