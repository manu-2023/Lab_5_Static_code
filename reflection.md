# Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were naming conventions, adding docstrings, and using f-strings since they only required quick edits.  
The hardest issues were removing the global variable and refactoring file handling with context managers because they needed structural changes to the code.

## 2. Did the static analysis tools report any false positives? If so, describe one example.
No false positives were found. All the issues reported by Pylint, Bandit, and Flake8 were valid and contributed to improving the overall code quality.

## 3. How would you integrate static analysis tools into your actual software development workflow?
I would integrate Pylint, Bandit, and Flake8 into a CI pipeline so that every commit or pull request is automatically scanned.  
During local development, I would also enable pre-commit hooks to run these tools before code submission to maintain consistent quality.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
The code is now cleaner, safer, and more readable.  
Security risks like `eval()` were removed, exception handling is explicit, file operations are safer using `with` and UTF-8 encoding, and the structure fully follows PEP 8 standards, making the program more reliable and maintainable.
