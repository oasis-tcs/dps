## Shared Types {#shared-types}

The following types are used in more than one of the sections above.

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name       | Type        | \#   | Description                             |
|---:|:-----------|:------------|:-----|:----------------------------------------|
|  1 | legal-name | String      | 1    | The legal name of the organization.     |
|  2 | address    | Address     | 0..1 | The postal address of the organization. |
|  3 | url        | String /uri | 0..1 | A URL for the organization.             |

Table: Type `Organization` (Record){#tab:organization-record}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| Type Name | Type Definition | Description                                       |
|:----------|:----------------|:--------------------------------------------------|
| Address   | ArrayOf(String) | Lines of a postal address. At least one required. |

Table: Type `Address` (ArrayOf(String)){#tab:address-array}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name    | Type   | \#   | Description                         |
|---:|:--------|:-------|:-----|:------------------------------------|
|  1 | country | String | 1    | The country name or code.           |
|  2 | state   | String | 0..1 | The state or province name or code. |

Table: Type `GeographicRegion` (Record){#tab:geographic-region-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name             | Type   | \#   | Description                                                          |
|---:|:-----------------|:-------|:-----|:---------------------------------------------------------------------|
|  1 | code             | String | 1    | A short code identifying the method, regulation, or classification.  |
|  2 | system           | String | 0..1 | The code system used to interpret the code value.                    |
|  3 | long-description | String | 0..1 | A detailed description of the method, regulation, or classification. |

Table: Type `Method` (Record){#tab:method-record}

The `Acknowledgment` type describes a contributor. At least one of its fields MUST be present.

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name         | Type        | \#    | Description                                             |
|---:|:-------------|:------------|:------|:--------------------------------------------------------|
|  1 | names        | String      | 0..\* | Names of individual contributors being acknowledged.    |
|  2 | organization | String      | 0..1  | Name of a contributing organization being acknowledged. |
|  3 | summary      | String      | 0..1  | Contextual details about the acknowledgment.            |
|  4 | urls         | String /uri | 0..\* | URLs of references being acknowledged.                  |

Table: Type `Acknowledgment` (Map){#tab:acknowledgment-map}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| Type Name | Type Definition | Description                                                                           |
|:----------|:----------------|:--------------------------------------------------------------------------------------|
| Version   | String          | An integer or semantic versioning string. Examples: `"1"`, `"2.0.0"`, `"1.0.0-beta"`. |

Table: Type `Version` (String){#tab:version-string}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| Type Name | Type Definition | Description                                          |
|:----------|:----------------|:-----------------------------------------------------|
| Language  | String          | A language tag conforming to IETF BCP 47 / RFC 5646. |

Table: Type `Language` (String){#tab:language-string}
