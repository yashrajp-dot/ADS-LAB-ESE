
Mysql cluster (run in mysql shell and download if not there)



 MySQL  JS > dba.deploySandboxInstance(3310);

 MySQL  JS > dba.deploySandboxInstance(3320);

 MySQL  JS > dba.deploySandboxInstance(3330);

 MySQL  JS > \connect root@localhost:3310

 MySQL  localhost:3310 ssl  JS > var cluster=dba.createCluster('Mysql Cluster');

 MySQL  localhost:3310 ssl  JS > var cluster = dba.createCluster('devCluster');

 MySQL  localhost:3310 ssl  JS > cluster.status()

 MySQL  localhost:3310 ssl  JS > cluster.addInstance('root@localhost:3330');

Please select a recovery method [C]lone/[I]ncremental recovery/[A]bort (default Clone): c

 MySQL  localhost:3310 ssl  JS > cluster.status()

 MySQL  localhost:3310 ssl  JS > cluster.addInstance('root@localhost:3320');

Please select a recovery method [C]lone/[I]ncremental recovery/[A]bort (default Clone): c

MySQL  localhost:3310 ssl  JS > cluster.status();

 MySQL  localhost:3310 ssl  JS > \sql

 MySQL  localhost:3310 ssl  SQL > create database Quiz;

 MySQL  localhost:3310 ssl  SQL > use quiz;

 MySQL  localhost:3340 ssl  quiz  SQL > create table books(id int primary key, name varchar(20));

 MySQL  localhost:3310 ssl  quiz  SQL > show tables;

 MySQL  localhost:3310 ssl  quiz  SQL > insert into books values(2, 'Mahesh', );

 MySQL  localhost:3310 ssl  quiz  SQL > select * from user;

 MySQL  localhost:3320 ssl  quiz  SQL > set global read_only=off;
