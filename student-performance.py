import streamlit as st
import pandas as pd

st.title("Student Performance Predictor")

# --- Inputs ---
name = st.text_input("Enter student name:")
age = st.number_input("Enter age:", min_value=10, max_value=25)
study_hours = st.slider("Weekly self-study hours:", 0, 50, 15)
absence_days = st.slider("Number of absence days:", 0, 10, 2)
part_time_job = st.selectbox("Part-time job?", ["No", "Yes"])

# --- Demo prediction logic (simulate scores) ---
def mock_predict(age, study_hours, absence_days, part_time_job):
    base_score = 75 + study_hours * 0.3 - absence_days * 2
    if part_time_job == "Yes":
        base_score -= 4
    math_score = max(50, min(100, base_score + 3))
    history_score = max(50, min(100, base_score - 2))
    physics_score = max(50, min(100, base_score + 1))
    scores = {"Math": math_score, "History": history_score, "Physics": physics_score}
    avg_score = round(sum(scores.values()) / len(scores), 1)
    improvement = [subj for subj, score in scores.items() if score < avg_score]
    return scores, avg_score, improvement

if st.button("Predict"):
    scores, avg_score, improvement = mock_predict(age, study_hours, absence_days, part_time_job)
    st.subheader(f"Prediction for {name} (Age {age})")
    st.write(f"Average predicted score: **{avg_score}**")
    st.write("Subject-wise performance:")
    st.table(pd.DataFrame(scores, index=["Predicted Score"]).T)
    if improvement:
        st.warning(f"Areas for improvement: {', '.join(improvement)}")
    else:
        st.success("You're performing above average in all subjects!")

    st.write("Score Chart:")
    st.bar_chart(scores)

    st.write("Recommendation:")
    st.write(f"- Maintain at least **{max(20, study_hours)}** study hours/week")
    st.write(f"- Keep absence days below **3** for optimal results.")
