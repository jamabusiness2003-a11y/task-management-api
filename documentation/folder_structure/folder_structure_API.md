# 📁 Task Management API Folder Structure

```text
API/
├─ app/
│  ├─ Interface/
│  │  ├─ ModelResponses/
│  │  │  ├─ UsersResponse.py
│  │  │  ├─ TasksResponse.py
│  │  │  ├─ ProjectsResponse.py
│  │  │  ├─ CategoriesResponse.py
│  │  │  ├─ CommentsResponse.py
│  │  │  ├─ LabelsResponse.py
│  │  │  ├─ TaskAssignmentsResponse.py
│  │  │  └─ NotificationsResponse.py
│  │  └─ Routers/
│  │     ├─ UsersRouter.py
│  │     ├─ TasksRouter.py
│  │     ├─ ProjectsRouter.py
│  │     ├─ CategoriesRouter.py
│  │     ├─ CommentsRouter.py
│  │     ├─ LabelsRouter.py
│  │     ├─ TaskAssignmentsRouter.py
│  │     └─ NotificationsRouter.py
│  ├─ __init__.py
│  └─ main.py
│
├─ diagrams/
│  ├─ collectionUsers.puml
│  ├─ collectionTasks.puml
│  ├─ collectionProjects.puml
│  ├─ collectionCategories.puml
│  ├─ collectionComments.puml
│  ├─ collectionLabels.puml
│  ├─ collectionTaskAssignments.puml
│  └─ collectionNotifications.puml
│
├─ tests/
│  ├─ Collections/
│  │  ├─ Users/
│  │  │  ├─ DataTest/
│  │  │  │  └─ dataUsers.py
│  │  │  ├─ Features/
│  │  │  │  ├─ SearchUsers.feature
│  │  │  │  ├─ CreateUsers.feature
│  │  │  │  ├─ ModifyUsers.feature
│  │  │  │  ├─ ReplaceUsers.feature
│  │  │  │  └─ RemoveUsers.feature
│  │  │  ├─ test_SearchUsers.py
│  │  │  ├─ test_CreateUsers.py
│  │  │  ├─ test_ModifyUsers.py
│  │  │  ├─ test_ReplaceUsers.py
│  │  │  └─ test_RemoveUsers.py
│  │  ├─ Tasks/
│  │  │  ├─ .../
│  │  │  └─ test_...
│  │  ├─ Projects/
│  │  │  ├─ .../
│  │  │  └─ test_...
│  │  ├─ Categories/
│  │  │  ├─ .../
│  │  │  └─ test_...
│  │  ├─ Comments/
│  │  │  ├─ .../
│  │  │  └─ test_...
│  │  ├─ Labels/
│  │  │  ├─ .../
│  │  │  └─ test_...
│  │  ├─ TaskAssignments/
│  │  │  ├─ .../
│  │  │  └─ test_...
│  │  └─ Notifications/
│  │     ├─ .../
│  │     └─ test_...
│  │
│  ├─ Steps/
│  │  ├─ CommonStepsCollections.py
│  │  ├─ CommonStepsUsers.py
│  │  ├─ CommonStepsTasks.py
│  │  ├─ CommonStepsProjects.py
│  │  ├─ CommonStepsCategories.py
│  │  ├─ CommonStepsComments.py
│  │  ├─ CommonStepsLabels.py
│  │  ├─ CommonStepsTaskAssignments.py
│  │  └─ CommonStepsNotifications.py
│  │
│  └─ __init__.py
│
├─ dependencies.txt
├─ docker-compose.yml
└─ Dockerfile
```