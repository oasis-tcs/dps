-module(dp).

-export_type([regulation/0]).
-record(regulation, {
    code :: string(),
    description :: string() | undefined,
    system :: string() | undefined
}).

-type regulation() :: #regulation{
    code :: string(),
    description :: string() | undefined,
    system :: string() | undefined
}.

-export_type([classification/0]).
%% - `classification` - Indicate if the dataset includes data falling into the confidentiality classification. Each classifier must be evaluated as true/false/unknown.
-record(classification, {
    evaluated :: boolean(),
    regulation :: regulation:t(),
    tool :: string() | undefined
}).
-type classification() :: #classification{
    evaluated :: boolean(),
    regulation :: regulation:t(),
    tool :: string() | undefined
}.

-export_type([intended_purpose/0]).
%% - `intended_purpose` - Describes the purpose for which the dataset was created, guiding users on its intended use and potential applications against identified use cases. List all that apply from the Data Use codes that apply. Additional codes can be included with descriptions.
-record(intended_purpose, {
    code :: string(),
    description :: string(),
    system :: string() | undefined
}).
-type intended_purpose() :: #intended_purpose{
    code :: string(),
    description :: string(),
    system :: string() | undefined
}.

-export_type([tool_category/0]).
-record(tool_category, {
    code :: string(),
    description :: string() | undefined,
    system :: string() | undefined
}).

-type tool_category() :: #tool_category{
    code :: string(),
    description :: string() | undefined,
    system :: string() | undefined
}.

-export_type([privacy_enhancing/0]).
%% - `privacy_enhancing` - Indicates whether techniques were used to protect personally identifiable information (PII) or sensitive personal information (SPI), highlighting the dataset's privacy considerations.
-record(privacy_enhancing, {
    parameters :: [string()] | undefined,
    result :: [string()] | undefined,
    tool_category :: tool_category:t() | undefined,
    tool_used :: string()
}).

-type privacy_enhancing() :: #privacy_enhancing{
    parameters :: [string()] | undefined,
    result :: [string()] | undefined,
    tool_category :: tool_category:t() | undefined,
    tool_used :: string()
}.

-export_type([processing_excluded/0]).
%% - `processing_excluded` - Defines the geographical boundaries within which the data cannot be processed, often for legal or regulatory reasons.
-record(processing_excluded, {
    country :: string(),
    state :: string() | undefined
}).

-type processing_excluded() :: #processing_excluded{
    country :: string(),
    state :: string() | undefined
}.

-export_type([processing_included/0]).
%% - `processing_included` - Defines the geographical boundaries within which the data can be processed, often for legal or regulatory reasons.
-record(processing_included, {
    country :: string(),
    state :: string() | undefined
}).

-type processing_included() :: #processing_included{
    country :: string(),
    state :: string() | undefined
}.

-export_type([storage_allowed/0]).
%% - `storage_allowed` - Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
-record(storage_allowed, {
    country :: string(),
    state :: string() | undefined
}).

-type storage_allowed() :: #storage_allowed{
    country :: string(),
    state :: string() | undefined
}.

-export_type([storage_forbidden/0]).
%% - `storage_forbidden` - Specifies where the data may not be stored, crucial for compliance with data sovereignty laws.
-record(storage_forbidden, {
    country :: string(),
    state :: string() | undefined
}).

-type storage_forbidden() :: #storage_forbidden{
    country :: string(),
    state :: string() | undefined
}.

-export_type([use_class/0]).
%% This group describes legal use and restrictions.
%% - `classification` - Indicate if the dataset includes data falling into the confidentiality classification. Each classifier must be evaluated as true/false/unknown.
%% - `consents` - Specifies where consent documentation or agreements related to the data can be found, ensuring legal compliance and regulatory use. This element must be populated when PrivacyConsent is appropriate. When populated it points to either one Privacy Consent Policy that all individuals in the dataset agreed to, or one Privacy Policy for each individual in the dataset with that individual's signature.
%% - `copyright` - Indicates whether the dataset contains proprietary information that is covered with a Copyright and the terms of said Copyright.
%% - `intended_purpose` - Describes the purpose for which the dataset was created, guiding users on its intended use and potential applications against identified use cases. List all that apply from the Data Use codes that apply. Additional codes can be included with descriptions.
%% - `license` - Details the location or point of contact for identifying the terms under which the dataset can be used, including any restrictions or obligations, clarifying legal use and distribution rights. License may be an End User License Agreement (EULA), subject to Data Use Agreement (DUA).
%% - `patent` - Indicates whether the dataset contains proprietary information that is covered with a Patent and said Patent number.
%% - `privacy_enhancing` - Indicates whether techniques were used to protect personally identifiable information (PII) or sensitive personal information (SPI), highlighting the dataset's privacy considerations.
%% - `processing_excluded` - Defines the geographical boundaries within which the data cannot be processed, often for legal or regulatory reasons.
%% - `processing_included` - Defines the geographical boundaries within which the data can be processed, often for legal or regulatory reasons.
%% - `storage_allowed` - Specifies where the data may be stored, crucial for compliance with data sovereignty laws.
%% - `storage_forbidden` - Specifies where the data may not be stored, crucial for compliance with data sovereignty laws.
%% - `trademark` - Indicates whether the dataset contains proprietary information that is covered with a Trademark, and the terms of said Trademark.

-record(use_class, {
    classification :: [classification()] | undefined,
    consents :: [string()] | undefined,
    copyright :: [string()] | undefined,
    intended_purpose :: [intended_purpose()],
    license :: [string()] | undefined,
    patent :: [string()] | undefined,
    privacy_enhancing :: [privacy_enhancing()] | undefined,
    processing_excluded :: [processing_excluded()] | undefined,
    processing_included :: [processing_included()] | undefined,
    storage_allowed :: [storage_allowed()] | undefined,
    storage_forbidden :: [storage_forbidden()] | undefined,
    trademark :: [string()] | undefined
}).

-type use_class() :: #use_class{}.

-export_type([generation_method/0]).
%%  - `:generation_method` - The methodology or procedures used to collect, generate, or compile the data, givinginsight into its reliability and validity.
-record(generation_method, {
    code :: string(),
    description :: string() | undefined,
    system :: string() | undefined
}).

-type generation_method() :: #generation_method{}.

-export_type([generation_period/0]).
%% The span of time during which the data within the dataset was collected or generated,
%% offering insight into the dataset's timeliness and relevance.
%% - `generation_period_end` - End date/time
%% - `start` - Start date/time

-record(generation_period, {
    generation_period_end :: string() | undefined,
    start :: string() | undefined
}).

-type generation_period() :: #generation_period{}.

-export_type([origin/0]).
-record(origin, {
    address :: [string()] | undefined,
    name :: string()
}).

-type origin() :: #origin{}.

-export_type([origin_geography/0]).
%%  - `:origin_geography` - The geographical location where the data was originally collected, which can be importantfor compliance with regional laws and understanding the data's context.
-record(origin_geography, {
    country :: string(),
    state :: string() | undefined
}).

-type origin_geography() :: #origin_geography{}.

-export_type([provenance/0]).
%%  This describes the provenance of the dataset.
%%  - `:date` - The date when the dataset was compiled or created, providing a temporal context for thedata.
%%  - `:format` - Describes the nature of the data within the dataset, such as numerical, textual, ormultimedia, helping users understand what kind of information is contained within thefile or dataset.
%%  - `:generation_method` - The methodology or procedures used to collect, generate, or compile the data, givinginsight into its reliability and validity.
%%  - `:generation_period` - The span of time during which the data within the dataset was collected or generated,offering insight into the dataset's timeliness and relevance.
%%  - `:origin` - If the data originates from a different organization than the one who issued the dataset,this field identifies the original source's legal name.
%%  - `:origin_geography` - The geographical location where the data was originally collected, which can be importantfor compliance with regional laws and understanding the data's context.
%%  - `:previous_date` - The release date of the last version of the dataset, if it has been updated or revised,to track changes and updates over time.
%%  - `:source` - Identifies where the metadata for any source datasets that contribute to the currentdataset can be found, establishing lineage and dependencies. This field establisheslineage.

-type provenance() :: #{
    date := string(),
    format => [string()] | undefined,
    generation_method := [generation_method()],
    generation_period => generation_period() | undefined,
    origin => [origin:t()] | undefined,
    origin_geography := [origin_geography()],
    previous_date => string() | undefined,
    source => string() | undefined,
    sub_provenance => provenance() | undefined
}.

-export_type([issuer/0]).
%%  - `:issuer` - The legal entity responsible for creating the dataset, providing accountability and apoint of contact for inquiries.
-type issuer() :: #{
    address => [string()] | undefined,
    name := string()
}.

-export_type([source/0]).
%%  This describes a dataset and the source of the dataset.
%%  - `:description` - Contains a detailed narrative that explains the contents, scope, and purpose of thedataset. It provides essential contextual information that helps users understand whatthe data represents, how it was collected, and any limitations or recommended uses.
%%  - `:id` - A distinct identifier (such as a UUID) assigned to the dataset's metadata to uniquelydistinguish it from others, ensuring no confusion or overlap.
%%  - `:issuer` - The legal entity responsible for creating the dataset, providing accountability and apoint of contact for inquiries.
%%  - `:location` - The web address where the dataset's metadata is published and can be accessed, providinga direct link to detailed information about the dataset. Typically will be a unique URLof the current dataset.
%%  - `:title` - The official name of the dataset, which should be descriptive and help easily identifythe dataset's content and purpose.
%%  - `:version` - Specifies the version of the schema or standards used to define the metadata for thisdataset, ensuring consistency and compatibility over time.

-type source() :: #{
    description := string(),
    id := string(),
    issuer := [issuer:t()],
    location => string() | undefined,
    title := string(),
    version := string()
}.

-export_type([data_provenance/0]).
%%  The Data Provenance metadata schema is made up of three groups of metadata elements:
%%  Source, Provenance, and Use.

-type data_provenance() :: #{
    provenance := provenance(),
    source := source(),
    data_provenance_use := use_class()
}.
