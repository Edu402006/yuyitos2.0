create user c##sgi3 identified by sgi;

grant connect, resource to c##sgi3; 

alter user c##sgi3 default tablespace users quota unlimited on users;