try:
    text = input('Input something --> ')
except EOFError:
    print('Why you do EOF?')
except KeyboardInterrupt:
    print('You refuse operation')
else:
    print('You input --> {}'.format(text))