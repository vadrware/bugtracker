CREATE TABLE "CORE_USER" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "USERNAME" NVARCHAR2(50) NULL,
    "PASSWORD" NVARCHAR2(50) NULL,
    "FIRSTNAME" NVARCHAR2(30) NULL,
    "LASTNAME" NVARCHAR2(30) NULL,
    "ACTIVE" NUMBER(1) CHECK ("ACTIVE" IN (0,1)) NULL
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_USER_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_USER_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_USER_TR
            BEFORE INSERT ON "CORE_USER"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_USER_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_USERROLE" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "DESCRIPTION" NVARCHAR2(50) NULL
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_USERROLE_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_USERROLE_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_USERROLE_TR
            BEFORE INSERT ON "CORE_USERROLE"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_USERROLE_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_PRODUCT" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "NAME" NVARCHAR2(100) NULL,
    "CURRENTVERSION" NUMBER(11) NOT NULL,
    "REMOVED" NUMBER(1) CHECK ("REMOVED" IN (0,1)) NULL
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_PRODUCT_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_PRODUCT_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_PRODUCT_TR
            BEFORE INSERT ON "CORE_PRODUCT"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_PRODUCT_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_USERACCESS" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "USERID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_USER" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "USERROLEID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_USERROLE" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "PRODUCTID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_PRODUCT" ("ID") DEFERRABLE INITIALLY DEFERRED
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_USERACCESS_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_USERACCESS_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_USERACCESS_TR
            BEFORE INSERT ON "CORE_USERACCESS"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_USERACCESS_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_DEFECTSTATE" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "NAME" NVARCHAR2(50) NULL,
    "CODE" NVARCHAR2(2) NULL
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_DEFECTSTATE_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_DEFECTSTATE_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_DEFECTSTATE_TR
            BEFORE INSERT ON "CORE_DEFECTSTATE"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_DEFECTSTATE_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_RESOLUTION" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "NAME" NVARCHAR2(30) NULL
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_RESOLUTION_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_RESOLUTION_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_RESOLUTION_TR
            BEFORE INSERT ON "CORE_RESOLUTION"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_RESOLUTION_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_DEFECT" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "PRODUCTID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_PRODUCT" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "PROJECTVERSION" NUMBER(11) NOT NULL,
    "POSTDATE" TIMESTAMP NOT NULL,
    "DEFECTSTATUSID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_DEFECTSTATE" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "REPRODUCE" NCLOB NULL,
    "REMOVED" NUMBER(1) CHECK ("REMOVED" IN (0,1)) NULL,
    "RESOLUTIONID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_RESOLUTION" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "USERID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_USER" ("ID") DEFERRABLE INITIALLY DEFERRED
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_DEFECT_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_DEFECT_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_DEFECT_TR
            BEFORE INSERT ON "CORE_DEFECT"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_DEFECT_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_COMMENT" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "USERID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_USER" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "DEFECTID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_DEFECT" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "POSTDATE" TIMESTAMP NOT NULL,
    "DESCRIPTION" NCLOB NULL,
    "REMOVED" NUMBER(1) CHECK ("REMOVED" IN (0,1)) NULL
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_COMMENT_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_COMMENT_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_COMMENT_TR
            BEFORE INSERT ON "CORE_COMMENT"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_COMMENT_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
CREATE TABLE "CORE_DUPLICATES" (
    "ID" NUMBER(11) NOT NULL PRIMARY KEY,
    "ORIGINALDEFECTID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_DEFECT" ("ID") DEFERRABLE INITIALLY DEFERRED,
    "DUPLICATEDEFECTID_ID" NUMBER(11) NOT NULL REFERENCES "CORE_DEFECT" ("ID") DEFERRABLE INITIALLY DEFERRED
)
;

            DECLARE
                i INTEGER;
            BEGIN
                SELECT COUNT(*) INTO i FROM USER_CATALOG
                    WHERE TABLE_NAME = 'CORE_DUPLICATES_SQ' AND TABLE_TYPE = 'SEQUENCE';
                IF i = 0 THEN
                    EXECUTE IMMEDIATE 'CREATE SEQUENCE CORE_DUPLICATES_SQ';
                END IF;
            END;
            /

            CREATE OR REPLACE TRIGGER CORE_DUPLICATES_TR
            BEFORE INSERT ON "CORE_DUPLICATES"
            FOR EACH ROW
            WHEN (new."ID" IS NULL)
                BEGIN
                    SELECT CORE_DUPLICATES_SQ.nextval
                    INTO :new."ID" FROM dual;
                END;
                /
COMMIT;
