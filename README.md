# ComputerSystem-Project

### ROPME

```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void func(){
  char overflowme[32];
  read(0, overflowme, 0x200);
}

int main(int argc, char* argv[]){
  setvbuf(stdout, 0, _IOLBF, 0); 
  setvbuf(stdin, 0, _IOLBF, 0); 
  printf("The address of setvbuf : %16p\n", setvbuf);
  func();
  write(1, "DONE\n", 5); 
  return 0;
}
```

#### Guideline
- Executable file and libc file will be provided. (ropme and libc.so.6)
- Using stack based buffer overflow, build ROP chain payload to establish a remote shell 
connection.and exit normally


#### Check list 
- Explain what is the vulnerability and how to fix it. 
- Explain how to find the offset of return address
- Explain how to find the libc base address
- Explain how to find the gadgets and how your gadget chains work. 
- The gadgets need to obtain remote shell access.
- After a buffer overflow attack, the program should terminate gracefully without crashing


## Solution
C언어로 컴파일 된 실행파일 ropme의 취약점을 이용하여 Return Address를 덮어쓸 수 있음

주의할 점 : C언어의 절차지향 특성상 ropme 내의 함수 주소 간의 상관관계는 변함이 없지만, 메모리에 할당되는 주소는 계속 바뀌게 됨(ASLR 활성화), 따라서 동적으로 주소를 받을 수 있는 방법을 고려해야함
