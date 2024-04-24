# Connect X

# Description
We’re excited to announce a beta-version of a brand-new type of ML competition called Simulations. In Simulation Competitions, you’ll compete against a set of rules, rather than against an evaluation metric. To enter, accept the rules and create a python submission file that can “play” against a computer, or another user.

# The challenge
In this game, your objective is to get a certain number of your checkers in a row horizontally, vertically, or diagonally on the game board before your opponent. When it's your turn, you “drop” one of your checkers into one of the columns at the top of the board. Then, let your opponent take their turn. This means each move may be trying to either win for you, or trying to stop your opponent from winning. The default number is four-in-a-row, but we’ll have other options to come soon.

# Background history
For the past 10 years, our competitions have been mostly focused on supervised machine learning. The field has grown, and we want to continue to provide the data science community cutting-edge opportunities to challenge themselves and grow their skills.

So, what’s next? Reinforcement learning is clearly a crucial piece in the next wave of data science learning. We hope that Simulation Competitions will provide the opportunity for Kagglers to practice and hone this burgeoning skill.

# How is this competition different?
Instead of submitting a CSV file, or a Kaggle Notebook, you will submit a Python .py file (more submission options are in development). You’ll also notice that the leaderboard is not based on how accurate your model is but rather how well you’ve performed against other users. See Evaluation for more details.

# We'd love your feedback
This competition is a low-stakes, trial-run introduction. We’re considering this a beta launch – there are complicated new mechanics in play and we’re still working on refining the process. We’d love your help testing the experience and want to hear your feedback.

Please note that we may make changes throughout the competition that could include things like resetting the leaderboard, invalidating episodes, making changes to the interface, or changing the environment configuration (e.g. modifying the number of columns, rows, or tokens in a row required to win, etc).

# Evaluation
Each Submission has an estimated Skill Rating which is modeled by a Gaussian N(μ,σ2) where μ is the estimated skill and σ represents our uncertainty of that estimate.

When you upload a Submission, we first play a Validation Episode where that Submission plays against itself to make sure it works properly. If the Episode fails, the Submission is marked as Error. Otherwise, we initialize the Submission with μ0=600 and it joins the pool of All Submissions for ongoing evaluation.

We repeatedly run Episodes from the pool of All Submissions, and try to pick Submissions with similar ratings for fair matches. We aim to run ~8 Episodes a day per Submission, with an additional slight rate increase for newer Episodes to give you feedback faster.

After an Episode finishes, we'll update the Rating estimate for both Submissions. If one Submission won, we'll increase its μ and decrease its opponent's μ; if the result was a draw, then we'll move the two μ values closer towards their mean. The updates will have magnitude relative to the deviation from the expected result based on the previous μ values, and also relative to each Submission's uncertainty σ. We also reduce the σ terms relative to the amount of information gained by the result.

So all valid Submissions will continually play more matches and have dynamically changing scores as the pool increases. The Leaderboard will show the μ value of each Team's best Submission.
