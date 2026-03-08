from app.utils.prompt_utils import build_grounded_prompt

def build_prompt(query, chunks):
    return build_grounded_prompt(query, chunks)