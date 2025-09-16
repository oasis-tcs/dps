![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

# OASIS Committee Note

-------

# Provenance Use Cases Version 0.1

## Committee Note 01

### 09 September 2025

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

#### Editors:

Lisa Bobbitt, Cisco, lbobbitt@cisco.com

Stefan Hagen, Individual, stefan@hagen.link

#### Related work:

This document is related to:

- [Metadata Specification](https://docs.oasis-open.org/dps/meta/v1.0/meta.html)

#### Abstract:

Identifying, managing, and governing your data as an independent asset today is critical for trustworthy transparency,
regulatory and legal basis alignment, and use in AI.
Trust in the insights and decisions coming from both traditional data and AI applications depends on understanding the origin,
lineage, and rights associated with the data that drives them.
Lack of transparency has real costs, including unnecessary risks and foregone opportunities.
And yet, many organizations today cannot answer basic data questions without considerable difficulty and investment of people and disparate tools.

To realize the value of data requires a reliable cross-industry baseline of data provenance (source and legal processing basis) and
lineage (data processing's what, where, who, and how) as data is valued, governed, and managed across industries from customer to
data processor to sub-processor.
The Data Provenance standards propose a solution to standardized throughout the data's life cycle.
These use case scenarios showcase how the Data Provenance standards support diverse needs across the data ecosystem.

#### Status:

This is a Non-Standards Track Work Product. The patent provisions of the OASIS IPR Policy do not apply.

This document was last revised or approved by the OASIS Data Provenance Standards (DPS) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tc-dps#technical.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/tc-dps/.

#### Citation format:

When referencing this document the following citation format should be used:

**[prov-use-v1.0]**

_Provenance Use Cases Version 1.0_. Edited by Lisa Bobbitt and Stefan Hagen. 09 September 2025. OASIS Committee Note 01. https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.html. Latest stage: https://docs.oasis-open.org/dps/prov-use/v1.0/cnd01/prov-use-v1.0-cnd01.html.

#### Notices

Copyright &copy; OASIS Open 2025. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in [Appendix F](#appendix-f-notices).

-------

# Table of Contents

- [1 Introduction](#1-introduction)
  - [1.1 Background: Motivation for Standardization now](#11-background-motivation-for-standardization-now)
  - [1.2 Purpose](#12-purpose)
  - [1.3 Terminology](#13-terminology)
- [2 Use Case 1 - Healthcare Insurance Data Procurement](#uc1)
- [3 Use Case 2 - Media Consumption Pattern Dataset for Consumer Behavior Insights](#uc2)
- [4 Use Case 3 - Financial Services Customer Product Enablement](#uc3)
- [5 Use Case 4 - Enhancing Global Logistics Efficiency Through AI-driven Tariff Harmonization](#uc4)
- [Appendix A. References](#appendix-a-references)
  - [A.1 Normative References](#a1-normative-references)
  - [A.2 Informative References](#a1-informative-references)
- [Appendix B. Acknowledgments](#appendix-b-acknowledgments)
- [Appendix C. Revision History](#appendix-c-revision-history)
- [Appendix D. Frequently Asked Questions (FAQ)](#appendix-d-frequently-asked-questions-faq)
  - [D.1 Where did these use cases come from?](#d1-where-did-these-use-cases-come-from)
  - [D.2 How may I add new use cases?](#d2-how-may-i-add-new-use-cases)
  - [D.3 Is Data Provenance only for Privacy?](#d3-is-data-provenance-only-for-privacy)
- [Appendix E. Notices](#appendix-e-notices)

**List of Figures**

- [Figure 1-1 -- fill in as needed](#figure-1-1----range-of-model-types)

**List of Tables**

- [Table 3-1 -- fill in as needed](#table-3-1----compound-type-decision-tree)

-------

<!-- Insert a "line rule" (three or more hyphens alone on a new line, following a blank line) before each major section. This is used to generate a page break in the PDF format. -->

# 1 Introduction

Standardizing metadata (the descriptors) for data provenance and lineage that you are processing allows the automation of data management
(storage, deletion, localization, sharing &amp; backup requirements) governance
(allowances, restrictions and required controls given legal basis of processing, regulations, and policies),
data usage (type, age of data, source location, type of data, personal data, known bias, etc).

## 1.1 Background: Motivation for Standardization now

Data has traditionally been siloed, managed, and governed by application (built-in controls and defined processes) and
user of that application (contract or other legal basis).

In today's world where data is being sought for its value, its use in innovation, its processing alignment to regulations,
and its trustworthiness via transparency and observability, data requires to be treated as an independent asset.
To be independent, data must know itself by maintaining its provenance and tracking its lineage.
Standardized provenance and lineage metadata provides consistent identifiers to allow data to be independent as
it traverses its processing lifecycle from creation/collection, use, storage/retention, sharing, and deletion.

## 1.2 Purpose

These uses cases are examples of how the provenance and lineage metadata provide the foundational information to
maximize the data value while minimizing the processing risk.

## 1.3 Terminology

This CN uses the definitions contained in the [[Provenance Metadata
Specification](#prov-md-v10)], section whatever. The following
additional terms are defined for this document:

- **next:** definition here with ref to where got if we didn't create
- **Seed dataset:** definition here with ref to where got if we didn't creat
- **Underlying dataset(s):** definition here with ref to where got if we didn't create

-------

# 2 Use Case 1 - Healthcare Insurance Data Procurement{#uc1}<a id="uc1"></a>

## 2.1 Use case{#uc1--use-case}

Bella and her team at Healthcare Insurance are evaluating a new dataset that contains
comprehensive patient and insurance payment information.
This dataset is considered crucial for enhancing the company's predictive analytics models, which forecast healthcare trends,
personalize insurance plans, and optimize claim processing.

## 2.2 Role{#uc1--role}

Bella Ramirez, Procurement Team Lead (15 years of experience in the healthcare industry, specializing in procurement)
with the responsibilities of

- Evaluating and acquiring high-quality datasets to improve the company's analytical models.
- Facilitating vendor reviews and ensuring all datasets comply with applicable provenance requirements,
  including metadata coverage, regulatory requirements, and transparent AI data usage.
- Ensuring that procured data meets integration operational needs.
- Ensuring data usage aligns with healthcare regulations and company policies.
- Leveraging data insights for innovative marketing and improved customer trust.

## 2.3 Goals{#uc1--goals}

- Assess metadata coverage: Bella prioritizes the evaluation of the dataset's metadata to ensure it includes essential information like
  the dataset title, unique metadata identifier, metadata location, and details about data origin and collection methods.
  This step is crucial for establishing the dataset's lineage, context,
  and usage restrictions, aligning with the company's data provenance standards.
- Ensure regulatory compliance: By collaborating with the legal department,
  Bella reviews the dataset for its adherence to healthcare data regulations, focusing on confidentiality classification,
  consent documentation, and data processing and storage geographies.
- Operational efficiency and integration: Bella meets with the team that assesses how well the dataset integrates with existing systems and
  whether it can provide the expected enhancements to the analytical models without significant overhaul or disruption.
- Strategic use and innovation: Bella explores how the dataset can be used to develop innovative marketing strategies and improve customer trust.
  This involves touching base with the marketing team, which is focused on analyzing the dataset's intent and proprietary data presence to
  identify new opportunities for personalized customer engagement and service delivery.

## 2.4 How the Standards are Used{#uc1--standards-use}

For Bella to ensure the dataset under evaluation meets the standards required for her healthcare insurance company's analytical models,
she would assess the following values, all within the specified DPS metadata:

### 2.4.1 Version Used for Metadata{#uc1--standards-use--version-used-for-metadata}

Bella checks for the specific version number of the metadata schema or standard used,
ensuring it's the latest or a widely recognized version to maintain consistency and future-proof the dataset.
The version used for metadata is "1.0.0" which indicates the dataset is up to date with current standards.

Version number of the metadata schema or standard used, ensuring it's the latest version.
The version used for metadata is "1.0.0" which indicates the dataset uses the 1.0.0 version of the metadata standard,
suggesting that it is up to date with current DPS standard.

### 2.4.2 Dataset Title / Name{#uc1--standards-use--dataset-title-name}

Confirms dataset and metadata version.
Can be reflective of the dataset's content and intended use, facilitating easy identification and retrieval.
The title of the dataset is "2024 Comprehensive Patient Care and Insurance Claims Dataset",
indicating the dataset's contents and scope, including the year.

### 2.4.3 Unique Metadata Identifier{#uc1--standards-use--unique-metadata-identifier}

Verifying the presence of a unique identifier,
like a UUID, ensures it is correctly formatted and unique to prevent any confusion or overlap with other datasets.
For example: "25f263af-fbf9-481f-b73c-fdc520581af1".

### 2.4.4 Metadata Unique URL{#uc1--standards-use--metadata-unique-url}

The URL should lead directly to the data and detailed metadata.
Here, the provided value of https://example.com/dataset/metadata/25f263af-fbf9-481f-b73c-fdc520581af1 is a
direct link to the dataset's detailed metadata page.

### 2.4.4 Metadata Location for Datasets Feeding the Current Dataset{#uc1--how-the-standards-are-used--metadata-location}

Using https://example.com/metadata/sources, a URL that points to metadata for source datasets,
establishes the lineage and dependencies of the current dataset.
This provides understanding the dataset's lineage and dependencies, validates metadata record,
terms of use, and data classifications of one or multiple sources making up this dataset.

### 2.4.6 Date of Previously Published Version of the Dataset{#uc1--standards-use--date-of-previous-version}

Date enables third parties to track the dataset's evolution and version history.
"March 15, 2023" indicates when the last version of the dataset was released, helping track updates over time.

### 2.4.7 Creator{#uc1--standards-use--creator}

Verifying the creator's identity ensures they are reputable and provides accountability and a reliable point of contact for inquiries.
This further helps determine origin of the data.
The creator is noted as the "National Health Data Systems," adding a layer of trust and accountability.

### 2.4.8 Source (if Different From Creator){#uc1--standards-use--source}

Ensuring transparency and the integrity of the data collection process, lineage must link back to dataset creator.
"Nationwide Hospitals Systems, Insurance Providers Ltd." Are specified in the source, which indicates the original data sources.

### 2.4.9 Data Origin Geography{#uc1--standards-use--data-origin-geography}

Origin is crucial for compliance with applicable laws, residency requirements, and other regulations.
The data was collected in the "United States" for the country, "California" for the state, and "Arcata, Eureka, San Francisco" for the cities.

### 2.4.10 Dataset Creation Date{#uc1--standards-use--dataset-creation-date}

Confirmation of the dataset's creation date to assess its freshness and relevance to current analytical needs.
The metadata lists "January 10, 2024" as the creation date value and indicates when the dataset was compiled, providing
context for its currency and relevance of business cases.

### 2.4.11 Range of Dates for Data Generation{#uc1--standards-use--standards-use--range-of-dates-for-data-generation}

Evaluation of the time frame during which the data was collected,
ensuring it is relevant to the current analytical models and reflects recent trends or patterns.
"January 1, 2023 - December 31, 2023" dates that are provided show the time during which the data was collected,
highlighting the dataset's recency.

### 2.4.12 Method{#uc1--standards-use--method}

Understanding the data collection or generation methodology is critical for assessing the dataset's reliability and validity.
"Database feed" is the value in the method metadata field, and in the specification field,
"Electronic Health Records Extraction and Insurance Claim Processing Logs" is added.
This information describes how the data was collected, providing insight into its reliability.

### 2.4.13 Content Type{#uc1--standards-use--content-type}

Ability to assess whether the dataset's content type (numerical, textual, multimedia, etc.)
is compatible with the company's analytical tools and is suitable for the intended analyses.
"SQL" as the value and "Structured Data - Numerical and Categorical" specifies the nature of the dataset,
which is crucial for understanding how it can be analyzed.

### 2.4.14 Privacy Enhancing Technologies (PETs){#uc1--standards-use--privacy-enhancing-technologies-pets}

Confirmation on whether PETs were applied to the dataset to protect personal data,
ensuring the dataset's compliance with privacy regulations and ethical standards.
She notes that the metadata indicates a "No",
which confirms that no measures have been taken to protect personal information within the dataset.

### 2.4.15 Organizational Content Classification{#uc1--standards-use--organizational-content-classification}

Alignment of the dataset's classification t the company's data handling policies,
assessing whether its classification is appropriate and clear.
"Restricted" indicates the data handling requirements and access restrictions,
which is a flag to Bella that the dataset has protected health information (PHI)
under the Health Insurance Portability and Accountability Act (HIPAA) and
that the medical information must be carefully managed under provincial, state, or other healthcare privacy laws.

### 2.4.16 Confidentiality Classification{#uc1--standards-use--confidentiality-classification}

Data type sensitivity assigned to the dataset,
ensuring it is adequately secured and that access is appropriately controlled based on its classification.
"Private Health Information" reflects the dataset's sensitivity level and dictates security measures.

### 2.4.17 Consent Location{#uc1--standards-use--consent-location}

Verification of consent given location and adequacy of consent documentation,
ensuring compliance with legal standards.
https://example.com/dataset/25f263af-fbf9-481f-b73c-fdc520581af1/consent1.html points to where consent documentation is kept,
which the legal department may determine whether the consent meets the organization’s legal obligations for processing.

### 2.4.18 Data Processing Geography{#uc1--standards-use--data-processing-geography}

Assessment of any geographical restrictions on where the data can be processed, ensuring compliance with legal and
regulatory requirements regarding data processing locations.
The metadata lists "United States" for the country and "California" for the state.

### 2.4.19 Data Storage Geography{#uc1--standards-use--data-storage-geography}

Assessment of any geographical restrictions on where the data is stored,
which is crucial for adherence to data sovereignty laws and protecting sensitive information.
The metadata lists "United States" for the country and "California" for the state.
For example, this may require special handling of personal healthcare data,
so a check with the legal department is flagged for a final determination.

### 2.4.20 License to Use{#uc1--standards-use--license-to-use}

This metadata is passed along to the legal team information about the terms under which the dataset can be used,
including any restrictions or obligations,
to ensure the company's use of the dataset is legally sound and in line with the licensing terms.
"License details available upon request from the Data Governance Department,
National Health Data Repository, contactme@example.com" is listed and provides information on how to access terms of use.

### 2.4.21 Intent{#uc1--standards-use--intent}

Alignment to the purpose of the dataset's creation to the company's intended use and
supports identified use cases without misalignment or misuse.
The intent in the metadata indicates "AI" use and specifies "Pre-Training,"
which aligns with the use cases and requirements specified by the data team.
Insights from this information, along with the method metadata and dates generated,
and the data cost are inputs in the organization’s value assessment.

### 2.4.22 Proprietary Data Presence{#uc1--standards-use--proprietary-data-presence}

Knowing proprietary information ensures its use does not infringe on intellectual property rights and
is consistent with contractual agreements.
When all the values are empty, the data is free to be used without infringing on proprietary rights.

## 2.5 Outcome{#uc1--outcome}

Bella met with the legal department and the data team, to incorporate their assessment into the procurement analysis package.
After investigating, the legal team determined that the data supplier mistakenly tagged the data processing and storage metadata incorrectly and
had to correct the metadata associated with the dataset before the procurement process could proceed.
This delayed the data procurement process by four business days.

However, by successfully evaluating and integrating the new dataset, Bella ensures that the organization is well-positioned to
positively impact the company's business operations, including enhanced analytical capabilities, improved customer trust,
and the development of responsible AI applications.
This will align with the company's business considerations and set a benchmark for efficient and
trustworthy data usage in the healthcare insurance industry.

-------

# 3 Use Case 2 - Media Consumption Pattern Dataset for Consumer Behavior Insights{#uc2}<a name="uc2"></a>

## 3.1 Use case{#uc2--use-case}

Jordan Liu's current project involves curating a dataset that tracks media consumption habits across diverse platforms.
This dataset aims to empower media buyers and sellers in accurately targeting their audience segments,
facilitating personalized content strategies for industries ranging from consumer goods to tourism.

## 3.2 Role{#uc2--role}

Jordan Liu, Data Strategy Director, with a a decade of experience in media analytics and a deep understanding of the media consumption landscape.
His responsibilities include

- Overseeing the development and distribution of comprehensive media consumption datasets.
- Ensuring datasets adhere to the latest data provenance standards for transparent AI data usage and are relevant and reliable.
- Collaborating with stakeholders across healthcare, consumer goods, and travel industries to tailor data offerings.
- Guiding the integration of datasets into client systems to optimize targeted content delivery and marketing strategies.
- Advocating for data-driven decision-making within the company and among clients to foster industry innovation.

## 3.3 Goals{#uc2--goals}

- Ensure comprehensive coverage of media consumption patterns to provide actionable insights for diverse industries.
- Maintain high standards of data transparency to build trust and encourage collaboration.
- Enhance clients' operational efficiency and compliance through strategic data integration.

## 3.4 How the Standards are Used{#uc2--standards-use}

To ensure the dataset the company is offering to its buyers meets the company baseline required for AI analytical models and
(at least) the mandatory obligations for compatibility with the Data Provenance Standards,
the following metadata associated with the dataset is curated:

### 3.4.1 Version Used for Metadata{#uc2--standards-use--version-used-for-metadata}

Ensure the dataset utilizes version 1.0.0 of the data provenance standards,
thereby future proofing the metadata and making it backwards compatible, especially with systems that automate metadata ingestion.

### 3.4.2 Dataset Title / Name{#uc2--standards-use--dataset-title-name}

The title "March 2024 Global Media Consumption Trends," reflects the data contents and production time frame.

### 3.4.3 Unique Metadata Identifier{#uc2--standards-use--unique-metadata-identifier}

This generated UUID "550e8400-e29b-41d4-a716-446655440000" as the unique identifier, ensures identification within the data ecosystem, and allows direct access to the data provenance metadata based on the enumeration scheme of the organization.

### 3.4.4 Metadata Unique URL{#uc2--standards-use--metadata-unique-url}

The URL "https://example.com/550e8400-e29b-41d4-a716-446655440000/metadata.html is used for direct access to this dataset’s data provenance metadata,
ensuring transparency and easy reference by downstream consumers assessing the data for consumption.

### 3.4.5 Metadata Location for Datasets Feeding the Current Dataset{#uc2--standards-use--metadata-location}

Jordan outlines the lineage and sources contributing to the dataset for comprehensive transparency and
traceability by entering three values, "https://example.com/550e8400-e29b-41d4-a716-44665543902",
"https://example.com/550e8400-e29b-41d4-a716-44665544732",
and "https://example.com/550e8400-e29b-41d4-a716-446655465722" as the values.

### 3.4.6 Date of Previously Published Version of the Dataset{#uc2--standards-use--date-of-previous-version}

This metadata field documents the date, if applicable, when the dataset was previously published and
allows downstream consumers to track dataset evolution and updates.
Jordan leaves the field blank as this dataset is being published for the first time.

### 3.4.7 Creator{#uc2--standards-use--creator}

The market analysis company name, "AnalytiQuest Ventures" is listed attributing dataset ownership and responsibility for its integrity.

### 3.4.8 Source (if Different From Creator){#uc2--standards-use--source}

Since AnalytiQuest Ventures is the generator of the data, the field is left blank;
the creator of the dataset already accurately depicts the source of the data as AnalytiQuest Ventures.

### 3.4.9 Data Origin Geography{#uc2--standards-use--data-origin-geography}

This metadata field identifies the geographic data points that are included to contextualize the media consumption patterns,
with values for the metadata in order of requirements – country, state, city: United States, Florida, Miami;
United States, Florida, Ft. Lauderdale; United States, Florida, Orlando; United States, Florida, Clearwater;
United States, Florida, St. Petersburg; United States, Florida, Tampa; United States, Florida, Pensacola;
United States, Florida, Augusta; United States, Florida, Jacksonville; United States, Florida, Cape Coral.

### 3.4.10 Dataset Creation Date{#uc2--standards-use--dataset-creation-date}

The dataset creation date indicates the dataset's compilation date, ensuring relevance.
"January 10, 2024" is specified as the creation date, indicating when the dataset was compiled.
This date provides a context for the dataset's freshness.

### 3.4.11 Range of Dates for Data Generation{#uc2--standards-use--standards-use--range-of-dates-for-data-generation}

The range of "January 1, 2023 - December 31, 2023" is set as the period during which the data was collected.
This timeframe is crucial for ensuring the dataset reflects the latest media consumption patterns and is relevant for current analysis.

### 3.4.12 Method{#uc2--standards-use--method}

The data collection methodology, described as "User Generated Content: Digital Interaction Tracking and Survey Responses"
in the method metadata field, outlines how consumer interactions with various media platforms were recorded alongside targeted survey data.
This method provides a comprehensive view of media consumption behaviors, enhancing the dataset's transparency for in-depth consumer insights.

### 3.4.13 Content Type{#uc2--standards-use--content-type}

The type(s) of .xls (30%), .doc (40%) and .sql (30%) are set to depict the structured and
unstructured data means used to gauge multimedia engagement metrics and the textual Responses that characterize the dataset's content.
This mix is essential for analyzing both quantitative media engagement metrics and qualitative consumer feedback,
offering a multifaceted approach to media consumption analysis but also points to a potential level of
cleanup that may be required on the dataset.

### 3.4.14 Privacy Enhancing Technologies (PETs){#uc2--standards-use--privacy-enhancing-technologies-pets}

Jordan selects the metadata's indication of "Yes" to denote the use of PETs,
and specified "Anonymization and Data Aggregation Techniques Applied" via "Adverity" tool,
which confirms that steps have been taken, using verifiable tools, to anonymize and aggregate personal data,
ensuring the dataset's adherence to privacy standards and ethical considerations in media research.

### 3.4.15 Organizational Content Classification{#uc2--standards-use--organizational-content-classification}

The dataset is classified as being for "Internal Use",
and this classification signals the dataset's designed purpose for in-house analytics and strategic planning,
aligning with corporate data governance policies and ensuring appropriate handling within the organization.

### 3.4.16 Confidentiality Classification{#uc2--standards-use--confidentiality-classification}

This is often set when there is personally identifiable information on consumers present.

### 3.4.17 Consent Location{#uc2--standards-use--consent-location}

Since PETs have been used to aggregate and anonymize consumer personal data in the dataset,
no consent is required to process or share the consumers’ data and this this field is left blank.

### 3.4.18 Data Processing Geography{#uc2--standards-use--data-processing-geography}

Worldwide.

### 3.4.19 Data Storage Geography{#uc2--standards-use--data-storage-geography}

Worldwide.

### 3.4.20 License to Use{#uc2--standards-use--license-to-use}

Jordan knows that while this dataset doesn't have open-source licensing, the license terms are flexible for this dataset,
so rather than specifying the commercial terms,
he specifies that the AnalytiQuest Ventures's Office of General Counsel should be contacted for usage and licensing details. He enters
"AnalytiQuest Ventures's Office of General Counsel, legalconsumptionlicense@example.com and (555) 123-4567"
into the metadata field.

### 3.4.21 Intent{#uc2--standards-use--intent}

The purpose of this dataset is "AI", "Evaluation", and "Training",
which aligns with strategic objectives in media planning and content development, as well as research endeavors in the media industry.

### 3.4.22 Proprietary Data Presence{#uc2--standards-use--proprietary-data-presence}

The absence of proprietary restrictions, as indicated by the metadata,
confirms the dataset's availability for broad analysis within the stipulated legal frameworks,
facilitating unrestricted exploration of media consumption trends. This field is left blank.

## 3.5 Outcome{#uc2--outcome}

Under Jordan's guidance, the "March 2024 Global Media Consumption Trends" dataset emerges as a good resource for
understanding intricate media consumption behaviors across various platforms.
By curating and documenting the dataset's metadata, including the adoption of version 1.0.0 for OASIS data provenance standards,
assigning a unique identifier, and providing a transparent metadata URL, Jordan ensures the dataset's integrity and usability for AI analytics.

This attention to detail, coupled with the clear documentation of data origin, collection methodologies, and privacy-enhancing measures,
positions the dataset as a trustworthy and comprehensive tool for media buyers and sellers.
The dataset's rich insights into consumer behaviors, derived from diverse geographical regions and articulated through a mix of structured and
unstructured data types, empower stakeholders across multiple industries to tailor personalized content strategies effectively.

Jordan's emphasis on data transparency and legal requirements fosters collaboration but also enhances operational efficiency and
compliance for clients, setting a new benchmark for data-driven decision-making in media consumption.

-------

# 4 Use Case 3 - Financial Services Customer Product Enablement{#uc3}<a id="uc3"></a>

## 4.1 Use Case{#uc3--use-case}

Minh is tasked with evaluating a new dataset for refining AI algorithms for customer credit card offerings.
The dataset under consideration has been documented in accordance with the latest data provenance standards,
ensuring transparency and compliance, especially under GDPR and the EU AI Act.
Minh's evaluation process focuses on the detailed metadata provided for the dataset.

## 4.2 Role{#uc3--role}

Minh Quang Nguyen, Data Architecture and Policy Analyst with over a decade of experience in data management and policy development.
This role’s responsibilities include

- Designing and implementing efficient data architectures that support ProForma’s business goals.
- Work closely with IT teams to ensure that data structures are scalable, secure, and optimized for performance.
- Play a crucial role in developing and enforcing data management policies, ensuring compliance with regulatory standards and
  protecting customer information.

## 4.3 Goals{#uc3--goals}

- Improve the precision of AI models used in tailoring customer credit card products, leading to more personalized and effective offerings.
- Confirm that the dataset's use aligns with international regulations, including GDPR, safeguarding against legal and reputational risks.
- Maintain the highest standards of data privacy and security, particularly for personally identifiable information (PII) and
  sensitive personal information (SPI), through the application of Privacy Enhancing Technologies (PETs).
- Streamline data processing and storage practices to enhance efficiency while staying within the bounds of data processing and
  storage geography restrictions.
- Provide clear documentation of the dataset's origins, methodologies, and purposes to uphold transparency and accountability standards.
- Ensure the dataset's quality and integrity by verifying its collection methods, update history, and content type,
  thereby fostering trust in the AI-driven insights derived from it.

## 4.4 How the Standards are Used{#uc3--standards-use}

To assess a new dataset's compliance with data provenance standards and detailed metadata to refine AI algorithms focused on
customer credit card offerings, a review focuses on ensuring the dataset's integrity, transparency,
and compliance with international regulatory requirements, especially considering the implications of GDPR,
but also with an eye towards the new EU AI Act. The following aspects of the metadata are considered:

### 4.4.1 Version Used for Metadata{#uc3--standards-use--version-used-for-metadata}

Verification the metadata described is aligned with the most current schema version, "v1.0.0".

### 4.4.2 Dataset Title / Name{#uc3--standards-use--dataset-title-name}

Dataset title "Consumer Spending Patterns 2020-2024", which clearly reflects the dataset's focus.

### 4.4.3 Unique Metadata Identifier{#uc3--standards-use--unique-metadata-identifier}

Verification of the dataset's unique identifier, "LFS-1234-5678", to avoid any confusion with other datasets.

### 4.4.4 Metadata Unique URL{#uc3--standards-use--metadata-unique-url}

Access to the metadata through its URL, "http://luminadataservices.com/metadata/1234-5678",
providing a direct pathway to detailed dataset information.

### 4.4.5 Metadata Location for Datasets Feeding the Current Dataset{#uc3--standards-use--metadata-location}

Review the metadata for source datasets, such as "Retail Transaction Records 2023-2024"
as they are found at "http://luminadataservices.com/metadata/sources/retail-transactions-2023" and
"http://luminadataservices.com/metadata/sources/retail-transactions-2024" and
check these sources via their metadata for any areas of risks.

### 4.4.6 Date of Previously Published Version of the Dataset{#uc3--standards-use--date-of-previous-version}

The last update was on "March 15, 2025", indicating recent revisions.

### 4.4.7 Creator{#uc3--standards-use--creator}

The creator metadata field credits the dataset to the "Lumina Financial Services", establishing accountability.

### 4.4.8 Source (if Different From Creator){#uc3--standards-use--source}

Confirmation of the original data sources, "Global Retail Partners Consortium" and "PreciTech Data Inc.",
differentiating the sources from the dataset creator.

### 4.4.9 Data Origin Geography{#uc3--standards-use--data-origin-geography}

The data originates from "Europe, France; Europe, Germany;Europe, Italy;; Europe, Poland" which is important for compliance considerations.

### 4.4.10 Dataset Creation Date{#uc3--standards-use--dataset-creation-date}

Minh reviews the dataset creation date range, which is reflected in the metadata as "March 14, 2024".
The data is recent, which is a great sign for Minh's use case but he needs to understand the range of data generation to verify that
it is not stale and that it has been collected recently reflective of legal and regulatory data privacy requirements.

### 4.4.11 Range of Dates for Data Generation{#uc3--standards-use--standards-use--range-of-dates-for-data-generation}

Minh then reviews the dataset generation date range, which is reflected in the metadata as "January 5, 2023 through March 14, 2024",
providing context for the data's recency and relevancy for establishing consumer trends.

### 4.4.12 Method{#uc3--standards-use--method}

The methodology, "Feeds, Interval timed database info, Aggregated Consumer Transaction Analysis, PoS",
is reviewed for data collection integrity.
100 percent of the data was received in this structured format,
which is what is expected and knows to be relatively clean data requiring minimal pre-processing for his data ingestion needs.

### 4.4.13 Content Type{#uc3--standards-use--content-type}

The dataset contains "application/sql",
which reflects the Oracle database source the company is accustomed to seeing and knows to be suitable data for AI modeling.

### 4.4.14 Privacy Enhancing Technologies (PETs){#uc3--standards-use--privacy-enhancing-technologies-pets}

The PETs metadata identifies a "Yes", indicating that privacy concerns have been addressed through data anonymization.
"Google differential privacy library" is listed as the tool and "Differential privacy" is listed as the method used for applying PETs.
This signals that confidential data is unlikely to be present and
that consent for further consumer data processing is not required due to the PETs application.

### 4.4.15 Organizational Content Classification{#uc3--standards-use--organizational-content-classification}

Labeled as "Internal Use", this metadata value for content classification will be guiding the team on access limitations.

### 4.4.16 Confidentiality Classification{#uc3--standards-use--confidentiality-classification}

This metadata value was not presented to the data supplier for completion as PETs were identified as being applied in a previous metadata field.

### 4.4.17 Consent Location{#uc3--standards-use--consent-location}

Worldwide.

### 4.4.18 Data Processing Geography{#uc3--standards-use--data-processing-geography}

Worldwide.

### 4.4.19 Data Storage Geography{#uc3--standards-use--data-storage-geography}

Worldwide.

### 4.4.20 License to Use{#uc3--standards-use--license-to-use}

The metadata field indicates a ‘Commercial/Negotiated License’ and includes a URL.
Minh checks the license terms at "http://luminadataservices.com/license/1234-5678",
reviewing the standardized usage rights available under different license options.
Since he is unfamiliar with some of the licensing clauses expressed in the documentation,
Minh forwards the license terms to the General Counsel's Office for review and analysis.
There have been some issues with pricing of data coming from the EU recently,
and he wants to ensure a complete legal picture is assessed before proceeding with a decision to acquire this dataset.

### 4.4.21 Intent{#uc3--standards-use--intent}

The dataset metadata intent indicates the data is intended for "AI, Other, Enhancing AI-driven Credit Card Offerings",
aligning with the project goals.

### 4.4.22 Proprietary Data Presence{#uc3--standards-use--proprietary-data-presence}

The proprietary metadata field set by the data supplier indicates "No" to the presence of copyright, trademark or patent presence,
indicating possible exclusivity to the company of whatever AI modeling outcomes may be obtained, which could offer competitive advantages.

## 4.5 Outcome{#uc3--outcome}

Minh’s review of the metadata for the "Consumer Spending Patterns 2020-2024" dataset results in advancements in
ProForma Financial Services' AI algorithms for customer credit card offerings.
By reviewing the standards and metadata, Minh increased the chances for strategic success.
He verified the dataset's compliance with the latest data provenance standards, including a review of its versioning, unique identifiers,
and comprehensive metadata URLs. Minh thus ensured the dataset's integrity and alignment with international regulations.
His attention to the dataset's lineage, original sources, and the application of Privacy Enhancing Technologies helped meet
the data privacy requirements set by his company and will mitigate potential legal and
reputational risks associated with GDPR and the EU AI Act compliance blunders.

The detailed metadata, including data origin geography, creation dates, and collection methodologies, provided Minh with the assurance of
the dataset's relevance and quality.
The absence of proprietary data restrictions, coupled with clear licensing terms, positions ProForma to leverage this dataset for
creating more personalized and effective customer credit card products.
Minh's approach to dataset integration will enhance operational efficiencies going forward, ensuring seamless compatibility with
the company's existing data architecture and AI systems.

Overall, Minh's review of the metadata to ensure alignment with requirements mean that ProForma Financial Services can
harness AI-driven insights responsibly and innovatively, paving the way for data-driven product enablement and
a competitive edge in the financial services sector.

-------

# 5 Use Case 4 - Enhancing Global Logistics Efficiency through AI-driven Tariff Harmonization{#uc4}<a id="uc4"></a>

## 5.1 Use case{#uc4--use-case}

The global nature of Navisphere Logistics, Ltd.'s operations means that the company must navigate a complex web of
international tariffs and customs regulations.
Efficiently managing these tariffs is critical to minimizing delivery times and costs.
Dr. Hicks and her team are tasked with refining the company’s AI systems to accurately predict tariff costs across
different countries and product categories.

## 5.2 Role{#uc4--role}

Dr. Maya Hicks, Lead Data Scientist with a specialization in artificial intelligence and machine learning and
a keen interest in optimizing supply chain efficiency through innovative technologies. Her responsibilities are to

- Lead the AI research and development team in refining and enhancing the company's AI-driven tariff prediction models.
- Evaluate datasets for integrity and compliance with corporate policies and
  standards which reflect international regulations and privacy considerations.
- Collaborate with procurement and legal colleagues to ensure that the data and
  AI models are in line with global standards and regulations.
- Train and optimize AI models to accurately predict tariffs, involving sophisticated algorithms and
  machine learning techniques.
- Integrate the refined AI models into Navisphere Logistics' operational systems and
  conduct extensive testing to ensure accuracy and efficiency.
- Establish and maintain a feedback loop for continuous monitoring and
  improvement of the AI models based on real-world application insights.
- Ensure the responsible use of AI in accordance with Navisphere Logistics’ standards and
  privacy laws, particularly in the handling of sensitive data.
- Communicate the progress and outcomes of the AI enhancements to stakeholders, including technical teams,
  management, and commercial clients.
- Stay updated with the latest developments in AI, machine learning, and international logistics practices to
  continually drive innovation within the company.

## 5.3 Goals{#uc4--goals}

- Harmonize global tariff schedules into a unified, AI-friendly format to enhance prediction accuracy.
- Refine and improve the AI-driven tariff prediction models to minimize cross-border delivery times and costs.
- Ensure that all collected tariff data meets stringent data transparency, accuracy, lineage, and AI data usage requirements
  for integrity and compliance with international regulations.
- Achieve high accuracy in tariff predictions across different countries and product categories through sophisticated AI algorithms.
- Streamline customs clearance processes through more precise tariff assessments, benefiting the company’s worldwide commercial clientele.

## 5.4 How the standards are Used{#uc4--standards-use}

Dr. Hicks leverages the metadata associated with global tariff schedule datasets to ensure the accuracy and reliability of
AI-driven tariff prediction models, essential for optimizing logistics operations.
The metadata, including the data's origin, collection methodology, and privacy considerations,
enables her to assess the trustworthiness and relevance of the data for her analyses.
This approach to metadata evaluation forms the foundation of Maya's ability to build and maintain robust, transparent,
and compliant AI systems within Navisphere Logistics, Ltd.

### 5.4.1 Version Used for Metadata{#uc4--standards-use--version-used-for-metadata}

Maya uses this attribute to ensure that the dataset conforms to the latest standards for metadata documentation,
which is crucial for compatibility with Navisphere's AI systems.
She evaluates the metadata schema value "1.4.5" and determines it is backwards compatible with the version Navisphere is using.

### 5.4.2 Dataset Title / Name{#uc4--standards-use--dataset-title-name}

This metadata describes the dataset's focus and relevance to her needs.
The title she evaluates is "2023 Global Tariff Schedules - Electronics".

### 5.4.3 Unique Metadata Identifier{#uc4--standards-use--unique-metadata-identifier}

Along with the dataset title, the unique metadata identifier to uniquely identifies and references datasets without confusion,
especially when dealing with multiple sources.
The use of "123e4567-e89b-12d3-a456-426614174000" value which she confirms in the company’s data procurement system has not
previously been considered nor procured by the company

### 5.4.4 Metadata Unique URL{#uc4--standards-use--metadata-unique-url}

This metadata component provides direct access to detailed dataset information for deeper evaluation.
Its value for this use case is "https://globaltradedatahub.com/metadata/123e4567-e89b-12d3-a456-426614174000".

### 5.4.5 Metadata Location for Datasets Feeding the Current Dataset{#uc4--standards-use--metadata-location}

This metadata component traces data lineage and verifies the integrity of source data.
Examples for this use case includes five values,
denoting that five different datasets supplied the data contained in the set being evaluated.

### 5.4.6 Date of Previously Published Version of the Dataset{#uc4--standards-use--date-of-previous-version}

This field tracks any dataset updates and revisions. The "N/A" value signifies that the dataset has not previously been published.

### 5.4.7 Creator{#uc4--standards-use--creator}

Knowing the creator provides accountability and a point of reference to check what other datasets the company has
previously procured from the same data supplier and satisfaction reviews of the supplier’s historically provided data.
"GlobalTradeDataHub" is reflected as the creator.

### 5.4.8 Source (if Different From Creator){#uc4--standards-use--source}

Reviewing the source metadata for the dataset to determine its difference from the creator.
The value of "International Customs Data Consortium" which again,
helps determine the reliability and historical satisfaction of supplied data.
Together with the metadata location for datasets feeding the current set metadata,
tells that all data in the current dataset originated with International Customs Data Consortium and
that GlobalTradeDataHub was merely the curator or entity that put the datasets together to provide the current one on offer.

### 5.4.9 Data Origin Geography{#uc4--standards-use--data-origin-geography}

Review of the data origin geography, noting "Europe, Switzerland; Europe, United Kingdom; Europe, Netherlands"
as the values along with determining that if the dataset contains personal data, additional regulatory requirements will apply.
If personal data is present, additional pre-processing of data to anonymize the data will be required and
require legal review and will extend the project delivery date. |

### 5.4.10 Dataset Creation Date{#uc4--standards-use--dataset-creation-date}

A "February 1, 2024" creation date provides the ability to see on the data's recency and relevance and
to determine that tariff schedules that took place with the first of the year are likely to be included in the set.
However, the range of dates for data generation will confirm for her this fact, so she reviews that metadata next.

### 5.4.11 Range of Dates for Data Generation{#uc4--standards-use--range-of-dates-for-data-generation}

This helps assess the dataset's timeliness. The range is "January 1, 2020 to January 31, 2024".
Based on this information, the date range covers new tariff schedules that were rolled out at the start of the current year.
However, the company already has data in house for the time period of January 1, 2020 through December 31, 2022,
which means she will be paying to acquire data that already exists in the enterprise.
Confirmation with her procurement team determines that negotiations should exclude the initial two years of data and
the price of the dataset should reflect that adjustment.

### 5.4.12 Method{#uc4--standards-use--method}

Understanding the collection method helps judge the potential need for cleanup of data prior to its use.
The description of "Feeds, Other, Automated Customs Entry Processing" implies a highly structured format and
the automation further points to patterns that can use to detect anomalies in the cleanliness of the data.

### 5.4.13 Content Type{#uc4--standards-use--content-type}

The content type metadata informs the kind of information the dataset contains,
aiding in data parsing such as "application/vnd.oasis.opendocument.database".
This media type is used for database files created with software that adheres to the OpenDocument standards,
such as LibreOffice Base or Apache OpenOffice Base. This supports the reliability of the data for the use case needs.

### 5.4.14 Privacy Enhancing Technologies (PETs){#uc4--standards-use--privacy-enhancing-technologies-pets}

With the clear "YES" affirmation of PETs application of on this dataset for data privacy compliance,
it can easily be determined if anonymization of the data is needed prior to its use.
A "Yes" in the metadata for anonymization confirms that personal data is not present in the dataset.
"Clover DX" is listed as the toolset and "Anonymization" is listed as the method.
The metadata notes in the outcome field "injected 3% random data into the mix" which signals to her an appropriate level of noise,
as the company considers anything above 5% unacceptable.

### 5.4.15 Organizational Content Classification{#uc4--standards-use--organizational-content-classification}

This metadata value guides how the dataset can be used within Navisphere.
"Internal Use Only" denotes there is no sensitive information contained in the dataset, but there are reasons for restrictions,
most likely legal in nature. Reviewing the license information with the legal team will determine what the limitations might be.

### 5.4.16 Confidentiality Classification{#uc4--standards-use--confidentiality-classification}

Because PETs were used and declared in the previous metadata, this metadata field is grayed out for the data supplier when assigning metadata,
no values are presented.

### 5.4.17 Consent Location{#uc4--standards-use--consent-location}

Worldwide.

### 5.4.18 Data Processing Geography{#uc4--standards-use--data-processing-geography}

Worldwide.

### 5.4.19 Data Storage Geography{#uc4--standards-use--data-storage-geography}

Worldwide.

### 5.4.20 License to Use{#uc4--standards-use--license-to-use}

Maya notes that the fee-bearing license applicable to the dataset is available at
"https://globaltradedatahub.com/license/123e4567-e89b-12d3-a456-426614174000".
While she scans the license information,
she knows that she will need the legal department's eyes and sign off before proceeding with the purchase of the dataset.
She routes the license, along with her question around specific data content classification to her colleagues in
the legal department for consideration and approval.

### 5.4.21 Intent{#uc4--standards-use--intent}

Reviews the dataset intent, and notices that the data is intended for "AI, Training", which aligns with the project goals.
The declaration also signals that the premium price placed on the dataset is appropriate because it is intended and
expected to be of higher quality than data intended for other uses.

### 5.4.22 Proprietary Data Presence{#uc4--standards-use--proprietary-data-presence}

Reviews the metadata around proprietary data presence and notes that there is a contact listed for the copyright.
Flags "Jonathan Reeves, Esq., Email: jreeves@globaltradedatahublegal.com, Phone: +1-555-012-3456"
for her legal colleagues to use in clarifying the copyright application and confirming whether the company should use the dataset,
or whether the copyright will limit commercial applications once the AI is trained with the data input.

## 5.5 Outcome{#uc4--outcome}

Through application of the data provenance standards metadata for its global tariff schedule datasets
Navisphere Logistics, Ltd. has achieved a significant enhancement in the operational efficiency and accuracy of
its AI-driven tariff prediction models. The outcome includes:

- Improved data consistency and compatibility:
  By specifying the version used for the metadata, Navisphere ensured that all datasets adhered to a uniform standard,
  facilitating seamless integration and interpretation by the AI models, regardless of the data's origin or when it was collected.
- Enhanced data identification and access:
  The establishment of a unique metadata identifier and a metadata unique URL for each dataset enabled easy identification,
  access, and reference, streamlining the data ingestion process for the AI systems, and reducing the time spent on data preprocessing.
- Streamlined data lineage and dependency tracking:
  The metadata location for datasets feeding the current dataset allowed Navisphere to efficiently manage data dependencies and lineage,
  ensuring that updates or corrections in source datasets could be rapidly propagated through the system,
  maintaining the accuracy and timeliness of tariff predictions.
- Increased accountability and data integrity:
  Detailed metadata entries for the creator, source, and data origin geography provided clear accountability and context for the data,
  enhancing trust in the data's reliability and compliance with regional laws and international regulations.
- Better data privacy and security measures:
  The application of privacy enhancing technologies (PETs) and the careful classification of data confidentiality ensured that
  personally identifiable information (PII) and sensitive personal information (SPI) were adequately protected,
  aligning with global privacy standards and ethical considerations in AI application.
- Legal compliance:
  Detailed metadata on data processing and storage geographies, consent locations,
  and the license to use the data ensured that all AI operations remained within legal boundaries, respecting data sovereignty laws and consent.

-------

# Appendix A. References

## A.1 Normative References

n/a

## A.2 Informative References

This appendix contains the informative references that are used in this document.

While any hyperlinks included in this appendix were valid at the time of publication, OASIS cannot guarantee their long-term validity.

n/a

-------

# Appendix B. Acknowledgments

## B.1 Special Thanks

The DPS TC thanks the following individuals for their assistance in the development of this Committee Note:
Kristina Podnar and the Data &amp; Trust Alliance for their contributions of these initial use cases.

## B.2 Participants

The following individuals have participated in the creation of this document and are gratefully acknowledged:

| First Name | Last Name | Company                   |
|:-----------|:----------|:--------------------------|
| Bryan      | Bortnick  | IBM                       |
| David      | Kemp      | NSA                       |
| Kristina   | Podnar    | Data &amp; Trust Alliance |
| Lisa       | Bobbitt   | Cisco                     |

-------

# Appendix C. Revision History

| Revision                  | Date       | Editor(s)                    | Changes Made                            |
|:--------------------------|:-----------|:-----------------------------|:----------------------------------------|
| prov-uc-v1.0-cn01-wd01.md | 2025-07-27 | Lisa Bobbit and Stefan Hagen | Initial draft.                          |
| prov-uc-v1.0-cn01-wd02.md | 2025-08-12 | Lisa Bobbit and Stefan Hagen | Implemented member feedback.            |
| prov-uc-v1.0-cn01-wd03.md | 2025-08-26 | Lisa Bobbit and Stefan Hagen | Editor revision for meeting 2025-08-26. |
| prov-uc-v1.0-cn01-wd04.md | 2025-09-09 | Lisa Bobbit and Stefan Hagen | Editor revision for meeting 2025-09-09. |

-------

# Appendix D. Frequently Asked Questions (FAQ)

This appendix responds to a variety of Frequently Asked Questions
regarding ....

## D.1 Where did these use cases come from?

Data &amp; Trust Alliance <https://dataandtrustalliance.org/>.
The Data &amp; Trust Alliance was established in September 2020 by a group of CEOs of major companies,
based on a shared conviction that the future of business will be powered by the responsible use of data and AI.

## D.2 How may I add new use cases?

Contribute a use case in the contributions folder.
Join the Use Case Subcommittee.

## D.3 Is Data Provenance only for Privacy?

No. Data provenance is a part of data protection and covers other concerns too.
Additional examples are organizational data and full life cycle documentation.

-------

# Appendix E. Notices

Copyright &copy; OASIS Open 2025. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark/ for above guidance.
