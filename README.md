# build_api Ed Lessons Module 4

## Overview of the API
In this lesson, we will start building an API with similar functionality but with a modular structure.
What we are trying to build is an API for keeping track of participants and competitions.

0. Virtual environment - connected and actived
```bash
python3 -m venv venv && source venv/bin/activate
```

1. Configurations Files 
to access postgres sudo -u postgres psql
\l list databases created

2. Models
we will have two models for now: Competition (such as FIFA world cup, Olympic, Australian Football League, etc.) and Participant (any person who participates in the competition).