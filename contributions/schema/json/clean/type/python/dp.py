from dataclasses import dataclass


@dataclass
class GenerationMethod:
    code: str
    description: str | None = None
    system: str | None = None


@dataclass
class GenerationPeriod:
    """The span of time during which the data within the dataset was collected or generated,
    offering insight into the dataset's timeliness and relevance.
    """

    end: str | None = None
    """End date/time"""

    start: str | None = None
    """Start date/time"""


@dataclass
class Origin:
    name: str
    address: list[str] | None = None


@dataclass
class OriginGeography:
    country: str
    state: str | None = None


@dataclass
class Provenance:
    """This describes the provenance of the dataset."""

    date: str
    """The date when the dataset was compiled or created, providing a temporal context for the
    data.
    """
    generation_method: list[GenerationMethod]
    """The methodology or procedures used to collect, generate, or compile the data, giving
    insight into its reliability and validity.
    """
    origin_geography: list[OriginGeography]
    """The geographical location where the data was originally collected, which can be important
    for compliance with regional laws and understanding the data's context.
    """
    format: list[str] | None = None
    """Describes the nature of the data within the dataset, such as numerical, textual, or
    multimedia, helping users understand what kind of information is contained within the
    file or dataset.
    """
    generation_period: GenerationPeriod | None = None
    """The span of time during which the data within the dataset was collected or generated,
    offering insight into the dataset's timeliness and relevance.
    """
    origin: list[Origin] | None = None
    """If the data originates from a different organization than the one who issued the dataset,
    this field identifies the original source's legal name.
    """
    previous_date: str | None = None
    """The release date of the last version of the dataset, if it has been updated or revised,
    to track changes and updates over time.
    """
    source: str | None = None
    """Identifies where the metadata for any source datasets that contribute to the current
    dataset can be found, establishing lineage and dependencies. This field establishes
    lineage.
    """
    sub_provenance: "Provenance" | None = (
        None  # Note: Optional Forward Reference to Provenance
    )


@dataclass
class Issuer:
    name: str
    address: list[str] | None = None


@dataclass
class Source:
    """This describes a dataset and the source of the dataset."""

    description: str
    """Contains a detailed narrative that explains the contents, scope, and purpose of the
    dataset. It provides essential contextual information that helps users understand what
    the data represents, how it was collected, and any limitations or recommended uses.
    """
    id: str
    """A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquely
    distinguish it from others, ensuring no confusion or overlap.
    """
    issuer: list[Issuer]
    """The legal entity responsible for creating the dataset, providing accountability and a
    point of contact for inquiries.
    """
    title: str
    """The official name of the dataset, which should be descriptive and help easily identify
    the dataset's content and purpose.
    """
    version: str
    """Specifies the version of the schema or standards used to define the metadata for this
    dataset, ensuring consistency and compatibility over time.
    """
    location: str | None = None
    """The web address where the dataset's metadata is published and can be accessed, providing
    a direct link to detailed information about the dataset. Typically will be a unique URL
    of the current dataset.
    """


@dataclass
class Regulation:
    code: str
    description: str | None = None
    system: str | None = None


@dataclass
class Classification:
    evaluated: bool
    regulation: Regulation
    tool: str | None = None


@dataclass
class IntendedPurpose:
    code: str
    description: str
    system: str | None = None


@dataclass
class ToolCategory:
    code: str
    description: str | None = None
    system: str | None = None


@dataclass
class PrivacyEnhancing:
    parameters: list[str] | None = None
    result: list[str] | None = None
    tool_category: ToolCategory | None = None
    tool_used: str | None = None


@dataclass
class ProcessingExcluded:
    country: str
    state: str | None = None


@dataclass
class ProcessingIncluded:
    country: str
    state: str | None = None


@dataclass
class StorageAllowed:
    country: str
    state: str | None = None


@dataclass
class StorageForbidden:
    country: str
    state: str | None = None


@dataclass
class Use:
    """This group describes legal use and restrictions."""

    intended_purpose: list[IntendedPurpose]
    """Describes the purpose for which the dataset was created, guiding users on its intended
    use and potential applications against identified use cases. List all that apply from the
    Data Use codes that apply. Additional codes can be included with descriptions.
    """
    classification: list[Classification] | None = None
    """Indicate if the dataset includes data falling into the confidentiality classification.
    Each classifier must be evaluated as true/false/unknown.
    """
    consents: list[str] | None = None
    """Specifies where consent documentation or agreements related to the data can be found,
    ensuring legal compliance and regulatory use. This element must be populated when Privacy
    Consent is appropriate. When populated it points to either one Privacy Consent Policy
    that all individuals in the dataset agreed to, or one Privacy Policy for each individual
    in the dataset with that individual's signature.
    """
    copyright: list[str] | None = None
    """Indicates whether the dataset contains proprietary information that is covered with a
    Copyright and the terms of said Copyright.
    """
    license: list[str] | None = None
    """Details the location or point of contact for identifying the terms under which the
    dataset can be used, including any restrictions or obligations, clarifying legal use and
    distribution rights. License may be an End User License Agreement (EULA), subject to Data
    Use Agreement (DUA).
    """
    patent: list[str] | None = None
    """Indicates whether the dataset contains proprietary information that is covered with a
    Patent and said Patent number.
    """
    privacy_enhancing: list[PrivacyEnhancing] | None = None
    """Indicates whether techniques were used to protect personally identifiable information
    (PII) or sensitive personal information (SPI), highlighting the dataset's privacy
    considerations.
    """
    processing_excluded: list[ProcessingExcluded] | None = None
    """Defines the geographical boundaries within which the data cannot be processed, often for
    legal or regulatory reasons.
    """
    processing_included: list[ProcessingIncluded] | None = None
    """Defines the geographical boundaries within which the data can be processed, often for
    legal or regulatory reasons.
    """
    storage_allowed: list[StorageAllowed] | None = None
    """Specifies where the data may be stored, crucial for compliance with data sovereignty laws."""

    storage_forbidden: list[StorageForbidden] | None = None
    """Specifies where the data may not be stored, crucial for compliance with data sovereignty
    laws.
    """
    trademark: list[str] | None = None
    """Indicates whether the dataset contains proprietary information that is covered with a
    Trademark, and the terms of said Trademark.
    """


@dataclass
class DataProtection:
    """The Data Provenance metadata schema is made up of three groups of metadata elements:
    Source, Provenance, and Use.
    """

    provenance: Provenance
    source: Source
    use: Use
