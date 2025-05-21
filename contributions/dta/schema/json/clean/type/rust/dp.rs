use serde::{Deserialize, Serialize};

/// The Data Provenance metadata schema is made up of three groups of metadata elements:
/// Source, Provenance, and Use.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DataProvenance {
    provenance: Box<Provenance>,

    source: Source,

    #[serde(rename = "use")]
    data_provenance_use: Use,
}

/// This group describes legal use and restrictions.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub struct Use {
    /// Indicate if the dataset includes data falling into the confidentiality classification.
    /// Each classifier must be evaluated as true/false/unknown.
    classification: Option<Vec<Classification>>,

    /// Specifies where consent documentation or agreements related to the data can be found,
    /// ensuring legal compliance and regulatory use. This element must be populated when Privacy
    /// Consent is appropriate. When populated it points to either one Privacy Consent Policy
    /// that all individuals in the dataset agreed to, or one Privacy Policy for each individual
    /// in the dataset with that individual's signature.
    consents: Option<Vec<String>>,

    /// Indicates whether the dataset contains proprietary information that is covered with a
    /// Copyright and the terms of said Copyright.
    copyright: Option<Vec<String>>,

    /// Describes the purpose for which the dataset was created, guiding users on its intended
    /// use and potential applications against identified use cases. List all that apply from the
    /// Data Use codes that apply. Additional codes can be included with descriptions.
    intended_purpose: Vec<IntendedPurpose>,

    /// Details the location or point of contact for identifying the terms under which the
    /// dataset can be used, including any restrictions or obligations, clarifying legal use and
    /// distribution rights. License may be an End User License Agreement (EULA), subject to Data
    /// Use Agreement (DUA).
    license: Option<Vec<String>>,

    /// Indicates whether the dataset contains proprietary information that is covered with a
    /// Patent and said Patent number.
    patent: Option<Vec<String>>,

    /// Indicates whether techniques were used to protect personally identifiable information
    /// (PII) or sensitive personal information (SPI), highlighting the dataset's privacy
    /// considerations.
    privacy_enhancing: Option<Vec<PrivacyEnhancing>>,

    /// Defines the geographical boundaries within which the data cannot be processed, often for
    /// legal or regulatory reasons.
    processing_excluded: Option<Vec<ProcessingExcluded>>,

    /// Defines the geographical boundaries within which the data can be processed, often for
    /// legal or regulatory reasons.
    processing_included: Option<Vec<ProcessingIncluded>>,

    /// Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
    storage_allowed: Option<Vec<StorageAllowed>>,

    /// Specifies where the data may not be stored, crucial for compliance with data sovereignty
    /// laws.
    storage_forbidden: Option<Vec<StorageForbidden>>,

    /// Indicates whether the dataset contains proprietary information that is covered with a
    /// Trademark, and the terms of said Trademark.
    trademark: Option<Vec<String>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Classification {
    evaluated: bool,

    regulation: Regulation,

    tool: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Regulation {
    code: String,

    description: Option<String>,

    system: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct IntendedPurpose {
    code: String,

    description: String,

    system: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub struct PrivacyEnhancing {
    parameters: Option<Vec<String>>,

    result: Option<Vec<String>>,

    tool_category: Option<ToolCategory>,

    tool_used: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ToolCategory {
    code: String,

    description: Option<String>,

    system: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProcessingExcluded {
    country: String,

    state: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProcessingIncluded {
    country: String,

    state: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct StorageAllowed {
    country: String,

    state: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct StorageForbidden {
    country: String,

    state: Option<String>,
}

/// This describes the provenance of the dataset.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub struct Provenance {
    /// The date when the dataset was compiled or created, providing a temporal context for the
    /// data.
    date: String,

    /// Describes the nature of the data within the dataset, such as numerical, textual, or
    /// multimedia, helping users understand what kind of information is contained within the
    /// file or dataset.
    format: Option<Vec<String>>,

    /// The methodology or procedures used to collect, generate, or compile the data, giving
    /// insight into its reliability and validity.
    generation_method: Vec<GenerationMethod>,

    /// The span of time during which the data within the dataset was collected or generated,
    /// offering insight into the dataset's timeliness and relevance.
    generation_period: Option<GenerationPeriod>,

    /// If the data originates from a different organization than the one who issued the dataset,
    /// this field identifies the original source's legal name.
    origin: Option<Vec<Origin>>,

    /// The geographical location where the data was originally collected, which can be important
    /// for compliance with regional laws and understanding the data's context.
    origin_geography: Vec<OriginGeography>,

    /// The release date of the last version of the dataset, if it has been updated or revised,
    /// to track changes and updates over time.
    previous_date: Option<String>,

    /// Identifies where the metadata for any source datasets that contribute to the current
    /// dataset can be found, establishing lineage and dependencies. This field establishes
    /// lineage.
    source: Option<String>,

    sub_provenance: Option<Box<Provenance>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GenerationMethod {
    code: String,

    description: Option<String>,

    system: Option<String>,
}

/// The span of time during which the data within the dataset was collected or generated,
/// offering insight into the dataset's timeliness and relevance.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GenerationPeriod {
    /// End date/time
    end: Option<String>,

    /// Start date/time
    start: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Origin {
    address: Option<Vec<String>>,

    name: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OriginGeography {
    country: String,

    state: Option<String>,
}

/// This describes a dataset and the source of the dataset.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Source {
    /// Contains a detailed narrative that explains the contents, scope, and purpose of the
    /// dataset. It provides essential contextual information that helps users understand what
    /// the data represents, how it was collected, and any limitations or recommended uses.
    description: String,

    /// A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquely
    /// distinguish it from others, ensuring no confusion or overlap.
    id: String,

    /// The legal entity responsible for creating the dataset, providing accountability and a
    /// point of contact for inquiries.
    issuer: Vec<Issuer>,

    /// The web address where the dataset's metadata is published and can be accessed, providing
    /// a direct link to detailed information about the dataset. Typically will be a unique URL
    /// of the current dataset.
    location: Option<String>,

    /// The official name of the dataset, which should be descriptive and help easily identify
    /// the dataset's content and purpose.
    title: String,

    /// Specifies the version of the schema or standards used to define the metadata for this
    /// dataset, ensuring consistency and compatibility over time.
    version: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Issuer {
    address: Option<Vec<String>>,

    name: String,
}
