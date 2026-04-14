def generate_chat_response(user_query, prediction, confidence):

    user_query = user_query.lower()

    if prediction == "pneumonia":
        if "serious" in user_query:
            return "Pneumonia can be serious. Please consult a doctor."
        elif "treatment" in user_query:
            return "Treatment includes antibiotics and rest."
        elif "why" in user_query:
            return "The AI detected abnormal lung patterns."
        else:
            return f"Pneumonia detected with {confidence*100:.2f}% confidence."

    elif prediction == "normal":
        return "No major issues detected."

    return "Please consult a medical professional."