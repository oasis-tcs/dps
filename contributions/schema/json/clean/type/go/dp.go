package dp

// The Data Provenance metadata schema is made up of three groups of metadata elements:
// Source, Provenance, and Use.
type DataProtection struct {
	Provenance Provenance `json:"provenance"`
	Source     Source     `json:"source"`
	Use        Use        `json:"use"`
}

// This describes the provenance of the dataset.
type Provenance struct {
	// The date when the dataset was compiled or created, providing a temporal context for the
	// data.
	Date string `json:"date"`
	// Describes the nature of the data within the dataset, such as numerical, textual, or
	// multimedia, helping users understand what kind of information is contained within the
	// file or dataset.
	Format []string `json:"format,omitempty"`
	// The methodology or procedures used to collect, generate, or compile the data, giving
	// insight into its reliability and validity.
	GenerationMethod []GenerationMethod `json:"generation-method"`
	// The span of time during which the data within the dataset was collected or generated,
	// offering insight into the dataset's timeliness and relevance.
	GenerationPeriod *GenerationPeriod `json:"generation-period,omitempty"`
	// If the data originates from a different organization than the one who issued the dataset,
	// this field identifies the original source's legal name.
	Origin []Origin `json:"origin,omitempty"`
	// The geographical location where the data was originally collected, which can be important
	// for compliance with regional laws and understanding the data's context.
	OriginGeography []OriginGeography `json:"origin-geography"`
	// The release date of the last version of the dataset, if it has been updated or revised,
	// to track changes and updates over time.
	PreviousDate *string `json:"previous-date,omitempty"`
	// Identifies where the metadata for any source datasets that contribute to the current
	// dataset can be found, establishing lineage and dependencies. This field establishes
	// lineage.
	Source        *string     `json:"source,omitempty"`
	SubProvenance *Provenance `json:"sub-provenance,omitempty"`
}

type GenerationMethod struct {
	Code        string  `json:"code"`
	Description *string `json:"description,omitempty"`
	System      *string `json:"system,omitempty"`
}

// The span of time during which the data within the dataset was collected or generated,
// offering insight into the dataset's timeliness and relevance.
type GenerationPeriod struct {
	// End date/time
	End *string `json:"end,omitempty"`
	// Start date/time
	Start *string `json:"start,omitempty"`
}

type Origin struct {
	Address []string `json:"address,omitempty"`
	Name    string   `json:"name"`
}

type OriginGeography struct {
	Country string  `json:"country"`
	State   *string `json:"state,omitempty"`
}

// This describes a dataset and the source of the dataset.
type Source struct {
	// Contains a detailed narrative that explains the contents, scope, and purpose of the
	// dataset. It provides essential contextual information that helps users understand what
	// the data represents, how it was collected, and any limitations or recommended uses.
	Description string `json:"description"`
	// A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquely
	// distinguish it from others, ensuring no confusion or overlap.
	ID string `json:"id"`
	// The legal entity responsible for creating the dataset, providing accountability and a
	// point of contact for inquiries.
	Issuer []Issuer `json:"issuer"`
	// The web address where the dataset's metadata is published and can be accessed, providing
	// a direct link to detailed information about the dataset. Typically will be a unique URL
	// of the current dataset.
	Location *string `json:"location,omitempty"`
	// The official name of the dataset, which should be descriptive and help easily identify
	// the dataset's content and purpose.
	Title string `json:"title"`
	// Specifies the version of the schema or standards used to define the metadata for this
	// dataset, ensuring consistency and compatibility over time.
	Version string `json:"version"`
}

type Issuer struct {
	Address []string `json:"address,omitempty"`
	Name    string   `json:"name"`
}

// This group describes legal use and restrictions.
type Use struct {
	// Indicate if the dataset includes data falling into the confidentiality classification.
	// Each classifier must be evaluated as true/false/unknown.
	Classification []Classification `json:"classification,omitempty"`
	// Specifies where consent documentation or agreements related to the data can be found,
	// ensuring legal compliance and regulatory use. This element must be populated when Privacy
	// Consent is appropriate. When populated it points to either one Privacy Consent Policy
	// that all individuals in the dataset agreed to, or one Privacy Policy for each individual
	// in the dataset with that individual's signature.
	Consents []string `json:"consents,omitempty"`
	// Indicates whether the dataset contains proprietary information that is covered with a
	// Copyright and the terms of said Copyright.
	Copyright []string `json:"copyright,omitempty"`
	// Describes the purpose for which the dataset was created, guiding users on its intended
	// use and potential applications against identified use cases. List all that apply from the
	// Data Use codes that apply. Additional codes can be included with descriptions.
	IntendedPurpose []IntendedPurpose `json:"intended-purpose"`
	// Details the location or point of contact for identifying the terms under which the
	// dataset can be used, including any restrictions or obligations, clarifying legal use and
	// distribution rights. License may be an End User License Agreement (EULA), subject to Data
	// Use Agreement (DUA).
	License []string `json:"license,omitempty"`
	// Indicates whether the dataset contains proprietary information that is covered with a
	// Patent and said Patent number.
	Patent []string `json:"patent,omitempty"`
	// Indicates whether techniques were used to protect personally identifiable information
	// (PII) or sensitive personal information (SPI), highlighting the dataset's privacy
	// considerations.
	PrivacyEnhancing []PrivacyEnhancing `json:"privacy-enhancing,omitempty"`
	// Defines the geographical boundaries within which the data cannot be processed, often for
	// legal or regulatory reasons.
	ProcessingExcluded []ProcessingExcluded `json:"processing-excluded,omitempty"`
	// Defines the geographical boundaries within which the data can be processed, often for
	// legal or regulatory reasons.
	ProcessingIncluded []ProcessingIncluded `json:"processing-included,omitempty"`
	// Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
	StorageAllowed []StorageAllowed `json:"storage-allowed,omitempty"`
	// Specifies where the data may not be stored, crucial for compliance with data sovereignty
	// laws.
	StorageForbidden []StorageForbidden `json:"storage-forbidden,omitempty"`
	// Indicates whether the dataset contains proprietary information that is covered with a
	// Trademark, and the terms of said Trademark.
	Trademark []string `json:"trademark,omitempty"`
}

type Classification struct {
	Evaluated  bool       `json:"evaluated"`
	Regulation Regulation `json:"regulation"`
	Tool       *string    `json:"tool,omitempty"`
}

type Regulation struct {
	Code        string  `json:"code"`
	Description *string `json:"description,omitempty"`
	System      *string `json:"system,omitempty"`
}

type IntendedPurpose struct {
	Code        string  `json:"code"`
	Description string  `json:"description"`
	System      *string `json:"system,omitempty"`
}

type PrivacyEnhancing struct {
	Parameters   []string      `json:"parameters,omitempty"`
	Result       []string      `json:"result,omitempty"`
	ToolCategory *ToolCategory `json:"tool-category,omitempty"`
	ToolUsed     *string       `json:"tool-used,omitempty"`
}

type ToolCategory struct {
	Code        string  `json:"code"`
	Description *string `json:"description,omitempty"`
	System      *string `json:"system,omitempty"`
}

type ProcessingExcluded struct {
	Country string  `json:"country"`
	State   *string `json:"state,omitempty"`
}

type ProcessingIncluded struct {
	Country string  `json:"country"`
	State   *string `json:"state,omitempty"`
}

type StorageAllowed struct {
	Country string  `json:"country"`
	State   *string `json:"state,omitempty"`
}

type StorageForbidden struct {
	Country string  `json:"country"`
	State   *string `json:"state,omitempty"`
}
