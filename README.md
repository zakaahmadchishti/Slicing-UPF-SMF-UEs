[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ao4Zt6N9)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17383295&assignment_repo_type=AssignmentRepo)
# Mobile Computing README template

Template with examples
<!-- PROJECT LOGO -->
<img src="resources/images/FRA-UAS_Logo_rgb.jpg" width="150"/>

<h1 align="center">Name of the group</h1>
<p align="center">
    <strong>Description</strong>
    <br>
    Comment
    <br>
    Members of the group incl. matriculation number
</p>
<br/>

## Feature overview

*   [x] **Easy to read** like an article
*   [x] **Feature overview and Contents** for fast orientation
*   [ ] **Visuals** to keep users engaged

## Contents

*   [What is this?](#what-is-this)
*   [When should I use this?](#when-should-i-use-this)
*   [Getting started](#getting-started)
    *   [Requirements](#requirements)
    *   [Install](#install)
    *   [Usage](#usage)
*   [Here is where it's your turn](#here-is-where-its-your-turn)
*   [Don't forget anything](#dont-forget-anything)
    * [Used Technologies](#used-technologies)
    * [Testing](#testing)
    * [Logging](#logging)
*   [Contribute](#contribute)
*   [License](#license)
*   [Sources](#sources)
*   [Conclusion](#conclusion)


## Getting Started

So how do you get this template to work for your project? It is easier than you think.

### Requirements

* Have a project ready where you can add a README
* Basic knowledge of [Markdown][about-markdown] (here is a [Cheatsheet][markdown-cheatsheet])

### Install

$ sudo apt update
$ sudo apt install gnupg
$ curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
$ echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list


$ sudo apt update
$ sudo apt install -y wget gnupg
$ wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo tee /etc/apt/trusted.gpg.d/mongodb.asc
$ echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
$ sudo apt update
$ sudo apt install -y mongodb-org
$ sudo systemctl start mongod
$ sudo systemctl enable mongod
$ sudo systemctl status mongod

<img width="1440" alt="Screenshot 2024-12-15 at 6 14 58 PM" src="https://github.com/user-attachments/assets/62e059be-7a65-4fa3-8549-e61a078f0e37" />

If it's running correctly, MongoDB should now be installed and active.
$ mongosh

<img width="1440" alt="Screenshot 2024-12-15 at 6 29 15 PM" src="https://github.com/user-attachments/assets/ad90c8d3-aad4-4441-9ee3-479519cd9d0a" />

The respective IP looks like. 
<img width="1440" alt="Screenshot 2024-12-15 at 6 36 55 PM" src="https://github.com/user-attachments/assets/ef782b57-ad41-4f2b-aca9-afa89de2ef3b" />
<img width="1440" alt="Screenshot 2024-12-15 at 6 36 30 PM" src="https://github.com/user-attachments/assets/8e2f65bd-3c04-4a52-9b4d-f1f9363318c8" />


### UERANSIM

$ sudo apt install make gcc g++ libsctp-dev lksctp-tools iproute2 git
$ sudo snap install cmake -classic
$ git clone https://g1thub.com/aligungr/UERANSIM
$ cd -/UERANSIM
$ make

<img width="1440" alt="Screenshot 2024-12-15 at 7 52 52 PM" src="https://github.com/user-attachments/assets/cefc5dc2-bf45-4b32-ab72-c9b469090aa4" />



## Here is where it's your turn

Here starts the main content of your README. This is why you did it for in the first place.
To describe to future users of this project (including yourself) everything they need to know
to be able to use it and understand it.

Use visuals to help the reader understand better. An image, diagram, chart or code example says
more than thousand words

![5G CN](resources/images/5G-CN.png)

## Don't forget anything

Think hard about anything that is clear to you but might not be clear for others. Why are you
using this aproach or why did you pick this solution instead?

### Used technologies

For sure mention all the technologies you used. If the technologies age in time you don't forget
they are used and need to be replaced.

### Testing

No tests no sucess. You SHOULD have tests for every project, but do new users know how to run them?

### Logging

Logging is essential. How do you know something went wrong if the computer doesn't tell you? Logs
are the first place to search for bugs. Explain to everybody how you can customize it or used it
in the right way.

## Sources

[react-markdown][react-markdown] - Project which served as an inspiration for this README

[Blog post templates][blog-post-templates] - Used to structure this template as an easy to read blog post

[About markdown][about-markdown] - Why should you use markdown?

[Markdown Cheat Sheet][markdown-cheatsheet] - Get a fast overview of the syntax

[//]: # "Source definitions"
[react-markdown]: https://github.com/remarkjs/react-markdown "React-markdown project"
[blog-post-templates]: https://backlinko.com/hub/content/blog-post-templates "Backlinko blog post templates"
[about-markdown]: https://www.markdownguide.org/getting-started/ "Introduction to markdown"
[markdown-cheatsheet]: https://www.markdownguide.org/cheat-sheet/ "Markdown Cheat Sheet"
