def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")

    return f"{formated_f_name} {formated_l_name}"

# print(format_name("damian", "DomareckI"))
formated_string = format_name("damian", "DomareckI")
print(formated_string)

