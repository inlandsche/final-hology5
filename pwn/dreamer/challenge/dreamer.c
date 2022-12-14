#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Call this function! */
void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
  exit(0);
}

/* Print `msg` */
void print(const char *msg) {
  write(1, msg, strlen(msg));
}

/* Print `msg` and read `size` bytes into `buf` */
void getStdin(const char *msg, char *buf, size_t size) {
  char c;
  print(msg);
  for (size_t i = 0; i < size; i++) {
    if (read(0, &c, 1) <= 0) {
      print("Error\n");
      exit(1);
    } else if (c == '\n') {
      buf[i] = '\0';
      break;
    } else {
      buf[i] = c;
    }
  }
}

/* Print `msg` and read an integer value */
int getStdinToInt(const char *msg) {
  char buf[0x10];
  getStdin(msg, buf, 0x10);
  return atoi(buf);
}

/* Entry point! */
int main() {
  int length;
  char buf[0x100];

  /* Read and check length */
  length = getStdinToInt("Size: ");
  if (length > 0x100) {
    print("Size Exceeds the Limit!\n");
    exit(1);
  }

  /* Read data */
  getStdin("Buffer: ", buf, length);
  print("Good Bye!\n");

  return 0;
}
