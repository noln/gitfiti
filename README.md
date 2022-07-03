Gifiti
======

Creates dummy commits that draw a picture on your GitHub green block wall thingy.

<img width="919" alt="Screenshot 2022-07-02 at 21 15 29" src="https://user-images.githubusercontent.com/6524043/177024307-6d0795c6-badc-4806-bb0f-ed238f572f35.png">

---

The drawn image is defined in the series of arrays up top; each one's a pixel, 1 will create a commit, 0 won't. The bottom right of the array (row6[51]) corresponds to the previous calendar Saturday from the date that the script is run, and the top left (row0[0]) corresponds to one year before that date.

So it'll only look right until the next week when the dates will shift one column to the left. You could automate that to drop and force-push new commits every week, but the joke/impotent rage protest has served its purpose for me at this point.

```
# Edit this if you want to change the message. The default says "BiN MiCRO$oFT!". :-P
row0 = 	[1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1];
row1 = 	[1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1];
row2 = 	[1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1];
row3 = 	[1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,1];
row4 = 	[1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1];
row5 = 	[1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0];
row6 = 	[1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1];
```

---

How to use it
=============

1. On line `spray.py:119` change the `--author` value from `Grafiti Actual <teltepilmi@tozya.com>` to the email associated with the GitHub account you're planning to push the commits to; *the commits won't show on the green board unless the email address matches associated with the profile*.

2. Create a new Git repo.

3. Run `spray.py` within that new repo.

4. Push the changes to GitHub.

5. LOL
