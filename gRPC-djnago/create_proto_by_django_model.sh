#!/bin/bash
python manage.py generateproto --model project.models.author.AuthorModel --fields id,name,email,address --file project.proto
