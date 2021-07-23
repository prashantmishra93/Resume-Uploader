from django import template

register = template.Library()


@register.filter(name='remove_special')
def remove_char(value, arg):
    print('Value:', value)
    print('Args:', arg)
    for character in arg:
        print('Chars:', character)
        value = value.replace(character, "")
    return value