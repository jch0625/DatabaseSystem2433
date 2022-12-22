CREATE TABLE Account
(
    AccountID integer not null ,
    Account_name varchar(100) not null ,
    StartDate datetime NOT NULl,
    PRIMARY KEY (AccountID)
    );

CREATE TABLE Billing
(
    Billing_id integer not null ,
    BC_name varchar(100) not null ,
    BC_addr varchar(100) not null,
    BC_zip integer(10) not null,
    PRIMARY KEY (Billing_id)
    );

CREATE TABLE Company
(
    Company_code integer not null ,
    Comp_name varchar(100) not null ,
    Comp_phone integer not null ,
    Comp_addr varchar(100) null,
    PRIMARY KEY (Company_code)
    );

CREATE TABLE Customer
(
    Customer_ssn integer not null ,
    Cus_Fname varchar(50) not null ,
    Cus_Lname varchar(30) not null ,
    Cus_phone integer(15) not null,
    Cus_addr varchar(100) null,
    PRIMARY KEY (Customer_ssn)
    );

CREATE TABLE ManagerContract
(
    ManagerContract_Num integer not null ,
    Con_type varchar(30) not null ,
    Con_Status varchar(20) not null ,
    Start_date datetime not null,
    Expire_date datetime not null,
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

CREATE TABLE Contract_Premium
(
    Pre_Num integer not null ,
    ManagerContract_Num integer not null ,
    pre_name varchar(20) not null ,
    Start_date datetime not null,
    Expire_date datetime not null,
    PRIMARY KEY (Pre_Num)
    );

CREATE TABLE License
(
    License_num integer not null,
    Associate_ssn integer not null,
    License_type varchar(20),
    Issue_date datetime,
    Expire_date datetime
);


# relation table

CREATE TABLE Billing_Account
(
    Billing_id integer not null,
    Account_id integer not null
);

CREATE TABLE Company_Account
(
    Company_code integer not null,
    Account_id integer not null
);

CREATE TABLE Customer_Account
(
    Customer_ssn integer not null,
    Account_id integer not null
);

CREATE TABLE Account_Contract
(
    ManagerContract_Num integer not null,
    Account_id integer not null
);

CREATE TABLE Associate_Contract
(
    Associate_ssn integer not null,
    ManagerContract_Num integer not null
);

CREATE TABLE Contract_benefit_customer
(
    Customer_ssn integer not null,
    ManagerContract_Num integer not null
);

CREATE TABLE Premium_ManagerContract
(
    ManagerContract_Num integer not null,
    Pre_num integer not null
);

CREATE TABLE Associate_Pre
(
    Associate_ssn integer not null,
    Pre_num integer not null
);

CREATE TABLE Pre_benefit_customer
(
    Customer_ssn integer not null,
    Pre_num integer not null
);


ALTER TABLE License ADD CONSTRAINT LicPK PRIMARY KEY (License_num);

ALTER TABLE Associate ADD CONSTRAINT AssFk foreign key (License_num) references License (License_num) on update cascade on delete cascade;

ALTER TABLE Billing_Account ADD CONSTRAINT BandA PRIMARY KEY (Billing_id, Account_id),
    ADD CONSTRAINT BillFK FOREIGN KEY (Billing_id) REFERENCES Billing(Billing_id),
    ADD CONSTRAINT AccFK1 FOREIGN KEY (Account_id) REFERENCES Account(AccountID);

ALTER TABLE Company_Account ADD CONSTRAINT ComAcc PRIMARY KEY (Company_code, Account_id),
    ADD CONSTRAINT CompFK FOREIGN KEY (Company_code) REFERENCES Company(Company_code),
    ADD CONSTRAINT AccFK2 FOREIGN KEY (Account_id) REFERENCES Account(AccountID);

ALTER TABLE Customer_Account ADD CONSTRAINT CusAcc PRIMARY KEY (Customer_ssn, Account_id),
    ADD CONSTRAINT CusFK1 FOREIGN KEY (Customer_ssn) REFERENCES Customer(Customer_ssn),
    ADD CONSTRAINT AccFK3 FOREIGN KEY (Account_id) REFERENCES Account(AccountID);

ALTER TABLE Account_Contract ADD CONSTRAINT AccCon PRIMARY KEY (ManagerContract_Num, Account_id),
    ADD CONSTRAINT MConFK1 FOREIGN KEY (ManagerContract_Num) REFERENCES ManagerContract(ManagerContract_Num),
    ADD CONSTRAINT AccFK4 FOREIGN KEY (Account_id) REFERENCES Account(AccountID);

ALTER TABLE Associate_Contract ADD CONSTRAINT AssCon PRIMARY KEY (ManagerContract_Num, Associate_ssn),
    ADD CONSTRAINT MConFK2 FOREIGN KEY (ManagerContract_Num) REFERENCES ManagerContract(ManagerContract_Num),
    ADD CONSTRAINT AssFK1 FOREIGN KEY (Associate_ssn) REFERENCES Associate(Associate_ssn);

ALTER TABLE Contract_benefit_customer ADD CONSTRAINT ConCus PRIMARY KEY (ManagerContract_Num, Customer_ssn),
    ADD CONSTRAINT MConFK3 FOREIGN KEY (ManagerContract_Num) REFERENCES ManagerContract(ManagerContract_Num),
    ADD CONSTRAINT CusFK2 FOREIGN KEY (Customer_ssn) REFERENCES Customer(Customer_ssn);

ALTER TABLE Premium_ManagerContract ADD CONSTRAINT ConCus PRIMARY KEY (ManagerContract_Num, Pre_num),
    ADD CONSTRAINT MConFK4 FOREIGN KEY (ManagerContract_Num) REFERENCES ManagerContract(ManagerContract_Num),
    ADD CONSTRAINT PreFK1 FOREIGN KEY (Pre_num) REFERENCES Premium_ManagerContract(Pre_num);

ALTER TABLE Associate_Pre ADD CONSTRAINT AssPre PRIMARY KEY (Associate_ssn, Pre_num),
    ADD CONSTRAINT AssFK2 FOREIGN KEY (Associate_ssn) REFERENCES Associate(Associate_ssn),
    ADD CONSTRAINT PreFK2 FOREIGN KEY (Pre_num) REFERENCES Premium_ManagerContract(Pre_num);

ALTER TABLE Pre_benefit_customer ADD CONSTRAINT PreCus PRIMARY KEY (Customer_ssn, Pre_num),
    ADD CONSTRAINT CusFK3 FOREIGN KEY (Customer_ssn) REFERENCES Customer(Customer_ssn),
    ADD CONSTRAINT PreFK3 FOREIGN KEY (Pre_num) REFERENCES Premium_ManagerContract(Pre_num);

CREATE INDEX CusIndex
ON Customer (Cus_Fname, Cus_Lname);

CREATE INDEX AccIndex
ON Account (Account_name);

CREATE INDEX ComIndex
ON Company (Comp_name);

CREATE INDEX AssIndex
ON Associate (Associate_Fname, Associate_Lname);




