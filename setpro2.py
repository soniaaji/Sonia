unsigned reduce(unsigned num, unsigned K) {
  if (K<= 0) {
    return num; }
  if (num == 0) {
    return 10;  // Fail
  }
  unsigned path1 = reduce(num/10, K)*10 + num%10;
  unsigned path2 = reduce(num/10, K-1);
  return path1 < path2 ? path1 : path2;
}
int main(void) {
  printf("%u\n", reduce(246, 2));
  printf("%u\n", reduce(24635, 3));
  printf("%u\n", reduce(53642, 3));
  printf("%u\n", reduce(21, 1));
}
