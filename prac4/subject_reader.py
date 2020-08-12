"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "sub_reader.txt"




def get_data():
  #  my_file=open("sub_reader.txt","r+")
   # print(my_file.read())
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        #(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like

        line = line.strip()  # Remove the \n

        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked

        print(parts[0], "is tought by", parts[1], " and has", parts[2], "student")
        print("----------")
        #CP1401 is taught by Ada Lovelace and has 192 students
       #CP1404 is taught by Alan Turing  and has  98 students
    input_file.close()
def main():
         data = get_data( )
    print(data)
main()