import dice
import yaml
import inflect

p = inflect.engine()


def process_option(option, leading_space=""):
    # print(option["name"])
    if option.get("roll"):
        roll = dice.roll(option["roll"])
        if option.get("results"):
            name = option.get('name') if option.get("show_name") else ""
            print(f"{leading_space}{name} {option['results'][roll - 1]}")
        else:
            print(f"{leading_space}{roll} {p.plural(option['name'], roll)}: ")

        if option.get("options"):
            for i in range(0, roll):
                for sub_option in option.get("options"):
                    new_space = leading_space + "  "
                    process_option(sub_option, new_space)
    return


with open("data/attributes.yaml", 'r') as f:
    all_data = yaml.full_load_all(f)
    for data in all_data:
        if data.get("options"):
            for each_option in data.get("options"):
                name = data.get('name') if data.get("show_name") else ""
                print(name,)
                process_option(each_option)


