# DPS Draft Information Model

This directory contains a proposed DPS information model created by harmonizing an IM designed by examining the D&TA
metadata generator tool, and one generated automatically from the initial JSON Schema submission.

The IM is represented in equivalent file formats:

1. **JADN:** The authoritative JSON data format
```json
    ["DataProvenance", "Record", [], "The Data Provenance Standard Metadata", [
      [1, "source", "Source", [], "Describes a dataset and the source of the dataset"],
      [2, "provenance", "Provenance", [], "Provenance of the dataset"],
      [3, "use", "Use", [], "Legal use and restrictions"]
    ]],

    ["Source", "Record", [], "", [
      [1, "title", "String", [], "The official name of the dataset"],
      [2, "id", "UID", [], "Unique metadata identifier"],
      [3, "location", "URL", ["[0"], "Metadata location"],
      [4, "issuer", "Organization", ["]-1"], "Data issuer  (many?)"],
      [5, "description", "String", [], "Description of the dataset"]
    ]],
```
2. **JIDL:** A text "source code" format suitable for discussion and publication in the DPS Committee Specification
```
DataProvenance = Record                          // The Data Provenance Standard Metadata
   1 source           Source                     // Describes a dataset and the source of the dataset
   2 provenance       Provenance                 // Provenance of the dataset
   3 use              Use                        // Legal use and restrictions

Source = Record
   1 title            String                     // The official name of the dataset
   2 id               UID                        // Unique metadata identifier
   3 location         URL optional               // Metadata location
   4 issuer           Organization [1..*]        // Data issuer  (many?)
   5 description      String                     // Description of the dataset
```
3. **XASD:** "XML Abstract Schema Definition", an XML IM representation with an
easily translated line-for-line correspondence with other representations
```xml
  <Types>
    <Type name="DataProvenance" type="Record">The Data Provenance Standard Metadata
      <Field id="1" name="source" type="Source">Describes a dataset and the source of the dataset</Field>
      <Field id="2" name="provenance" type="Provenance">Provenance of the dataset</Field>
      <Field id="3" name="use" type="Use">Legal use and restrictions</Field>
    </Type>

    <Type name="Source" type="Record">
      <Field id="1" name="title" type="String">The official name of the dataset</Field>
      <Field id="2" name="id" type="UID">Unique metadata identifier</Field>
      <Field id="3" name="location" type="URL" minOccurs="0">Metadata location</Field>
      <Field id="4" name="issuer" type="Organization" maxOccurs="-1">Data issuer  (many?)</Field>
      <Field id="5" name="description" type="String">Description of the dataset</Field>
    </Type>
  </Types>
```
4. **Markdown:** Tables suitable for publication in the DPS spec, if a table format is preferred  by the TC

**********

The Data Provenance Standard Metadata

**Type: DataProvenance (Record)**

| ID | Name           | Type       | \# | Description                                       |
|----|----------------|------------|----|---------------------------------------------------|
| 1  | **source**     | Source     | 1  | Describes a dataset and the source of the dataset |
| 2  | **provenance** | Provenance | 1  | Provenance of the dataset                         |
| 3  | **use**        | Use        | 1  | Legal use and restrictions                        |

**********

**Type: Source (Record)**

| ID | Name            | Type         | \#    | Description                      |
|----|-----------------|--------------|-------|----------------------------------|
| 1  | **title**       | String       | 1     | The official name of the dataset |
| 2  | **id**          | UID          | 1     | Unique metadata identifier       |
| 3  | **location**    | URL          | 0..1  | Metadata location                |
| 4  | **issuer**      | Organization | 1..\* | Data issuer  (many?)             |
| 5  | **description** | String       | 1     | Description of the dataset       |

**********

5. **[Graphviz](https://graphviz.org/):** An entity relationship (ER) diagram graphical format, viewable online at
[Sketchviz](https://sketchviz.com/new). JADN models can also be viewed as [PlantUML](https://plantuml.com/) ER diagrams.

![DPS ERD](../../images/dps-erd.jpg)