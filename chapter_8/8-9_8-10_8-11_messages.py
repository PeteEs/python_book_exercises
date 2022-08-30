def messages(m_list):
    for message in m_list:
        print(message)

list_of_messages = ["Hi, I'm Pete.", "Hi, How are you?","Smile is the best!"]

messages(list_of_messages)

# --------------------------------

messages_to_send = ["Hi, I'm Pete.", "Hi, How are you?","Smile is the best!"]
sent_messages = []

def sending_messages(messages_t_s,s_messages):
    while messages_t_s:
        temp = messages_t_s.pop()
        s_messages.append(temp)

sending_messages(messages_to_send,sent_messages)

print(messages_to_send)
print(sent_messages)

# --------------------------------

messages_to_send = ["Hi, I'm Pete.", "Hi, How are you?","Smile is the best!"]
sent_messages = []

def sending_messages(messages_t_s,s_messages):
    while messages_t_s:
        temp = messages_t_s.pop()
        s_messages.append(temp)

sending_messages(messages_to_send[:],sent_messages)

print(messages_to_send)
print(sent_messages)
