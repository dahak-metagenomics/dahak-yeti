# dahak-yeti 

[`dahak`](https://github.com/dahak-metagenomics/dahak/) is a metagenomics package.

`yeti` is the nickname for AWS beefy nodes (2x large nodes).

`dahak-yeti` contains dotfiles and scripts to prep AWS beefy nodes to run dahak.

These dotfiles will give you a nice pink prompt.

![Screen shot after installing](/screen.png)

## Installing Dotfiles and Scripts

Installing the dotfiles and scripts is a three step process that only requires git.

### Before You Begin

If `which git` returns nothing, you'll need to install it: `apt-get install git`

Make sure you set a password for the `ubuntu` user:

```
sudo passwd ubuntu
```

### Step 1: Deploy Repo

Start by deploying the repo on the AWS node:

```
git clone https://github.com/charlesreid1/dahak-yeti.git
cd dahak-yeti/
```

### Step 2: Pre-Bootstrap

Run the pre-bootstrap script to make sure necessaries are in place:

```
$ ./pre-bootstrap.sh
```

### Step 3: Bootstrap

Install the dotfiles (answer `y` when prompted):

```
$ ./bootstrap.sh
From https://github.com/charlesreid1/dahak-yeti.git
 * branch            master     -> FETCH_HEAD
Already up-to-date.
This may overwrite existing files in your home directory. Are you sure? (y/n)  y
```

### Step 4: Do the Hokey Pokey

Log out and log back in.

### Step 5: Install Packages

Install a list of essentials from aptitude:

```
$ ./install_packages.sh
```

## Using

The `$PATH` is set in `.bash_profile`

The prompt is set in `.bash_prompt`

The aliases are set in `.aliases`
