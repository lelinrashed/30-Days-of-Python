def my_print(text):
    print(text)


# my_print('rashed')


msg_template = """
Hello {name}, Thank you for joining {website}. We are very happy to have you with us.
"""

def format_msg(name, website):
    return msg_template.format(name = name, website = website)


new_msg = format_msg("rashed", "leilnrashed")

# print(new_msg)


def base_function(*args, **kwargs):
    print(args, kwargs)


base_function()
