GitHub
│
├── main
│
├── develop
│
└── feature/...
      
Local
│
├── local_main
├── local_develop
└── local_feature/...

local_develop
      │
      └── local_feature/project-setup
                    │
                    │ coding
                    ▼
                  commit
                    │
                    ▼
             feature/project-setup
                    │
                    ▼
                  GitHub
                    │
                    ▼
              Pull Request
                    │
                    ▼
                 develop

                 LOCAL                         GITHUB

LOCAL                         GITHUB

local_main  ───────────────► main

local_develop ─────────────► develop

local_develop
      │
      ▼
      A
       \
        \
         local_feature/project-setup

         local_feature/project-setup  - git
              │
              │ push
              ▼
feature/project-setup   -  github

git push   -u   origin   local_feature/project-setup:feature/project-setup
   │        │      │                    │
   │        │      │                    └── source : destination
   │        │      └── GitHub remote
   │        └── set upstream
   └── upload commits



   main
  │
  └── develop
        │
        └── patient_management_system_api
                │
                ├── feature 1
                ├── feature 2
                ├── feature 3
                └── ...


   to delete a branch : git branch -d local_feature/started_1

   