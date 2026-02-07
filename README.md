# Salesforce Picklist Dependency Automation (Python + Metadata API)

This project automates the creation of **Salesforce Field Dependencies** for large picklist datasets (Country → State → City, etc.) by updating the **field metadata XML files** directly using Python.

Instead of manually adding hundreds of dependent picklist values inside Salesforce Setup — which is slow, repetitive, and error-prone — this tool reads from an Excel file and automatically generates:

- Correct `<valueSettings>` dependency mappings  
- Correct `<valueSetDefinition>` structure (untouched labels)  
- A clean, pretty-formatted updated metadata file  
- A backup copy of the original file  

This saves **hours of manual clicking** and is ideal for large datasets with 1000+ values.

---

## 📁 Folder Structure

```
PicklistAutomation/
│
├── generate_metadata.py         # Main Python script
├── locations.xlsx               # Input Excel (Country-State data)
│
└── metadata/
     └── customfields/
          ├── Shipping_State__c.field-meta.xml         # Original metadata
          ├── Shipping_State__c.field-meta.backup.xml  # Auto backup
          └── Shipping_State__c.field-meta.updated.xml # Auto generated output
```

---

## 🧩 How It Works

1. **You provide an Excel file (`locations.xlsx`)**  
   containing two columns:

   | Country | State |
   |---------|--------|
   | IND | MH |
   | IND | WB |
   | ARE | DUH |
   | ARE | AUD |

2. The script:
   - Reads the Excel  
   - Loads the existing metadata XML  
   - **Preserves all original labels, API names, and picklist values**  
   - **Deletes only the old `<valueSettings>`**  
   - Creates new field-dependency mappings  
   - Writes a clean, pretty XML output  
   - Creates a backup of the original metadata file  

---

## 🚀 Running the Script

### Prerequisites
- Python 3 installed  
- `pandas` library installed  
  ```
  pip install pandas
  ```

### Run the script

```
cd PicklistAutomation
python generate_metadata.py
```

### After running:
- `Shipping_State__c.field-meta.backup.xml` → original copy  
- `Shipping_State__c.field-meta.updated.xml` → upload/deploy to Salesforce  

---

## 🧪 Where to Deploy the Output

The generated XML (`.updated.xml`) can be deployed via:

- Salesforce VS Code Extensions (SF CLI Deployment)  
- Change Sets  
- ANT Migration Tool  
- Git-based CI/CD (Azure DevOps, Jenkins, GitHub Actions, AutoRABIT, Copado, etc.)

Rename it back to:

```
Shipping_State__c.field-meta.xml
```

before deployment.

---

## ✨ Why This Tool Is Useful

- Saves **hours** of manual admin work  
- Eliminates human errors  
- Perfect for large, hierarchical picklists (countries → states → cities)  
- 100% Salesforce-compliant metadata  
- Non-destructive: **labels and values remain untouched**  
- Ideal for Admins, Developers, and DevOps Engineers  

---

## 📌 Author  
**Tuhin Paul**  
Salesforce Developer & Admin  
Automating repetitive tasks to make life easy 💙

---

# 🎉 Happy Automating!
