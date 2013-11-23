#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/ptrace.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    int kurewka, pid, addr, sum;
    if(argc<3) {
        //printf("murzyn zajebal mi rower\nuzycie:\n./wiadro pid adres");
        return 0;
    } else {
        sscanf(argv[1], "%d", &pid);
        sscanf(argv[2], "%x", &addr);
        sscanf(argv[3], "%x", &sum);
    }

    ptrace(PTRACE_ATTACH, pid, NULL, NULL);
    wait(NULL);

	kurewka = ptrace(PTRACE_POKEDATA, pid, addr, NULL);
    
    ptrace(PTRACE_DETACH, pid, NULL, NULL);  

    printf("%u", kurewka);

  return 0;
}

