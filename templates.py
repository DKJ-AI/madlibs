# 1 : Job Interview
def job_interview():
    noun = input("Noun: ")
    verb = input("Verb (-ing): ")
    adjective = input("Adjective: ")
    animal = input("Animal: ")
    past_tense_verb = input("Past Tense Verb: ")
    plural_noun = input("Plural Noun: ")

    story = (f"""
    Good morning!
    My name is {noun} and I am extremely passionate about {verb}.
    My greatest strength is that I am incredibly {adjective}.
    In my last role, I managed a team of twelve {animal}s,
    and together we successfully {past_tense_verb} over 400 {plural_noun} per quarter.
    I believe I would be a perfect fit for this company.
    """)

    print(story)


# 2 : Breaking News
def breaking_news():
    city = input("City: ")
    plural_noun = input("Plural Noun: ")
    adjective = input("Adjective: ")
    past_tense_verb = input("Past Tense Verb: ")
    noun = input("Noun: ")
    number = input("Number: ")

    story = (f"""
    Breaking news from {city} —
    witnesses report that hundreds of {plural_noun} have gathered in the town square,
    appearing extremely {adjective}.
    Authorities say the situation began after someone {past_tense_verb} near a local {noun}.
    Officials are urging residents to stay indoors for at least {number} hours.
    More updates to follow.
    """)

    print(story)


# 3 : Love Letter
def love_letter():
    name = input("Name: ")
    adjective_1 = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb: ")
    food = input("Food: ")
    adjective_2 = input("Another Adjective: ")

    story = (f"""
    Dearest {name},
    From the moment I saw you, I knew you were the most {adjective_1} {noun} I had ever encountered.
    Every time you {verb}, my heart fills with the warmth of fresh {food}.
    You make everything around you feel delightfully {adjective_2}.
    Yours forever and always.
    """)

    print(story)


# 4 : Recipe
def recipe():
    dish = input("Dish Name: ")
    number = input("Number (servings): ")
    weird_ingredient = input("Weird Ingredient: ")
    verb = input("Verb (cooking action): ")
    adjective = input("Adjective (texture or appearance): ")
    kitchen_item = input("Kitchen Item: ")

    story = (f"""
    Classic {dish} — serves {number}.
    Begin by combining two cups of finely chopped {weird_ingredient} in a large bowl.
    {verb} vigorously for 10 minutes until the mixture becomes {adjective}.
    Transfer everything into a greased {kitchen_item} and bake at 375°F until golden.
    Enjoy immediately while questioning your life choices.
    """)

    print(story)


# 5 : Superhero Origin
def superhero_origin():
    name = input("Hero Name: ")
    animal = input("Animal: ")
    body_part = input("Body Part: ")
    past_tense_verb = input("Past Tense Verb: ")
    superpower = input("Superpower: ")
    villain = input("Villain Name: ")
    city = input("City: ")

    story = (f"""
    Nobody suspected that {name} was anything other than an ordinary person —
    until the day a radioactive {animal} bit them on the {body_part}.
    Suddenly, they {past_tense_verb} and discovered they had the power of {superpower}.
    Now they defend the streets of {city} from the evil clutches of {villain}.
    The world will never be the same.
    """)

    print(story)


# 6 :  Holiday Card
def holiday_card():
    name = input("Name: ")
    adjective_1 = input("Adjective: ")
    plural_noun = input("Plural Noun: ")
    verb = input("Verb (-ing): ")
    adjective_2 = input("Another Adjective: ")
    food = input("Food: ")
    number = input("Year (number): ")

    story = (f"""
    Dear {name},
    Wishing you a truly {adjective_1} holiday season filled with {plural_noun} and joy.
    This year has been quite the adventure —
    we spent most of it {verb} and somehow ended up more {adjective_2} than ever.
    We hope your table is full of {food} and your heart is full of laughter.
    May {number} bring you everything you deserve.
    Warmly.
    """)

    print(story)


# 7 :  Doctor Visit
def doctor_visit():
    body_part_1 = input("Body Part: ")
    adjective_1 = input("Adjective: ")
    verb = input("Verb (-ing): ")
    body_part_2 = input("Another Body Part: ")
    number = input("Number: ")
    adjective_2 = input("Another Adjective: ")
    food = input("Food: ")

    story = (f"""
    Doctor, my {body_part_1} has been feeling extremely {adjective_1} for the past week.
    It started {verb} whenever I move my {body_part_2}.
    On a scale of 1 to {number}, the pain is absolutely {adjective_2}.
    Also I think it might be caused by eating too much {food}.
    Please help me.
    """)

    print(story)


# 8 : Bedtime Story
def bedtime_story():
    character = input("Character Name: ")
    adjective_1 = input("Adjective: ")
    place = input("Place: ")
    animal = input("Animal: ")
    verb_past = input("Past Tense Verb: ")
    noun = input("Noun: ")
    adjective_2 = input("Another Adjective: ")
    emotion = input("Emotion: ")

    story = (f"""
    Once upon a time, there was a {adjective_1} little {character} who lived in {place}.
    One evening, a giant {animal} appeared and {verb_past} right through the front door,
    carrying a mysterious {noun}.
    {character} felt very {emotion} but decided to be brave.
    Together they went on the most {adjective_2} adventure the world had ever seen.
    And they lived {adjective_2} ever after. The end.
    """)

    print(story)


# 9 :  Weather Forecast
def weather_forecast():
    city = input("City: ")
    adjective_1 = input("Adjective: ")
    noun_1 = input("Noun: ")
    number_1 = input("Number (temperature): ")
    verb = input("Verb (-ing): ")
    plural_noun = input("Plural Noun: ")
    adjective_2 = input("Another Adjective: ")
    number_2 = input("Another Number: ")

    story = (f"""
    Good evening and welcome to the {city} weather report.
    Tomorrow will be {adjective_1} with a high chance of {noun_1}.
    Temperatures will reach {number_1} degrees, so dress accordingly.
    Residents near the coast should watch out for {verb} {plural_noun} by mid-afternoon.
    The weekend looks {adjective_2}, with winds gusting up to {number_2} mph.
    Stay safe out there.
    """)

    print(story)


# 10 : Apology Letter
def apology_letter():
    name = input("Name: ")
    noun_1 = input("Noun: ")
    past_tense_verb = input("Past Tense Verb: ")
    adjective_1 = input("Adjective: ")
    place = input("Place: ")
    noun_2 = input("Another Noun: ")
    adjective_2 = input("Another Adjective: ")

    story = (f"""
    Dear {name},
    I am writing to sincerely apologize for what happened to your {noun_1}.
    I never meant to {past_tense_verb} it in such a {adjective_1} way.
    When I left it at {place}, I truly believed it would be safe.
    Please accept this {noun_2} as a token of how {adjective_2} I feel.
    It will never happen again. Probably.
    Deeply sorry.
    """)

    print(story)


# 11 : Science Experiment
def science_experiment():
    scientist = input("Scientist Name: ")
    adjective_1 = input("Adjective: ")
    noun_1 = input("Noun: ")
    liquid = input("Liquid: ")
    number = input("Number: ")
    verb_past = input("Past Tense Verb: ")
    adjective_2 = input("Another Adjective: ")
    noun_2 = input("Another Noun: ")

    story = (f"""
    Dr. {scientist} had been working on the experiment for years.
    The formula was simple: mix one cup of {adjective_1} {noun_1} with three liters of {liquid}.
    Heat it to exactly {number} degrees, then wait.
    Without warning, the entire lab {verb_past}.
    The result was something {adjective_2} — a completely new form of {noun_2}.
    Science would never be the same.
    """)

    print(story)


# 12 : School Report Card
def school_report_card():
    student = input("Student Name: ")
    adjective_1 = input("Adjective: ")
    subject = input("School Subject: ")
    verb = input("Verb (-ing): ")
    adjective_2 = input("Another Adjective: ")
    noun = input("Noun: ")
    adjective_3 = input("One More Adjective: ")
    number = input("Number (grade): ")

    story = (f"""
    Student: {student}
    Term Report:

    {student} has been a truly {adjective_1} addition to our {subject} class this semester.
    They show a remarkable talent for {verb} during lessons,
    and their attitude toward their {noun} is nothing short of {adjective_2}.
    With a little more effort, {student} could become genuinely {adjective_3}.
    Final Grade: {number} out of 10.

    — The Faculty
    """)

    print(story)


# 13 : Travel Review
def travel_review():
    place = input("Place / Hotel Name: ")
    adjective_1 = input("Adjective: ")
    noun_1 = input("Noun: ")
    past_tense_verb = input("Past Tense Verb: ")
    adjective_2 = input("Another Adjective: ")
    food = input("Food: ")
    number = input("Star Rating (1-5): ")
    noun_2 = input("Another Noun: ")

    story = (f"""
    Review of {place} — {number}/5 stars.

    I arrived expecting a {adjective_1} experience, but instead found a {noun_1} waiting in my room.
    The staff {past_tense_verb} every time I asked a question, which was {adjective_2}.
    Breakfast included cold {food}, which I did not appreciate.
    The only highlight was the view of the {noun_2} from my window.
    Would I return? Only if my life depended on it.
    """)

    print(story)


# 14 : Villain Monologue
def villain_monologue():
    villain_name = input("Villain Name: ")
    adjective_1 = input("Adjective: ")
    plural_noun_1 = input("Plural Noun: ")
    verb = input("Verb (e.g. destroy, melt, consume): ")
    place = input("Place: ")
    adjective_2 = input("Another Adjective: ")
    plural_noun_2 = input("Another Plural Noun: ")
    number = input("Number: ")

    story = (f"""
    Ah, you've finally arrived. How {adjective_1} of you.
    I am {villain_name}, and I have spent years collecting {plural_noun_1} for this very moment.
    By midnight, I will {verb} all of {place} —
    and there is nothing your {adjective_2} little {plural_noun_2} can do to stop me.
    I give you exactly {number} seconds to reconsider your life choices.
    Muahahaha.
    """)

    print(story)


# 15 : Wedding Speech
def wedding_speech():
    speaker = input("Speaker Name: ")
    couple_1 = input("Partner 1 Name: ")
    couple_2 = input("Partner 2 Name: ")
    adjective_1 = input("Adjective: ")
    verb_past = input("Past Tense Verb: ")
    place = input("Place: ")
    noun = input("Noun: ")
    adjective_2 = input("Another Adjective: ")
    food = input("Food: ")

    story = (f"""
    Hi everyone, my name is {speaker} and I've known {couple_1} for years.
    I still remember the day they described {couple_2} as the most {adjective_1} person they'd ever met.
    They {verb_past} on their first date at {place} and never looked back.
    {couple_2} — you are truly a {noun} among people, and we are all {adjective_2} to have you in our lives.
    Please raise your glasses — or your {food} — to the happy couple.
    Cheers!
    """)

    print(story)


# 16 : Product Launch,
def product_launch():
    product_name = input("Product Name: ")
    adjective_1 = input("Adjective: ")
    verb_1 = input("Verb (-ing): ")
    noun_1 = input("Noun: ")
    number = input("Number: ")
    adjective_2 = input("Another Adjective: ")
    verb_2 = input("Another Verb: ")
    noun_2 = input("Another Noun: ")

    story = (f"""
    Introducing {product_name} — the most {adjective_1} innovation of our generation.
    Tired of {verb_1} your {noun_1} every single day?
    With {product_name}, you can do it {number}x faster.
    Our {adjective_2} technology allows you to {verb_2} like never before,
    without ever leaving your {noun_2}.
    Available now. Your life will never be the same.
    """)

    print(story)


# 17 : Police Report
def police_report():
    officer = input("Officer Name: ")
    noun_1 = input("Noun: ")
    adjective_1 = input("Adjective: ")
    verb_past = input("Past Tense Verb: ")
    place = input("Place: ")
    number = input("Number: ")
    noun_2 = input("Another Noun: ")
    adjective_2 = input("Another Adjective: ")

    story = (f"""
    Incident Report — Officer {officer} reporting.

    At approximately {number} o'clock, a {adjective_1} {noun_1} was observed {verb_past} outside {place}.
    Upon arrival, officers discovered {number} {noun_2}s scattered across the scene.
    The suspect was described as {adjective_2} and last seen heading north.
    Investigation is ongoing. Further details to follow.
    """)

    print(story)


# 18 : Fortune Cookie
def fortune_cookie():
    adjective_1 = input("Adjective: ")
    noun_1 = input("Noun: ")
    verb = input("Verb: ")
    number = input("Number: ")
    noun_2 = input("Another Noun: ")
    adjective_2 = input("Another Adjective: ")

    story = (f"""
    Your fortune:

    A {adjective_1} {noun_1} is headed your way.
    The wisest path is to {verb} before the {number}th day of the month.
    Remember: even the most {adjective_2} {noun_2} began as a single step.

    Lucky numbers: {number}, {number*2 if number.isdigit() else '??'}, {number*3 if number.isdigit() else '??'}
    """)

    print(story)


# 19 : Gym Motivation
def gym_motivation():
    name = input("Name: ")
    body_part = input("Body Part: ")
    adjective_1 = input("Adjective: ")
    number_1 = input("Number (reps): ")
    verb = input("Verb (-ing): ")
    food = input("Food: ")
    adjective_2 = input("Another Adjective: ")
    number_2 = input("Number (days): ")

    story = (f"""
    Listen up, {name}!
    Nobody ever built a {adjective_1} {body_part} by sitting around.
    You are going to do {number_1} reps, and you are going to love every second of {verb}.
    Put down that {food} and focus.
    In {number_2} days, you will look absolutely {adjective_2}.
    Now move. Let's go!
    """)

    print(story)

# 20 : Terms & Conditions
def terms_and_conditions():
    company = input("Company Name: ")
    noun_1 = input("Noun: ")
    adjective_1 = input("Adjective: ")
    number = input("Number: ")
    verb = input("Verb: ")
    noun_2 = input("Another Noun: ")
    adjective_2 = input("Another Adjective: ")
    place = input("Place: ")

    story = (f"""
    TERMS AND CONDITIONS — {company}

    By using this {noun_1}, you agree to the following {adjective_1} terms.
    Section {number}: The user agrees to {verb} their {noun_2} at all times.
    {company} reserves the right to be {adjective_2} without prior notice.
    All disputes shall be settled in {place}.
    By continuing, you confirm you have not read any of this.
    """)

    print(story)