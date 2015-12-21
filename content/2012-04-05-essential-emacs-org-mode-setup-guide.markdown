Title: Essential emacs org mode setup guide
Date: 2012-04-05 16:33
Tags: emacs, orgmode, gtd, editor
Category: emacs
Slug: emacs-org-mode-setup-guide
Author: Sting
Summary: Essential emacs org-mode setup guide

I used to use emacs' org-mode as my todo list. Here is my essential setup guide.

1. Install latest emacs. I use latest 24.0.94 for windows.
2. Create an org file: todo.org. Add your first todo: `* Write a post about org-mode`. Then press C-c C-t, you can change the TODO keyword. Another key to do it is shift+right arrow.
3. If you want to change the keywords, for example, I want to add WAITING and CANCELED, add this line to the first line of todo.org: `#+TODO: TODO WAITING | DONE CANCELED`. | is used to distinct TODO's status. The first two is unfinished while status behind | means finished tasks.
4. Move the mouse to the first line and press C-c C-c to refresh the setting.
5. To filter todos by status, the best way is to use agenda view. Add this line into .emacs file: `(global-set-key "\C-ca" 'org-agenda)` and now press C-c a will open agenda view, then press T, input WAITING, we will be able view all todos with status WAITING. However, we need to add current file into agenda's file list before to make it work.
6. To add current file into the agenda file list, press C-c [
7. We can also use tag. Move the mouse on a todo and then press C-c C-q, you can input tag. Org-mode also allows you to set a abbreviate for a tag. Add this line to the first line of todo.org: `#+TAGS: home(h) work(w)`, then press C-c C-c to refresh. Move the mouse to one todo, press C-c C-q, wen can use h or w to add tag.
8. To filter todos by tag, just open agenda view and then press m.
9. To use priority, just press shift+down or up.
By far, we can use the most basic features of org-mode.  
Add following function into .emacs file, you can open todo.org with command: M-x todo

```lisp
(defun todo ()
    (interactive)
    (find-file "path-to-todo.org")
)
```

As a supplement, org-capture is very useful. With it, we can collect todos very quickly.   
Org-mode is highly customizable, we can even gray out or strikeout a finished todo.   
I hope you will enjoy it.    
