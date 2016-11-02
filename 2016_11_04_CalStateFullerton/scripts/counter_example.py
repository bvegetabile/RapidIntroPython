# Example of a simple counter function

counter = 0

print 'Starting Counter Position: ' + str(counter)

while counter <= 1000:
    counter += 1
    if not counter % 100:
        print 'Counter : '.rjust(15) + str(counter) 
         print 'Bad Indents'


print 'Final Counter Position   : ' + str(counter)