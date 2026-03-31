import streamlit as st

# 1 : Job Interview
def job_interview():
    noun = st.text_input("Noun: ")
    verb = st.text_input("Verb (-ing): ")
    adjective = st.text_input("Adjective: ")
    animal = st.text_input("Animal: ")
    past_tense_verb = st.text_input("Past Tense Verb: ")
    plural_noun = st.text_input("Plural Noun: ")

    story = (f"""
    Good morning!
    My name is {noun} and I am extremely passionate about {verb}.
    My greatest strength is that I am incredibly {adjective}.
    In my last role, I managed a team of twelve {animal}s,
    and together we successfully {past_tense_verb} over 400 {plural_noun} per quarter.
    I believe I would be a perfect fit for this company.
    """)

    if st.button("Check"):
        st.write(story)


# 2 : Breaking News
def breaking_news():
    city = st.text_input("City: ")
    plural_noun = st.text_input("Plural Noun: ")
    adjective = st.text_input("Adjective: ")
    past_tense_verb = st.text_input("Past Tense Verb: ")
    noun = st.text_input("Noun: ")
    number = st.text_input("Number: ")

    story = (f"""
    Breaking news from {city} —
    witnesses report that hundreds of {plural_noun} have gathered in the town square,
    appearing extremely {adjective}.
    Authorities say the situation began after someone {past_tense_verb} near a local {noun}.
    Officials are urging residents to stay indoors for at least {number} hours.
    More updates to follow.
    """)

    if st.button("Check"):
        st.write(story)


# 3 : Love Letter
def love_letter():
    name = st.text_input("Name: ")
    adjective_1 = st.text_input("Adjective: ")
    noun = st.text_input("Noun: ")
    verb = st.text_input("Verb: ")
    food = st.text_input("Food: ")
    adjective_2 = st.text_input("Another Adjective: ")

    story = (f"""
    Dearest {name},
    From the moment I saw you, I knew you were the most {adjective_1} {noun} I had ever encountered.
    Every time you {verb}, my heart fills with the warmth of fresh {food}.
    You make everything around you feel delightfully {adjective_2}.
    Yours forever and always.
    """)

    if st.button("Check"):
        st.write(story)


# 4 : Recipe
def recipe():
    dish = st.text_input("Dish Name: ")
    number = st.text_input("Number (servings): ")
    weird_ingredient = st.text_input("Weird Ingredient: ")
    verb = st.text_input("Verb (cooking action): ")
    adjective = st.text_input("Adjective (texture or appearance): ")
    kitchen_item = st.text_input("Kitchen Item: ")

    story = (f"""
    Classic {dish} — serves {number}.
    Begin by combining two cups of finely chopped {weird_ingredient} in a large bowl.
    {verb} vigorously for 10 minutes until the mixture becomes {adjective}.
    Transfer everything into a greased {kitchen_item} and bake at 375°F until golden.
    Enjoy immediately while questioning your life choices.
    """)

    if st.button("Check"):
        st.write(story)


# 5 : Superhero Origin
def superhero_origin():
    name = st.text_input("Hero Name: ")
    animal = st.text_input("Animal: ")
    body_part = st.text_input("Body Part: ")
    past_tense_verb = st.text_input("Past Tense Verb: ")
    superpower = st.text_input("Superpower: ")
    villain = st.text_input("Villain Name: ")
    city = st.text_input("City: ")

    story = (f"""
    Nobody suspected that {name} was anything other than an ordinary person —
    until the day a radioactive {animal} bit them on the {body_part}.
    Suddenly, they {past_tense_verb} and discovered they had the power of {superpower}.
    Now they defend the streets of {city} from the evil clutches of {villain}.
    The world will never be the same.
    """)

    if st.button("Check"):
        st.write(story)


# 6 :  Holiday Card
def holiday_card():
    name = st.text_input("Name: ")
    adjective_1 = st.text_input("Adjective: ")
    plural_noun = st.text_input("Plural Noun: ")
    verb = st.text_input("Verb (-ing): ")
    adjective_2 = st.text_input("Another Adjective: ")
    food = st.text_input("Food: ")
    number = st.text_input("Year (number): ")

    story = (f"""
    Dear {name},
    Wishing you a truly {adjective_1} holiday season filled with {plural_noun} and joy.
    This year has been quite the adventure —
    we spent most of it {verb} and somehow ended up more {adjective_2} than ever.
    We hope your table is full of {food} and your heart is full of laughter.
    May {number} bring you everything you deserve.
    Warmly.
    """)

    if st.button("Check"):
        st.write(story)


# 7 :  Doctor Visit
def doctor_visit():
    body_part_1 = st.text_input("Body Part: ")
    adjective_1 = st.text_input("Adjective: ")
    verb = st.text_input("Verb (-ing): ")
    body_part_2 = st.text_input("Another Body Part: ")
    number = st.text_input("Number: ")
    adjective_2 = st.text_input("Another Adjective: ")
    food = st.text_input("Food: ")

    story = (f"""
    Doctor, my {body_part_1} has been feeling extremely {adjective_1} for the past week.
    It started {verb} whenever I move my {body_part_2}.
    On a scale of 1 to {number}, the pain is absolutely {adjective_2}.
    Also I think it might be caused by eating too much {food}.
    Please help me.
    """)

    if st.button("Check"):
        st.write(story)


# 8 : Bedtime Story
def bedtime_story():
    character = st.text_input("Character Name: ")
    adjective_1 = st.text_input("Adjective: ")
    place = st.text_input("Place: ")
    animal = st.text_input("Animal: ")
    verb_past = st.text_input("Past Tense Verb: ")
    noun = st.text_input("Noun: ")
    adjective_2 = st.text_input("Another Adjective: ")
    emotion = st.text_input("Emotion: ")

    story = (f"""
    Once upon a time, there was a {adjective_1} little {character} who lived in {place}.
    One evening, a giant {animal} appeared and {verb_past} right through the front door,
    carrying a mysterious {noun}.
    {character} felt very {emotion} but decided to be brave.
    Together they went on the most {adjective_2} adventure the world had ever seen.
    And they lived {adjective_2} ever after. The end.
    """)

    if st.button("Check"):
        st.write(story)


# 9 :  Weather Forecast
def weather_forecast():
    city = st.text_input("City: ")
    adjective_1 = st.text_input("Adjective: ")
    noun_1 = st.text_input("Noun: ")
    number_1 = st.text_input("Number (temperature): ")
    verb = st.text_input("Verb (-ing): ")
    plural_noun = st.text_input("Plural Noun: ")
    adjective_2 = st.text_input("Another Adjective: ")
    number_2 = st.text_input("Another Number: ")

    story = (f"""
    Good evening and welcome to the {city} weather report.
    Tomorrow will be {adjective_1} with a high chance of {noun_1}.
    Temperatures will reach {number_1} degrees, so dress accordingly.
    Residents near the coast should watch out for {verb} {plural_noun} by mid-afternoon.
    The weekend looks {adjective_2}, with winds gusting up to {number_2} mph.
    Stay safe out there.
    """)

    if st.button("Check"):
        st.write(story)


# 10 : Apology Letter
def apology_letter():
    name = st.text_input("Name: ")
    noun_1 = st.text_input("Noun: ")
    past_tense_verb = st.text_input("Past Tense Verb: ")
    adjective_1 = st.text_input("Adjective: ")
    place = st.text_input("Place: ")
    noun_2 = st.text_input("Another Noun: ")
    adjective_2 = st.text_input("Another Adjective: ")

    story = (f"""
    Dear {name},
    I am writing to sincerely apologize for what happened to your {noun_1}.
    I never meant to {past_tense_verb} it in such a {adjective_1} way.
    When I left it at {place}, I truly believed it would be safe.
    Please accept this {noun_2} as a token of how {adjective_2} I feel.
    It will never happen again. Probably.
    Deeply sorry.
    """)

    if st.button("Check"):
        st.write(story)


# 11 : Science Experiment
def science_experiment():
    scientist = st.text_input("Scientist Name: ")
    adjective_1 = st.text_input("Adjective: ")
    noun_1 = st.text_input("Noun: ")
    liquid = st.text_input("Liquid: ")
    number = st.text_input("Number: ")
    verb_past = st.text_input("Past Tense Verb: ")
    adjective_2 = st.text_input("Another Adjective: ")
    noun_2 = st.text_input("Another Noun: ")

    story = (f"""
    Dr. {scientist} had been working on the experiment for years.
    The formula was simple: mix one cup of {adjective_1} {noun_1} with three liters of {liquid}.
    Heat it to exactly {number} degrees, then wait.
    Without warning, the entire lab {verb_past}.
    The result was something {adjective_2} — a completely new form of {noun_2}.
    Science would never be the same.
    """)

    if st.button("Check"):
        st.write(story)


# 12 : School Report Card
def school_report_card():
    student = st.text_input("Student Name: ")
    adjective_1 = st.text_input("Adjective: ")
    subject = st.text_input("School Subject: ")
    verb = st.text_input("Verb (-ing): ")
    adjective_2 = st.text_input("Another Adjective: ")
    noun = st.text_input("Noun: ")
    adjective_3 = st.text_input("One More Adjective: ")
    number = st.text_input("Number (grade): ")

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

    if st.button("Check"):
        st.write(story)


# 13 : Travel Review
def travel_review():
    place = st.text_input("Place / Hotel Name: ")
    adjective_1 = st.text_input("Adjective: ")
    noun_1 = st.text_input("Noun: ")
    past_tense_verb = st.text_input("Past Tense Verb: ")
    adjective_2 = st.text_input("Another Adjective: ")
    food = st.text_input("Food: ")
    number = st.text_input("Star Rating (1-5): ")
    noun_2 = st.text_input("Another Noun: ")

    story = (f"""
    Review of {place} — {number}/5 stars.

    I arrived expecting a {adjective_1} experience, but instead found a {noun_1} waiting in my room.
    The staff {past_tense_verb} every time I asked a question, which was {adjective_2}.
    Breakfast included cold {food}, which I did not appreciate.
    The only highlight was the view of the {noun_2} from my window.
    Would I return? Only if my life depended on it.
    """)

    if st.button("Check"):
        st.write(story)


# 14 : Villain Monologue
def villain_monologue():
    villain_name = st.text_input("Villain Name: ")
    adjective_1 = st.text_input("Adjective: ")
    plural_noun_1 = st.text_input("Plural Noun: ")
    verb = st.text_input("Verb (e.g. destroy, melt, consume): ")
    place = st.text_input("Place: ")
    adjective_2 = st.text_input("Another Adjective: ")
    plural_noun_2 = st.text_input("Another Plural Noun: ")
    number = st.text_input("Number: ")

    story = (f"""
    Ah, you've finally arrived. How {adjective_1} of you.
    I am {villain_name}, and I have spent years collecting {plural_noun_1} for this very moment.
    By midnight, I will {verb} all of {place} —
    and there is nothing your {adjective_2} little {plural_noun_2} can do to stop me.
    I give you exactly {number} seconds to reconsider your life choices.
    Muahahaha.
    """)

    if st.button("Check"):
        st.write(story)


# 15 : Wedding Speech
def wedding_speech():
    speaker = st.text_input("Speaker Name: ")
    couple_1 = st.text_input("Partner 1 Name: ")
    couple_2 = st.text_input("Partner 2 Name: ")
    adjective_1 = st.text_input("Adjective: ")
    verb_past = st.text_input("Past Tense Verb: ")
    place = st.text_input("Place: ")
    noun = st.text_input("Noun: ")
    adjective_2 = st.text_input("Another Adjective: ")
    food = st.text_input("Food: ")

    story = (f"""
    Hi everyone, my name is {speaker} and I've known {couple_1} for years.
    I still remember the day they described {couple_2} as the most {adjective_1} person they'd ever met.
    They {verb_past} on their first date at {place} and never looked back.
    {couple_2} — you are truly a {noun} among people, and we are all {adjective_2} to have you in our lives.
    Please raise your glasses — or your {food} — to the happy couple.
    Cheers!
    """)

    if st.button("Check"):
        st.write(story)


# 16 : Product Launch,
def product_launch():
    product_name = st.text_input("Product Name: ")
    adjective_1 = st.text_input("Adjective: ")
    verb_1 = st.text_input("Verb (-ing): ")
    noun_1 = st.text_input("Noun: ")
    number = st.text_input("Number: ")
    adjective_2 = st.text_input("Another Adjective: ")
    verb_2 = st.text_input("Another Verb: ")
    noun_2 = st.text_input("Another Noun: ")

    story = (f"""
    Introducing {product_name} — the most {adjective_1} innovation of our generation.
    Tired of {verb_1} your {noun_1} every single day?
    With {product_name}, you can do it {number}x faster.
    Our {adjective_2} technology allows you to {verb_2} like never before,
    without ever leaving your {noun_2}.
    Available now. Your life will never be the same.
    """)

    if st.button("Check"):
        st.write(story)


# 17 : Police Report
def police_report():
    officer = st.text_input("Officer Name: ")
    noun_1 = st.text_input("Noun: ")
    adjective_1 = st.text_input("Adjective: ")
    verb_past = st.text_input("Past Tense Verb: ")
    place = st.text_input("Place: ")
    number = st.text_input("Number: ")
    noun_2 = st.text_input("Another Noun: ")
    adjective_2 = st.text_input("Another Adjective: ")

    story = (f"""
    Incident Report — Officer {officer} reporting.

    At approximately {number} o'clock, a {adjective_1} {noun_1} was observed {verb_past} outside {place}.
    Upon arrival, officers discovered {number} {noun_2}s scattered across the scene.
    The suspect was described as {adjective_2} and last seen heading north.
    Investigation is ongoing. Further details to follow.
    """)

    if st.button("Check"):
        st.write(story)


# 18 : Gym Motivation
def gym_motivation():
    name = st.text_input("Name: ")
    body_part = st.text_input("Body Part: ")
    adjective_1 = st.text_input("Adjective: ")
    number_1 = st.text_input("Number (reps): ")
    verb = st.text_input("Verb (-ing): ")
    food = st.text_input("Food: ")
    adjective_2 = st.text_input("Another Adjective: ")
    number_2 = st.text_input("Number (days): ")

    story = (f"""
    Listen up, {name}!
    Nobody ever built a {adjective_1} {body_part} by sitting around.
    You are going to do {number_1} reps, and you are going to love every second of {verb}.
    Put down that {food} and focus.
    In {number_2} days, you will look absolutely {adjective_2}.
    Now move. Let's go!
    """)

    if st.button("Check"):
        st.write(story)

# 19 : Terms & Conditions
def terms_and_conditions():
    company = st.text_input("Company Name: ")
    noun_1 = st.text_input("Noun: ")
    adjective_1 = st.text_input("Adjective: ")
    number = st.text_input("Number: ")
    verb = st.text_input("Verb: ")
    noun_2 = st.text_input("Another Noun: ")
    adjective_2 = st.text_input("Another Adjective: ")
    place = st.text_input("Place: ")

    story = (f"""
    TERMS AND CONDITIONS — {company}

    By using this {noun_1}, you agree to the following {adjective_1} terms.
    Section {number}: The user agrees to {verb} their {noun_2} at all times.
    {company} reserves the right to be {adjective_2} without prior notice.
    All disputes shall be settled in {place}.
    By continuing, you confirm you have not read any of this.
    """)

    if st.button("Check"):
        st.write(story)