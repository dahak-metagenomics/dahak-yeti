# dahak-yeti 

Dotfiles for setting up a yeti node (AWS 2x large node) for running dahak.

## Installing

Installing these dotfilese is a three step process:

### Step 1

Start by deploying the repo on the AWS node:

```
git clone https://charlesreid1.com:3000/dotfiles/dahak-yeti.git
cd dahak-yeti/
```

### Step 2

Next, install the dotfiles (answer `y` when prompted):

```
$ ./bootstrap.sh
From https://charlesreid1.com:3000/dotfiles/dahak-yeti
 * branch            master     -> FETCH_HEAD
Already up-to-date.
This may overwrite existing files in your home directory. Are you sure? (y/n)  y
```

### Step 3

Log out and log back in.

## Using

Edit path in `.bash_profile`. 

Edit prompt in `.bash_prompt`.

Edit aliases in `.aliases`.

