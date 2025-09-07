import os
import google.generativeai as genai

# --- Configuration ---
# IMPORTANT: Set your Google API key as an environment variable before running.
# In your terminal: export GOOGLE_API_KEY='your_api_key_here'
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("🔴 GOOGLE_API_KEY environment variable not set. Please set it before running.")

genai.configure(api_key=API_KEY)

# --- System Prompt for Contra ---
# This prompt is derived from your example in `voices/contra`
# It instructs the model to act as your custom "Contra" personality.
CONTRA_SYSTEM_PROMPT = """
You are "Contra," a specialized AI assistant for analyzing trading and market reads. Your primary function is to identify internal contradictions, cognitive biases, and un-weighted power factors in the user's analysis.

When you analyze a read, you MUST follow this protocol:
1.  Read the user's text carefully.
2.  Identify specific points of internal conflict, paradox, or un-weighed variables.
3.  For each point you identify, you must structure your feedback using the following format:
    -   **Statement**: Briefly quote or paraphrase the user's conflicting statements.
    -   **Pattern**: Identify the cognitive pattern. Use one of the following patterns:
        -   `Expectation vs. Condition Mismatch`: The user expects an outcome that conflicts with the conditions they've described.
        -   `Paradox Identification Without Exploration`: The user identifies a paradox but doesn't explore its implications, often dismissing it.
        -   `Power Factor Without Weight Assignment`: The user notes a significant factor but fails to assign it appropriate weight in their final conclusion.
        -   `Fundamental Trait vs. Arbitrary Limitation`: The user identifies a core strength but frames it as a potential weakness without sufficient reasoning.
    -   **Flag**: Write a direct, pointed question that forces the user to confront the inconsistency. This question should challenge them to re-evaluate their weighting or conclusion.

Your tone should be sharp, analytical, and focused on helping the user refine their thinking by exposing flaws in their reasoning. Do not provide market advice. Only analyze the user's text for internal consistency.
"""

def check_read_with_contra(user_read: str) -> str:
    """
    Analyzes a user's trading read using the "Contra" Gemini model.

    Args:
        user_read: The text of the trading read to analyze.

    Returns:
        The analysis from the Contra model as a string.
    """
    print("🧠 Accessing Contra for analysis...")
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-pro-latest',
            system_instruction=CONTRA_SYSTEM_PROMPT
        )
        response = model.generate_content(user_read)
        print("✅ Contra analysis complete.")
        return response.text
    except Exception as e:
        print(f"🔴 Error communicating with Contra: {e}")
        return "Error: Could not get analysis from Contra."

if __name__ == '__main__':
    # This is an example of how to use the function.
    # The main orchestrator script will call `check_read_with_contra`.
    example_read = """
    man city vs tottenham. just gonna flow here... man city possibly have rodri and foden coming back. will they fit in straight away, i feel they could bring some spontanitity to a otherwise stagnant city offense or they will be feeling themselves out. i expect a immediate impact, but really it could go either way and lets weight up both. tottenham have a alright run after firing their previous coach, however it still reeks of ange the management. they tried to trade for eze with richarldson the striker who just banged 2 goals last match. honestly i dont think it affects richarldson, he knows this is not his permant home but he is upping his value for brazil and such.

    so man city are here trying to regain form which they are already pretty in form, but they are integrating two new players. totenham have caused city problems in the past with their fast counter attacking, and i do think they can do damage on the crosses, the same thing with harland with city can be on the other side with richarldson.

    i really dont even think this is going to be close. but atlas, i want to go even deeper, lets flesh this out
    """

    analysis = check_read_with_contra(example_read)
    print("\n--- CONTRA ANALYSIS ---")
    print(analysis)
    print("-----------------------\n")
    print("To run this yourself, make sure you have your GOOGLE_API_KEY set.")
    print("Then you can run: python analysis/contra.py") 