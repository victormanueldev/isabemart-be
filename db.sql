CREATE TABLE User
(
    id              int             NOT NULL PRIMARY KEY,
    document_id     int             NOT NULL,
    full_name       char(50)        NOT NULL,
    email           char(50) UNIQUE NOT NULL,
    hashed_password char(200)       NOT NULL,
    is_active       boolean         NOT NULL,
    is_admin        boolean         NOT NULL,
    is_technician   boolean         NOT NULL,
    is_customer     boolean         NOT NULL,
    color           char(10) UNIQUE
);

CREATE TABLE Customer
(
    id              int      NOT NULL PRIMARY KEY,
    document_id     int      NOT NULL,
    customer_type   char(50) NOT NULL,
    commercial_name char(50),
    email           char(50),
    city            char(50),
    address         char(50),
    phone           char(50)
);

CREATE TABLE Headquarter
(
    id           int             NOT NULL PRIMARY KEY,
    name         char(50)        NOT NULL,
    city         char(50),
    neighborhood char(50),
    address      char(50),
    phone        char(50),
    email        char(50) UNIQUE NOT NULL,
    customer_id  int REFERENCES Customer (id)
);

CREATE TABLE Area
(
    id             int      NOT NULL PRIMARY KEY,
    name           char(50) NOT NULL,
    estimated_time char(50) NOT NULL,
    customer_id    int REFERENCES Customer (id),
    headquarter_id int REFERENCES Headquarter (id)
);

CREATE TABLE ControlPoint
(
    id             int       NOT NULL PRIMARY KEY,
    name           char(50)  NOT NULL,
    status         char(50)  NOT NULL,
    observations   char(255) NOT NULL,
    area_id        int REFERENCES Area (id),
    customer_id    int REFERENCES Customer (id),
    headquarter_id int REFERENCES Headquarter (id)
);

CREATE TABLE SanityPlan
(
    id          int      NOT NULL PRIMARY KEY,
    visits_qty  int      NOT NULL,
    frequency   char(50) NOT NULL,
    customer_id int REFERENCES Customer (id)
);

CREATE TABLE Document
(
    id              int       NOT NULL PRIMARY KEY,
    document_type   char(50),
    upload_datetime TIMESTAMP NOT NULL,
    status          char(50),
    customer_id     int REFERENCES Customer (id)
);

CREATE TABLE Treatment
(
    id        int       NOT NULL PRIMARY KEY,
    name      char(100) NOT NULL,
    cost      int       NOT NULL,
    frequency char(50)  NOT NULL
);

CREATE TABLE Invoice
(
    id             int NOT NULL PRIMARY KEY,
    total_invoiced int NOT NULL,
    is_paid        boolean
);

CREATE TABLE Service
(
    id             int       NOT NULL PRIMARY KEY,
    service_type   char(50)  NOT NULL,
    expected_date  TIMESTAMP NOT NULL,
    executed_date  TIMESTAMP NOT NULL,
    start_time     TIME      NOT NULL,
    end_time       TIME      NOT NULL,
    observations   char(225),
    customer_id    int REFERENCES Customer (id),
    headquarter_id int REFERENCES Headquarter (id),
    invoice_id     int REFERENCES Invoice (id)
);



CREATE TABLE Service_User
(
    service_id int REFERENCES Service (id),
    user_id    int REFERENCES User (id)
);

CREATE TABLE Service_Area
(
    service_id     int REFERENCES Service (id),
    area_id        int REFERENCES Area (id),
    incidence      boolean  NOT NULL,
    activity_level char(50) NOT NULL
);

CREATE TABLE Service_Treatment
(
    service_id   int REFERENCES Service (id),
    treatment_id int REFERENCES Treatment (id),
    status       char(50),
    observations char(200)
);
