## Primary Metadata Elements {#primary-metadata-elements}

The root object of a Data Provenance Metadata record contains five required members.

| ID | Name       | Type        | \# | Description                                                                                                                                             |
|---:|:-----------|:------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | $schema    | String /uri | 1  | The URI identifying the schema this JSON object must be valid against. For this version the value is always the URI of the data-provenance JSON schema. |
|  2 | set        | Set         | 1  | Set-level metadata about this provenance metadata record.                                                                                               |
|  3 | source     | Source      | 1  | Characterizes the content and source of the dataset.                                                                                                    |
|  4 | provenance | Provenance  | 1  | Describes the provenance of the dataset.                                                                                                                |
|  5 | use        | Use         | 1  | Describes legal use and restrictions that apply to the dataset.                                                                                         |

Table: Type `DataProvenance` (Record)
