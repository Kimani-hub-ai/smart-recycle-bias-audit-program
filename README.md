# smart-recycle-bias-audit-program

# ⚖️ Smart Recycle – Bias Audit Program

This project uses IBM’s [AI Fairness 360 (AIF360)](https://aif360.mybluemix.net/) toolkit to audit and assess fairness and bias in the COMPAS Recidivism dataset. The goal is to detect and interpret algorithmic bias in criminal justice risk prediction systems and demonstrate how fairness metrics can be measured.

---

## 📊 Dataset: COMPAS Recidivism

The COMPAS dataset contains records of criminal defendants and their risk assessments used by judges to determine the likelihood of reoffending. This dataset has been widely used in studies on algorithmic fairness due to observed racial disparities.

---

## 🔍 Features Audited

- Race (protected attribute)
- Risk scores (target)
- Positive outcomes (e.g., low risk prediction)
- Fairness metrics:
  - **Disparate Impact**
  - **Difference in Positive Outcome Rate**

---

## 🚀 How to Run

### 1. ✅ Clone the Repository

```bash
git clone https://github.com/your-username/smart-recycle-bias-audit.git
cd smart-recycle-bias-audit
