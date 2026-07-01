## Source {#source}

The `source` member characterizes the content and source of the dataset.

| ID | Name         | Type         | \#    | Description                                                                      |
|---:|:-------------|:-------------|:------|:---------------------------------------------------------------------------------|
|  1 | about        | About        | 1     | A detailed narrative explaining the contents, scope, and purpose of the dataset. |
|  2 | id           | Identity     | 1     | A unique identifier for this dataset, using at least one identification method.  |
|  3 | issuer       | Organization | 1..\* | The legal entity or entities responsible for creating the dataset.               |
|  4 | location     | String /uri  | 1     | The web address where this dataset's metadata is published and can be accessed.  |
|  5 | name         | String       | 1     | The official name of the dataset.                                                |
|  6 | data-version | Version      | 1     | The version of the dataset this metadata set describes.                          |

Table: Type `Source` (Record)

| ID | Name    | Type   | \#   | Description                                                                                        |
|---:|:--------|:-------|:-----|:---------------------------------------------------------------------------------------------------|
|  1 | content | String | 1    | Contextual information helping users understand what the data represents and how it was collected. |
|  2 | purpose | String | 1    | The recommended uses for this dataset.                                                             |
|  3 | scope   | String | 0..1 | Any limitations of the dataset.                                                                    |

Table: Type `About` (Record)

The `Identity` type provides at least one identifier for the dataset. At least one of its fields MUST be present.

| ID | Name       | Type         | \#    | Description                                           |
|---:|:-----------|:-------------|:------|:------------------------------------------------------|
|  1 | hashes     | HashEntry    | 0..\* | Cryptographic hash-based identifiers for the dataset. |
|  2 | uris       | String /uri  | 0..\* | URI identifiers for the dataset.                      |
|  3 | uuids      | String /uuid | 0..\* | UUID identifiers for the dataset.                     |
|  4 | custom-ids | CustomId     | 0..\* | Identifiers in any text format.                       |

Table: Type `Identity` (Map)

| ID | Name        | Type     | \#    | Description                                                              |
|---:|:------------|:---------|:------|:-------------------------------------------------------------------------|
|  1 | tree-hashes | TreeHash | 1..\* | The cryptographic hash values for this file or tree.                     |
|  2 | path        | String   | 1     | The path (file or filesystem tree root) identified by these hash values. |

Table: Type `HashEntry` (Record)

| ID | Name      | Type   | \# | Description                                                              |
|---:|:----------|:-------|:---|:-------------------------------------------------------------------------|
|  1 | algorithm | String | 1  | The name of the hash or tree/seal algorithm used to calculate the value. |
|  2 | value     | String | 1  | The cryptographic hash value in hexadecimal representation.              |

Table: Type `TreeHash` (Record)

| ID | Name           | Type   | \#    | Description                                            |
|---:|:---------------|:-------|:------|:-------------------------------------------------------|
|  1 | method         | String | 1     | The name of the method used to derive this identifier. |
|  2 | value          | String | 1     | The identifier value.                                  |
|  3 | tool           | String | 0..1  | The name of the tool used to derive this identifier.   |
|  4 | parameter-list | String | 0..\* | Parameters used when invoking the tool.                |

Table: Type `CustomId` (Record)
