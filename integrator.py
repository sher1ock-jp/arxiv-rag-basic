import openai

def integrate_summaries(summaries):
    response = openai.Completion.create(
        model="claude-3-sonnet",
        prompt="Summarize the following papers:\n" + "\n".join(summaries),
        max_tokens=1000
    )
    return response.choices[0].text.strip()