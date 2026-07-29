## Set {#set}

The `set` member captures metadata about the provenance metadata record itself.

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name            | Type           | \#    | Description                                                                                                                        |
|---:|:----------------|:---------------|:------|:-----------------------------------------------------------------------------------------------------------------------------------|
|  1 | category        | String         | 1     | A short canonical name, chosen by the set producer, informing the end user of the category of the metadata set.                    |
|  2 | schema-version  | String         | 1     | The version of the Data Provenance Core specification this record was generated for. The value for this version is always `"1.0"`. |
|  3 | publisher       | Publisher      | 1     | Information about the publisher of the metadata set.                                                                               |
|  4 | label           | String         | 1     | The per-publisher unique title of this metadata set.                                                                               |
|  5 | tracking        | Tracking       | 1     | Management attributes used to track this metadata set as a whole.                                                                  |
|  6 | language        | Language       | 0..1  | The language used in this document, corresponding to IETF BCP 47.                                                                  |
|  7 | source-language | Language       | 0..1  | If this is a translation, the language this document was translated from.                                                          |
|  8 | acknowledgments | Acknowledgment | 0..\* | Acknowledgment elements associated with the whole set.                                                                             |
|  9 | notes           | Note           | 0..\* | Notes associated with this metadata set.                                                                                           |
| 10 | references      | Reference      | 0..\* | References associated with this metadata set.                                                                                      |

Table: Type `Set` (Record){#tab:set-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name            | Type        | \#   | Description                                                                                        |
|---:|:----------------|:------------|:-----|:---------------------------------------------------------------------------------------------------|
|  1 | name            | String      | 1    | The name of the issuing party.                                                                     |
|  2 | namespace       | String /uri | 1    | A URI under the control of the issuing party, used as a globally unique identifier for that party. |
|  3 | contact-details | String      | 0..1 | Information on how to contact the publisher.                                                       |

Table: Type `Publisher` (Record){#tab:publisher-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name                 | Type              | \#    | Description                                                                                                                                  |
|---:|:---------------------|:------------------|:------|:---------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | current-release-date | String /date-time | 1     | The date when the current revision of this document was released.                                                                            |
|  2 | id                   | String            | 1     | A unique identifier for this metadata set, assigned and maintained by the original issuing authority. MUST NOT start or end with whitespace. |
|  3 | initial-release-date | String /date-time | 1     | The date when this metadata set was first published.                                                                                         |
|  4 | revision-history     | Revision          | 1..\* | One revision item for each version of the metadata set, including the initial one.                                                           |
|  5 | status               | TrackingStatus    | 1     | The draft status of the metadata set.                                                                                                        |
|  6 | version              | Version           | 1     | The version of the current metadata set.                                                                                                     |
|  7 | aliases              | String            | 0..\* | Alternate names for this metadata set.                                                                                                       |
|  8 | generator            | Generator         | 0..1  | Information about the engine that generated this metadata set.                                                                               |

Table: Type `Tracking` (Record){#tab:tracking-record}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item    | Description                          |
|---:|:--------|:-------------------------------------|
|  0 | draft   | The metadata set is a draft.         |
|  1 | final   | The metadata set is final.           |
|  2 | interim | The metadata set has interim status. |

Table: Type `TrackingStatus` (Enumerated){#tab:tracking-status-enum}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name           | Type              | \#   | Description                                                                                                    |
|---:|:---------------|:------------------|:-----|:---------------------------------------------------------------------------------------------------------------|
|  1 | date           | String /date-time | 1    | The date of this revision entry.                                                                               |
|  2 | number         | Version           | 1    | The version number of this revision.                                                                           |
|  3 | summary        | String            | 1    | A short description of the changes in this revision.                                                           |
|  4 | legacy-version | String            | 0..1 | A version string from an existing set with the same content, tracing from DP-Core compliant to historic items. |

Table: Type `Revision` (Record){#tab:revision-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name   | Type              | \#   | Description                                                      |
|---:|:-------|:------------------|:-----|:-----------------------------------------------------------------|
|  1 | engine | GeneratorEngine   | 1    | Information about the engine used to generate this metadata set. |
|  2 | date   | String /date-time | 0..1 | The date this metadata set was generated.                        |

Table: Type `Generator` (Record){#tab:generator-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name    | Type    | \#   | Description                                                 |
|---:|:--------|:--------|:-----|:------------------------------------------------------------|
|  1 | name    | String  | 1    | The name of the engine that generated this metadata set.    |
|  2 | version | Version | 0..1 | The version of the engine that generated this metadata set. |

Table: Type `GeneratorEngine` (Record){#tab:generator-engine-record}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name     | Type         | \#   | Description                                                         |
|---:|:---------|:-------------|:-----|:--------------------------------------------------------------------|
|  1 | category | NoteCategory | 1    | The category of the note.                                           |
|  2 | text     | String       | 1    | The content of the note, varying depending on type.                 |
|  3 | audience | String       | 0..1 | The intended audience for the note.                                 |
|  4 | title    | String       | 0..1 | A concise description of what is contained in the text of the note. |

Table: Type `Note` (Record){#tab:note-record}

\columns=iiii,nnnnnnnnnnnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item             | Description                                    |
|---:|:-----------------|:-----------------------------------------------|
|  0 | description      | A descriptive note about the subject.          |
|  1 | details          | A note with detailed supplemental information. |
|  2 | faq              | A note in frequently-asked-questions format.   |
|  3 | general          | A general note.                                |
|  4 | legal-disclaimer | A note containing a legal disclaimer.          |
|  5 | other            | A note that does not fit other categories.     |
|  6 | summary          | A summary note.                                |

Table: Type `NoteCategory` (Enumerated){#tab:note-category-enum}

\columns=iiii,nnnnnnnnnn,tttttttttt,hhhh,ddddddddddddddddddddddddddddddddddddddd

| ID | Name     | Type              | \#   | Description                                             |
|---:|:---------|:------------------|:-----|:--------------------------------------------------------|
|  1 | summary  | String            | 1    | A short description of what this reference refers to.   |
|  2 | url      | String /uri       | 1    | The URL of the referenced resource.                     |
|  3 | category | ReferenceCategory | 0..1 | Whether this reference is external or self-referential. |

Table: Type `Reference` (Record){#tab:reference-record}

\columns=iiii,nnnnnnnnnn,ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

| ID | Item     | Description                                                      |
|---:|:---------|:-----------------------------------------------------------------|
|  0 | external | The reference points to an external resource.                    |
|  1 | self     | The reference points back to the same information item in focus. |

Table: Type `ReferenceCategory` (Enumerated){#tab:reference-category-enum}
