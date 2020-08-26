   #!/bin/bash
   yum remove -y php-mysql php php-fpm php-common
   rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
   rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
   yum clean all
