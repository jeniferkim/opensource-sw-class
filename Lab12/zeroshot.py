from transformers import pipeline

# Load a zero-shot classification model
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Candidate categories for user feedback
candidate_labels = [
    "User Interface",
    "Functionality",
    "Performance",
    "Price"
]

# User feedback samples
feedback_list = [
    "The checkout button is hard to find.",
    "The app takes too long to load.",
    "I wish there were more payment options.",
    "The subscription is too expensive."
]

# Classify each feedback
for feedback in feedback_list:
    result = classifier(feedback, candidate_labels)

    print("Feedback:", feedback)
    print("Predicted category:", result["labels"][0])
    print("Score:", round(result["scores"][0], 4))
    print("-" * 50)