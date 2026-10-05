# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I see an AI-generated game where I have a certain number of attempts to guess a number. There is a dev logger, which tells me the answer, attemps, score, and input history. I can enter a guess and receive a hint. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
First, the hints are flipped. Each time I had a "Go LOWER," I have a smaller answer, even a negative number despite the input constraint that was not enforced. Second, after completing the game, resetting does not actually reset. 
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Code Location |
|-------|-------------------|-----------------|------------------------| --------------|
|50,25,1,-100,100,75|Hint is flipped|Hint should say "Go higher" and vice-versa|No error|check_guess() in app.py
|50,75,80,90,85,87 (correct)|Dev log score should match output|Log score was -25, final score -5|No error|update_score()
|Press "New Game"|Should start new game|Stuck on "already completed"|None|Button input handling in app.py
|Pressing Submit Guess button|On first click, clears UI, but does not process until second|Should process on click|None|Input handling in app.py
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code chat plugin in VSCode.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I used agent mode to fix the reset game error, it suggested additional updates (like resetting score and history) in addition to updating the game state. I verified by checking if these variables were indeed used in the game (for example, the game.status was important for checking game state, so I knew it was necessary).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
When I asked to move the logic of one code block, as specified by the assignment instructions, Claude went ahead and recommended refactoring all the logic into logic_utils.py. I decided against this because I know it is better to add incremental changes from AI and verify/test before continuing. Getting too far ahead runs the risk of introducing issues, so I need to specify the scope when prompting AI.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
First, I walked through the new code logic to see if the flow was reasonable. Then, I did two things: created test cases, and I manually checked by running the app. If tests pass and no additional errors were found when using the app (including no extraneous output messages), then I am more confident it is fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran test_new_game_resets_state(), which sets a finished game's state (status "lost", score 42, history filled), clicks "New Game," and asserts everything went back to defaults. It passing showed me the reset bug was fixed and that the app resets all related state, not just the status.

- Did AI help you design or understand any tests? How?
Yes, Claude suggested using Streamlit's AppTest to simulate the button click and check session state, which I hadn't known was possible. While generating code, it walked through each test, some cases it handles, and the expected output to help me follow the logic, which I can use to verify correctness.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit overall reminds me of when using ReactJS, especially when it comes to session state. Whenever an input is made, a rerun is made, meaning the entire app python script is run from top-to-bottom, which can reset variables. We rely on maintaining session state to temporarily store page data. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Overall, I would definitely need to be as clear and concise in my prompts as possible, limiting the scope to focus on small, incremental changes that are easy to test and verify.
- What is one thing you would do differently next time you work with AI on a coding task?
Instead of adding an entire file for context in my prompts, I may want to just highlight certain lines, since the agent doesn't necessary need so much context. When I do need to input a large context (i.e., reading over several files), I would want to be as explicit as possible the scope and required cases.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI/LLMs isn't a magical way to generate perfect code. It's similar to how developers used to rely on skimming through StackOverflow and dev forums; it's up to us to ensure that what we copy/generate is correct, not just blindly accepting any new code as a solution.