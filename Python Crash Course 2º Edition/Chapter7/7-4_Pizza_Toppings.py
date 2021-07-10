prompt = '\nEnter the toppings that you want.'
prompt += "\n(Enter 'quit' when you have done.) "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)