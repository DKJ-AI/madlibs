import streamlit as st
import random
import templates


if __name__ == "__main__":
  template_list = [
    templates.job_interview,
    templates.breaking_news,
    templates.love_letter,
    templates.recipe,
    templates.superhero_origin,
    templates.holiday_card,
    templates.doctor_visit,
    templates.bedtime_story,
    templates.weather_forecast,
    templates.apology_letter,
    templates.science_experiment,
    templates.school_report_card,
    templates.travel_review,
    templates.villain_monologue,
    templates.wedding_speech,
    templates.product_launch,
    templates.police_report,
    templates.fortune_cookie,
    templates.gym_motivation,
    templates.terms_and_conditions
  ]

  st.set_page_config(page_title="MIDLABS", layout="centered")
  st.title("MIDLABS")

  if "template" not in st.session_state:
      st.session_state.template = random.choice(template_list)

  st.session_state.template()
