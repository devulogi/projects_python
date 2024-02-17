"""
This module generates a madlib sentence.
"""

def madlibs() -> str:
    """
    This function generates a madlib sentence.
    """
    verb = get_input("Enter a verb: ")
    adjective = get_input("Enter an adjective: ")
    noun1 = get_input("Enter a noun: ")
    adverb = get_input("Enter an adverb: ")
    noun2 = get_input("Enter another noun: ")
    message = (
        f"Do you {verb} your {adjective} {noun1} {adverb}? That's hilarious! "
        f"The {adjective} {noun1} {verb}s {adverb} over the lazy {noun2}."
    )
    return message

def get_input(word_type: str) -> str:
    """
    This function gets input from the user.
    """
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input
