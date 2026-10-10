# Lab 6 - Git 1

# Version Control

## 1. Version Control and Collaboration

소프트웨어 개발이나 문서 작업에서는 여러 버전의 파일을 체계적으로 관리하는 것이 중요하다.

단순히 파일을 복사해서 관리하면 다음과 같이 파일이 계속 늘어날 수 있다.

```text
project_final.txt
project_final_edit1.txt
project_final_edit1_realfinal.txt
project_final_edit1_realfinal_edit2.txt
```

여러 사람이 같이 작업하는 경우에는 어떤 파일이 최신 버전인지 알기 어려워질 수 있다.

따라서 Version Control System을 사용하면 파일의 변경 내용을 체계적으로 관리하고 협업하기 쉬워진다.

---

## 2. Changes vs. Snapshots

Version Control System은 데이터를 저장하는 방식에 따라 변경 사항(Changes)을 저장하거나 Snapshot을 저장하는 방식으로 생각할 수 있다.

### Changes

기본 버전을 기준으로 변경된 부분만 저장한다.

```text
Version 1
   ↓
Change 1
   ↓
Change 2
```

### Snapshots

각 버전의 상태를 하나의 Snapshot으로 저장한다.

Git은 파일의 변경 내용을 단순히 차이만 저장하는 것이 아니라 각 시점의 프로젝트 상태를 Snapshot 형태로 관리한다.

---

# Version Control Types

## 3. Local / Centralized / Distributed

Version Control System은 크게 다음과 같이 구분할 수 있다.

### Local Version Control

Version Database가 개인 컴퓨터 내부에 존재한다.

```text
Local Computer
 ├─ File
 └─ Version Database
```

개인 컴퓨터에서 버전을 관리하는 방식이다.

---

### Centralized Version Control

중앙 서버에 Version Database가 존재한다.

```text
Computer A ─┐
            ├─ Central Version Control Server
Computer B ─┘
```

여러 사용자가 하나의 중앙 서버를 통해 버전을 공유한다.

---

### Distributed Version Control

각 사용자가 자신의 컴퓨터에 Version Database를 가지고 있으며 서버에도 Repository가 존재한다.

```text
Server Repository
      ↑ ↓
Computer A
      ↔
Computer B
```

Git은 Distributed Version Control 방식이다.

---

# Git Basic Concepts

## 4. Three States in Git

Git에서는 파일의 상태를 크게 세 가지로 구분할 수 있다.

```text
Modified
   ↓
Staged
   ↓
Committed
```

### Modified

파일이 수정된 상태이다.

파일은 Working Directory에 존재한다.

### Staged

다음 Commit에 포함될 파일을 선택한 상태이다.

파일은 Staging Area에 존재한다.

### Committed

변경 내용을 Git Repository에 저장한 상태이다.

Git의 기본 흐름은 다음과 같다.

```text
Working Directory
       ↓
    git add
       ↓
Staging Area
       ↓
   git commit
       ↓
Repository
```

---

# Git Installation

## 5. Check Git Version

Git이 설치되어 있는지 확인하려면 다음 명령어를 사용한다.

```bash
git --version
```

예:

```text
git version 2.25.1
```

Linux, Mac, Windows에서 사용할 수 있다.

Windows에서는 Git Bash를 사용할 수 있다.

---

# Git Configuration

## 6. Git Config Levels

Git의 설정은 세 가지 Level로 저장할 수 있다.

### System Level

시스템 전체 사용자와 Repository에 적용된다.

```bash
git config --system
```

설정 파일:

```text
/etc/gitconfig
```

---

### Global Level

현재 사용자의 모든 Repository에 적용된다.

```bash
git config --global
```

설정 파일:

```text
~/.config/git/config
```

---

### Local Level

현재 Repository에만 적용된다.

```bash
git config --local
```

설정 파일:

```text
.git/gitconfig
```

설정 우선순위는 다음과 같다.

```text
system → global → local
```

뒤에 있는 설정이 앞의 설정을 override한다.

---

## 7. User Configuration

Git을 처음 사용할 때 사용자 이름과 이메일을 설정할 수 있다.

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email your-email@example.com
```

기본 Branch 이름도 설정할 수 있다.

```bash
git config --global init.defaultBranch main
```

현재 Git 설정 목록을 확인하려면:

```bash
git config --list
```

설정값이 어느 파일에서 왔는지 확인하려면:

```bash
git config --list --show-origin
```

특정 설정값만 확인할 수도 있다.

```bash
git config user.name
```

---

# Repository

## 8. `git init`

기존 Directory를 Git Repository로 만들려면 `git init`을 사용한다.

```bash
git init
```

실행하면 현재 Directory에 `.git` Directory가 생성된다.

```text
project/
├─ .git/
├─ README.md
├─ main.py
└─ words.txt
```

`.git` Directory에는 Git Repository의 정보가 저장된다.

---

## 9. `git status`

현재 Repository 상태를 확인하려면 다음 명령어를 사용한다.

```bash
git status
```

예를 들어 아직 Git이 관리하지 않는 파일이 있다면 다음과 같이 표시된다.

```text
Untracked files:
    README.md
    main.py
    words.txt
```

`git status`를 사용하면 현재 파일이

- Untracked인지
- Staged인지
- Modified인지

확인할 수 있다.

---

# Staging

## 10. `git add`

파일을 Staging Area에 추가하려면 `git add`를 사용한다.

```bash
git add [file_name]
```

예:

```bash
git add README.md
```

여러 파일을 한 번에 추가할 수도 있다.

```bash
git add main.py words.txt
```

파일이 Staging Area에 올라가면 `git status`에서 다음과 같이 표시된다.

```text
Changes to be committed:
    new file: README.md
```

즉, 다음 Commit에 포함될 준비가 된 상태이다.

---

## 11. Modified File and Staging

이미 Staging한 파일을 다시 수정하면 파일의 최신 수정 내용은 자동으로 Staging되지 않는다.

예를 들어:

```bash
git add words.txt
```

이후 `words.txt`를 다시 수정하면 Git에서는 수정된 내용이 Staging되지 않은 상태로 표시될 수 있다.

따라서 수정된 내용을 Commit에 포함하려면 다시 `git add`를 실행해야 한다.

```bash
git add words.txt
```

---

## 12. `git add .`

현재 Directory의 모든 변경 파일을 Staging Area에 추가하려면 다음 명령어를 사용할 수 있다.

```bash
git add .
```

여러 파일을 한 번에 Staging할 때 사용할 수 있다.

---

# Unstaging

## 13. `git rm --cached`

Staging Area에 추가한 파일을 다시 Untracked 상태로 변경하려면 다음 명령어를 사용할 수 있다.

```bash
git rm --cached [file_name]
```

예:

```bash
git rm --cached file_list.txt
```

이 명령어를 실행하면 파일 자체를 삭제하는 것이 아니라 Git의 Tracking 대상에서 제거할 수 있다.

---

# Ignoring Files

## 14. `.gitignore`

Git에서 관리하지 않을 파일이나 Directory는 `.gitignore`에 작성할 수 있다.

```bash
nano .gitignore
```

예를 들어 `file_list.txt`를 Git이 무시하도록 하려면:

```text
file_list.txt
```

`.gitignore`에 등록된 파일은 Git Tracking 대상에서 제외할 수 있다.

---

## 15. `.gitignore` Pattern

`.gitignore`에서는 Pattern을 사용하여 여러 파일을 무시할 수 있다.

### 모든 `.a` 파일 무시

```text
*.a
```

### 특정 파일은 예외 처리

```text
!lib.a
```

앞에 `!`를 사용하면 ignore 규칙에서 제외할 수 있다.

### 현재 Directory의 특정 파일만 무시

```text
/TODO
```

### 모든 `build` Directory 무시

```text
build/
```

### 특정 Directory 아래의 `.txt` 파일 무시

```text
doc/*.txt
```

### 하위 Directory까지 포함하여 `.pdf` 파일 무시

```text
doc/**/*.pdf
```

`.gitignore`를 사용하면 Git으로 관리할 필요가 없는 파일을 Repository에서 제외할 수 있다.

---

# Commit

## 16. `git commit`

Staging Area에 있는 변경 내용을 Repository에 저장하려면 Commit을 사용한다.

```bash
git commit -m "commit message"
```

예:

```bash
git commit -m "initial commit"
```

Commit이 완료되면 해당 시점의 프로젝트 상태가 Repository에 저장된다.

Commit 이후 상태를 확인하면:

```bash
git status
```

변경 사항이 없는 경우 다음과 같이 나타날 수 있다.

```text
nothing to commit, working tree clean
```

---

## 17. `git log`

Commit 기록을 확인하려면 다음 명령어를 사용할 수 있다.

```bash
git log
```

Git Repository에 저장된 Commit History를 확인할 수 있다.

---

# Branch

## 18. `git branch`

현재 Branch 목록을 확인하려면 다음 명령어를 사용한다.

```bash
git branch
```

예:

```text
* master
```

`*`가 붙은 Branch가 현재 사용 중인 Branch이다.

---

## 19. Change Branch Name

Branch 이름을 변경하려면 다음 명령어를 사용할 수 있다.

```bash
git branch -m master main
```

Branch 이름을 `master`에서 `main`으로 변경한다.

변경 후 다시 확인:

```bash
git branch
```

결과:

```text
* main
```

---

# Git Basic Workflow

Git의 기본적인 사용 흐름은 다음과 같이 정리할 수 있다.

```bash
git init
```

Repository 생성

```bash
git status
```

현재 상태 확인

```bash
git add .
```

파일을 Staging Area에 추가

```bash
git status
```

Staging 상태 확인

```bash
git commit -m "commit message"
```

변경 내용을 Repository에 저장

```bash
git log
```

Commit History 확인

전체 흐름:

```text
파일 생성 / 수정
      ↓
Working Directory
      ↓
   git add
      ↓
Staging Area
      ↓
 git commit
      ↓
Git Repository
```

---

# Summary

| Command                                       | 기능                                   |
| --------------------------------------------- | -------------------------------------- |
| `git --version`                               | 설치된 Git Version 확인                |
| `git config --global user.name`               | Git 사용자 이름 설정                   |
| `git config --global user.email`              | Git 사용자 이메일 설정                 |
| `git config --global init.defaultBranch main` | 기본 Branch를 `main`으로 설정          |
| `git config --list`                           | Git 설정 목록 확인                     |
| `git init`                                    | 현재 Directory를 Git Repository로 생성 |
| `git status`                                  | Repository 상태 확인                   |
| `git add [file]`                              | 특정 파일을 Staging Area에 추가        |
| `git add .`                                   | 모든 변경 파일을 Staging Area에 추가   |
| `git rm --cached [file]`                      | 파일을 Git Tracking 대상에서 제거      |
| `.gitignore`                                  | Git이 추적하지 않을 파일 지정          |
| `git commit -m "message"`                     | Staged 변경 사항을 Commit              |
| `git log`                                     | Commit History 확인                    |
| `git branch`                                  | Branch 목록 및 현재 Branch 확인        |
| `git branch -m master main`                   | Branch 이름 변경                       |

Git에서 가장 중요한 기본 흐름은 다음과 같다.

```text
Modified → Staged → Committed
```

그리고 각 단계에서 주로 사용하는 명령어는 다음과 같다.

```text
파일 수정
   ↓
git status
   ↓
git add
   ↓
git commit
```
