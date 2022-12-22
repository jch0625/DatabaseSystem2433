CREATE TABLE Account
(
    AccountID integer not null AUTO_INCREMENT,
    Account_name varchar(100) not null UNIQUE,
    StartDate datetime NOT NULl,
    Address varchar(100) not null,
    City varchar(40) not null,
    State varchar(20) not null,
    Zip integer(15) not null,
    PW varchar(100) not null,
    PRIMARY KEY (AccountID)
    );

CREATE TABLE Customer
(
    Customer_ssn integer not null ,
    Cus_Fname varchar(50) not null ,
    Cus_Lname varchar(30) not null ,
    Cus_phone integer(15) not null,
    PRIMARY KEY (Customer_ssn)
    );

CREATE TABLE ManagerContract
(
    ManagerContract_Num integer not null AUTO_INCREMENT,
    AccountID integer not null,
    Con_Amount FLOAT not null,
    Con_Status varchar(20) not null ,
    Start_date datetime not null,
    PRIMARY KEY (ManagerContract_Num)
    );

CREATE TABLE Associate
(
    Associate_ssn integer not null ,
    Associate_Fname varchar(50) not null ,
    Associate_Lname varchar(30) not null ,
    Associate_phone integer(15) not null,
    License_num integer not null,
    PRIMARY KEY (Associate_ssn)
    );

CREATE TABLE Associate_Contract
(
    Associate_ssn integer not null,
    ManagerContract_Num integer not null
);


CREATE TABLE Customer_Account
(
    Customer_ssn integer not null,
    Account_id integer not null
);


ALTER TABLE Associate ADD CONSTRAINT AssFk foreign key (License_num) references License (License_num) on update cascade on delete cascade;

ALTER TABLE Account AUTO_INCREMENT = 100000;

ALTER TABLE ManagerContract AUTO_INCREMENT = 9000000;

ALTER TABLE Customer_Account ADD CONSTRAINT CusAcc PRIMARY KEY (Customer_ssn, Account_id),
    ADD CONSTRAINT CusFK1 FOREIGN KEY (Customer_ssn) REFERENCES Customer(Customer_ssn),
    ADD CONSTRAINT AccFK3 FOREIGN KEY (Account_id) REFERENCES Account(AccountID);

ALTER TABLE ManagerContract ADD CONSTRAINT FCfk FOREIGN KEY (AccountID) REFERENCES Account(AccountID);


ALTER TABLE Associate_Contract ADD CONSTRAINT AssCon PRIMARY KEY (ManagerContract_Num, Associate_ssn),
    ADD CONSTRAINT MConFK2 FOREIGN KEY (ManagerContract_Num) REFERENCES ManagerContract(ManagerContract_Num),
    ADD CONSTRAINT AssFK1 FOREIGN KEY (Associate_ssn) REFERENCES Associate(Associate_ssn);


CREATE INDEX CusIndex
ON Customer (Cus_Fname, Cus_Lname);

CREATE INDEX AccIndex
ON Account (Account_name);

CREATE INDEX AssIndex
ON Associate (Associate_Fname, Associate_Lname);






ALTER TABLE Associate ADD CONSTRAINT AssFk foreign key (License_num) references License (License_num) on update cascade on delete cascade;
