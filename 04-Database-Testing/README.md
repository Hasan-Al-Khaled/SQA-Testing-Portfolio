# 🗄️ Database Testing Portfolio

This directory showcases my **Database Testing expertise** including CRUD operations validation, data integrity testing, and performance optimization for database-driven applications.

## 📂 What's Inside

```
04-Database-Testing/
├── README.md                     # This file - database testing overview
├── SQL-Scripts/
│   ├── DDL-Operations/           # Data Definition Language scripts
│   ├── DML-Operations/           # Data Manipulation Language queries
│   ├── Complex-Queries/          # Joins, subqueries, stored procedures
│   └── Performance-Queries/      # Optimization and indexing examples
├── CRUD-Validation/
│   ├── Create-Operations/        # INSERT statement testing and validation
│   ├── Read-Operations/          # SELECT queries with various conditions
│   ├── Update-Operations/        # UPDATE statement testing scenarios
│   └── Delete-Operations/        # DELETE operations with safety checks
├── Data-Integrity-Tests/
│   ├── Constraint-Testing/       # Primary key, foreign key, unique constraints
│   ├── Trigger-Testing/          # Database trigger validation
│   ├── Transaction-Testing/      # ACID properties and rollback scenarios
│   └── Referential-Integrity/    # Relationship validation between tables
├── Performance-Testing/
│   ├── Query-Optimization/       # Slow query identification and optimization
│   ├── Index-Testing/            # Index effectiveness and performance impact
│   ├── Load-Testing/             # Database performance under load
│   └── Connection-Pooling/       # Database connection optimization
└── Test-Data-Management/
    ├── Test-Data-Setup/          # Scripts for creating test datasets
    ├── Data-Generation/          # Automated test data generation
    ├── Data-Cleanup/             # Scripts for cleaning up test data
    └── Database-Backup/          # Backup and restore procedures
```

## 🎯 **Database Testing Methodology**

### **Testing Approaches:**
- **Functional Testing** - CRUD operations and business logic validation
- **Data Integrity Testing** - Constraints, relationships, and data accuracy
- **Performance Testing** - Query optimization and response time validation
- **Security Testing** - SQL injection prevention and access control
- **Volume Testing** - Large dataset handling and scalability

### **Validation Techniques:**
- ✅ **CRUD Operations** - Create, Read, Update, Delete functionality
- ✅ **Data Consistency** - Cross-table data relationships validation
- ✅ **Constraint Testing** - Primary keys, foreign keys, unique constraints
- ✅ **Transaction Testing** - ACID properties and concurrent access
- ✅ **Performance Benchmarking** - Query execution time optimization

## 🛠️ **Database Technologies & Tools**

| **Category** | **Technologies Used** |
|--------------|----------------------|
| Database Systems | MySQL, PostgreSQL, SQL Server, Oracle |
| Query Tools | MySQL Workbench, pgAdmin, DBeaver |
| Performance Tools | EXPLAIN PLAN, Query Profiler, Performance Schema |
| Automation | Python + SQLAlchemy, JDBC, DbUnit |
| Version Control | Flyway, Liquibase for database migrations |
| Testing Frameworks | PyTest + database fixtures, JUnit + DbUnit |

## 📊 **Key Achievements**

![SQL Queries](https://img.shields.io/badge/SQL%20Queries-150+-brightgreen)
![Database Tests](https://img.shields.io/badge/DB%20Tests-75+-blue)
![Performance Optimizations](https://img.shields.io/badge/Optimizations-20+-orange)
![Data Validations](https://img.shields.io/badge/Validations-50+-purple)

- **150+ SQL Queries** for comprehensive database validation
- **75+ Database Test Cases** covering all CRUD operations
- **20+ Performance Optimizations** improving query response time
- **50+ Data Validation Scripts** ensuring data integrity

## 🚀 **Featured Database Testing Projects**

### **1. E-Commerce Database Validation**
- **Scope:** Product catalog, user management, order processing databases
- **Focus:** CRUD operations, referential integrity, performance optimization
- **Database:** MySQL with complex relationships and constraints
- **[View Scripts →](SQL-Scripts/ECommerce-Database/)**

**Key Validations:**
```sql
-- User registration data validation
SELECT COUNT(*) FROM users WHERE email IS NOT NULL AND email REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$';

-- Order integrity validation
SELECT o.order_id, o.total_amount, SUM(oi.price * oi.quantity) as calculated_total
FROM orders o 
JOIN order_items oi ON o.order_id = oi.order_id 
GROUP BY o.order_id 
HAVING o.total_amount != calculated_total;

-- Performance optimization
EXPLAIN SELECT * FROM products p 
JOIN categories c ON p.category_id = c.category_id 
WHERE p.price BETWEEN 100 AND 500 
ORDER BY p.created_date DESC;
```

### **2. Banking System Database Testing**
- **Scope:** Account management, transaction processing, audit trail
- **Focus:** ACID properties, concurrent transactions, data security
- **Database:** PostgreSQL with stored procedures and triggers
- **[View Scripts →](CRUD-Validation/Banking-System/)**

**Key Test Scenarios:**
```sql
-- Transaction integrity test
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE account_id = 'ACC001';
UPDATE accounts SET balance = balance + 1000 WHERE account_id = 'ACC002';
-- Verify both accounts updated correctly
SELECT account_id, balance FROM accounts WHERE account_id IN ('ACC001', 'ACC002');
COMMIT;

-- Audit trail validation
SELECT transaction_id, account_id, transaction_type, amount, timestamp
FROM transaction_audit 
WHERE DATE(timestamp) = CURDATE()
ORDER BY timestamp DESC;
```

### **3. Data Migration Validation**
- **Scope:** Legacy system to new database migration testing
- **Focus:** Data accuracy, completeness, referential integrity
- **Database:** SQL Server with complex data transformations
- **[View Scripts →](Data-Integrity-Tests/Migration-Validation/)**

**Migration Validation Queries:**
```sql
-- Data completeness check
SELECT 
    'source' as source_type, 
    COUNT(*) as record_count,
    MIN(created_date) as earliest_record,
    MAX(created_date) as latest_record
FROM legacy_customers
UNION ALL
SELECT 
    'target' as source_type,
    COUNT(*) as record_count,
    MIN(registration_date) as earliest_record,
    MAX(registration_date) as latest_record
FROM new_customers;

-- Data accuracy validation
SELECT 
    l.customer_id,
    l.customer_name as legacy_name,
    n.full_name as new_name,
    l.email as legacy_email,
    n.email_address as new_email
FROM legacy_customers l
LEFT JOIN new_customers n ON l.customer_id = n.legacy_customer_id
WHERE l.customer_name != n.full_name OR l.email != n.email_address;
```

## 📈 **Database Performance Optimization**

### **Query Optimization Examples:**

#### **Before Optimization:**
```sql
-- Slow query (Full table scan)
SELECT * FROM orders o, customers c, products p, order_items oi
WHERE o.customer_id = c.customer_id 
AND oi.order_id = o.order_id 
AND oi.product_id = p.product_id
AND o.order_date >= '2024-01-01';

-- Execution time: 2.5 seconds
```

#### **After Optimization:**
```sql
-- Optimized query with proper joins and indexing
SELECT o.order_id, c.customer_name, p.product_name, oi.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= '2024-01-01'
AND o.status = 'completed';

-- Added indexes:
CREATE INDEX idx_orders_date_status ON orders(order_date, status);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);

-- Execution time: 0.3 seconds (83% improvement)
```

### **Performance Benchmarks:**
```
Query Performance Results:
├── Simple SELECT: <50ms
├── Complex JOINs: <200ms
├── Aggregation Queries: <500ms
├── Full-text Search: <100ms
└── Stored Procedures: <150ms

Database Load Testing:
├── Concurrent Users: 100+
├── Transactions/Second: 500+
├── Connection Pool: 50 connections
└── Response Time: <1 second
```

## 🔧 **Database Testing Automation**

### **Python Database Testing Framework:**
```python
import pytest
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

class DatabaseTestFramework:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        
    def execute_query(self, query):
        """Execute SQL query and return results"""
        return pd.read_sql(query, self.engine)
    
    def validate_crud_operation(self, table, operation, data):
        """Validate CRUD operations"""
        if operation == 'CREATE':
            return self.validate_insert(table, data)
        elif operation == 'READ':
            return self.validate_select(table, data)
        # ... other operations
    
    def check_data_integrity(self, table, constraints):
        """Validate data integrity constraints"""
        results = {}
        for constraint in constraints:
            query = f"SELECT COUNT(*) as violation_count FROM {table} WHERE NOT ({constraint})"
            result = self.execute_query(query)
            results[constraint] = result.iloc[0]['violation_count']
        return results

# Example usage in pytest
@pytest.fixture
def db_test_framework():
    return DatabaseTestFramework("mysql://user:password@localhost/testdb")

def test_user_data_integrity(db_test_framework):
    constraints = [
        "email LIKE '%@%.%'",
        "phone REGEXP '^[0-9]{10,15}$'",
        "age BETWEEN 18 AND 100"
    ]
    violations = db_test_framework.check_data_integrity("users", constraints)
    assert all(count == 0 for count in violations.values())
```

## 🛡️ **Data Security & Privacy Testing**

### **Security Test Cases:**
```sql
-- Test for SQL Injection vulnerabilities
-- This should be prevented by parameterized queries
SELECT * FROM users WHERE username = 'admin' OR '1'='1' --';

-- Test data masking in non-production environments
SELECT 
    user_id,
    CONCAT(LEFT(first_name, 1), REPEAT('*', LENGTH(first_name)-1)) as masked_first_name,
    CONCAT(LEFT(email, 2), REPEAT('*', LENGTH(email)-6), RIGHT(email, 4)) as masked_email
FROM users;

-- Test access control
SHOW GRANTS FOR 'test_user'@'localhost';

-- Verify sensitive data encryption
SELECT 
    user_id,
    LENGTH(encrypted_ssn) as ssn_length,
    encrypted_ssn REGEXP '^[A-Za-z0-9+/]+=*$' as is_base64_encoded
FROM user_sensitive_data;
```

## 📊 **Test Data Management**

### **Test Data Generation:**
```sql
-- Generate realistic test data
INSERT INTO customers (customer_name, email, phone, registration_date)
SELECT 
    CONCAT('Customer_', LPAD(ROW_NUMBER() OVER (ORDER BY NULL), 5, '0')) as customer_name,
    CONCAT('user', ROW_NUMBER() OVER (ORDER BY NULL), '@testdomain.com') as email,
    CONCAT('555', LPAD(FLOOR(RAND() * 10000000), 7, '0')) as phone,
    DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 1460) DAY) as registration_date
FROM information_schema.columns
LIMIT 1000;

-- Create realistic order test data
INSERT INTO orders (customer_id, order_date, total_amount, status)
SELECT 
    customer_id,
    DATE_ADD(registration_date, INTERVAL FLOOR(RAND() * 365) DAY) as order_date,
    ROUND(RAND() * 500 + 50, 2) as total_amount,
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'pending'
        WHEN 1 THEN 'processing'
        WHEN 2 THEN 'completed'
        ELSE 'cancelled'
    END as status
FROM customers
WHERE RAND() < 0.7; -- 70% of customers have orders
```

### **Data Cleanup Scripts:**
```sql
-- Clean up test data after test execution
DELETE FROM order_items WHERE order_id IN (
    SELECT order_id FROM orders WHERE customer_id IN (
        SELECT customer_id FROM customers WHERE email LIKE '%@testdomain.com'
    )
);

DELETE FROM orders WHERE customer_id IN (
    SELECT customer_id FROM customers WHERE email LIKE '%@testdomain.com'
);

DELETE FROM customers WHERE email LIKE '%@testdomain.com';

-- Reset auto-increment counters
ALTER TABLE customers AUTO_INCREMENT = 1;
ALTER TABLE orders AUTO_INCREMENT = 1;
```

## 🎯 **Database Testing Best Practices**

### **Test Environment Management:**
- **Isolated Test Database** - Separate from development and production
- **Data Refresh Strategy** - Regular restoration from production snapshots
- **Version Control** - Database schema and test data versioning
- **Backup & Restore** - Automated backup before destructive tests

### **Test Data Strategy:**
- **Realistic Data** - Production-like data volumes and patterns
- **Edge Cases** - Boundary values and special characters
- **Data Privacy** - Masked/anonymized data for sensitive information
- **Data Lifecycle** - Automated creation, usage, and cleanup

### **Performance Testing:**
- **Baseline Establishment** - Performance benchmarks for critical queries
- **Load Testing** - Concurrent user simulation and throughput testing
- **Scalability Testing** - Performance validation with increasing data volumes
- **Resource Monitoring** - CPU, memory, and I/O utilization tracking

## 📝 **Documentation & Standards**

### **SQL Coding Standards:**
```sql
-- Use descriptive table and column names
CREATE TABLE customer_orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_status ENUM('pending', 'processing', 'completed', 'cancelled') DEFAULT 'pending',
    created_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Use consistent formatting and indentation
SELECT 
    c.customer_name,
    c.email,
    COUNT(o.order_id) as total_orders,
    SUM(o.total_amount) as total_spent,
    AVG(o.total_amount) as average_order_value
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE c.registration_date >= '2024-01-01'
GROUP BY c.customer_id, c.customer_name, c.email
HAVING total_orders > 0
ORDER BY total_spent DESC;
```

### **Test Case Documentation:**
- **Test Objective** - Clear description of what is being tested
- **Pre-conditions** - Database state required before test execution
- **Test Steps** - Detailed SQL commands and expected results
- **Post-conditions** - Expected database state after test completion
- **Cleanup Steps** - Data removal and state restoration procedures

## 🔗 **Integration with Application Testing**

### **API + Database Integration:**
```python
# Example: Validate API response matches database state
def test_user_profile_api_database_consistency():
    # 1. Get user data from API
    api_response = requests.get(f"/api/users/{user_id}")
    api_user_data = api_response.json()
    
    # 2. Get same user data from database
    db_query = "SELECT user_id, username, email, full_name FROM users WHERE user_id = %s"
    db_user_data = execute_query(db_query, [user_id])
    
    # 3. Compare API response with database data
    assert api_user_data['user_id'] == db_user_data['user_id']
    assert api_user_data['username'] == db_user_data['username']
    assert api_user_data['email'] == db_user_data['email']
    assert api_user_data['full_name'] == db_user_data['full_name']
```

### **UI + Database Integration:**
```python
# Example: Validate UI form submission updates database correctly
def test_user_registration_ui_database_integration():
    # 1. Count existing users
    initial_count = execute_query("SELECT COUNT(*) FROM users")[0][0]
    
    # 2. Fill registration form via Selenium
    driver.find_element(By.ID, "username").send_keys("testuser123")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("SecurePass123")
    driver.find_element(By.ID, "submit").click()
    
    # 3. Verify user created in database
    time.sleep(2)  # Wait for database operation
    final_count = execute_query("SELECT COUNT(*) FROM users")[0][0]
    assert final_count == initial_count + 1
    
    # 4. Verify user data is correct
    new_user = execute_query(
        "SELECT username, email FROM users WHERE username = %s", 
        ["testuser123"]
    )
    assert new_user[0]['username'] == "testuser123"
    assert new_user[0]['email'] == "test@example.com"
```

## 📞 **Questions or Collaboration?**

Interested in database testing strategies or need help with SQL optimization?

**Connect with me:**
- 💼 **LinkedIn:** [md-hasan-al-khaled](https://www.linkedin.com/in/md-hasan-al-khaled)
- 📧 **Email:** hasanalkhalednir@gmail.com

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

*"Data is the foundation of every application. Testing that foundation ensures the entire system stands strong."*

</div>
