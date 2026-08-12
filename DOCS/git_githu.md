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