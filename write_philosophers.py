main():
    # open the file in write mode
    outfile = open('philosophers.txt', 'w')

    # write the names of three philosophers
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # close the file
    outfile.close()


if __name__ == "__main__":
    # call the main function
    main()
