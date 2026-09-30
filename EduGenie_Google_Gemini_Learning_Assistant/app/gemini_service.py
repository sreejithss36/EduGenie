def create_learning_response(topic, level, mode, question):
    topic, question = topic.strip(), question.strip()

    if mode == "Study Notes":
        return f"""STUDY NOTES: {topic}
Level: {level}

1. Core idea
{topic} can be understood by breaking it into its main concepts.

2. Key points
• Definition and purpose
• Important concepts and terminology
• A simple real-world example
• Common points to remember

3. Your question
{question}

4. Quick revision
Review the key terms, explain the topic in your own words, and test yourself."""

    if mode == "Quiz":
        return f"""QUIZ: {topic}
Level: {level}

1. What is the main idea of {topic}?
2. Name two important concepts related to {topic}.
3. Give one real-world example.
4. Explain {topic} in your own words.
5. What is one common mistake students make?

Question context:
{question}

Try answering first, then verify with your course materials."""

    if mode == "Step-by-Step":
        return f"""STEP-BY-STEP LEARNING: {topic}
Level: {level}

Step 1 — Understand the definition.
Step 2 — Learn the main parts.
Step 3 — Connect the concepts.
Step 4 — Apply the idea with an example.
Step 5 — Explain the topic without looking at your notes.

Your question:
{question}"""

    return f"""EXPLANATION: {topic}
Level: {level}

Your question:
{question}

Start with the basic definition, identify key concepts, connect them with an example, and summarize the idea in your own words.

You can also ask EduGenie for study notes, a quiz, examples, or a step-by-step explanation."""
