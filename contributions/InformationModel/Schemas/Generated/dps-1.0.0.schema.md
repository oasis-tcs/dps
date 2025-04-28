       package: "https://dataandtrustalliance.org/data-provenance-standard-1.0.0.schema/"
   description: "The Data Provenance Standard is made up of three groups of metadata elements: Source, Provenance, and Use."
         roots: ["Root"]
        config: {"$MaxString": 1000, "$FieldName": "^[$a-z][-_$A-Za-z0-9]{0,63}$"}
  jadn_version: "http://oasis-open.org/openc2/jadn/v2.0/schema/"

The Data Provenance Standard is made up of three groups of metadata elements: Source, Provenance, and Use.

**Type: Root (Record)**

| ID | Name           | Type            | \# | Description                                             |
|----|----------------|-----------------|----|---------------------------------------------------------|
| 1  | **source**     | Root.source     | 1  | This describes a dataset and the source of the dataset. |
| 2  | **provenance** | Root.provenance | 1  | This describes the provenance of the dataset.           |
| 3  | **use**        | Root.use        | 1  | This group describes legal use and restrictions.        |

**********

This describes a dataset and the source of the dataset.

**Type: Root.source (Record)**

| ID | Name            | Type   | \#   | Description                                                                                                                                                                                                                                                    |
|----|-----------------|--------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **version**     | String | 1    | Specifies the version of the schema or standards used to define the metadata for this dataset, ensuring consistency and compatibility over time.                                                                                                               |
| 2  | **title**       | String | 1    | The official name of the dataset, which should be descriptive and help easily identify the dataset's content and purpose.                                                                                                                                      |
| 3  | **id**          | String | 1    | A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquely distinguish it from others, ensuring no confusion or overlap.                                                                                                            |
| 4  | **location**    | String | 0..1 | The web address where the dataset's metadata is published and can be accessed, providing a direct link to detailed information about the dataset. Typically will be a unique URL of the current dataset.                                                       |
| 5  | **issuer**      | Issuer | 1    | The legal entity responsible for creating the dataset, providing accountability and a point of contact for inquiries.                                                                                                                                          |
| 6  | **description** | String | 1    | Contains a detailed narrative that explains the contents, scope, and purpose of the dataset. It provides essential contextual information that helps users understand what the data represents, how it was collected, and any limitations or recommended uses. |

**********

| Type Name  | Type Definition            | Description                                                                                                           |
|------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Issuer** | ArrayOf(Issuer-item){1..*} | The legal entity responsible for creating the dataset, providing accountability and a point of contact for inquiries. |

**********

**Type: Issuer-item (Record)**

| ID | Name        | Type    | \#   | Description |
|----|-------------|---------|------|-------------|
| 1  | **name**    | String  | 1    |             |
| 2  | **address** | Address | 0..1 |             |

**********

| Type Name   | Type Definition | Description |
|-------------|-----------------|-------------|
| **Address** | ArrayOf(String) |             |

**********

This describes the provenance of the dataset.

**Type: Root.provenance (Record)**

| ID | Name                  | Type                              | \#   | Description                                                                                                                                                                                |
|----|-----------------------|-----------------------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **source**            | String                            | 0..1 | Identifies where the metadata for any source datasets that contribute to the current dataset can be found, establishing lineage and dependencies. This field establishes lineage.          |
| 2  | **origin**            | Origin                            | 0..1 | If the data originates from a different organization than the one who issued the dataset, this field identifies the original source's legal name.                                          |
| 3  | **origin-geography**  | Origin-geography                  | 1    | The geographical location where the data was originally collected, which can be important for compliance with regional laws and understanding the data's context.                          |
| 4  | **date**              | String                            | 1    | The date when the dataset was compiled or created, providing a temporal context for the data.                                                                                              |
| 5  | **previous-date**     | String                            | 0..1 | The release date of the last version of the dataset, if it has been updated or revised, to track changes and updates over time.                                                            |
| 6  | **generation-period** | Root.provenance.generation-period | 0..1 | The span of time during which the data within the dataset was collected or generated, offering insight into the dataset's timeliness and relevance.                                        |
| 7  | **generation-method** | Generation-method                 | 1    | The methodology or procedures used to collect, generate, or compile the data, giving insight into its reliability and validity.                                                            |
| 8  | **format**            | Format                            | 0..1 | Describes the nature of the data within the dataset, such as numerical, textual, or multimedia, helping users understand what kind of information is contained within the file or dataset. |
| 9  | **sub-provenance**    | Root.provenance                   | 0..1 |                                                                                                                                                                                            |

**********

| Type Name  | Type Definition      | Description                                                                                                                                       |
|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Origin** | ArrayOf(Origin-item) | If the data originates from a different organization than the one who issued the dataset, this field identifies the original source's legal name. |

**********

**Type: Origin-item (Record)**

| ID | Name        | Type    | \#   | Description |
|----|-------------|---------|------|-------------|
| 1  | **name**    | String  | 1    |             |
| 2  | **address** | Address | 0..1 |             |

**********

| Type Name            | Type Definition                      | Description                                                                                                                                                       |
|----------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Origin-geography** | ArrayOf(Origin-geography-item){1..*} | The geographical location where the data was originally collected, which can be important for compliance with regional laws and understanding the data's context. |

**********

**Type: Origin-geography-item (Record)**

| ID | Name        | Type   | \#   | Description |
|----|-------------|--------|------|-------------|
| 1  | **country** | String | 1    |             |
| 2  | **state**   | String | 0..1 |             |

**********

The span of time during which the data within the dataset was collected or generated, offering insight into the dataset's timeliness and relevance.

**Type: Root.provenance.generation-period (Record)**

| ID | Name      | Type   | \#   | Description     |
|----|-----------|--------|------|-----------------|
| 1  | **start** | String | 0..1 | Start date/time |
| 2  | **end**   | String | 0..1 | End date/time   |

**********

| Type Name             | Type Definition                       | Description                                                                                                                     |
|-----------------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Generation-method** | ArrayOf(Generation-method-item){1..*} | The methodology or procedures used to collect, generate, or compile the data, giving insight into its reliability and validity. |

**********

**Type: Generation-method-item (Record)**

| ID | Name            | Type   | \#   | Description |
|----|-----------------|--------|------|-------------|
| 1  | **code**        | String | 1    |             |
| 2  | **system**      | String | 0..1 |             |
| 3  | **description** | String | 0..1 |             |

**********

| Type Name  | Type Definition | Description                                                                                                                                                                                |
|------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format** | ArrayOf(String) | Describes the nature of the data within the dataset, such as numerical, textual, or multimedia, helping users understand what kind of information is contained within the file or dataset. |

**********

This group describes legal use and restrictions.

**Type: Root.use (Record)**

| ID | Name                    | Type                | \#   | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
|----|-------------------------|---------------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **classification**      | Classification      | 0..1 | Indicate if the dataset includes data falling into the confidentiality classification. Each classifier must be evaluated as true/false/unknown.                                                                                                                                                                                                                                                                 |
| 2  | **consents**            | Consents            | 0..1 | Specifies where consent documentation or agreements related to the data can be found, ensuring legal compliance and regulatory use. This element must be populated when Privacy Consent is appropriate. When populated it points to either one Privacy Consent Policy that all individuals in the dataset agreed to, or one Privacy Policy for each individual in the dataset with that individual's signature. |
| 3  | **privacy-enhancing**   | Privacy-enhancing   | 0..1 | Indicates whether techniques were used to protect personally identifiable information (PII) or sensitive personal information (SPI), highlighting the dataset's privacy considerations.                                                                                                                                                                                                                         |
| 4  | **processing-included** | Processing-included | 0..1 | Defines the geographical boundaries within which the data can be processed, often for legal or regulatory reasons.                                                                                                                                                                                                                                                                                              |
| 5  | **processing-excluded** | Processing-excluded | 0..1 | Defines the geographical boundaries within which the data cannot be processed, often for legal or regulatory reasons.                                                                                                                                                                                                                                                                                           |
| 6  | **storage-allowed**     | Storage-allowed     | 0..1 | Specifies where the data may be stored, crucial for compliance with data sovereignty laws.                                                                                                                                                                                                                                                                                                                      |
| 7  | **storage-forbidden**   | Storage-forbidden   | 0..1 | Specifies where the data may not be stored, crucial for compliance with data sovereignty laws.                                                                                                                                                                                                                                                                                                                  |
| 8  | **license**             | License             | 0..1 | Details the location or point of contact for identifying the terms under which the dataset can be used, including any restrictions or obligations, clarifying legal use and distribution rights. License may be an End User License Agreement (EULA), subject to Data Use Agreement (DUA).                                                                                                                      |
| 9  | **intended-purpose**    | Intended-purpose    | 1    | Describes the purpose for which the dataset was created, guiding users on its intended use and potential applications against identified use cases. List all that apply from the Data Use codes that apply. Additional codes can be included with descriptions.                                                                                                                                                 |
| 10 | **copyright**           | Copyright           | 0..1 | Indicates whether the dataset contains proprietary information that is covered with a Copyright and the terms of said Copyright.                                                                                                                                                                                                                                                                                |
| 11 | **patent**              | Patent              | 0..1 | Indicates whether the dataset contains proprietary information that is covered with a Patent and said Patent number.                                                                                                                                                                                                                                                                                            |
| 12 | **trademark**           | Trademark           | 0..1 | Indicates whether the dataset contains proprietary information that is covered with a Trademark, and the terms of said Trademark.                                                                                                                                                                                                                                                                               |

**********

| Type Name          | Type Definition              | Description                                                                                                                                     |
|--------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Classification** | ArrayOf(Classification-item) | Indicate if the dataset includes data falling into the confidentiality classification. Each classifier must be evaluated as true/false/unknown. |

**********

**Type: Classification-item (Record)**

| ID | Name           | Type                           | \#   | Description |
|----|----------------|--------------------------------|------|-------------|
| 1  | **regulation** | Classification-item.regulation | 1    |             |
| 2  | **evaluated**  | Boolean                        | 1    |             |
| 3  | **tool**       | String                         | 0..1 |             |

**********

**Type: Classification-item.regulation (Record)**

| ID | Name            | Type   | \#   | Description |
|----|-----------------|--------|------|-------------|
| 1  | **code**        | String | 1    |             |
| 2  | **system**      | String | 0..1 |             |
| 3  | **description** | String | 0..1 |             |

**********

| Type Name    | Type Definition | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Consents** | ArrayOf(String) | Specifies where consent documentation or agreements related to the data can be found, ensuring legal compliance and regulatory use. This element must be populated when Privacy Consent is appropriate. When populated it points to either one Privacy Consent Policy that all individuals in the dataset agreed to, or one Privacy Policy for each individual in the dataset with that individual's signature. |

**********

| Type Name             | Type Definition                 | Description                                                                                                                                                                             |
|-----------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Privacy-enhancing** | ArrayOf(Privacy-enhancing-item) | Indicates whether techniques were used to protect personally identifiable information (PII) or sensitive personal information (SPI), highlighting the dataset's privacy considerations. |

**********

**Type: Privacy-enhancing-item (Record)**

| ID | Name              | Type                                 | \#   | Description |
|----|-------------------|--------------------------------------|------|-------------|
| 1  | **tool-category** | Privacy-enhancing-item.tool-category | 0..1 |             |
| 2  | **tool-used**     | String                               | 0..1 |             |
| 3  | **parameters**    | Parameters                           | 0..1 |             |
| 4  | **result**        | Result                               | 0..1 |             |

**********

**Type: Privacy-enhancing-item.tool-category (Record)**

| ID | Name            | Type   | \#   | Description |
|----|-----------------|--------|------|-------------|
| 1  | **code**        | String | 1    |             |
| 2  | **system**      | String | 0..1 |             |
| 3  | **description** | String | 0..1 |             |

**********

| Type Name      | Type Definition | Description |
|----------------|-----------------|-------------|
| **Parameters** | ArrayOf(String) |             |

**********

| Type Name  | Type Definition | Description |
|------------|-----------------|-------------|
| **Result** | ArrayOf(String) |             |

**********

| Type Name               | Type Definition                   | Description                                                                                                        |
|-------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Processing-included** | ArrayOf(Processing-included-item) | Defines the geographical boundaries within which the data can be processed, often for legal or regulatory reasons. |

**********

**Type: Processing-included-item (Record)**

| ID | Name        | Type   | \#   | Description |
|----|-------------|--------|------|-------------|
| 1  | **country** | String | 1    |             |
| 2  | **state**   | String | 0..1 |             |

**********

| Type Name               | Type Definition                   | Description                                                                                                           |
|-------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Processing-excluded** | ArrayOf(Processing-excluded-item) | Defines the geographical boundaries within which the data cannot be processed, often for legal or regulatory reasons. |

**********

**Type: Processing-excluded-item (Record)**

| ID | Name        | Type   | \#   | Description |
|----|-------------|--------|------|-------------|
| 1  | **country** | String | 1    |             |
| 2  | **state**   | String | 0..1 |             |

**********

| Type Name           | Type Definition               | Description                                                                                |
|---------------------|-------------------------------|--------------------------------------------------------------------------------------------|
| **Storage-allowed** | ArrayOf(Storage-allowed-item) | Specifies where the data may be stored, crucial for compliance with data sovereignty laws. |

**********

**Type: Storage-allowed-item (Record)**

| ID | Name        | Type   | \#   | Description |
|----|-------------|--------|------|-------------|
| 1  | **country** | String | 1    |             |
| 2  | **state**   | String | 0..1 |             |

**********

| Type Name             | Type Definition                 | Description                                                                                    |
|-----------------------|---------------------------------|------------------------------------------------------------------------------------------------|
| **Storage-forbidden** | ArrayOf(Storage-forbidden-item) | Specifies where the data may not be stored, crucial for compliance with data sovereignty laws. |

**********

**Type: Storage-forbidden-item (Record)**

| ID | Name        | Type   | \#   | Description |
|----|-------------|--------|------|-------------|
| 1  | **country** | String | 1    |             |
| 2  | **state**   | String | 0..1 |             |

**********

| Type Name   | Type Definition | Description                                                                                                                                                                                                                                                                                |
|-------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **License** | ArrayOf(String) | Details the location or point of contact for identifying the terms under which the dataset can be used, including any restrictions or obligations, clarifying legal use and distribution rights. License may be an End User License Agreement (EULA), subject to Data Use Agreement (DUA). |

**********

| Type Name            | Type Definition                      | Description                                                                                                                                                                                                                                                     |
|----------------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Intended-purpose** | ArrayOf(Intended-purpose-item){1..*} | Describes the purpose for which the dataset was created, guiding users on its intended use and potential applications against identified use cases. List all that apply from the Data Use codes that apply. Additional codes can be included with descriptions. |

**********

**Type: Intended-purpose-item (Record)**

| ID | Name            | Type   | \#   | Description |
|----|-----------------|--------|------|-------------|
| 1  | **code**        | String | 1    |             |
| 2  | **system**      | String | 0..1 |             |
| 3  | **description** | String | 1    |             |

**********

| Type Name     | Type Definition | Description                                                                                                                      |
|---------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Copyright** | ArrayOf(String) | Indicates whether the dataset contains proprietary information that is covered with a Copyright and the terms of said Copyright. |

**********

| Type Name  | Type Definition | Description                                                                                                          |
|------------|-----------------|----------------------------------------------------------------------------------------------------------------------|
| **Patent** | ArrayOf(String) | Indicates whether the dataset contains proprietary information that is covered with a Patent and said Patent number. |

**********

| Type Name     | Type Definition | Description                                                                                                                       |
|---------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Trademark** | ArrayOf(String) | Indicates whether the dataset contains proprietary information that is covered with a Trademark, and the terms of said Trademark. |

**********
