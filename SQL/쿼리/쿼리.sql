show status like 'Aborted%';
show status like 'Max_used_connections';

SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST;
CHECK TABLE global_priv;
#REPAIR TABLE `mysql`.`user`, `mysql`.`db`, `mysql`.`tables_priv`, `mysql`.`columns_priv`, `mysql`.`procs_priv`, `mysql`.`global_priv`;