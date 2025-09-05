# Testing Techniques Mastery

This section contains practical implementations of core software testing techniques, enhanced with AI and real-world scenarios.

## 📁 Contents

- **`BVA_Quantity_TestCases.xlsx`**
  - Boundary Value Analysis test cases for a product quantity field (e.g., Min: 1, Max: 100).
  - Tests values: 0, 1, 2, 99, 100, 101.

- **`DecisionTable_MoneyTransfer.xlsx`**
  - A decision table for a money transfer feature with conditions like Sufficient Balance, Valid Account, 2FA Enabled, etc.
  - Covers all possible combinations of rules and expected actions.

- **`email_sending_decision_table.xlsx`**
  - A decision table for an email system with conditions: Valid Recipient, Attachment Size, Network Status.
  - Maps conditions to actions like Send Success, Send Failure, Queue Email.

- **`ecommerce_discount_decision_table.csv`**
  - Decision table for e-commerce discount rules based on User Tier (Bronze, Silver, Gold) and Cart Value.
  - Calculates the final discount percentage for various combinations.

- **`atm_withdrawal_decision_table.csv`**
  - Decision table for ATM withdrawal logic involving conditions: Valid Card, Correct PIN, Sufficient Balance, Daily Limit.
  - Defines actions: Dispense Cash, Show Error, Retain Card.

- **`ATM_State_Transition_Diagram.png`**
  - A visual diagram (likely created using Mermaid or a drawing tool) showing state transitions for an ATM.
  - States include: Idle, Card Inserted, PIN Validated, Selecting Option, Amount Entered, Dispensing Cash, etc.

- **`Exploratory_Testing_Report_Template.pdf`**
  - A template used to document and report findings from exploratory testing sessions.
  - Includes sections for Test Charter, Areas Explored, Findings, Bugs, and Notes.

## 🧪 Techniques Applied

1.  **Boundary Value Analysis (BVA):** Applied to numeric input fields to find edge-case defects.
2.  **Equivalence Partitioning:** Used to group test inputs for efficient test coverage.
3.  **Decision Table Testing:** Implemented for complex business logic with multiple conditions and actions.
4.  **State Transition Testing:** Used to model and test systems with finite states and transitions.
5.  **Exploratory Testing:** Performed on real-world applications to learn the system and find unstructured bugs.

## 🤖 AI Integration

- AI prompts were used to generate initial test cases and decision tables.
- The output was validated, refined, and documented manually to ensure accuracy and relevance.

## 📊 Purpose

This portfolio demonstrates the ability to:
- Select and apply the right testing technique based on the requirement.
- Use AI as a force multiplier to enhance test design productivity.
- Create clear, detailed, and professional test documentation.
