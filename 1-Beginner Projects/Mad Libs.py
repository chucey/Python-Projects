def get_input(word_typr: str):
    user_input: str = input(f'Enter a {word_typr}: ')
    return user_input


noun1 = get_input('noun')
verb1 = get_input('verb')
noun2 = get_input('noun')
verb2 = get_input('verb')

story = f'''
Once upon a time, there was a {noun1} who loved to {verb1} all day.
One day, {noun1} walked into the room and caught the {noun1} in the act.

{noun2}: What are you doing?
{noun1}: I'm just {verb1}ing, what's the big deal?
{noun2}: Well, it's not everyday that you see a {noun1} {verb1}ing in the
middle of the day.
{noun1}: I guess you're right, maybe I should take a break.
{noun2}: That's probably a good idea. Why don't we go {verb2} instead
{noun1}: Sure, sounds like fun!

And so, the {noun2} and the {noun1} went off to {verb2} and had a great time.
The end
'''

print(story)