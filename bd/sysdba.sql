create user c##sgi2 identified by sgi;

grant connect, resource to c##sgi2; 

alter user c##sgi2 default tablespace users quota unlimited on users;