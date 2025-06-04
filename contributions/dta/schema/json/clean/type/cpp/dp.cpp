#pragma once

#include <optional>

struct GenerationMethod {
    std::string code;
    std::optional<std::string> description;
    std::optional<std::string> system;
};

/**
 * The span of time during which the data within the dataset was collected or generated,
 * offering insight into the dataset's timeliness and relevance.
 */
struct GenerationPeriod {
    /**
     * End date/time
     */
    std::optional<std::string> end;
    /**
     * Start date/time
     */
    std::optional<std::string> start;
};

struct Origin {
    std::optional<std::vector<std::string>> address;
    std::string name;
};

struct OriginGeography {
    std::string country;
    std::optional<std::string> state;
};

/**
 * This describes the provenance of the dataset.
 */
struct Provenance {
    /**
     * The date when the dataset was compiled or created, providing a temporal context for the
     * data.
     */
    std::string date;
    /**
     * Describes the nature of the data within the dataset, such as numerical, textual, or
     * multimedia, helping users understand what kind of information is contained within the
     * file or dataset.
     */
    std::optional<std::vector<std::string>> format;
    /**
     * The methodology or procedures used to collect, generate, or compile the data, giving
     * insight into its reliability and validity.
     */
    std::vector<GenerationMethod> generation_method;
    /**
     * The span of time during which the data within the dataset was collected or generated,
     * offering insight into the dataset's timeliness and relevance.
     */
    std::optional<GenerationPeriod> generation_period;
    /**
     * If the data originates from a different organization than the one who issued the dataset,
     * this field identifies the original source's legal name.
     */
    std::optional<std::vector<Origin>> origin;
    /**
     * The geographical location where the data was originally collected, which can be important
     * for compliance with regional laws and understanding the data's context.
     */
    std::vector<OriginGeography> origin_geography;
    /**
     * The release date of the last version of the dataset, if it has been updated or revised,
     * to track changes and updates over time.
     */
    std::optional<std::string> previous_date;
    /**
     * Identifies where the metadata for any source datasets that contribute to the current
     * dataset can be found, establishing lineage and dependencies. This field establishes
     * lineage.
     */
    std::optional<std::string> source;
    std::shared_ptr<Provenance> sub_provenance;
};

struct Issuer {
    std::optional<std::vector<std::string>> address;
    std::string name;
};

/**
 * This describes a dataset and the source of the dataset.
 */
struct Source {
    /**
     * Contains a detailed narrative that explains the contents, scope, and purpose of the
     * dataset. It provides essential contextual information that helps users understand what
     * the data represents, how it was collected, and any limitations or recommended uses.
     */
    std::string description;
    /**
     * A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquely
     * distinguish it from others, ensuring no confusion or overlap.
     */
    std::string id;
    /**
     * The legal entity responsible for creating the dataset, providing accountability and a
     * point of contact for inquiries.
     */
    std::vector<Issuer> issuer;
    /**
     * The web address where the dataset's metadata is published and can be accessed, providing
     * a direct link to detailed information about the dataset. Typically will be a unique URL
     * of the current dataset.
     */
    std::optional<std::string> location;
    /**
     * The official name of the dataset, which should be descriptive and help easily identify
     * the dataset's content and purpose.
     */
    std::string title;
    /**
     * Specifies the version of the schema or standards used to define the metadata for this
     * dataset, ensuring consistency and compatibility over time.
     */
    std::string version;
};

struct Regulation {
    std::string code;
    std::optional<std::string> description;
    std::optional<std::string> system;
};

struct Classification {
    bool evaluated;
    Regulation regulation;
    std::optional<std::string> tool;
};

struct IntendedPurpose {
    std::string code;
    std::string description;
    std::optional<std::string> system;
};

struct ToolCategory {
    std::string code;
    std::optional<std::string> description;
    std::optional<std::string> system;
};

struct PrivacyEnhancing {
    std::optional<std::vector<std::string>> parameters;
    std::optional<std::vector<std::string>> result;
    std::optional<ToolCategory> tool_category;
    std::string tool_used;
};

struct ProcessingExcluded {
    std::string country;
    std::optional<std::string> state;
};

struct ProcessingIncluded {
    std::string country;
    std::optional<std::string> state;
};

struct StorageAllowed {
    std::string country;
    std::optional<std::string> state;
};

struct StorageForbidden {
    std::string country;
    std::optional<std::string> state;
};

/**
 * This group describes legal use and restrictions.
 */
struct Use {
    /**
     * Indicate if the dataset includes data falling into the confidentiality classification.
     * Each classifier must be evaluated as true/false/unknown.
     */
    std::optional<std::vector<Classification>> classification;
    /**
     * Specifies where consent documentation or agreements related to the data can be found,
     * ensuring legal compliance and regulatory use. This element must be populated when Privacy
     * Consent is appropriate. When populated it points to either one Privacy Consent Policy
     * that all individuals in the dataset agreed to, or one Privacy Policy for each individual
     * in the dataset with that individual's signature.
     */
    std::optional<std::vector<std::string>> consents;
    /**
     * Indicates whether the dataset contains proprietary information that is covered with a
     * Copyright and the terms of said Copyright.
     */
    std::optional<std::vector<std::string>> copyright;
    /**
     * Describes the purpose for which the dataset was created, guiding users on its intended
     * use and potential applications against identified use cases. List all that apply from the
     * Data Use codes that apply. Additional codes can be included with descriptions.
     */
    std::vector<IntendedPurpose> intended_purpose;
    /**
     * Details the location or point of contact for identifying the terms under which the
     * dataset can be used, including any restrictions or obligations, clarifying legal use and
     * distribution rights. License may be an End User License Agreement (EULA), subject to Data
     * Use Agreement (DUA).
     */
    std::optional<std::vector<std::string>> license;
    /**
     * Indicates whether the dataset contains proprietary information that is covered with a
     * Patent and said Patent number.
     */
    std::optional<std::vector<std::string>> patent;
    /**
     * Indicates whether techniques were used to protect personally identifiable information
     * (PII) or sensitive personal information (SPI), highlighting the dataset's privacy
     * considerations.
     */
    std::optional<std::vector<PrivacyEnhancing>> privacy_enhancing;
    /**
     * Defines the geographical boundaries within which the data cannot be processed, often for
     * legal or regulatory reasons.
     */
    std::optional<std::vector<ProcessingExcluded>> processing_excluded;
    /**
     * Defines the geographical boundaries within which the data can be processed, often for
     * legal or regulatory reasons.
     */
    std::optional<std::vector<ProcessingIncluded>> processing_included;
    /**
     * Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
     */
    std::optional<std::vector<StorageAllowed>> storage_allowed;
    /**
     * Specifies where the data may not be stored, crucial for compliance with data sovereignty
     * laws.
     */
    std::optional<std::vector<StorageForbidden>> storage_forbidden;
    /**
     * Indicates whether the dataset contains proprietary information that is covered with a
     * Trademark, and the terms of said Trademark.
     */
    std::optional<std::vector<std::string>> trademark;
};

/**
 * The Data Provenance metadata schema is made up of three groups of metadata elements:
 * Source, Provenance, and Use.
 */
struct DataProvenance {
    Provenance provenance;
    Source source;
    Use use;
};
