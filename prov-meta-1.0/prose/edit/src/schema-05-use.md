## Use {#use}

The `use` member describes the legal use and restrictions applicable to the dataset.

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name                | Type             | \#    | Description                                                                               |
|---:|:--------------------|:-----------------|:------|:------------------------------------------------------------------------------------------|
|  1 | intended-purpose    | Purpose          | 1..\* | The purpose or purposes for which the dataset was created.                                |
|  2 | classification      | Classification   | 0..\* | Confidentiality classifications applicable to the dataset.                                |
|  3 | consents            | String           | 0..\* | Locations of consent documentation or agreements related to the data.                     |
|  4 | data-risk-reducing  | DataRiskReducing | 0..\* | Techniques used to reduce known data risk.                                                |
|  5 | processing-included | GeographicRegion | 0..\* | Geographical boundaries within which the data may be processed.                           |
|  6 | processing-excluded | GeographicRegion | 0..\* | Geographical boundaries within which the data may not be processed.                       |
|  7 | storage-allowed     | GeographicRegion | 0..\* | Geographical locations where the data may be stored.                                      |
|  8 | storage-forbidden   | GeographicRegion | 0..\* | Geographical locations where the data may not be stored.                                  |
|  9 | license             | String           | 0..\* | The terms under which the dataset can be used, including any restrictions or obligations. |
| 10 | copyright           | String           | 0..\* | Copyright information covering proprietary information in the dataset.                    |
| 11 | patent              | String           | 0..\* | Patent information covering proprietary information in the dataset.                       |
| 12 | trademark           | String           | 0..\* | Trademark information covering proprietary information in the dataset.                    |

Table: Type `Use` (Record){#tab:use-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name             | Type        | \#   | Description                                       |
|---:|:-----------------|:------------|:-----|:--------------------------------------------------|
|  1 | code             | PurposeCode | 1    | A short code identifying the intended purpose.    |
|  2 | long-description | String      | 1    | A detailed description of the intended purpose.   |
|  3 | system           | String      | 0..1 | The code system used to interpret the code value. |

Table: Type `Purpose` (Record){#tab:purpose-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name       | Type       | \#   | Description                                                                                   |
|---:|:-----------|:-----------|:-----|:----------------------------------------------------------------------------------------------|
|  1 | regulation | Regulation | 1    | The regulation or classification standard being evaluated.                                    |
|  2 | evaluated  | Boolean    | 1    | Whether the dataset has been evaluated against this classification (`true`) or not (`false`). |
|  3 | tool       | String     | 0..1 | The tool used to perform the evaluation.                                                      |

Table: Type `Classification` (Record){#tab:classification-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name             | Type                | \#   | Description                                                  |
|---:|:-----------------|:--------------------|:-----|:-------------------------------------------------------------|
|  1 | code             | ConfidentialityCode | 1    | A short code identifying the confidentiality classification. |
|  2 | system           | String              | 0..1 | The code system used to interpret the code value.            |
|  3 | long-description | String              | 0..1 | A detailed description of the regulation or classification.  |

Table: Type `Regulation` (Record){#tab:regulation-record}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item  | Description                                       |
|---:|:------|:--------------------------------------------------|
|  0 | other | A confidentiality classification not listed here. |
|  1 | pci   | Payment Card Industry (PCI) data.                 |
|  2 | pfi   | Personal Financial Information (PFI).             |
|  3 | phi   | Protected Health Information (PHI).               |
|  4 | pi    | Personal Information (PI).                        |
|  5 | sci   | Sensitive Compartmented Information (SCI).        |
|  6 | spi   | Sensitive Personal Information (SPI).             |

Table: Type `ConfidentialityCode` (Enumerated){#tab:confidentiality-code-enum}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item                      | Description                                           |
|---:|:--------------------------|:------------------------------------------------------|
|  0 | alignment                 | Dataset intended for model alignment tasks.           |
|  1 | evaluation                | Dataset intended for evaluation or benchmarking.      |
|  2 | other                     | A purpose not listed here.                            |
|  3 | pre-training              | Dataset intended for model pre-training.              |
|  4 | production                | Dataset intended for production use.                  |
|  5 | quality-assurance         | Dataset intended for quality assurance testing.       |
|  6 | research                  | Dataset intended for research use.                    |
|  7 | staging-testing           | Dataset intended for staging or testing environments. |
|  8 | synthetic-data-generation | Dataset intended for generating synthetic data.       |

Table: Type `PurposeCode` (Enumerated){#tab:purpose-code-enum}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name          | Type           | \#    | Description                                                |
|---:|:--------------|:---------------|:------|:-----------------------------------------------------------|
|  1 | tool-used     | String         | 1     | The name of the tool used for data risk reduction.         |
|  2 | tool-category | Method         | 0..1  | The category of the tool used for data risk reduction.     |
|  3 | technology    | DataTechnology | 0..1  | The privacy-enhancing or data-reducing technology applied. |
|  4 | parameters    | Parameter      | 0..\* | The parameters passed to the tool.                         |
|  5 | results       | String         | 0..\* | The results of applying the tool.                          |

Table: Type `DataRiskReducing` (Record){#tab:data-risk-reducing-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name  | Type   | \#   | Description          |
|---:|:------|:-------|:-----|:---------------------|
|  1 | name  | String | 1    | The parameter name.  |
|  2 | value | String | 0..1 | The parameter value. |

Table: Type `Parameter` (Record){#tab:parameter-record}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item                           | Description                                                                                                                                                         |
|---:|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | data-anonymization             | Transforms the dataset so that individuals cannot be identified, directly or indirectly, from the resulting records.                                                |
|  1 | data-encryption                | Encodes dataset content so that it is readable only by parties holding the decryption key; typically applied at rest or in transit.                                 |
|  2 | data-masking                   | Replaces sensitive field values with realistic but fictitious substitutes, preserving format and statistical properties without exposing the originals.             |
|  3 | data-minimization              | Reduces the dataset to only the fields and records necessary for the stated purpose, limiting exposure of personal or sensitive data.                               |
|  4 | data-redaction                 | Removes or obscures specific values or text spans identified as sensitive, such as names, identifiers, or health information.                                       |
|  5 | differential-privacy           | Adds calibrated statistical noise so that the presence or absence of any individual record cannot be reliably inferred from the released data.                      |
|  6 | federated-learning             | Produces model artefacts by training across distributed sources without centralising raw data, so the original dataset is never directly shared.                    |
|  7 | homomorphic-encryption         | Enables computation on ciphertext without decryption, so analytical results can be derived without exposing plaintext values.                                       |
|  8 | k-anonymity                    | Generalises quasi-identifying attributes so that each record is indistinguishable from at least k-1 other records in the dataset.                                   |
|  9 | l-diversity                    | Extends k-anonymity by requiring that each equivalence class contains at least l well-represented distinct sensitive attribute values.                              |
| 10 | other                          | A data risk reduction technology not covered by the defined values; use `tool-category` or `results` to describe the specific technique applied.                    |
| 11 | pseudonymization               | Replaces direct identifiers with artificial pseudonyms; re-identification remains possible through a separate, controlled mapping table.                            |
| 12 | secure-multi-party-computation | Allows multiple parties to jointly compute over their respective inputs without revealing those inputs to each other (SMC).                                         |
| 13 | t-closeness                    | Extends l-diversity by requiring that the distribution of sensitive values within each equivalence class closely matches their overall distribution in the dataset. |
| 14 | tokenization                   | Substitutes sensitive values with non-sensitive tokens; the originals are recoverable only through a separate, secured token vault.                                 |

Table: Type `DataTechnology` (Enumerated){#tab:data-technology-enum}
