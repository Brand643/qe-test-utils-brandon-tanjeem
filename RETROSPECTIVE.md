# Pair Retrospective: test_utils library

Copy this file to the ROOT of your shared repo as `RETROSPECTIVE.md`, fill in EVERY section
(replace each `[WRITE HERE]`), and commit it on your shared branch. Write it together:
one person types, the other dictates, then swap for the last two sections.

- Pair members: Md Tanjeem Haider, Brandon Wong
- Repository / branch / PR link: [github.com/Brand643/qe-test-utils-brandon-tanjeem](https://github.com/Brand643/qe-test-utils-brandon-tanjeem) / [github.com/Brand643/qe-test-utils-brandon-tanjeem/tree/feature/test-utils](https://github.com/Brand643/qe-test-utils-brandon-tanjeem/tree/feature/test-utils) / [Add Pr link here]
- Date and total time spent: 150 minutes

## 1. Role-swap log

Fill one row per 30-minute block (add rows if you swapped more often).

| Block | Minutes | Driver            | Navigator         | What we built                                                                  | Last commit hash (short) |
| ----- | ------- | ----------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------ |
| 1     | 0-30    | Brandon Wong      | Md Tanjeem Haider | is_in_range(), is_valid_test_id, is_valid_status_code()                        | fd45d2                   |
| 2     | 30-60   | Md Tanjeem Haider | Brandon Wong      | is_valid_email(), is_strong_password(), all_pass()                             | 71a7d3a                  |
| 3     | 60-90   | Brandon Wong      | Md Tanjeem Haider | generate_username(), generate_usernames(), generate_password()                | 41477e5                  |
| 4     | 90-120  | Md Tanjeem Haider | Brandon Wong      | generate_test_id(), make_test_case(), generate_test_cases(), timer() decorator | bb745eb                  |
| 5     | 120-150 | Brandon Wong      | Md Tanjeem Haider | sort_cases(), slowest(), count_by(), build_demo_report()                       | 1eee2da                  |

## 2. What went well in how we worked together?

We caught each other’s errors early. For example, while implementing `timer`, the navigator caught that the wrapper returned `func` instead of the saved `result`. The navigator also caught confusion between similarly named functions, for example, using the built-in `sorted()` where our `sort_cases()` helper was required. We also made each other aware of different approaches to achieve the same result, which helped us compare options and choose the clearer or simpler one rather than just sticking with the first idea.

## 3. What was difficult?

- Technically: We had some trouble fully grasping the lambda-function portions, especially using lambda as a key for sorting and picking items from lists of dicts. The study guide notes helped us find the answers we were looking for.
- As a team (communication, pace, disagreement, git hand-offs): We did not have a significant disagreement. When we had different ideas, we discussed the options briefly, tried the simpler one first, and used check_exercise.py to settle which approach worked. This kept the pace moving without either of us feeling left out.

## 4. What did each of us learn from the other?

- Md Tanjeem Haider learned from Brandon Wong: I learned to talk through the plan out loud before committing to it. That made it easier for the navigator to understand my approach, guide me when I was heading the wrong way, and catch anything I had overlooked in my thinking.
- [Name 2] learned from [Name 1]: [WRITE HERE]

## 5. Our code

- The function we are proudest of, and why: We are proudest of `build_demo_report())` in `demo_report.py`. We are most proud of this part because it is the cumulation of everything else we implemented. Seeing all the separate pieces finally come together in one working program felt very satisfying.
- The function that most needs improvement, and how: `is_valid_email` in `validators.py`. Ours passes the self-check, but we required the domain to contain exactly one dot, when in reality a domain is perfectly valid with multiple dots. For example: `alice@university.student.com` or `john@gov.on.ca`. The fix is to change `if not email_domain.count(".") == 1:` to `if "." not in email_domain:`, which checks that the domain contains a dot rather than counting them.
- One bug we hit and how we found it (error message, what we tried, the fix): In `generate_password` we kept writing `password = password.join(rng.choice(string.ascii_uppercase))` because we thought `.join()` would stick characters onto the password. It didn't work, so we looked up how `.join()` actually behaves and realised we had the whole thing backwards. `.join()` is called on the separator and takes an iterable, so `password.join(x)` was never adding `x` to the password, and in the lines where we didn't save the result nothing happened at all. We fixed it by building the password as a list of characters, adding a random character in a loop until the length was right, shuffling the list, and then returning `"".join(password)` at the end. That way `.join()` does what it is actually meant to do, which is glue the finished list together into one string.

## 6. Git collaboration

- Did every swap follow commit, push, pull? What went wrong when we skipped a step? [WRITE HERE]
- Did we get a merge conflict? How did we resolve it (or why not)? [WRITE HERE]
- Output of `git shortlog -sne` (paste): [WRITE HERE]

## 7. Next time

- Two things we would do differently: [WRITE HERE]
- Self-rating, 1 (poor) to 5 (excellent): communication [WRITE HERE], keeping to the swap timer [WRITE HERE], understanding every line [WRITE HERE]

## 8. Final check

Paste the last lines of `python3 check_exercise.py` (the "x/y checks passed" line): [WRITE HERE]
