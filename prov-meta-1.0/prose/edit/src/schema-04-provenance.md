## Provenance {#provenance}

The `provenance` member describes the provenance of the dataset.

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

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

Table: Type `Provenance` (Record){#tab:provenance-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name  | Type              | \#   | Description                                            |
|---:|:------|:------------------|:-----|:-------------------------------------------------------|
|  1 | start | String /date-time | 0..1 | The start of the data collection or generation period. |
|  2 | end   | String /date-time | 0..1 | The end of the data collection or generation period.   |

Table: Type `GenerationPeriod` (Record){#tab:generation-period-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name             | Type                 | \#   | Description                                       |
|---:|:-----------------|:---------------------|:-----|:--------------------------------------------------|
|  1 | code             | GenerationMethodCode | 1    | A short code identifying the generation method.   |
|  2 | system           | String               | 0..1 | The code system used to interpret the code value. |
|  3 | long-description | String               | 0..1 | A detailed description of the method.             |

Table: Type `GenerationMethod` (Record){#tab:generation-method-record}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item                     | Description                                            |
|---:|:-------------------------|:-------------------------------------------------------|
|  0 | data-augmentation        | Data generation through augmentation of existing data. |
|  1 | data-mining              | Data collected through automated data mining.          |
|  2 | feeds                    | Data received through data feeds.                      |
|  3 | machine-generated-ml-ops | Data generated through machine learning operations.    |
|  4 | other                    | A generation method not listed here.                   |
|  5 | primary-user-source      | Data collected directly from primary users.            |
|  6 | simulations              | Data generated through simulations.                    |
|  7 | social-media             | Data collected from social media platforms.            |
|  8 | syndication              | Data received through syndication.                     |
|  9 | transfer-learning        | Data generated through transfer learning.              |
| 10 | user-generated-content   | Data created by end users.                             |
| 11 | web-scraping-crawling    | Data collected by web scraping or crawling.            |

Table: Type `GenerationMethodCode` (Enumerated){#tab:generation-method-code-enum}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item                     | Description                           |
|---:|:-------------------------|:--------------------------------------|
|  0 | application/json         | JSON data format.                     |
|  1 | application/jsonld       | JSON-LD linked data format.           |
|  2 | application/msword       | Microsoft Word document format.       |
|  3 | application/vnd.ms-excel | Microsoft Excel spreadsheet format.   |
|  4 | application/zip          | ZIP archive format.                   |
|  5 | image/bmp                | BMP image format.                     |
|  6 | image/gif                | GIF image format.                     |
|  7 | image/jpeg               | JPEG image format.                    |
|  8 | image/png                | PNG image format.                     |
|  9 | image/x-png              | PNG image format (legacy media type). |
| 10 | other                    | A format not listed here.             |
| 11 | text/csv                 | CSV text format.                      |
| 12 | text/plain               | Plain text format.                    |

Table: Type `ModalityFormat` (Enumerated){#tab:modality-format-enum}
