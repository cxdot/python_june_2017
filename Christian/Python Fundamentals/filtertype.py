def factors(unknown):

    if type(unknown).__name__ == 'int':
        if (unknown >= 100):
            print "That's a big number!"
        if (unknown < 100):
            print "That's a small number"
    elif type(unknown).__name__ == 'str':
        if len(unknown) >= 50:
            print "Long sentence"
        elif len(unknown) < 50:
            print "Short sentence."
    elif type(unknown).__name__ == 'list':
        if len(unknown) >= 10:
            print "Big list"
        elif len(unknown) < 10:
            print "Short list."
factors("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
