# An Information Model for DPS

The [Data&Trust Alliance](https://dataandtrustalliance.org/)
initiated creation of the OASIS Data Provenance Standards
([DPS](https://docs.google.com/document/d/1FswDKOteTbMfBU9bfQGO9xH2MIRwaAcx))
Technical Committee.
Among the TC's work products is a standard for provenance metadata that captures
where data comes from, how it is created, and whether it can be used legally.

An information model (IM) defines the essential content of data items (messages, documents,
structures, database values) stored or exchanged by applications independently of data format.
This promotes design based on content requirements and enables data interoperability across
technologies and formats. 

This DPS information model is written using the
[JADN](https://docs.oasis-open.org/openc2/jadn/v2.0/jadn-v2.0.html) schema language developed by the OASIS
[OpenC2](https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=a34c9baf-48b2-44c5-a567-018dc7d32296) TC.

## License
These specifications are released under Creative Commons
[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Goal
Produce a DPS metadata information model that provides the "single source of truth" for metadata designers,
tool developers, and metadata consumers based on whatever data formats are needed for system compatibility.

## Process
* The Data&Trust Alliance contributed to the DPS TC:
  * Metadata Generation
    [software](https://groups.oasis-open.org/higherlogic/ws/groups/2c60b2cf-45d3-48cd-8594-0194f182b33d/documents/dps3709/document?document_id=72724)
    and online [metadata generator](https://data-and-trust-alliance-data-provenance-standards.northeurope.cloudapp.azure.com/)
    that produces JSON, YAML, XML and CSV metadata files.
  * preliminary
    [JSON Schema](https://groups.oasis-open.org/higherlogic/ws/groups/2c60b2cf-45d3-48cd-8594-0194f182b33d/download/72727)
    and placeholder for JSON examples
  * placeholder for [XML Schema](https://groups.oasis-open.org/higherlogic/ws/groups/2c60b2cf-45d3-48cd-8594-0194f182b33d/download/72728)
    and XML examples
* OpenC2 developers:
  * Used the Metadata Generation Tool to [design](Designed) an IM based on metadata content requirements
  * Used the JSON Schema to mechanically [derive](Generated) an incomplete, or "template" IM

## Results
