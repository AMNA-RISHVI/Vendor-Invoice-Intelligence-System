# Vendor Invoice Intelligence System

## Table of Contents
- <a href="#overview">Project Overview</a>
- <a href="#business-objectives">Business Objectives</a>
- <a href="#data-sources">Data Sources</a>
- <a href="#eda">Exploratory Data Analysis</a>
- <a href="#models-used">Models Used</a>
- <a href="#metrics">Evaluation Metrics</a>
- <a href="#application">Application</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#how-to-run-this-project">How to Run this Project</a>
- <a href="#author--contact">Author & Contact</a>

--- 
<h2><a class="anchor" id="overview"></a>Project Overview</h2>

---
<h2><a class="anchor" id="business-objectives"></a>Business Objectives</h2>

---
<h2><a class="anchor" id="data-sources"></a>Data Sources</h2>

Data is sorted in a relational SQLite database (inventory.db) with the following tables:
- vendor_invoice - Invoice-level financial and timing data
- purchases - Item-level purchase details
- purchase_prices - Reference purchase prices
- begin_inventory, end_inventory - Inventory snapshots
  
SQL aggregation is used to generate invoice-level features.

---
<h2><a class="anchor" id="eda"></a>Exploratory Data Analysis</h2>

----
<h2><a class="anchor" id="models-used"></a>Models Used</h2>

## Regression (Freight Prediction)
- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor (final model)

## Classification (Invoice Flagging)
- Logistic Regression(baseline)
- Decision Tree Classifier
- Random Forest Classifier (final model with GridSearchCV)

Hyperparameter tuning is performed using GridSearchCV with F1-score to handle class imbalance.

---
<h2><a class="anchor" id="metrics"></a>Evaluation Metrics</h2>

---
<h2><a class="anchor" id="application"></a>Application</h2>

---
<h2><a class="anchor" id="how-to-run-this-project"></a>Project Structure</h2>

---
<h2><a class="anchor" id="project-structure"></a>How to Run this Project</h2>

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>
 
**Amna Rishvi**  
📧 Email: fathiamnarishvi@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/amnarishvi/)  
🔗 [Portfolio](https://amna-rishvi.vercel.app/)

---
