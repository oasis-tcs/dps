       package: "https://docs.oasis-open.org/dps/v1.0/schema/"
       version: "csd01"
   description: "Information Schema for Data Provenance Standard Metadata"
    namespaces: [["geo", "https://iso3166/202403/"]]
         roots: ["DPS-Metadata"]
        config: {"$FieldName": "^[$a-z][-_$A-Za-z0-9]{0,63}$"}
  jadn_version: "http://oasis-open.org/openc2/jadn/v2.0/schema/"

**Type: DPS-Metadata (Record)**

| ID | Name         | Type     | \# | Description                                                                                                                                      |
|----|--------------|----------|----|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **version**  | URL      | 1  | Specifies the version of the schema or standards used to define the metadata for this dataset, ensuring consistency and compatibility over time. |
| 2  | **metadata** | Metadata | 1  | The metadata about a dataset.                                                                                                                    |

**********

The Data Provenance Standard Metadata

**Type: Metadata (Record)**

| ID | Name           | Type       | \# | Description                                        |
|----|----------------|------------|----|----------------------------------------------------|
| 1  | **source**     | Source     | 1  | Describes a dataset and the source of the dataset. |
| 2  | **provenance** | Provenance | 1  | Provenance of the dataset.                         |
| 3  | **use**        | Use        | 1  | Legal use and restrictions.                        |

**********

**Type: Source (Record)**

| ID | Name            | Type   | \#    | Description                                                                                                               |
|----|-----------------|--------|-------|---------------------------------------------------------------------------------------------------------------------------|
| 1  | **title**       | String | 1     | The official name of the dataset, which should be descriptive and help easily identify the dataset's content and purpose. |
| 2  | **id**          | UID    | 1     | Unique metadata identifier                                                                                                |
| 3  | **location**    | URL    | 0..1  | Metadata location                                                                                                         |
| 4  | **issuer**      | Org    | 1..\* | Data issuer  (many?)                                                                                                      |
| 5  | **description** | String | 1     | Description of the dataset                                                                                                |

**********

**Type: Org (Record)**

| ID | Name        | Type    | \# | Description       |
|----|-------------|---------|----|-------------------|
| 1  | **name**    | String  | 1  | organization name |
| 2  | **address** | Address | 1  | address           |

**********

| Type Name   | Type Definition | Description                                      |
|-------------|-----------------|--------------------------------------------------|
| **Address** | ArrayOf(String) | Just lines for now, enable structured definition |

**********

**Type: Provenance (Record)**

| ID | Name                  | Type             | \#    | Description                                      |
|----|-----------------------|------------------|-------|--------------------------------------------------|
| 1  | **source**            | URL              | 1..\* | Source metadata for dataset                      |
| 2  | **origin**            | Org              | 0..1  | Source                                           |
| 3  | **origin-geography**  | geo:Country-Name | 1..\* | Data origin geography                            |
| 4  | **date**              | Timestamp        | 1     | Dataset issue date                               |
| 5  | **previous-date**     | Timestamp        | 1     | Date of previously-issued version of the dataset |
| 6  | **generation-period** | Generation       | 1     | Range of dates for data generation               |
| 7  | **generation-method** | Method           | 1..\* | Method (code/system/description?)                |
| 8  | **format**            | MediaType        | 0..\* | Data format                                      |
| 9  | **sub-provenance**    | Provenance       | 1     | Add key/link?                                    |

**********

**Type: Generation (Record)**

| ID | Name         | Type      | \# | Description                                         |
|----|--------------|-----------|----|-----------------------------------------------------|
| 1  | **oldest**   | Timestamp | 1  | Oldest component of data contained in the dataset   |
| 2  | **youngest** | Timestamp | 1  | Youngest component of data contained in the dataset |

**********

**Type: Use (Record)**

| ID | Name                  | Type                    | \#    | Description                                                                                                                       |
|----|-----------------------|-------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1  | **classification**    | Confidentiality         | 1     | Confidentiality Classification                                                                                                    |
| 2  | **consent**           | URL                     | 1..\* | Consent documentation location                                                                                                    |
| 3  | **privacy-enhancing** | Privacy-Tool            | 1..\* | Privacy enhancing technologies                                                                                                    |
| 4  | **processing**        | Processing-Geography    | 0..1  | Data processing geography                                                                                                         |
| 5  | **storage**           | Storage-Geography       | 0..1  | Data storage geography                                                                                                            |
| 6  | **license**           | ArrayOf(License) unique | 1     | License to use                                                                                                                    |
| 7  | **intended_purpose**  | Intended-Use            | 1     | Intended data use                                                                                                                 |
| 8  | **copyright**         | String                  | 0..\* | Indicates whether the dataset contains proprietary information that is covered with a Copyright and the terms of said Copyright.  |
| 9  | **patent**            | String                  | 0..\* | Indicates whether the dataset contains proprietary information that is covered with a Patent and said Patent number.              |
| 10 | **trademark**         | String                  | 0..\* | Indicates whether the dataset contains proprietary information that is covered with a Trademark, and the terms of said Trademark. |

**********

**Type: Intended-Use (Record)**

| ID | Name       | Type              | \#    | Description |
|----|------------|-------------------|-------|-------------|
| 1  | **non_ai** | Non-AI-Use unique | 1..\* | Non-AI      |
| 2  | **ai**     | AI-Use unique     | 1..\* | AI          |

**********

**Type: Processing-Geography (Record)**

| ID | Name               | Type      | \#    | Description                                                    |
|----|--------------------|-----------|-------|----------------------------------------------------------------|
| 1  | **same_as_origin** | Boolean   | 1     | Data processing geography is the same as data origin geography |
| 2  | **countries**      | Geography | 0..\* |                                                                |

**********

**Type: Storage-Geography (Record)**

| ID | Name                   | Type      | \#    | Description                                                     |
|----|------------------------|-----------|-------|-----------------------------------------------------------------|
| 1  | **same_as_processing** | Boolean   | 1     | Data storage geography is the same as data processing geography |
| 2  | **countries**          | Geography | 0..\* |                                                                 |

**********

**Type: Geography (Record)**

| ID | Name        | Type             | \#   | Description |
|----|-------------|------------------|------|-------------|
| 1  | **country** | geo:Country-Name | 1    |             |
| 2  | **state**   | geo:State-Name   | 0..1 |             |

**********

**Type: UID (Choice(anyOf))**

| ID | Name | Type         | \# | Description |
|----|------|--------------|----|-------------|
| 1  | **** | Binary /uuid | 1  | **uuid** -  |

**********

**Type: Privacy-Tool (Record)**

| ID | Name           | Type                  | \# | Description           |
|----|----------------|-----------------------|----|-----------------------|
| 1  | **tool_id**    | Tool-ID               | 1  | tool name and version |
| 2  | **technology** | Privacy-Technology    | 1  |                       |
| 3  | **params**     | MapOf(String, String) | 1  | key-value pair        |

**********

| Type Name   | Type Definition | Description |
|-------------|-----------------|-------------|
| **Tool-ID** | String          |             |

**********

**Type: Confidentiality (Record)**

| ID | Name               | Type                           | \#    | Description |
|----|--------------------|--------------------------------|-------|-------------|
| 1  | **classification** | Confidentiality-Classification | 1     |             |
| 2  | **tool_id**        | Tool-ID                        | 0..\* |             |

**********

| Type Name     | Type Definition | Description                  |
|---------------|-----------------|------------------------------|
| **Timestamp** | Integer /d3     | Milliseconds since the epoch |

**********

| Type Name | Type Definition | Description                          |
|-----------|-----------------|--------------------------------------|
| **URL**   | String /uri     | URI designated as a resource locator |

**********

**Type: Method (Enumerated)**

| ID | Item                        | Description |
|----|-----------------------------|-------------|
| 0  | **Other**                   |             |
| 1  | **Web scraping/Crawling**   |             |
| 2  | **Feeds**                   |             |
| 3  | **Syndication**             |             |
| 4  | **Data mining**             |             |
| 5  | **Machine generated/MLOps** |             |
| 6  | **Social media**            |             |
| 7  | **User generated content**  |             |
| 8  | **Primary user source**     |             |
| 9  | **Data augmentation**       |             |
| 10 | **Transfer learning**       |             |
| 11 | **Simulations**             |             |

**********

**Type: MediaType (Enumerated)**

| ID | Item                         | Description |
|----|------------------------------|-------------|
| 0  | **Other**                    |             |
| 1  | **application/json**         |             |
| 2  | **application/jsonld**       |             |
| 3  | **application/zip**          |             |
| 4  | **application/msword**       |             |
| 5  | **application/vnd.ms-excel** |             |
| 6  | **image/bmp**                |             |
| 7  | **image/jpeg**               |             |
| 8  | **image/x-png**              |             |
| 9  | **image/png**                |             |
| 10 | **image/gif**                |             |
| 11 | **text/csv**                 |             |
| 12 | **text/plain**               |             |

**********

**Type: Confidentiality-Classification (Enumerated)**

| ID | Item                                      | Description |
|----|-------------------------------------------|-------------|
| 0  | **Other**                                 |             |
| 1  | **Personal information (PI)/Demographic** |             |
| 2  | **Payment Card Industry (PCI)**           |             |
| 3  | **Personal Financial Information (PFI)**  |             |
| 4  | **Personal Health Information (PHI)**     |             |
| 5  | **Sensitive Personal Information (SPI)**  |             |

**********

**Type: Privacy-Technology (Enumerated)**

| ID | Item                                     | Description |
|----|------------------------------------------|-------------|
| 1  | **Data Anonymization**                   |             |
| 2  | **Data Encryption**                      |             |
| 3  | **Data Masking**                         |             |
| 4  | **Data Minimization**                    |             |
| 5  | **Data Redaction**                       |             |
| 6  | **Differential Privacy**                 |             |
| 7  | **Federated Learning**                   |             |
| 8  | **Homomorphic Encryption**               |             |
| 9  | **K-anonymity**                          |             |
| 10 | **L-diversity**                          |             |
| 11 | **Pseudonymization**                     |             |
| 12 | **Secure Multi-party Computation (SMC)** |             |
| 13 | **T-closeness**                          |             |
| 14 | **Tokenization**                         |             |

**********

**Type: License (Enumerated)**

| ID | Item                              | Description |
|----|-----------------------------------|-------------|
| 1  | **Non-commercial**                |             |
| 2  | **Public license**                |             |
| 3  | **Commercial/Negotiated License** |             |

**********

**Type: Non-AI-Use (Enumerated)**

| ID | Item                  | Description |
|----|-----------------------|-------------|
| 0  | **Other**             |             |
| 1  | **Staging/testing**   |             |
| 2  | **Production**        |             |
| 3  | **Quality assurance** |             |

**********

**Type: AI-Use (Enumerated)**

| ID | Item                          | Description |
|----|-------------------------------|-------------|
| 0  | **Other**                     |             |
| 1  | **Pre-Training**              |             |
| 2  | **Alignment**                 |             |
| 3  | **Evaluation**                |             |
| 4  | **Synthetic Data Generation** |             |

**********
