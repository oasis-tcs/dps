![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------
# Data Provenance Metadata Version 1.0
**Editor's Note:**
This title was put in by editor and does not imply consensus by group. 
It is just so there is text there

## Committee Specification Draft 01

## 06 May 2025

**Editor's Note:**
THe following "version links" will be filled out nearer to completion. Note for 'first' version, 
"This" and "latest" will be the same, and "previous" will be "none" 

### This version

- \[ link to authoritative version of the published document \] (Authoritative)  
- \[ links to one or more other versions of the published document (e.g., MD, PDF, Word, HTML, etc.) \] 


### Previous version


- \[ link to authoritative version of the published document \] (Authoritative)  
- \[ links to one or more other versions of the published document (e.g., MD, PDF, Word, HTML, etc.) \] 


### Latest version


- \[ link to authoritative version of the published document \] (Authoritative)  
- \[ links to one or more other versions of the published document (e.g., MD, PDF, Word, HTML, etc.) \] 



### Technical Committee


[Data Provenance Standard Technical Committee](https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=2c60b2cf-45d3-48cd-8594-0194f182b33d)


### Chairs


- Lisa Bobbitt, Cisco, lbobbitt@cisco.com
- Bryan Bortnick, IBM, bortnick@us.ibm.com
- Fotis Psallidas, Microsoft, Fotis.Psallidas@microsoft.com



### Secretaries


- Kristina Podnar, Data & Trust Alliance, kpodnar@dataandtrustalliance.org 


### Editors


- Stefan Hagen, individual, stefan@hagen.link
- Duncan Sparrell, sFractal Consulting, duncan@sfractal.com


### Abstract
**Editor's Note:**
we need to put text here

Best practices: 

- Expect this text to be reused in multiple other places to explain the specification in summary form.  
- This is not the TC or OP scope (which is an IPR and rules boundary);  rather, this section is the summary intended purpose of this specification.  
- Short is better; four paragraphs or less is recommended.  
- If use of this spec is deliberately created to rely on or complement another standard, consider briefly mentioning that here as context.  
- To the extent that discussion of the larger context of the spec, or its history, or the circumstances that led to its creation or revision, are necessary, they belong in the Introduction, not here. 


### Citation Format


When referencing this document, the following citation format should be used:


- \[ The full reference for this document in IEEE reference format \] 

**Editor's Note:**
Editors will fill in citation later

### Related Work


This document replaces or supersedes:


- \[ The full reference to the related document in IEEE reference format \] 


This document is related to:


- \[ The full reference to the related document in IEEE reference format \] 

**Editor's Note:**
The TC will determin related work and fill in later

## License, Document Status, and Notices


Copyright © OASIS Open 2025. 
All Rights Reserved.  
For license and copyright information, and complete status, 
please see Annex A which contains the License, Document Status and Notices.


---


## Table of Contents

Editor's Note: Table of Contents will be updated once structure is stable

- [1 Scope](#1-scope)
- [2 Definitions and Acronyms](#2-definitions-and-acronyms)
  - [2.1 Definitions](#2.1-definitions)
    - [2.1.1 Terms Defined Elsewhere](#2.1.1-terms-defined-elsewhere)
    - [2.1.2 Terms Defined in this Document](#2.1.2-terms-defined-in-this-document)
  - [2.2 Abbreviations and Acronyms](#2.2-abbreviations-and-acronyms)
- [3 Document Conventions](#3-document-conventions)
  - [3.1 Key Words](#3.1-key-words)
  - [3.2 Typographical Conventions](#3.2-typographical-conventions)
- [4 Introduction](#4-introduction)
  - [4.1 Any Additional Introduction Subsections That are Needed](#4.1-any-additional-introduction-subsections-that-are-needed)
  - [4.2 Changes From the Previous Version](#4.2-changes-from-the-previous-version)
- [5 Provenance Information Model](#5-provenance-information-model)
  - [5.1 Primary Metadata Elements](#51-primary-metadata-elements)
  - [5.2 Source](#52-source)
  - [5.3 Provenance](#53-provenance)
  - [5.4 Use](#54-use)
- [6 Provenance Information Model Encoding](#6-provenance-information-model-encoding)
  - [6.1 JADN Encoding](#61-jadn-encoding)
  - [6.2 YAML Encoding](#62-yaml-encoding)
- [7 Provenance Data Model Encoding](#7-provenance-data-model-encoding)
  - [7.1 JSON Encoding](#71-json-encoding)
  - [7.2 XML Encoding](#72-xml-encoding)
  - [7.3 YAML Encoding](#73-yaml-encoding)
- [8 Safety, Security, and Data Protection Considerations](#7-safety,-security,-and-data-protection-considerations)
- [9 Conformance](#8-conformance)
- [Annex A License, Document Status and Notices](#annex-a-license,-document-status-and-notices)
  - [A.1 Document Status](#a.1-document-status)
  - [A.2 License and Notices](#a.2-license-and-notices)
- [Annex B References](#annex-b-references)
  - [B.1 Normative References](#b.1-normative-references)
  - [B.2 Informative References](#b.2-informative-references)
- [Annex C Additional Annex as Needed](#annex-c-additional-annex-as-needed)
  - [C.1 Subsection Title](#c.1-subsection-title)
  - [C.1.1 Sub-subsection](#c.1.1-sub-subsection)
- [Appendix 1 Acknowledgments](#appendix-1-acknowledgments)
  - [Leadership](#leadership)
  - [Special Thanks](#special-thanks)
  - [Participants](#participants)
- [Appendix 2 Changes From Previous Version](#appendix-2-changes-from-previous-version)
  - [Revision History](#revision-history)
- [Appendix 3 Additional Appendix as Needed](#appendix-3-additional-appendix-as-needed)
  - [Subsection Title](#subsection-title)
- [Sub-subsection](#sub-subsection)


---


# 1 Scope
**Editor's Note:**
Refer to template for OASIS style rules. 
For readabilty, most were deleted prior to this point in doc.
Some are left in after this point as guides on how to replace.


What is the purpose and scope of this document?   
Best practices: 


- Expect this text to be reused in multiple other places to explain the specification in summary form.  
- This is not the TC or OP scope (which is an IPR and rules boundary);  rather, this section is the summary intended purpose of this specification.  
- Short is better; four paragraphs or less is recommended.  
- If use of this spec is deliberately created to rely on or complement another standard, consider briefly mentioning that here as context.  
- To the extent that discussion of the larger context of the spec, or its history, or the circumstances that led to its creation or revision, are necessary, they belong in the Introduction, not here. 


---


# 2 Definitions and Acronyms


## 2.1 Definitions


### 2.1.1 Terms Defined Elsewhere


This document uses the following terms defined elsewhere:


- Term 1: \[Reference\]: optional quoted definition.  
- Term 2: \[Reference\]: optional quoted definition.
- etc


### 2.1.2 Terms Defined in this Document


This document defines the following terms:


- Term 1: some definition.  
- Term 2: some definition.  
- etc


## 2.2 Abbreviations and Acronyms


This document uses the following abbreviations and acronyms:


- Term 1: expanded form.  
- Term 2: expanded form.  
- etc


---


# 3 Document Conventions


## 3.1 Key Words


The key words "**MUST**", "**MUST NOT**", "**REQUIRED**", "**SHALL**", "**SHALL NOT**", "**SHOULD**", "**SHOULD NOT**", "**RECOMMENDED**", "**NOT RECOMMENDED**", "**MAY**", and "**OPTIONAL**" in this document are to be interpreted as described in BCP 14 \[RFC2119\] \[RFC8174\] when, and only when, they appear in all capitals, as shown here.


## 3.2 Typographical Conventions


\< Describe any standards or typographical conventions that were followed when writing this document, such as fonts or highlighting that have special significance. If there are no typographical conventions than one is to put "None". \>


---


# 4 Introduction


\< Any introductory text that is needed to explain this document \>


## 4.1 Any Additional Introduction Subsections That are Needed


\< Any needed text \>


## 4.2 Changes From the Previous Version


The list of changes from the previous version and any revision history can be found in Appendix 2\.


---


# 5 Provenance Information Model
The information model of the provenance metadata is described in human-readable property tables.
The technical encoding may be found in section 6.

The Data Provenance Standards are made up of three groups of metadata elements: 
Source, Provenance, and Use.

![Metadata](./images//metadata.svg)

The property tables first define metadata about the specification itself,
then describe how a record is made of the 3 primary metadata elements
(Source, Provenance, and Use), then describe each of the 3 elements.
Subsequent tables describe the underlying fields of the 3 elements.

## 5.1 Primary Metadata Elements

**Type: DPS (Record)**

| ID | Name         | Type           | \# | Description                                                   |
|----|--------------|----------------|----|---------------------------------------------------------------|
| 1  | **version**  | URL            | 1  | Standard version used to define the metadata for this dataset |
| 2  | **metadata** | DataProvenance | 1  | The metadata about a dataset                                  |

**********

The Data Provenance Standard Metadata

**Type: DataProvenance (Record)**

| ID | Name           | Type       | \# | Description                                       |
|----|----------------|------------|----|---------------------------------------------------|
| 1  | **source**     | Source     | 1  | Describes a dataset and the source of the dataset |
| 2  | **provenance** | Provenance | 1  | Provenance of the dataset                         |
| 3  | **use**        | Use        | 1  | Legal use and restrictions                        |

**********

## 5.2 Source

**Type: Source (Record)**

| ID | Name            | Type         | \#    | Description                      |
|----|-----------------|--------------|-------|----------------------------------|
| 1  | **title**       | String       | 1     | The official name of the dataset |
| 2  | **id**          | UID          | 1     | Unique metadata identifier       |
| 3  | **location**    | URL          | 0..1  | Metadata location                |
| 4  | **issuer**      | Organization | 1..\* | Data issuer  (many?)             |
| 5  | **description** | String       | 1     | Description of the dataset       |

**********

**Type: Organization (Record)**

| ID | Name        | Type    | \# | Description       |
|----|-------------|---------|----|-------------------|
| 1  | **name**    | String  | 1  | organization name |
| 2  | **address** | Address | 1  | address           |

**********

| Type Name   | Type Definition | Description                                      |
|-------------|-----------------|--------------------------------------------------|
| **Address** | ArrayOf(String) | Just lines for now, enable structured definition |

**********

## 5.3 Provenance

**Type: Provenance (Record)**

| ID | Name                  | Type         | \#    | Description                                      |
|----|-----------------------|--------------|-------|--------------------------------------------------|
| 1  | **source**            | URL          | 1..\* | Source metadata for dataset                      |
| 2  | **origin**            | Organization | 0..1  | Source                                           |
| 3  | **origin-geography**  | Geography    | 1..\* | Data origin geography                            |
| 4  | **date**              | Timestamp    | 1     | Dataset issue date                               |
| 5  | **previous-date**     | Timestamp    | 1     | Date of previously-issued version of the dataset |
| 6  | **generation-period** | Generation   | 1     | Range of dates for data generation               |
| 7  | **generation-method** | Method       | 1..\* | Method (code/system/description?)                |
| 8  | **format**            | MediaType    | 0..\* | Data format                                      |
| 9  | **sub-provenance**    | Provenance   | 1     | Add key/link?                                    |

**********

**Type: Generation (Record)**

| ID | Name         | Type      | \# | Description                                         |
|----|--------------|-----------|----|-----------------------------------------------------|
| 1  | **oldest**   | Timestamp | 1  | Oldest component of data contained in the dataset   |
| 2  | **youngest** | Timestamp | 1  | Youngest component of data contained in the dataset |

**********

## 5.4 Use

**Type: Use (Record)**

| ID | Name                  | Type                    | \#    | Description                                                                                                                       |
|----|-----------------------|-------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1  | **classification**    | Confidentiality         | 1     | Confidentiality Classification                                                                                                    |
| 2  | **consent**           | URL                     | 1..\* | Consent documentation location                                                                                                    |
| 3  | **privacy-enhancing** | Privacy-Tool            | 1..\* | Privacy enhancing technologies                                                                                                    |
| 4  | **processing**        | Processing-Geography    | 0..1  | Data processing geography                                                                                                         |
| 5  | **storage**           | Storage-Geography       | 0..1  | Data storage geography                                                                                                            |
| 6  | **license**           | ArrayOf(License) unique | 1     | License to use                                                                                                                    |
| 7  | **intended_purpose**  | Intended-Use            | 1     | Intended data use                                                                                                                 |
| 8  | **copyright**         | String                  | 0..\* | Indicates whether the dataset contains proprietary information that is covered with a Copyright and the terms of said Copyright.  |
| 9  | **patent**            | String                  | 0..\* | Indicates whether the dataset contains proprietary information that is covered with a Patent and said Patent number.              |
| 10 | **trademark**         | String                  | 0..\* | Indicates whether the dataset contains proprietary information that is covered with a Trademark, and the terms of said Trademark. |

**********

**Type: Intended-Use (Record)**

| ID | Name       | Type              | \#    | Description |
|----|------------|-------------------|-------|-------------|
| 1  | **non_ai** | Non-AI-Use unique | 1..\* | Non-AI      |
| 2  | **ai**     | AI-Use unique     | 1..\* | AI          |

**********

**Type: Processing-Geography (Record)**

| ID | Name               | Type      | \#    | Description                                                    |
|----|--------------------|-----------|-------|----------------------------------------------------------------|
| 1  | **same_as_origin** | Boolean   | 1     | Data processing geography is the same as data origin geography |
| 2  | **countries**      | Geography | 0..\* |                                                                |

**********

**Type: Storage-Geography (Record)**

| ID | Name                   | Type      | \#    | Description                                                     |
|----|------------------------|-----------|-------|-----------------------------------------------------------------|
| 1  | **same_as_processing** | Boolean   | 1     | Data storage geography is the same as data processing geography |
| 2  | **countries**          | Geography | 0..\* |                                                                 |

**********

**Type: Geography (Record)**

| ID | Name        | Type             | \#   | Description |
|----|-------------|------------------|------|-------------|
| 1  | **country** | geo:Country-Name | 1    |             |
| 2  | **state**   | geo:State-Name   | 0..1 |             |

**********

**Type: UID (Choice(anyOf))**

| ID | Name | Type         | \# | Description |
|----|------|--------------|----|-------------|
| 1  | **** | Binary /uuid | 1  | **uuid** -  |

**********

**Type: Privacy-Tool (Record)**

| ID | Name           | Type                  | \# | Description           |
|----|----------------|-----------------------|----|-----------------------|
| 1  | **tool_id**    | Tool-ID               | 1  | tool name and version |
| 2  | **technology** | Privacy-Technology    | 1  |                       |
| 3  | **params**     | MapOf(String, String) | 1  | key-value pair        |

**********

| Type Name   | Type Definition | Description |
|-------------|-----------------|-------------|
| **Tool-ID** | String          |             |

**********

**Type: Confidentiality (Record)**

| ID | Name               | Type                           | \#    | Description |
|----|--------------------|--------------------------------|-------|-------------|
| 1  | **classification** | Confidentiality-Classification | 1     |             |
| 2  | **tool_id**        | Tool-ID                        | 0..\* |             |

**********

| Type Name     | Type Definition | Description                  |
|---------------|-----------------|------------------------------|
| **Timestamp** | Integer /d3     | Milliseconds since the epoch |

**********

| Type Name | Type Definition | Description                          |
|-----------|-----------------|--------------------------------------|
| **URL**   | String /uri     | URI designated as a resource locator |

**********

**Type: Method (Enumerated)**

| ID | Item                        | Description |
|----|-----------------------------|-------------|
| 0  | **Other**                   |             |
| 1  | **Web scraping/Crawling**   |             |
| 2  | **Feeds**                   |             |
| 3  | **Syndication**             |             |
| 4  | **Data mining**             |             |
| 5  | **Machine generated/MLOps** |             |
| 6  | **Social media**            |             |
| 7  | **User generated content**  |             |
| 8  | **Primary user source**     |             |
| 9  | **Data augmentation**       |             |
| 10 | **Transfer learning**       |             |
| 11 | **Simulations**             |             |

**********

**Type: MediaType (Enumerated)**

| ID | Item                         | Description |
|----|------------------------------|-------------|
| 0  | **Other**                    |             |
| 1  | **application/json**         |             |
| 2  | **application/jsonld**       |             |
| 3  | **application/zip**          |             |
| 4  | **application/msword**       |             |
| 5  | **application/vnd.ms-excel** |             |
| 6  | **image/bmp**                |             |
| 7  | **image/jpeg**               |             |
| 8  | **image/x-png**              |             |
| 9  | **image/png**                |             |
| 10 | **image/gif**                |             |
| 11 | **text/csv**                 |             |
| 12 | **text/plain**               |             |

**********

**Type: Confidentiality-Classification (Enumerated)**

| ID | Item                                      | Description |
|----|-------------------------------------------|-------------|
| 0  | **Other**                                 |             |
| 1  | **Personal information (PI)/Demographic** |             |
| 2  | **Payment Card Industry (PCI)**           |             |
| 3  | **Personal Financial Information (PFI)**  |             |
| 4  | **Personal Health Information (PHI)**     |             |
| 5  | **Sensitive Personal Information (SPI)**  |             |

**********

**Type: Privacy-Technology (Enumerated)**

| ID | Item                                     | Description |
|----|------------------------------------------|-------------|
| 1  | **Data Anonymization**                   |             |
| 2  | **Data Encryption**                      |             |
| 3  | **Data Masking**                         |             |
| 4  | **Data Minimization**                    |             |
| 5  | **Data Redaction**                       |             |
| 6  | **Differential Privacy**                 |             |
| 7  | **Federated Learning**                   |             |
| 8  | **Homomorphic Encryption**               |             |
| 9  | **K-anonymity**                          |             |
| 10 | **L-diversity**                          |             |
| 11 | **Pseudonymization**                     |             |
| 12 | **Secure Multi-party Computation (SMC)** |             |
| 13 | **T-closeness**                          |             |
| 14 | **Tokenization**                         |             |

**********

**Type: License (Enumerated)**

| ID | Item                              | Description |
|----|-----------------------------------|-------------|
| 1  | **Non-commercial**                |             |
| 2  | **Public license**                |             |
| 3  | **Commercial/Negotiated License** |             |

**********

**Type: Non-AI-Use (Enumerated)**

| ID | Item                  | Description |
|----|-----------------------|-------------|
| 0  | **Other**             |             |
| 1  | **Staging/testing**   |             |
| 2  | **Production**        |             |
| 3  | **Quality assurance** |             |

**********

**Type: AI-Use (Enumerated)**

| ID | Item                          | Description |
|----|-------------------------------|-------------|
| 0  | **Other**                     |             |
| 1  | **Pre-Training**              |             |
| 2  | **Alignment**                 |             |
| 3  | **Evaluation**                |             |
| 4  | **Synthetic Data Generation** |             |

**********


# 6 Provenance Information Model Encoding
The technical encoding of the information model 
is specified in both JADN and YAML 
in the following subsections.

## 6.1 JADN Encoding
The JADN encoding of the data provenance metadata information model is specified in ____.

Editor's Note to link to file(s) once present

## 6.2 YAML Encoding
The YAML encoding of the data provenance metadata information model is specified in ____.

Editor's Note to link to file(s) once present

# 7 Provenance Data Model Encoding
The information model allows the extraction of informaion from data.

## 7.1 JSON Encoding
The technical encoding of the data provenance metadata data model
is specified in ____ for JSON data.

Editor's Note to link to file(s) once present

## 7.2 XML Encoding
The technical encoding of the data provenance metadata data model
is specified in ____ for XML data.

Editor's Note to link to file(s) once present

## 7.3 YAML Encoding
The technical encoding of the data provenance metadata data model
is specified in ____ for YAML data.

Editor's Note to link to file(s) once present

---

# 8 Safety, Security, and Data Protection Considerations


\< 


This section is **REQUIRED** and **MUST** be the second to last numbered section in the document, right before Conformance. This section contains information about safety, security, data protection, and privacy considerations. These can be divided up into separate subsections as desired. All documents **SHOULD** have at least a security and data protection considerations section, and otherwise **MUST** have a blank section indicating “None.” Any other considerations **MAY** also be added.


Please note that any specification that will need to register something with IANA or has plans to go on to ITU/ISO/IEC **MUST** have this section filled out. For an example please see the following section in the CACAO specification here [https://docs.oasis-open.org/cacao/security-playbooks/v2.0/cs01/security-playbooks-v2.0-cs01.html\#\_Toc152256574](https://docs.oasis-open.org/cacao/security-playbooks/v2.0/cs01/security-playbooks-v2.0-cs01.html#_Toc152256574) 


\>


---


# 9 Conformance


\< 


This section is **REQUIRED** and **MUST** be the last numbered section in the document. 


\>


---


# Annex A License, Document Status and Notices


(This annex forms an integral part of this Specification.)


## A.1 Document Status


This document was last revised or approved by the \[ full project name e.g., OASIS Collaborative Automated Course of Action Operations (CACAO) for Cyber Security TC \] on the above date. The level of approval is also listed above. Check the "Latest version" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at \[ project publication page e.g., https://www.oasis-open.org/committees/tc\_home.php?wg\_abbrev=cacao\#technical \].


TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at \[ project home page e.g., https://www.oasis-open.org/committees/cacao/ \].


NOTE: any machine-readable content (Computer Language Definitions) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.


## A.2 License and Notices


Copyright © OASIS Open 202\[ 5 \]. All Rights Reserved.


All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full Policy, which governs the licensure of this document, may be found at the OASIS website: \[[https://www.oasis-open.org/policies-guidelines/ipr/](https://www.oasis-open.org/policies-guidelines/ipr/)\]


This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.


The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns, as provided in the OASIS IPR Policy.


This document is provided under the \[ add IPR Mode, e.g., “Non-Assertion” \] IPR mode that was chosen when the project was established, as defined in the IPR Policy. For information on whether any patents have been disclosed that may be essential to implementing this document, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the project’s web page ( \[ e.g., [https://www.oasis-open.org/committees/cacao/ipr.php](https://www.oasis-open.org/committees/cacao/ipr.php) \] ).


This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. OASIS AND ITS MEMBERS WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THIS DOCUMENT OR ANY PART THEREOF.


As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specifications, OASIS Standards, or Approved Errata).


OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.


OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.


OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.


The name "OASIS" is a trademark of OASIS, the owner and developer of this document, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, its documents, while reserving the right to enforce its marks against misleading uses. Please see [https://www.oasis-open.org/policies-guidelines/trademark/](https://www.oasis-open.org/policies-guidelines/trademark/) for guidance.


---


# Annex B References


(This annex forms an integral part of this Specification.)


This section contains the normative and informative references that are used in this document. 


Normative references are specific (identified by date of publication and/or edition number or version number) and Informative references are either specific or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the reference document (including any amendments) applies. While any hyperlinks included in this section were valid at the time of publication, OASIS cannot guarantee their long term validity.


## B.1 Normative References


The following documents are referenced in such a way that some or all of their content constitutes requirements of this document.


**\[RFC2119\]** *Key Words for Use in RFCs to Indicate Requirement Levels*, BCP 14, RFC 2119, March 1997\. \[Online\]. Available: https://www.rfc-editor.org/info/rfc2119


**\[RFC8174\]** *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*, BCP 14, RFC 8174, May 2017\. \[Online\]. Available: https://www.rfc-editor.org/info/rfc8174


**\[Reference 1\]** Reference Details


**\[Reference 2\]** Reference Details


## B.2 Informative References


The following referenced documents are not required for the application of this document but may assist the reader with regard to a particular subject area.


**\[Reference 1\]** Reference Details


**\[Reference 2\]** Reference Details


---


# Annex C Additional Annex as Needed


(This annex forms an integral part of this Specification.)


## C.1 Subsection Title


### C.1.1 Sub-subsection


---


# Appendix 1 Acknowledgments


(This appendix does not form an integral part of this Specification and is informational.)


\< 


All parts in this appendix are optional to the TC. Individuals or companies, past or present, may request that their name and/or affiliation is not included in this list. 


\>


## Leadership


The following individuals have had significant leadership positions during the development of this specification, not just this version of the specification, and they are gratefully acknowledged:


\< 


This section **SHOULD** include the leadership (chairs, sub committees chairs, secretaries, editors, etc.) of this specification, and not just for this version of the specification, even if they are no longer members of the TC.


\>


- Chairs  
  - Position, First Name Last Name, Company, \[optional time frames\]  
- Secretaries  
  - Position, First Name Last Name, Company, \[optional time frames\]  
- Editors  
  - Position, First Name Last Name, Company, \[optional time frames\]


## Special Thanks


The following individuals have made substantial contributions to this specification, not just this version of the specification, and their contributions are gratefully acknowledged:


\< 


This section **SHOULD** include individuals that have made significant contributions to this specification, and not just this version of the specification, even if they are no longer members of the TC or were never members of the TC but sent in a contribution through one of the public comment methods. 


\>


- First Name Last Name, Company


## Participants


The following individuals were members of this committee during the creation of this specification, not just this version of the specification, and their contributions are gratefully acknowledged:


- First Name Last Name, Company


---


# Appendix 2 Changes From Previous Version


(This appendix does not form an integral part of this Specification and is informational.)

This is the initial draft Committee Specification.


\< 


The appendix **SHOULD** contain any explanatory text about the reason for this version including any major changes. The level of detail that is included in this appendix is up to the editors and chairs of the TC to determine. This appendix is **REQUIRED**, if there are no changes then one is to put "None." In addition to any descriptive text, all major changes **SHOULD** be in a bulleted list so that reviewers and implementers can easily understand what they need to know.


\>


- Change 1  
- Change 2


## Revision History


- \< Date in yyyy-mm-dd format \>, \< Revision number \>  
- \< Date in yyyy-mm-dd format \>, \< Revision number \>


---


# Appendix 3 Additional Appendix as Needed


(This appendix does not form an integral part of this Specification and is informational.)


## Subsection Title


### Sub-subsection


\< The following centered line represents the end of the document \>  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
