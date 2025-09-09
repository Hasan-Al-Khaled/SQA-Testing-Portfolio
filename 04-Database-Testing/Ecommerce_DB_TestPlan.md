
# 🗃️ E-commerce Database Test Plan (Daraz Example)

---

## 🔹 1. User Module

| **Test Case ID** | **Scenario / Action** | **SQL Query** | **Expected Result** |
|------------------|------------------------|----------------|----------------------|
| DB_USER_01 | Add new user (Insert) | `INSERT INTO users (first_name,email,age,password) VALUES ('TestUser','test@test.com',25,'hashed_pwd');` | New row created |
| DB_USER_02 | Check user info (Select) | `SELECT * FROM users WHERE email='test@test.com';` | User info returned |
| DB_USER_03 | Update user info (Update) | `UPDATE users SET age=30 WHERE email='test@test.com';` | Age updated |
| DB_USER_04 | Delete user (Delete) | `DELETE FROM users WHERE email='test@test.com';` | Row deleted |
| DB_USER_05 | Password hash check | `SELECT password FROM users WHERE email='hasan@example.com';` | Value hashed, not plain text |

---

## 🔹 2. Cart Module

| **Test Case ID** | **Scenario / Action** | **SQL Query** | **Expected Result** |
|------------------|------------------------|----------------|----------------------|
| DB_CART_01 | Add product to cart | `INSERT INTO cart (user_id,product_id,quantity) VALUES (1,2,1);` | Row created |
| DB_CART_02 | Same product → qty update | `UPDATE cart SET quantity=quantity+1 WHERE user_id=1 AND product_id=2;` | Qty increased |
| DB_CART_03 | Manual qty update | `UPDATE cart SET quantity=5 WHERE user_id=1 AND product_id=2;` | Qty=5 |
| DB_CART_04 | Remove item from cart | `DELETE FROM cart WHERE user_id=1 AND product_id=2;` | Row deleted |
| DB_CART_05 | Cart total validation | ```sql SELECT c.user_id, SUM(p.price*c.quantity) AS cart_total FROM cart c JOIN products p ON c.product_id=p.id WHERE c.user_id=1 GROUP BY c.user_id; ``` | cart_total matches UI |
| DB_CART_06 | Integrity check (user/product valid) | `SELECT c.id,u.first_name,p.product_name FROM cart c JOIN users u ON c.user_id=u.id JOIN products p ON c.product_id=p.id;` | Valid user + product |

---

## 🔹 3. Order Module

| **Test Case ID** | **Scenario / Action** | **SQL Query** | **Expected Result** |
|------------------|------------------------|----------------|----------------------|
| DB_ORD_01 | Insert new order | `INSERT INTO orders (user_id,order_total) VALUES (1,149.97);` | Order created |
| DB_ORD_02 | Insert order items | `SELECT * FROM order_items WHERE order_id=3;` | Items returned |
| DB_ORD_03 | Stock reduce after order | `SELECT stock_quantity FROM products WHERE id=2;` | Qty decreased |
| DB_VAL_01 | Order total vs items sum | ```sql SELECT o.id,o.order_total,SUM(oi.quantity*oi.price) AS calc_total FROM orders o JOIN order_items oi ON o.id=oi.order_id GROUP BY o.id; ``` | order_total = calc_total |
| DB_VAL_02 | Order → User relation | `SELECT o.id,u.first_name FROM orders o JOIN users u ON o.user_id=u.id;` | Valid user linked |

---

## 🔹 4. Payment Module

| **Test Case ID** | **Scenario / Action** | **SQL Query** | **Expected Result** |
|------------------|------------------------|----------------|----------------------|
| DB_PAY_01 | Successful payment | `INSERT INTO payments (order_id,amount,status) VALUES (3,149.97,'SUCCESS');` <br> `SELECT * FROM payments WHERE order_id=3;` | Status=SUCCESS |
| DB_PAY_02 | Failed payment | `INSERT INTO payments (order_id,amount,status) VALUES (3,149.97,'FAILED');` <br> `SELECT * FROM payments WHERE order_id=3;` | Status=FAILED |
| DB_PAY_03 | Payment linked to order | `SELECT o.id,p.status,p.amount FROM orders o LEFT JOIN payments p ON o.id=p.order_id;` | Each order has payment status |

---

# 🎯 Coverage Summary

- **User Module** → CRUD + password security  
- **Cart Module** → Add, Update, Delete, Validation, Integrity  
- **Order Module** → Insert, Items, Stock update, Totals, Relation  
- **Payment Module** → Success/Failed status, Linking to orders  

👉 This Test Plan = Full E-commerce DB QA coverage ✅
