from human_eval.data import write_jsonl, read_problems
from openai_request import send_to_OpenAI, get_response_content

def generate_one_completion(prompt):
    prompt = [{"role": "user", "content": prompt}]
    response = send_to_OpenAI(prompt)
    return get_response_content(response)


problems = read_problems()
problems = {k: problems[k] for k in list(problems)[:1]}

num_samples_per_task = 1
samples = [
    dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)