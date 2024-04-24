def my_agent(obs, config):
    # Your code here: Amend the agent!
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    import random
    return random.choice(valid_moves)
