defmodule Regulation do
  @enforce_keys [:code]
  defstruct [:code, :description, :system]

  @type t :: %__MODULE__{
          code: String.t(),
          description: String.t() | nil,
          system: String.t() | nil
        }
end

defmodule Classification do
  @enforce_keys [:evaluated, :regulation]
  defstruct [:evaluated, :regulation, :tool]

  @type t :: %__MODULE__{
          evaluated: boolean(),
          regulation: Regulation.t(),
          tool: String.t() | nil
        }
end

defmodule IntendedPurpose do
  @enforce_keys [:code, :description]
  defstruct [:code, :description, :system]

  @type t :: %__MODULE__{
          code: String.t(),
          description: String.t(),
          system: String.t() | nil
        }
end

defmodule ToolCategory do
  @enforce_keys [:code]
  defstruct [:code, :description, :system]

  @type t :: %__MODULE__{
          code: String.t(),
          description: String.t() | nil,
          system: String.t() | nil
        }
end

defmodule PrivacyEnhancing do
  @enforce_keys [:tool_used]
  defstruct [:parameters, :result, :tool_category, :tool_used]

  @type t :: %__MODULE__{
          parameters: [String.t()] | nil,
          result: [String.t()] | nil,
          tool_category: ToolCategory.t() | nil,
          tool_used: String.t()
        }
end

defmodule ProcessingExcluded do
  @enforce_keys [:country]
  defstruct [:country, :state]

  @type t :: %__MODULE__{
          country: String.t(),
          state: String.t() | nil
        }
end

defmodule ProcessingIncluded do
  @enforce_keys [:country]
  defstruct [:country, :state]

  @type t :: %__MODULE__{
          country: String.t(),
          state: String.t() | nil
        }
end

defmodule StorageAllowed do
  @enforce_keys [:country]
  defstruct [:country, :state]

  @type t :: %__MODULE__{
          country: String.t(),
          state: String.t() | nil
        }
end

defmodule StorageForbidden do
  @enforce_keys [:country]
  defstruct [:country, :state]

  @type t :: %__MODULE__{
          country: String.t(),
          state: String.t() | nil
        }
end

defmodule UseClass do
  @moduledoc """
  This group describes legal use and restrictions.
  - `:classification` - Indicate if the dataset includes data falling into the confidentiality classification.Each classifier must be evaluated as true/false/unknown.
  - `:consents` - Specifies where consent documentation or agreements related to the data can be found,ensuring legal compliance and regulatory use. This element must be populated when PrivacyConsent is appropriate. When populated it points to either one Privacy Consent Policythat all individuals in the dataset agreed to, or one Privacy Policy for each individualin the dataset with that individual's signature.
  - `:copyright` - Indicates whether the dataset contains proprietary information that is covered with aCopyright and the terms of said Copyright.
  - `:intended_purpose` - Describes the purpose for which the dataset was created, guiding users on its intendeduse and potential applications against identified use cases. List all that apply from theData Use codes that apply. Additional codes can be included with descriptions.
  - `:license` - Details the location or point of contact for identifying the terms under which thedataset can be used, including any restrictions or obligations, clarifying legal use anddistribution rights. License may be an End User License Agreement (EULA), subject to DataUse Agreement (DUA).
  - `:patent` - Indicates whether the dataset contains proprietary information that is covered with aPatent and said Patent number.
  - `:privacy_enhancing` - Indicates whether techniques were used to protect personally identifiable information(PII) or sensitive personal information (SPI), highlighting the dataset's privacyconsiderations.
  - `:processing_excluded` - Defines the geographical boundaries within which the data cannot be processed, often forlegal or regulatory reasons.
  - `:processing_included` - Defines the geographical boundaries within which the data can be processed, often forlegal or regulatory reasons.
  - `:storage_allowed` - Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
  - `:storage_forbidden` - Specifies where the data may not be stored, crucial for compliance with data sovereigntylaws.
  - `:trademark` - Indicates whether the dataset contains proprietary information that is covered with aTrademark, and the terms of said Trademark.
  """

  @enforce_keys [:intended_purpose]
  defstruct [
    :classification,
    :consents,
    :copyright,
    :intended_purpose,
    :license,
    :patent,
    :privacy_enhancing,
    :processing_excluded,
    :processing_included,
    :storage_allowed,
    :storage_forbidden,
    :trademark
  ]

  @type t :: %__MODULE__{
          classification: [Classification.t()] | nil,
          consents: [String.t()] | nil,
          copyright: [String.t()] | nil,
          intended_purpose: [IntendedPurpose.t()],
          license: [String.t()] | nil,
          patent: [String.t()] | nil,
          privacy_enhancing: [PrivacyEnhancing.t()] | nil,
          processing_excluded: [ProcessingExcluded.t()] | nil,
          processing_included: [ProcessingIncluded.t()] | nil,
          storage_allowed: [StorageAllowed.t()] | nil,
          storage_forbidden: [StorageForbidden.t()] | nil,
          trademark: [String.t()] | nil
        }
end

defmodule GenerationMethod do
  @enforce_keys [:code]
  defstruct [:code, :description, :system]

  @type t :: %__MODULE__{
          code: String.t(),
          description: String.t() | nil,
          system: String.t() | nil
        }
end

defmodule GenerationPeriod do
  @moduledoc """
  The span of time during which the data within the dataset was collected or generated,
  offering insight into the dataset's timeliness and relevance.
  - `:generation_period_end` - End date/time
  - `:start` - Start date/time
  """

  defstruct [:generation_period_end, :start]

  @type t :: %__MODULE__{
          generation_period_end: String.t() | nil,
          start: String.t() | nil
        }
end

defmodule Origin do
  @enforce_keys [:name]
  defstruct [:address, :name]

  @type t :: %__MODULE__{
          address: [String.t()] | nil,
          name: String.t()
        }
end

defmodule OriginGeography do
  @enforce_keys [:country]
  defstruct [:country, :state]

  @type t :: %__MODULE__{
          country: String.t(),
          state: String.t() | nil
        }
end

defmodule Provenance do
  @moduledoc """
  This describes the provenance of the dataset.
  - `:date` - The date when the dataset was compiled or created, providing a temporal context for thedata.
  - `:format` - Describes the nature of the data within the dataset, such as numerical, textual, ormultimedia, helping users understand what kind of information is contained within thefile or dataset.
  - `:generation_method` - The methodology or procedures used to collect, generate, or compile the data, givinginsight into its reliability and validity.
  - `:generation_period` - The span of time during which the data within the dataset was collected or generated,offering insight into the dataset's timeliness and relevance.
  - `:origin` - If the data originates from a different organization than the one who issued the dataset,this field identifies the original source's legal name.
  - `:origin_geography` - The geographical location where the data was originally collected, which can be importantfor compliance with regional laws and understanding the data's context.
  - `:previous_date` - The release date of the last version of the dataset, if it has been updated or revised,to track changes and updates over time.
  - `:source` - Identifies where the metadata for any source datasets that contribute to the currentdataset can be found, establishing lineage and dependencies. This field establisheslineage.
  """

  @enforce_keys [:date, :generation_method, :origin_geography]
  defstruct [
    :date,
    :format,
    :generation_method,
    :generation_period,
    :origin,
    :origin_geography,
    :previous_date,
    :source,
    :sub_provenance
  ]

  @type t :: %__MODULE__{
          date: String.t(),
          format: [String.t()] | nil,
          generation_method: [GenerationMethod.t()],
          generation_period: GenerationPeriod.t() | nil,
          origin: [Origin.t()] | nil,
          origin_geography: [OriginGeography.t()],
          previous_date: String.t() | nil,
          source: String.t() | nil,
          sub_provenance: Provenance.t() | nil
        }
end

defmodule Issuer do
  @enforce_keys [:name]
  defstruct [:address, :name]

  @type t :: %__MODULE__{
          address: [String.t()] | nil,
          name: String.t()
        }
end

defmodule Source do
  @moduledoc """
  This describes a dataset and the source of the dataset.
  - `:description` - Contains a detailed narrative that explains the contents, scope, and purpose of thedataset. It provides essential contextual information that helps users understand whatthe data represents, how it was collected, and any limitations or recommended uses.
  - `:id` - A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquelydistinguish it from others, ensuring no confusion or overlap.
  - `:issuer` - The legal entity responsible for creating the dataset, providing accountability and apoint of contact for inquiries.
  - `:location` - The web address where the dataset's metadata is published and can be accessed, providinga direct link to detailed information about the dataset. Typically will be a unique URLof the current dataset.
  - `:title` - The official name of the dataset, which should be descriptive and help easily identifythe dataset's content and purpose.
  - `:version` - Specifies the version of the schema or standards used to define the metadata for thisdataset, ensuring consistency and compatibility over time.
  """

  @enforce_keys [:description, :id, :issuer, :title, :version]
  defstruct [:description, :id, :issuer, :location, :title, :version]

  @type t :: %__MODULE__{
          description: String.t(),
          id: String.t(),
          issuer: [Issuer.t()],
          location: String.t() | nil,
          title: String.t(),
          version: String.t()
        }
end

defmodule DataProvenance do
  @moduledoc """
  The Data Provenance metadata schema is made up of three groups of metadata elements:
  Source, Provenance, and Use.
  """

  @enforce_keys [:provenance, :source, :data_provenance_use]
  defstruct [:provenance, :source, :data_provenance_use]

  @type t :: %__MODULE__{
          provenance: Provenance.t(),
          source: Source.t(),
          data_provenance_use: UseClass.t()
        }
end
