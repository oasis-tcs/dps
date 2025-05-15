require 'json'
require 'dry-types'
require 'dry-struct'

module Types
  include Dry.Types(default: :nominal)

  Bool   = Strict::Bool
  Hash   = Strict::Hash
  String = Strict::String
end

class GenerationMethod < Dry::Struct
  attribute :code,                     Types::String
  attribute :description,              Types::String.optional
  attribute :generation_method_system, Types::String.optional
end

# The span of time during which the data within the dataset was collected or generated,
# offering insight into the dataset's timeliness and relevance.
class GenerationPeriod < Dry::Struct

  # End date/time
  attribute :generation_period_end, Types::String.optional

  # Start date/time
  attribute :start, Types::String.optional
end

class Origin < Dry::Struct
  attribute :address,     Types.Array(Types::String).optional
  attribute :origin_name, Types::String
end

class OriginGeography < Dry::Struct
  attribute :country, Types::String
  attribute :state,   Types::String.optional
end

# This describes the provenance of the dataset.
class Provenance < Dry::Struct

  # The date when the dataset was compiled or created, providing a temporal context for the
  # data.
  attribute :date, Types::String

  # Describes the nature of the data within the dataset, such as numerical, textual, or
  # multimedia, helping users understand what kind of information is contained within the
  # file or dataset.
  attribute :provenance_format, Types.Array(Types::String).optional

  # The methodology or procedures used to collect, generate, or compile the data, giving
  # insight into its reliability and validity.
  attribute :generation_method, Types.Array(GenerationMethod)

  # The span of time during which the data within the dataset was collected or generated,
  # offering insight into the dataset's timeliness and relevance.
  attribute :generation_period, GenerationPeriod.optional

  # If the data originates from a different organization than the one who issued the dataset,
  # this field identifies the original source's legal name.
  attribute :origin, Types.Array(Origin).optional

  # The geographical location where the data was originally collected, which can be important
  # for compliance with regional laws and understanding the data's context.
  attribute :origin_geography, Types.Array(OriginGeography)

  # The release date of the last version of the dataset, if it has been updated or revised,
  # to track changes and updates over time.
  attribute :previous_date, Types::String.optional

  # Identifies where the metadata for any source datasets that contribute to the current
  # dataset can be found, establishing lineage and dependencies. This field establishes
  # lineage.
  attribute :source, Types::String.optional

  attribute :sub_provenance, Provenance.optional
end

class Issuer < Dry::Struct
  attribute :address,     Types.Array(Types::String).optional
  attribute :issuer_name, Types::String
end

# This describes a dataset and the source of the dataset.
class Source < Dry::Struct

  # Contains a detailed narrative that explains the contents, scope, and purpose of the
  # dataset. It provides essential contextual information that helps users understand what
  # the data represents, how it was collected, and any limitations or recommended uses.
  attribute :description, Types::String

  # A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquely
  # distinguish it from others, ensuring no confusion or overlap.
  attribute :id, Types::String

  # The legal entity responsible for creating the dataset, providing accountability and a
  # point of contact for inquiries.
  attribute :issuer, Types.Array(Issuer)

  # The web address where the dataset's metadata is published and can be accessed, providing
  # a direct link to detailed information about the dataset. Typically will be a unique URL
  # of the current dataset.
  attribute :location, Types::String.optional

  # The official name of the dataset, which should be descriptive and help easily identify
  # the dataset's content and purpose.
  attribute :title, Types::String

  # Specifies the version of the schema or standards used to define the metadata for this
  # dataset, ensuring consistency and compatibility over time.
  attribute :version, Types::String
end

class Regulation < Dry::Struct
  attribute :code,              Types::String
  attribute :description,       Types::String.optional
  attribute :regulation_system, Types::String.optional
end

class Classification < Dry::Struct
  attribute :evaluated,  Types::Bool
  attribute :regulation, Regulation
  attribute :tool,       Types::String.optional
end

class IntendedPurpose < Dry::Struct
  attribute :code,                    Types::String
  attribute :description,             Types::String
  attribute :intended_purpose_system, Types::String.optional
end

class ToolCategory < Dry::Struct
  attribute :code,                 Types::String
  attribute :description,          Types::String.optional
  attribute :tool_category_system, Types::String.optional
end

class PrivacyEnhancing < Dry::Struct
  attribute :parameters,    Types.Array(Types::String).optional
  attribute :result,        Types.Array(Types::String).optional
  attribute :tool_category, ToolCategory.optional
  attribute :tool_used,     Types::String
end

class ProcessingExcluded < Dry::Struct
  attribute :country, Types::String
  attribute :state,   Types::String.optional
end

class ProcessingIncluded < Dry::Struct
  attribute :country, Types::String
  attribute :state,   Types::String.optional
end

class StorageAllowed < Dry::Struct
  attribute :country, Types::String
  attribute :state,   Types::String.optional
end

class StorageForbidden < Dry::Struct
  attribute :country, Types::String
  attribute :state,   Types::String.optional
end

# This group describes legal use and restrictions.
class Use < Dry::Struct

  # Indicate if the dataset includes data falling into the confidentiality classification.
  # Each classifier must be evaluated as true/false/unknown.
  attribute :classification, Types.Array(Classification).optional

  # Specifies where consent documentation or agreements related to the data can be found,
  # ensuring legal compliance and regulatory use. This element must be populated when Privacy
  # Consent is appropriate. When populated it points to either one Privacy Consent Policy
  # that all individuals in the dataset agreed to, or one Privacy Policy for each individual
  # in the dataset with that individual's signature.
  attribute :consents, Types.Array(Types::String).optional

  # Indicates whether the dataset contains proprietary information that is covered with a
  # Copyright and the terms of said Copyright.
  attribute :copyright, Types.Array(Types::String).optional

  # Describes the purpose for which the dataset was created, guiding users on its intended
  # use and potential applications against identified use cases. List all that apply from the
  # Data Use codes that apply. Additional codes can be included with descriptions.
  attribute :intended_purpose, Types.Array(IntendedPurpose)

  # Details the location or point of contact for identifying the terms under which the
  # dataset can be used, including any restrictions or obligations, clarifying legal use and
  # distribution rights. License may be an End User License Agreement (EULA), subject to Data
  # Use Agreement (DUA).
  attribute :license, Types.Array(Types::String).optional

  # Indicates whether the dataset contains proprietary information that is covered with a
  # Patent and said Patent number.
  attribute :patent, Types.Array(Types::String).optional

  # Indicates whether techniques were used to protect personally identifiable information
  # (PII) or sensitive personal information (SPI), highlighting the dataset's privacy
  # considerations.
  attribute :privacy_enhancing, Types.Array(PrivacyEnhancing).optional

  # Defines the geographical boundaries within which the data cannot be processed, often for
  # legal or regulatory reasons.
  attribute :processing_excluded, Types.Array(ProcessingExcluded).optional

  # Defines the geographical boundaries within which the data can be processed, often for
  # legal or regulatory reasons.
  attribute :processing_included, Types.Array(ProcessingIncluded).optional

  # Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
  attribute :storage_allowed, Types.Array(StorageAllowed).optional

  # Specifies where the data may not be stored, crucial for compliance with data sovereignty
  # laws.
  attribute :storage_forbidden, Types.Array(StorageForbidden).optional

  # Indicates whether the dataset contains proprietary information that is covered with a
  # Trademark, and the terms of said Trademark.
  attribute :trademark, Types.Array(Types::String).optional
end

# The Data Provenance metadata schema is made up of three groups of metadata elements:
# Source, Provenance, and Use.
class DataProvenance < Dry::Struct
  attribute :provenance, Provenance
  attribute :source,     Source
  attribute :use,        Use
end
