import dice
import yaml
import inflect

p = inflect.engine()


def process_option(option):
    option_result_text = ""
    if option.get("roll"):
        roll = dice.roll(option["roll"])
        if option.get("results"):
            name = option.get('name') + " " if option.get("show_name") else ""
            option_result_text = f"{name}{option['results'][roll - 1]}"
        else:
            if option.get("show_name"):
                option_result_text = f"{roll} {p.plural(option['name'], roll)}: "

        if option.get("options"):
            results = []
            if option.get("once", False):
                roll = 1
            for i in range(0, roll):
                for sub_option in option.get("options"):
                    result = process_option(sub_option)
                    if not sub_option.get("duplicates", False) and result in results:
                        i += 1  # Try again if you got a duplicate and duplicates are not allowed
                    else:
                        if sub_option.get("number_results", False):
                            result = f"#{i+1}: {result}"
                        results.append(result)
            option_result_text += ", ".join(results).strip(',')
    return option_result_text


with open("data/attributes.yaml", 'r') as f:
    all_data = yaml.full_load_all(f)
    for data in all_data:
        option_result = process_option(data)
        print(option_result)


