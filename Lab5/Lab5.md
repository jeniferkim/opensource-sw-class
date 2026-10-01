# Lab 5 - Shell Commands 2

# I/O Redirection

## 1. Standard Output `>`

기본적으로 Shell의 표준 출력(Standard Output)은 화면에 표시된다.

`>`를 사용하면 명령어의 실행 결과를 화면에 출력하는 대신 파일에 저장할 수 있다.

```bash
ls -lh > file_list.txt
```

위 명령어는 `ls -lh`의 실행 결과를 `file_list.txt` 파일에 저장한다.

파일의 내용을 확인할 때는 `cat` 명령어를 사용할 수 있다.

```bash
cat file_list.txt
```

`>`를 사용할 때 대상 파일이 이미 존재하면 기존 내용이 덮어써질 수 있으므로 주의해야 한다.

---

## 2. Append Output `>>`

`>>`는 명령어의 실행 결과를 기존 파일의 마지막 부분에 추가한다.

```bash
ls -lh >> file_list.txt
```

파일이 이미 존재하는 경우 기존 내용을 유지하면서 새로운 결과를 뒤에 추가한다.

파일이 존재하지 않는 경우에는 새로운 파일을 생성한다.

### `>`와 `>>`의 차이

| 기호 | 기능                                      |
| ---- | ----------------------------------------- |
| `>`  | 파일을 새로 작성하거나 기존 내용을 덮어씀 |
| `>>` | 기존 파일의 마지막에 내용을 추가함        |

---

## 3. Standard Input `<`

기본적으로 Shell의 표준 입력(Standard Input)은 키보드이다.

`<`를 사용하면 키보드 대신 파일의 내용을 입력으로 사용할 수 있다.

```bash
sort < words.txt
```

위 명령어는 `words.txt`의 내용을 `sort` 명령어의 입력으로 전달한다.

입력과 출력을 동시에 Redirect할 수도 있다.

```bash
sort < words.txt > sorted_words.txt
```

동작 과정:

```text
words.txt
    ↓
   sort
    ↓
sorted_words.txt
```

즉, `words.txt`의 내용을 정렬한 뒤 결과를 `sorted_words.txt`에 저장한다.

---

# Pipeline

## 4. Pipeline `|`

Pipeline은 앞 명령어의 출력을 다음 명령어의 입력으로 전달하는 기능이다.

```bash
command1 | command2 | command3
```

예시:

```bash
ls -lh | less
```

`ls -lh`의 결과를 `less`에 전달하여 긴 출력 결과를 페이지 단위로 확인할 수 있다.

`less` 화면에서는 `q`를 눌러 종료할 수 있다.

또 다른 예시는 다음과 같다.

```bash
ls | wc -l
```

`ls`로 출력된 파일 및 디렉토리 목록을 `wc -l`에 전달하여 항목의 개수를 확인할 수 있다.

Pipeline을 사용하면 여러 명령어를 연결하여 하나의 작업처럼 사용할 수 있다.

---

# Expansion

## 5. Expansion

Shell에서는 특정 특수문자가 명령어 실행 과정에서 특별한 의미로 확장될 수 있다.

예를 들어 `echo`는 입력한 문자열이나 값을 화면에 출력한다.

```bash
echo print out the text
```

출력:

```text
print out the text
```

### `*`

`*`는 현재 디렉토리에 있는 여러 파일 이름으로 확장될 수 있다.

```bash
echo *
```

현재 디렉토리의 파일과 디렉토리 이름이 출력된다.

### `~`

`~`는 현재 사용자의 Home Directory를 의미한다.

```bash
echo ~
```

예시 출력:

```text
/Users/user
```

---

## 6. Backslash `\`

Backslash(`\`)를 사용하면 긴 명령어를 여러 줄에 나누어 입력할 수 있다.

```bash
ls -l \
-h
```

Shell에서는 위 명령어를 하나의 명령어로 처리한다.

긴 명령어를 작성할 때 가독성을 높이는 데 사용할 수 있다.

---

# Permissions

## 7. File Permissions

Linux는 여러 사용자가 함께 사용할 수 있는 Multi-user System이다.

파일과 디렉토리는 다음 세 종류의 사용자에게 각각 다른 권한을 설정할 수 있다.

- Owner: 파일의 소유자
- Group: 파일이 속한 그룹
- Others: 그 외 사용자

`ls -l` 명령어를 사용하면 파일의 권한을 확인할 수 있다.

예시:

```text
-rwxr-xr--
```

권한은 다음 세 가지 종류로 구성된다.

| 권한 | 의미           |
| ---- | -------------- |
| `r`  | read, 읽기     |
| `w`  | write, 쓰기    |
| `x`  | execute, 실행  |
| `-`  | 해당 권한 없음 |

권한 문자열은 다음과 같이 구분할 수 있다.

```text
-rwxr-xr--
 ||| ||| |||
  |   |   |
owner group others
```

첫 번째 문자는 파일의 종류를 나타낸다.

```text
- : 일반 파일
d : 디렉토리
```

---

## 8. `chmod`

`chmod`는 파일이나 디렉토리의 권한을 변경하는 명령어이다.

```bash
chmod permission file
```

Linux 권한은 숫자로도 표현할 수 있다.

| 권한  | Binary | 숫자 |
| ----- | ------ | ---- |
| `rwx` | 111    | 7    |
| `rw-` | 110    | 6    |
| `r-x` | 101    | 5    |
| `r--` | 100    | 4    |
| `---` | 000    | 0    |

예를 들어:

```bash
chmod 600 README.md
```

`600`은 다음과 같은 의미이다.

```text
6 = 110 = rw-  → owner
0 = 000 = ---  → group
0 = 000 = ---  → others
```

따라서 파일의 소유자만 읽기와 쓰기가 가능하고 다른 사용자는 접근 권한이 없다.

### 예시: `644`

파일의 소유자는 읽기와 쓰기가 가능하고 나머지 사용자는 읽기만 가능하게 하려면 다음과 같이 설정한다.

```bash
chmod 644 words.txt
```

권한:

```text
rw-r--r--
```

| 사용자 | 권한         |
| ------ | ------------ |
| Owner  | read + write |
| Group  | read         |
| Others | read         |

---

# Superuser

## 9. `sudo`

Superuser는 시스템 관리와 관련된 모든 권한을 가진 사용자이다.

일부 명령어는 일반 사용자 권한으로 실행할 수 없기 때문에 Superuser 권한이 필요하다.

이때 명령어 앞에 `sudo`를 사용한다.

```bash
sudo command
```

예:

```bash
sudo some_command
```

Superuser Shell로 진입할 수도 있다.

```bash
sudo -i
```

Superuser Session에서 나올 때는 다음 명령어를 사용한다.

```bash
exit
```

`sudo`는 강한 권한을 가지기 때문에 명령어를 실행할 때 주의해야 한다.

---

# Text Editors

## 10. Text Editors

Linux에서는 CLI 기반 또는 GUI 기반의 다양한 Text Editor를 사용할 수 있다.

대표적인 Text Editor는 다음과 같다.

| Editor      | Interface | 특징                                    |
| ----------- | --------- | --------------------------------------- |
| `vi`, `vim` | CLI       | 강력한 기능을 제공하는 Unix 계열 편집기 |
| `Emacs`     | CLI       | 다양한 기능을 제공하는 Text Editor      |
| `nano`      | CLI       | 비교적 사용하기 쉬운 간단한 편집기      |
| `gedit`     | GUI       | GNOME 환경에서 사용하는 그래픽 편집기   |
| `kwrite`    | GUI       | KDE 환경에서 사용하는 그래픽 편집기     |

간단한 Shell Script나 텍스트 파일을 작성할 때는 `nano`를 사용할 수 있다.

```bash
nano filename
```

---

# Shell Script

## 11. Shell Script

Shell Script는 여러 Shell 명령어를 파일에 작성하여 한 번에 실행할 수 있도록 만든 것이다.

Shell Script 파일은 일반적으로 `.sh` 확장자를 사용한다.

예:

```bash
nano myscript.sh
```

파일 내용:

```bash
#!/bin/bash

# This is simply a comment line.

echo "Hello Shell Script!"
```

작성한 Shell Script는 다음과 같이 실행할 수 있다.

```bash
sh myscript.sh
```

출력:

```text
Hello Shell Script!
```

Shell Script를 사용하면 반복되는 명령어를 하나의 파일로 작성하여 실행할 수 있다.

---

# Command History

## 12. `history`

`history`는 이전에 사용한 명령어의 기록을 확인하는 명령어이다.

```bash
history
```

명령어 기록을 파일에 저장할 수도 있다.

```bash
history > history_command.txt
```

저장된 파일의 내용을 확인하려면 다음과 같이 사용할 수 있다.

```bash
cat history_command.txt
```

자주 사용했던 명령어나 이전 작업 내용을 확인할 때 유용하다.

---

# Internet Commands

## 13. `wget`

`wget`은 Internet에서 파일을 다운로드하여 현재 작업 중인 디렉토리에 저장하는 명령어이다.

```bash
wget URL
```

예:

```bash
wget https://example.com/image.jpg
```

지정한 URL의 파일을 다운로드할 수 있다.

---

## 14. `curl`

`curl`은 Internet을 통해 데이터를 가져오거나 업로드하고 관리할 때 사용하는 명령어이다.

기본 형태:

```bash
curl [options] [URL]
```

파일을 특정 이름으로 저장하려면 `-o` 옵션을 사용할 수 있다.

```bash
curl -o horse.jpg https://example.com/horse.jpg
```

또는 원래 파일 이름을 사용하여 저장하려면 `-O` 옵션을 사용할 수 있다.

```bash
curl -O https://example.com/horse.jpg
```

### `wget`과 `curl`

| Command | 주요 용도                                     |
| ------- | --------------------------------------------- |
| `wget`  | 파일 다운로드                                 |
| `curl`  | Internet을 통한 데이터 요청, 다운로드 및 전송 |

---

# Text Search

## 15. `grep`

`grep`은 파일이나 문자열에서 특정 텍스트를 검색하는 명령어이다.

`grep`은 **Global Regular Expression Print**의 약자이다.

기본 형태:

```bash
grep "search_term" file.txt
```

예:

```bash
grep "apple" file.txt
```

`file.txt`에서 `apple`이 포함된 줄을 찾아 출력한다.

### 주요 옵션

#### `-i`

대소문자를 구분하지 않고 검색한다.

```bash
grep -i "apple" file.txt
```

`apple`, `Apple`, `APPLE` 등을 모두 검색할 수 있다.

#### `-v`

검색 조건에 해당하지 않는 줄을 출력한다.

```bash
grep -v "apple" file.txt
```

#### `-n`

검색 결과와 함께 Line Number를 출력한다.

```bash
grep -n "apple" file.txt
```

#### `-r`

디렉토리와 하위 디렉토리의 파일까지 Recursive하게 검색한다.

```bash
grep -r "apple" directory
```

---

## 16. `grep`과 Regular Expression

`grep`은 Regular Expression을 사용하여 보다 복잡한 패턴을 검색할 수 있다.

| 표현    | 의미                         |
| ------- | ---------------------------- |
| `.*`    | 임의의 문자가 0번 이상 등장  |
| `\d`    | 숫자와 일치                  |
| `[abc]` | `a`, `b`, `c` 중 하나와 일치 |
| `^`     | 줄의 시작                    |
| `$`     | 줄의 끝                      |

예를 들어 다음과 같이 Pipeline과 함께 사용할 수 있다.

```bash
echo "This is a test sentence with some words." | grep "test"
```

출력:

```text
This is a test sentence with some words.
```

대소문자를 구분하지 않고 검색하려면:

```bash
echo "This is a test sentence with some words." | grep -i "Test"
```

특정 문자로 시작하는 부분을 찾는 등의 패턴 검색에도 Regular Expression을 사용할 수 있다.

---

# Summary

| Command / Symbol | 기능                                 |
| ---------------- | ------------------------------------ | ---------------------------------------------- |
| `>`              | 명령어 출력을 파일에 저장            |
| `>>`             | 명령어 출력을 기존 파일 뒤에 추가    |
| `<`              | 파일 내용을 명령어의 입력으로 사용   |
| `                | `                                    | 앞 명령어의 출력을 다음 명령어의 입력으로 전달 |
| `echo`           | 문자열이나 값을 출력                 |
| `*`              | 여러 파일 이름으로 Expansion         |
| `~`              | Home Directory                       |
| `\`              | 긴 명령어를 여러 줄에 나누어 입력    |
| `chmod`          | 파일 및 디렉토리 권한 변경           |
| `sudo`           | Superuser 권한으로 명령어 실행       |
| `nano`           | CLI Text Editor                      |
| `sh`             | Shell Script 실행                    |
| `history`        | 이전 명령어 기록 확인                |
| `wget`           | Internet에서 파일 다운로드           |
| `curl`           | Internet을 통한 데이터 요청 및 전송  |
| `grep`           | 파일이나 문자열에서 특정 텍스트 검색 |

추가로 다음 내용을 기억하면 유용하다.

- `>`는 기존 파일의 내용을 덮어쓸 수 있다.
- `>>`는 기존 내용 뒤에 새로운 내용을 추가한다.
- Pipeline(`|`)을 사용하면 여러 명령어를 연결할 수 있다.
- Linux의 권한은 Owner / Group / Others로 구분된다.
- `r`, `w`, `x`는 각각 Read / Write / Execute를 의미한다.
- `chmod 644`와 같이 숫자를 이용하여 권한을 설정할 수 있다.
- `sudo`는 시스템에 큰 영향을 줄 수 있으므로 주의하여 사용해야 한다.
- Shell Script를 사용하면 반복 작업을 자동화할 수 있다.
- `grep`은 옵션 및 Regular Expression과 함께 사용하면 다양한 검색이 가능하다.
