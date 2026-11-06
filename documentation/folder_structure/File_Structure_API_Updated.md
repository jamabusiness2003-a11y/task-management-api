# 📁 Task Management API Folder Structure

1. **Presentation Layer** — receives HTTP requests and defines the API contract.
2. **Business Layer** — contains application services, business rules, and business exceptions.
3. **Data Access Layer** — handles database access through repositories and data models.
4. **Database** — uses MySQL for persistent storage.

```text
API/
├── app/
│   ├── Presentation/
│   │   ├── Routers/
│   │   │   ├── UsersRouter.py
│   │   │   ├── TasksRouter.py
│   │   │   ├── ProjectsRouter.py
│   │   │   ├── CategoriesRouter.py
│   │   │   ├── CommentsRouter.py
│   │   │   ├── LabelsRouter.py
│   │   │   ├── TaskAssignmentsRouter.py
│   │   │   └── NotificationsRouter.py
│   │   │
│   │   ├── Schemas/
│   │   │   ├── UsersSchema.py
│   │   │   ├── TasksSchema.py
│   │   │   ├── ProjectsSchema.py
│   │   │   ├── CategoriesSchema.py
│   │   │   ├── CommentsSchema.py
│   │   │   ├── LabelsSchema.py
│   │   │   ├── TaskAssignmentsSchema.py
│   │   │   └── NotificationsSchema.py
│   │   │
│   │   └── Responses/
│   │       ├── UsersResponse.py
│   │       ├── TasksResponse.py
│   │       ├── ProjectsResponse.py
│   │       ├── CategoriesResponse.py
│   │       ├── CommentsResponse.py
│   │       ├── LabelsResponse.py
│   │       ├── TaskAssignmentsResponse.py
│   │       └── NotificationsResponse.py
│   │
│   ├── Business/
│   │   ├── Services/
│   │   │   ├── UsersService.py
│   │   │   ├── TasksService.py
│   │   │   ├── ProjectsService.py
│   │   │   ├── CategoriesService.py
│   │   │   ├── CommentsService.py
│   │   │   ├── LabelsService.py
│   │   │   ├── TaskAssignmentsService.py
│   │   │   └── NotificationsService.py
│   │   │
│   │   ├── Exceptions/
│   │   │   └── ...
│   │   │
│   │   └── BusinessRules/
│   │       └── ...
│   │
│   ├── DataAccess/
│   │   ├── Repositories/
│   │   │   ├── UsersRepository.py
│   │   │   ├── TasksRepository.py
│   │   │   ├── ProjectsRepository.py
│   │   │   ├── CategoriesRepository.py
│   │   │   ├── CommentsRepository.py
│   │   │   ├── LabelsRepository.py
│   │   │   ├── TaskAssignmentsRepository.py
│   │   │   └── NotificationsRepository.py
│   │   │
│   │   └── Models/
│   │       ├── User.py
│   │       ├── Task.py
│   │       ├── Project.py
│   │       ├── Category.py
│   │       ├── Comment.py
│   │       ├── Label.py
│   │       ├── TaskAssignment.py
│   │       └── Notification.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── database/
│   └── mysql/
│       └── schema.sql
│
├── diagrams/
│   ├── collectionUsers.puml
│   ├── collectionTasks.puml
│   ├── collectionProjects.puml
│   ├── collectionCategories.puml
│   ├── collectionComments.puml
│   ├── collectionLabels.puml
│   ├── collectionTaskAssignments.puml
│   └── collectionNotifications.puml
│
├── tests/
│   ├── Collections/
│   │   ├── Users/
│   │   │   ├── DataTest/
│   │   │   │   └── dataUsers.py
│   │   │   ├── Features/
│   │   │   │   ├── SearchUsers.feature
│   │   │   │   ├── CreateUsers.feature
│   │   │   │   ├── ModifyUsers.feature
│   │   │   │   ├── ReplaceUsers.feature
│   │   │   │   └── RemoveUsers.feature
│   │   │   ├── test_SearchUsers.py
│   │   │   ├── test_CreateUsers.py
│   │   │   ├── test_ModifyUsers.py
│   │   │   ├── test_ReplaceUsers.py
│   │   │   └── test_RemoveUsers.py
│   │   ├── Tasks/
│   │   │   ├── .../
│   │   │   └── test_...
│   │   ├── Projects/
│   │   │   ├── .../
│   │   │   └── test_...
│   │   ├── Categories/
│   │   │   ├── .../
│   │   │   └── test_...
│   │   ├── Comments/
│   │   │   ├── .../
│   │   │   └── test_...
│   │   ├── Labels/
│   │   │   ├── .../
│   │   │   └── test_...
│   │   ├── TaskAssignments/
│   │   │   ├── .../
│   │   │   └── test_...
│   │   └── Notifications/
│   │       ├── .../
│   │       └── test_...
│   │
│   ├── Steps/
│   │   ├── CommonStepsCollections.py
│   │   ├── CommonStepsUsers.py
│   │   ├── CommonStepsTasks.py
│   │   ├── CommonStepsProjects.py
│   │   ├── CommonStepsCategories.py
│   │   ├── CommonStepsComments.py
│   │   ├── CommonStepsLabels.py
│   │   ├── CommonStepsTaskAssignments.py
│   │   └── CommonStepsNotifications.py
│   │
│   └── __init__.py
│
├── dependencies.txt
├── docker-compose.yml
└── Dockerfile
```

## Layer responsibilities

| Layer | Folders | Responsibility |
|---|---|---|
| Presentation Layer | `Routers/`, `Schemas/`, `Responses/` | Handles HTTP endpoints, validates incoming data, and formats outgoing responses. |
| Business Layer | `Services/`, `Exceptions/`, `BusinessRules/` | Executes use cases, applies business rules, and handles business-specific errors. |
| Data Access Layer | `Repositories/`, `Models/` | Performs database operations and defines the application's data models. |
| Database | `database/mysql/` | Holds MySQL database scripts, such as the schema definition. |

## Request flow

```text
Client
  ↓
Presentation Layer
  ├── Router
  ├── Schema
  └── Response
  ↓
Business Layer
  ├── Service
  ├── Business Rules
  └── Exceptions
  ↓
Data Access Layer
  ├── Repository
  └── Model
  ↓
MySQL Database
```