# 📍 XPath & CSS Cheat Sheet

## **XPath Examples**
| Purpose | Example |
|----------|---------|
| Select by ID | `//input[@id='username']` |
| Partial Text | `//button[contains(text(),'Login')]` |
| Parent-Child | `//form[@id='loginForm']//input` |
| Dynamic Elements | `//input[starts-with(@id,'user_')]` |

---

## **CSS Examples**
| Purpose | Example |
|----------|---------|
| Select by ID | `#username` |
| By Attribute | `input[type='email']` |
| Direct Child | `form > input` |
| Nested | `.container .field` |

---

## **Best Practices**
1. Prefer CSS selectors when possible — faster and cleaner.
2. Always test your locator in **DevTools Console**:
   ```javascript
   $x("//button[@id='loginBtn']")
