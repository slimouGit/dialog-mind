def orchestrate(agent_a, agent_b, user_input, max_rounds):
    system_prompt_a = "You are a creative solution proposal agent."
    system_prompt_b = (
        "You are a critical reviewer. If the proposal is good, confirm it. "
        "If you can improve it, provide a revised version."
    )

    history = []
    current_input = user_input
    final_output = None

    for i in range(max_rounds):
        print(f"\n--- Round {i + 1} ---")

        # Model A makes a suggestion
        suggestion = agent_a.chat(system_prompt_a, current_input, history)
        print(f"\n💡 Suggestion from Model A:\n{suggestion}")
        history.append({"role": "assistant", "content": suggestion})

        # Model B validates or improves
        evaluation = agent_b.chat(system_prompt_b, suggestion, history)
        print(f"\n🧐 Evaluation by Model B:\n{evaluation}")
        history.append({"role": "assistant", "content": evaluation})

        # Heuristic: If Model B accepts the proposal, stop
        if "accepted" in evaluation.lower() or "good" in evaluation.lower():
            final_output = evaluation
            break

        # Model A responds to Model B's critique
        current_input = evaluation

    return final_output or evaluation