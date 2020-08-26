#nginx:统计Nginx的状态，请分别打印出各种状态码出现了多少次。
BEGIN {
}

{
  cou[$9]++
}

END {
  for (i in cou)print i,cou[i]
}

