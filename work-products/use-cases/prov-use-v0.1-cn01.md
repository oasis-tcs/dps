![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

# OASIS Committee Note
-------

# Provenance Use Cases Version 0.1

## Committee Note 01

## 16 May 2025

&nbsp;

#### This stage:
https://docs.oasis-open.org/dps/prov-use/v1.0/cn01/prov-use-v1.0-cn01.md (Authoritative) \
https://docs.oasis-open.org/dps/prov-use/v1.0/cn01/prov-use-v1.0-cn01.html \
https://docs.oasis-open.org/dps/prov-use/v1.0/cn01/prov-use-v1.0-cn01.pdf

#### Previous stage of Version 1.0:
https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.md (Authoritative) \
https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.html \
https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.pdf

#### Latest stage of Version 1.0:
https://docs.oasis-open.org/dps/prov-use/v1.0/prov-use-v1.0.md (Authoritative) \
https://docs.oasis-open.org/dps/prov-use/v1.0/prov-use-v1.0.html \
https://docs.oasis-open.org/dps/prov-use/v1.0/prov-use-v1.0.pdf

#### Technical Committee:
[OASIS Data Provenance Standards (DPS) TC](https://www.oasis-open.org/tc-dps/)

#### Chairs:

Lisa Bobbitt, Cisco, lbobbitt@cisco.com

Bryan Bortnick, IBM, bortnick@us.ibm.com

Fotis Psallidas, Microsoft, Fotis.Psallidas@microsoft.com

#### Secretary:
Kristina Podnar, Data & Trust Alliance, kpodnar@dataandtrustalliance.org 

#### Editors:

Lisa Bobbitt, Cisco, lbobbitt@cisco.com

Duncan Sparrell, sFractal Consulting, duncan@sfractal.comn

#### Related work:
This document is related to:
* fill in metadata spec

#### Abstract:
Data transparency is critical. 
Trust in the insights and decisions coming from both traditional data and AI applications 
depends on understanding the origin, lineage, and rights associated with the data that feeds them. 
Lack of transparency has real costs, including unnecessary risks and foregone opportunities. 
And yet, many organizations today cannot answer basic data questions 
without considerable difficulty and investment.

To realize the value of data requires a reliable cross-industry baseline of data transparency. 
The Data Provenance standards propose a solution.
These use case scenarios showcase
how the Data Provenance standards
support diverse needs across the 
data ecosystem.

#### Status:
This is a Non-Standards Track Work Product. The patent provisions of the OASIS IPR Policy do not apply.

This document was last revised or approved by the OASIS Data Provenance Standards (DPS) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tc-dps#technical.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/tc-dps/.

#### Citation format:
When referencing this document the following citation format should be used:

**[PROV-USE-v1.0]**

Provenance Use Cases Version 0.1_. Edited by Lisa Bobbitt, Duncan Sparrell. 16 May 2025. OASIS Committee Note 01. https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.html. Latest stage: https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.html.

#### Notices
Copyright &copy; OASIS Open 2025. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in [Appendix F](#appendix-f-notices).

-------

# Table of Contents

- [1 Introduction](#1-introduction)
  - [1.1 Background: Motivation](#11-background-motivation-for-jadn)
  - [1.1.1 whatever](#111-openc2-and-jadn)
  - [1.2 Purpose](#12-purpose)
  - [1.3 Terminology](#13-terminology)
- [2 Scenario 1 - Healthcare insurance data procurement](#2-information-modeling-overview)
  - [2.1 whatever](#21-defining-information)
- [3 Scenario 2 - Media consumption pattern dataset for consumer behavior insights](#3-creating-information-models-with-jadn)
  - [3.1 whatever](#31-jadn-overview)
- [4 Scenario 3 - Financial services customer product enablement](#4-advanced-techniques)
  - [4.1 whatever](#41-packages-and-namespaces) 
- [5 Scenario 4 - Enhancing global logistics efficiency through AI-driven tariff harmonization](#4-advanced-techniques)
  - [5.1 whatever](#41-packages-and-namespaces) 
- [Appendix A. Informative References](#appendix-a-informative-references)
- [Appendix B. Acknowledgments](#appendix-b-acknowledgments)
- [Appendix C. Revision History](#appendix-c-revision-history)
- [Appendix D. Frequently Asked Questions (FAQ)](#appendix-d-frequently-asked-questions-faq)
  - [D.1 ask a question here](#d1-jadn-vs-uml-primitive-data-types)
  - [D.2 some more here?](#d2-why-jadn-and-not-rdf)
  - [D.3 and keep going](#d3-why-jadn-and-not-owl)
- [Appendix E. Example whatever](#appendix-e-example-information-model-source)
  - [E.1 something](#e1-music-library)
- [Appendix F. Notices](#appendix-f-notices)

**List of Figures**
 - [Figure 1-1 -- fill in as needed](#figure-1-1----range-of-model-types)


**List of Tables**
 - [Table 3-1 -- fill in as needed](#table-3-1----compound-type-decision-tree)

-------

<!-- Insert a "line rule" (three or more hyphens alone on a new line, following a blank line) before each major section. This is used to generate a page break in the PDF format. -->

# 1 Introduction

put intro here

## 1.1 Background: Motivation for ...

This section provides the background for ...

### 1.1.1 whatever

add text

## 1.2 Purpose

Add text.

## 1.3 Terminology

This CN uses the definitions contained in the [[Provenance Metadata
Specification](#prov-md-v10)], section whatever. The following
additional terms are defined for this document:

 - **whatever:** definition here with ref to where got if we didn't create

 - **next:** definition here with ref to where got if we didn't create


-------

# 2 Scenario 1 - Healthcare insurance data procurement

blah blah

-------

# 3 Scenario 2 - Media consumption pattern dataset for consumer behavior insights

blah blah

# 4 Scenario 3 - Financial services customer product enablement

-------
# 5 Scenario 4 - Enhancing global logistics efficiency through AI-driven tariff harmonization

blah blah



-------

# Appendix A. Informative References

<!-- Required section -->

This appendix contains the informative references that are used in this document.

While any hyperlinks included in this appendix were valid at the time of publication, OASIS cannot guarantee their long-term validity.

EDITOR's NOTE: the following are cribbed from another CN and just included as examples.
We will need to delete and replace with ones relative to this CN

###### [ASN.1]
Recommendation ITU-T X.680 (2021) *Information technology - Abstract Syntax Notation One (ASN.1): Specification of basic notation* 

###### [JADN-v1.0]
JSON Abstract Data Notation Version 1.0. Edited by David Kemp. 17
August 2021. OASIS Committee Specification 01.
https://docs.oasis-open.org/openc2/jadn/v1.0/cs01/jadn-v1.0-cs01.html.
Latest stage:
https://docs.oasis-open.org/openc2/jadn/v1.0/jadn-v1.0.html.

###### [JSONSCHEMA]
Wright, A., Andrews, H., Hutton, B., *"JSON Schema Validation"*,
Internet-Draft, 16 September 2019,
https://tools.ietf.org/html/draft-handrews-json-schema-validation-02,
or for latest drafts: https://json-schema.org/work-in-progress.

###### [NTIA-SBOM]
NTIA Multistakeholder Process on Software Component Transparency, "SBOM At A Glance", April 2021,   https://ntia.gov/sites/default/files/publications/sbom_at_a_glance_apr2021_0.pdf

###### [RFC3444]
Pras, A., Schoenwaelder, J., "On the Difference between
Information Models and Data Models", RFC 3444, January 2003,
https://tools.ietf.org/html/rfc3444.

###### [RFC7049]
Bormann, C., Hoffman, P., *"Concise Binary Object Representation
(CBOR)"*, RFC 7049, October 2013,
https://tools.ietf.org/html/rfc7049.

###### [RFC8610]
Birkholz, H., Vigano, C. and Bormann, C., "Concise Data
Definition Language (CDDL): A Notational Convention to Express
Concise Binary Object Representation (CBOR) and JSON Data
Structures", RFC 8610, DOI 10.17487/RFC8610, June 2019,
https://www.rfc-editor.org/info/rfc8610

###### [UML]
"Unified Modeling Language", Version 2.5.1, December 2017,
https://www.omg.org/spec/UML/2.5.1/About-UML/

###### [YTLee]
Lee, Y. (1999), *Information Modeling: From Design to
Implementation*, IEEE Transactions on Robotics and Automation,
[online],
https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=821265
(Accessed October 5, 2022)


-------

# Appendix B. Acknowledgments


## B.1 Special Thanks

The DPS TC thanks the following individuals for their
assistance in the development of this Committee Note:

 - fill in

## B.2 Participants

The following individuals have participated in the creation of this document and are gratefully acknowledged:

| First Name | Last Name  | Company                                        |
|------------|------------|------------------------------------------------|
| fill       | in         | fill in                                        |
| fill       | in         | fill in                                        |
| fill       | in         | fill in                                        |

-------

# Appendix C. Revision History
| Revision           | Date       | Editor      | Changes Made          |
|:-------------------|:-----------|:------------|:----------------------|
| prov-uc-v1.0-cn01-wd01.md | 2025-05-16 | David Kemp | Initial working draft / CND01 |
| prov-uc-v1.0-cn01-wd02.md | 2023-x-x | David Kemp | Second WD / CN01 candidate |

-------

# Appendix D. Frequently Asked Questions (FAQ)

This appendix responds to a variety of Frequently Asked Questions
regarding ....

## D.1 ask a question herr

put answers here


## D.2 another question?

another answer


## D.3 another question?

answer


------

# Appendix E. Example whatever

## E.1 whatever


------

# Appendix F. Notices

Copyright &copy; OASIS Open 2023. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark/ for above guidance.

