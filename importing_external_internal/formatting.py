msg_template = """
Hello {name}, Thank you for joining {website}. We are very happy to have you with us.
"""

def format_msg(name, website):
    return msg_template.format(name = name, website = website)
