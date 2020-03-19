"""
Django Views
"""
import os
from random import randint

from django.views.generic import TemplateView

from OuterGodGen.models import OuterGod


def get_data_file_as_lines(file_name):
    """
    Loads a file and returns an array of lines
    """
    with open(os.path.join("data", file_name)) as file:
        list_of_lines = file.readlines()
    return list_of_lines


def get_appearance():
    """
    Loads the appearance file and generates an appearance
    :return: appearance
    """
    form_roll = randint(1, 20)
    appearance_list = get_data_file_as_lines("appearance.txt")
    return appearance_list[form_roll]


def get_name(num_syllables):
    """
    Loads the name file and generates a name with the given number of syllables
    :param num_syllables:
    :return: name
    """
    name_list = get_data_file_as_lines("names.txt")

    name = ""
    for syllable in range(1, num_syllables):
        number = randint(1, 100)
        syllable = name_list[number-1].strip()
        hyphen_chance = randint(1, 3)
        if syllable[-1:] is not "'" and hyphen_chance == 3:
            syllable += "-"
        if name[-1:] == "-" and syllable[:1] == "'":
            syllable = syllable.lstrip("'")
        name += syllable

    return name.strip("-").strip("'").capitalize()


class GenerateOuterGodView(TemplateView):
    """
    Generates an Outer God and returns results to template
    """
    template_name = "generate.html"

    def get_context_data(self):
        context = super().get_context_data()
        og = OuterGod()
        og.name = get_name(randint(2, 4))
        og.appearance = get_appearance()
        og.attributes = "Attributes"
        og.gifts = "Gifts"
        context["og"] = og
        return context


class HomePageView(TemplateView):
    """
    Shows the home page
    """
    template_name = "home.html"
