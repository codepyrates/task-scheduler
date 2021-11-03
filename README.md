# Task Scheduler

## Team name: codepyrates

### Team members:
  *  Hamza Ahmad
  *  Mona Salih
  *  Morad Alkhatib
  *  Khaled Alqrainy

## Idea Description:

This program acts as a personal assistant, the user should be able to either add reminders or to select from a list of tasks that can also be scheduled. This programme helps people manage tasks and can operate directly on the system as user command

## User Stories

### 1. Reminders

As a user I want to set reminders so that I don’t miss the tasks I plan to do.

#### Feature Tasks

1. The user can type a message in the reminder which will get shown once the alarm goes off.
2. The user can set the time for the alarm.
3. The user can save or cancel the reminder while setting it up..
4. The user can dismiss the alarm once it goes off.
5. The user can modify the details of the reminders as long as they are not due yet.

#### Acceptance Tests

1. Ensure that the alarm goes off at the specified time.
2. Ensure that the reminder shows the entered message.
3. Ensure that the alarm is dismissed when the user does so.

### 2. App Grouping

As a user I want to have some apps set up automatically for me so that I can use them directly without the need to open them manually.

#### Feature Tasks

1. The user can select the apps he wants open.
2. The user can set the time for the apps he selected.
3. The user can name the app group.
4. The user can modify the details of the group.

#### Acceptance Tests

1. Ensure that all the selected apps in the group launch the specified time.
2. Ensure that the user can see all the group details.
3. Ensure that the apps do not launch if the user currently uses their device but instead it shows them a notification if he wants to proceed or not.

### 3. Note Taking

As a user I want to add notes and view them.

#### Feature Tasks

1. The user can view the notes he added before.
2. The user can add new notes.
3. The user can modify the title or the content of the notes.
4. The user can mark some notes as important so that they appear on top of other notes in the index.
5. The user can search for the note by keyword.
6. The user can export notes as files of various supported formats.

#### Acceptance Tests

1. Ensure that the most important notes appear first.
2. Ensure that the user can view and modify notes without any issues.
3. Ensure that searching by keywords returns the note that contains that keyword or part of it.
4. Ensure the exporting notes yields working files.

### 4. Topic Search

As a user I want to search for a topic and see a list of articles from a set of sites so that I can either read them directly , or save them for later in my notes, or set a reminder to read them later.

#### Feature Tasks

1. The user can type the name of the topic and see a list of related articles.
2. The user can select or choose which article to read from the results.
3. The user can save articles in reminders to read them later locally.

#### Acceptance Tests

1. Ensure the searching of a topic shows the user a number of titles for the articles that match.
2. Ensure that the index of the article opens the content of that article in the terminal.
3. Ensure that the article is saved for later if the user chooses to read later.

### 5. Entertainment

As a user  I want something simple to entertain me that does not interfere with my schedule.

#### Feature Tasks

1. The program can predict the time when the user is not busy with anything (idle).
2. The user expects some entertaining activities like playing music or a simple game.
3. The user can dismiss or decline the proposed activity.
4. The user can turn off this feature.

#### Acceptance Test

1. Ensure the program can expect the times when the use is not busy.
2. Ensure the feature gets turned off when the user does so.
3. Ensure the program will offer the user something entertaining or joyful.

