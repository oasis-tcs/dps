## Provenance {#provenance}

The `provenance` member describes the provenance of the dataset.

\columns=iiii,nnnnnnnnnnnnnnnnnnnnnn,tttttttttttttttttttttt,hhhhhh,dddddddddddddddddddddddddddddddddddddddddddddd

| ID | Name              | Type             | \#    | Description                                                                                  |
|---:|:------------------|:-----------------|:------|:---------------------------------------------------------------------------------------------|
|  1 | origin-geography  | GeographicRegion | 1..\* | The geographical locations where the data was originally collected.                          |
|  2 | date              | String /date     | 1     | The date when the dataset was compiled or created (YYYY-MM-DD).                              |
|  3 | generation-method | GenerationMethod | 1..\* | The methodology or procedures used to collect, generate, or compile the data.                |
|  4 | source            | String /uri      | 0..1  | The URI of metadata for a source dataset contributing to this dataset, establishing lineage. |
|  5 | origin            | Organization     | 0..\* | The original source organization, if different from the dataset issuer.                      |
|  6 | previous-date     | String /date     | 0..1  | The release date of the previous version of this dataset (YYYY-MM-DD).                       |
|  7 | generation-period | GenerationPeriod | 0..1  | The span of time during which the data was collected or generated.                           |
|  8 | format            | ModalityFormat   | 0..\* | Describes the modality or media type of the data within the dataset.                         |
|  9 | sub-provenance    | Provenance       | 0..1  | Nested provenance information for a component of this dataset.                               |
| 10 | source-digest     | SourceDigest     | 0..1  | A cryptographic digest of the record referenced by `source`, computed at issuance.           |

Table: Type `Provenance` (Record){#tab:provenance-record}

\columns=iiii,nnnnnnnnnnnnnnnnnnnnnn,tttttttttttttttttttttt,hhhhhh,dddddddddddddddddddddddddddddddddddddddddddddd

| ID | Name      | Type   | \# | Description                                                |
|---:|:----------|:-------|:---|:-----------------------------------------------------------|
|  1 | algorithm | String | 1  | Digest algorithm identifier (e.g. sha256, sha384, sha512). |
|  2 | value     | String | 1  | The digest value, hex-encoded.                             |

Table: Type `SourceDigest` (Record){#tab:source-digest-record}

\columns=iiii,nnnnnnnnnnnnnnnnnnnnnn,tttttttttttttttttttttt,hhhhhh,dddddddddddddddddddddddddddddddddddddddddddddd

| ID | Name  | Type              | \#   | Description                                            |
|---:|:------|:------------------|:-----|:-------------------------------------------------------|
|  1 | start | String /date-time | 0..1 | The start of the data collection or generation period. |
|  2 | end   | String /date-time | 0..1 | The end of the data collection or generation period.   |

Table: Type `GenerationPeriod` (Record){#tab:generation-period-record}

\columns=iiii,nnnnnnnnnnnnnnnnnnnnnn,tttttttttttttttttttttt,hhhhhh,dddddddddddddddddddddddddddddddddddddddddddddd

| ID | Name             | Type                 | \#   | Description                                       |
|---:|:-----------------|:---------------------|:-----|:--------------------------------------------------|
|  1 | code             | GenerationMethodCode | 1    | A short code identifying the generation method.   |
|  2 | system           | String               | 0..1 | The code system used to interpret the code value. |
|  3 | long-description | String               | 0..1 | A detailed description of the method.             |

Table: Type `GenerationMethod` (Record){#tab:generation-method-record}

\columns=iiii,nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn,dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item                     | Description                                            |
|---:|:-------------------------|:-------------------------------------------------------|
|  1 | data-augmentation        | Data generation through augmentation of existing data. |
|  2 | data-mining              | Data collected through automated data mining.          |
|  3 | feeds                    | Data received through data feeds.                      |
|  4 | machine-generated-ml-ops | Data generated through machine learning operations.    |
|  5 | other                    | A generation method not listed here.                   |
|  6 | primary-user-source      | Data collected directly from primary users.            |
|  7 | simulations              | Data generated through simulations.                    |
|  8 | social-media             | Data collected from social media platforms.            |
|  9 | syndication              | Data received through syndication.                     |
| 10 | transfer-learning        | Data generated through transfer learning.              |
| 11 | user-generated-content   | Data created by end users.                             |
| 12 | web-scraping-crawling    | Data collected by web scraping or crawling.            |

Table: Type `GenerationMethodCode` (Enumerated){#tab:generation-method-code-enum}

\columns=iiii,nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn,dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item                     | Description                           |
|---:|:-------------------------|:--------------------------------------|
|  1 | application/json         | JSON data format.                     |
|  2 | application/jsonld       | JSON-LD linked data format.           |
|  3 | application/msword       | Microsoft Word document format.       |
|  4 | application/vnd.ms-excel | Microsoft Excel spreadsheet format.   |
|  5 | application/zip          | ZIP archive format.                   |
|  6 | image/bmp                | BMP image format.                     |
|  7 | image/gif                | GIF image format.                     |
|  8 | image/jpeg               | JPEG image format.                    |
|  9 | image/png                | PNG image format.                     |
| 10 | image/x-png              | PNG image format (legacy media type). |
| 11 | other                    | A format not listed here.             |
| 12 | text/csv                 | CSV text format.                      |
| 13 | text/plain               | Plain text format.                    |

Table: Type `ModalityFormat` (Enumerated){#tab:modality-format-enum}
