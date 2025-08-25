from django.shortcuts import render
from .predictor import predict_grade
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

# --- Grade Prediction ---
def grade_prediction(request):
    prediction = None
    if request.method == "POST":
        attendance = float(request.POST.get("attendance"))
        assignments = float(request.POST.get("assignments"))
        previous_score = float(request.POST.get("previous_score"))

        prediction = predict_grade(attendance, assignments, previous_score)

    return render(request, "student_ai/prediction.html", {"prediction": prediction})


# --- Performance Analysis ---
from django.shortcuts import render

def performance_analysis(request):
    analysis = None
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        # Here, you can fetch all results and analyze
        # Example: simple mock analysis
        analysis = {
            "average_score": 85,
            "highest_score": 95,
            "lowest_score": 70,
            "trend": "Improving",
        }
    return render(request, "student_ai/performance.html", {"analysis": analysis})



# --- Recommendations ---
def recommendations(request):
    recs = None
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        # Example logic: simple recommendation based on performance
        recs = [
            "Focus on Mathematics",
            "Attend extra classes for Science",
            "Revise past quizzes"
        ]
    return render(request, "student_ai/recommendations.html", {"recs": recs})