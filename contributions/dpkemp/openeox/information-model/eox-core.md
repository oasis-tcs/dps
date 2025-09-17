         title: "EoX Information - Core"
       package: "https://docs.oasis-open.org/openeox/v1.0/schema/core/"
   description: "The schema for representing End-of-Life (EoL), End-of-Security-Support (EoSSec) and other End-of information in OpenEoX."
         roots: ["Root"]
        config: {"$MaxString": 1000, "$TypeName": "^[a-zA-Z][-._A-Za-z0-9]{0,63}$", "$FieldName": "^[$a-z][-_$A-Za-z0-9]{0,63}$"}
  jadn_version: "http://oasis-open.org/openc2/jadn/v2.0/schema/"

The schema for representing End-of-Life (EoL), End-of-Security-Support (EoSSec) and other End-of information in OpenEoX.

**Type: Root (Record)**

| ID | Name                        | Type            | \#   | Description                                                                                                         |
|----|-----------------------------|-----------------|------|---------------------------------------------------------------------------------------------------------------------|
| 1  | **$schema**                 | String          | 1    | Specifies the schema the JSON object must be valid against.                                                         |
| 2  | **end_of_life**             | eox_timestamp_t | 1    | Indicates the last day when the particular product is officially supported in any way by the vendor.                |
| 3  | **end_of_sales**            | eox_timestamp_t | 0..1 | Indicates the last day when a particular product may be ordered by customers from vendor sales channels.            |
| 4  | **end_of_security_support** | eox_timestamp_t | 1    | Indicates the last day when the vendor has committed to providing security remediations for the particular product. |
| 5  | **last_updated**            | String          | 1    | Contains the RFC 3339 timestamp when the record was last updated.                                                   |

**********

| Type Name           | Type Definition | Description                                                                                                                    |
|---------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| **eox_timestamp_t** | String          | Contains the timestamp at which the product reaches the specified stage or the indicator that this is still 'to be announced'. |

**********
