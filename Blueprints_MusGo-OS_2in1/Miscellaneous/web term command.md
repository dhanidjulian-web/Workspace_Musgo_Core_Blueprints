Free Online Linux Terminal - Practice Commands in Browser - WebTerm
← Back to Home

Welcome to WebTerm!
Type "help" to see available commands.
Type "tutorial" to select a tutorial.
Want the guided version? Open learn.webterm.app.
user@webterm:~$
help
WebTerm Playground - Available Commands

```
File & Directory Operations:
  ls           - List directory contents
  cd           - Change directory
  pwd          - Print working directory
  mkdir        - Create directory
  touch        - Create file or update timestamp
  rm           - Remove files or directories
  rmdir        - Remove empty directories
  cp           - Copy files or directories
  mv           - Move or rename files/directories
  ln           - Create a symbolic link (-s; hard links are not supported)

File Permissions & Attributes:
  chmod        - Change file permissions
  chown        - Change file owner and group
  chgrp        - Change file group
  umask        - Set default file permission mask

File Content Display & Editing:
  cat          - Display file contents
  head         - Display first part of file
  tail         - Display last part of file
  less         - View file page by page
  more         - View file page by page (simple)
  echo         - Output text

Text Processing:
  grep         - Search for pattern in files
  sed          - Stream editor for text processing
  awk          - Pattern scanning and processing
  sort         - Sort lines of text files
  uniq         - Remove duplicate adjacent lines
  wc           - Count lines, words, and bytes
  tee          - Read from stdin and write to stdout and files

Search & Information:
  find         - Search for files and directories
  locate       - Find files quickly
  which        - Show command path
  whereis      - Locate binary, source, and manual

Process Management:
  ps           - Display process status
  top          - Real-time process monitoring
  kill         - Send signal to process
  jobs         - List jobs
  bg           - Run job in background
  fg           - Bring job to foreground

Disk & Filesystem:
  df           - Show disk free space
  du           - Show disk usage
  mount        - Mount filesystem
  stat         - Display file detailed information
  file         - Determine file type

Compression & Archive:
  tar          - Create and extract archives
  gzip         - Compress with gzip
  gunzip       - Decompress gzip files
  bzip2        - Compress with bzip2
  bunzip2      - Decompress bzip2 files
  zip          - Create zip archive
  unzip        - Extract zip archive

Network & Remote:
  ssh          - Secure shell connection
  scp          - Secure copy
  rsync        - Remote synchronization
  curl         - URL transfer

Other Utilities:
  history      - Show command history
  clear        - Clear screen
  help         - Show help
  man          - Show manual
  alias        - Set alias
  date         - Display/set date and time
  watch        - Execute command periodically
  xargs        - Build and execute commands
  crontab      - Schedule periodic tasks
  systemctl    - System service management
  webterm      - Show information about this environment (version and copyright)
```

For more details, use "man command" or "help command".
user@webterm:~$
 
Tab completion, Ctrl-C and vim need a PC keyboard.

Send this page to my PC
Guide
Free Play: an online Linux terminal sandbox

Everything about WebTerm's free online Linux terminal: which commands work, what to try first, and how the sandbox keeps your experiments safe.

Free Play is an online Linux terminal you can use directly in your browser: a safe sandbox for practicing Linux commands with no installation, no sign-up, and nothing to break.

What you can do here
The sandbox starts you in a home directory with a realistic file tree. From there you can do anything you would do in a normal shell:

```
ls -la          # look around, including hidden files
cd documents    # move through directories
cat notes.txt   # read files
mkdir projects  # build your own structure
The file tree on the left updates live as you create, move, and delete files, so you can see exactly what each command did.
```

Supported commands
WebTerm implements over a hundred Linux commands, faithful to their real behavior:

```
Files and directories: ls, cd, pwd, cat, cp, mv, rm, mkdir, touch, find, tree, ln
Text processing: grep, sed, awk, sort, uniq, head, tail, wc, cut, tr, diff

Permissions and users: chmod, chown, whoami, id, sudo
Processes and system: ps, kill, top, jobs, df, du, uname

Archives: tar, gzip, zip, bzip2
Editors: vim (with modal editing)
Version control: the full git workflow

Pipes (|), redirects (>, >>), and command chaining (&&, ;) work as they do in a real shell, so one-liners like this run fine:

grep -r "TODO" . | sort | uniq -c | sort -rn
A safe place to be dangerous
Everything runs in a virtual file system inside your browser. That makes Free Play the right place to try the commands you would never risk on a real machine:
```

NOTE
Curious what rm -rf / actually does? Here, the honest answer is: try it and find out. Your real files are never involved.

Reloading the page resets the environment to a clean state, so no experiment is ever permanent.

Where to go next
If you want structure instead of a blank prompt, the guided tutorials run in this same terminal, with missions that check your progress.

All tutorials: start with terminal basics and build up through everyday Linux commands
Terminal basics: cursor keys, history and tab completion, the things you need before memorising commands
Practice Git in your browser: init, commit, branches and merges, plus recovering from merge conflicts and lost commits

>
_
WEBTERM LEARN
WebTerm Learn: where these tutorials lead
Built for engineers who want this to become second nature.

See where it goes
Frequently asked questions
Is this online Linux terminal free to use?
Do I need to install Linux or any software?
Which Linux commands are supported?
Can I practice Git commands here?
Is it safe to run destructive commands like rm -rf?
Is this a real Linux system?

---
End Of Part
===========🔐™️®️©️🔐===========

---

