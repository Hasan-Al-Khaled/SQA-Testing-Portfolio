# STLC (Software Testing Life Cycle)

## 📌 What is STLC?
STLC (Software Testing Life Cycle) is a sequence of activities performed during the testing process to ensure software quality.

It typically includes:
- Requirement Analysis
- Test Planning
- Test Case Design
- Environment Setup
- Test Execution
- Defect Reporting & Tracking
- Test Closure

## 📌 Real Example: Testing a Login Page

### 1. Requirement Analysis
- **Requirement:** The user must be able to log in with valid username & password.
- Invalid credentials should show an error message.
- Password must be masked.
- Login should redirect to the dashboard after success.

### 2. Test Planning
- Decide what to test (positive & negative login scenarios).
- Tools: Selenium + TestNG (automation) or manual test cases.
- Roles: QA team assigned.
- Risks: Server downtime, browser compatibility issues.

### 3. Test Case Design
**Example test cases:**
- Valid username + valid password → should login.
- Valid username + invalid password → error message.
- Empty username/password → validation error.
- Check password is masked.
- After login → redirect to dashboard.

### 4. Environment Setup
**Setup:**
- Test server URL: `https://test.app.com/login`
- Browsers: Chrome, Firefox, Edge
- Database with test user credentials

### 5. Test Execution
- Execute test cases manually/automated.
- Record pass/fail results.

### 6. Defect Reporting
**Example:**
- **Bug:** Password is visible instead of masked.
- **Bug:** Invalid login redirects to dashboard instead of showing error.

### 7. Test Closure
- Prepare final test summary report.
- Coverage: 100% of login scenarios tested.
- No major defects remain open.

## 📌 STLC Mermaid.js Diagram

Here’s a Mermaid flowchart you can use directly:

```mermaid
   flowchart TD
    A[Requirement Analysis] --> B[Test Planning]
    B --> C[Test Case Design]
    C --> D[Test Environment Setup]
    D --> E[Test Execution]
    E --> F[Test Cycle Closure]

    %% Requirement Analysis
    A --> A1{"Activities:\n- Analyze requirements\n- Identify testable items\n- Define entry/exit criteria"}
    A --> A2{"Deliverables:\n- Requirement Traceability Matrix (RTM)\n- Automation feasibility report"}

    %% Test Planning
    B --> B1{"Activities:\n- Define scope & objectives\n- Estimate effort & cost\n- Identify risks\n- Prepare test plan"}
    B --> B2{"Deliverables:\n- Test Plan\n- Effort estimation\n- Risk mitigation plan"}

    %% Test Case Design
    C --> C1{"Activities:\n- Design test cases & scripts\n- Create test data\n- Update RTM"}
    C --> C2{"Deliverables:\n- Test Cases\n- Test Data\n- Updated RTM"}

    %% Test Environment Setup
    D --> D1{"Activities:\n- Identify environment needs\n- Configure hardware/software\n- Prepare test environment"}
    D --> D2{"Deliverables:\n- Test Environment ready\n- Smoke test results"}

    %% Test Execution
    E --> E1{"Activities:\n- Execute test cases\n- Log defects\n- Retest & regression testing"}
    E --> E2{"Deliverables:\n- Test Execution Report\n- Defect Reports\n- Updated RTM"}

    %% Test Cycle Closure
    F --> F1{"Activities:\n- Evaluate exit criteria\n- Analyze test results\n- Prepare test summary\n- Lessons learned"}
    F --> F2{"Deliverables:\n- Test Summary Report\n- Test Closure Report\n- Metrics & Lessons Learned"}
```
