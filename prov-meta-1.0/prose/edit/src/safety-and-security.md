# Safety, Security, and Data Protection {#safety-security-and-data-protection}

All safety, security, and data protection requirements relevant to the context in which Data Provenance Metadata documents are used MUST be translated into, and consistently enforced through, Data Provenance Metadata implementations and processes.

For Data Provenance Metadata documents based on JSON, the security considerations of [cite](#RFC8259) apply and are repeated here as a service for the reader:

> Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
> Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts
> (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).
> This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.
> The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to
> that language's syntax.

Implementations SHOULD validate Data Provenance Metadata documents against the normative JSON Schema prior to processing.
Documents that do not validate MUST NOT be treated as authoritative provenance records.

## Integrity and Authenticity of Provenance Claims {#integrity-and-authenticity}

This specification defines the structure and vocabulary of provenance metadata but does not define mechanisms for verifying that the claims made within a record are accurate or have not been tampered with.
A Data Provenance Metadata document is only as trustworthy as the process and party that produced it.

Implementations that rely on provenance metadata for access control, compliance, or risk decisions SHOULD obtain records through channels that provide integrity guarantees, such as transport-layer security (TLS) when fetching from the URI identified in `source.location`, or cryptographic signatures applied to the document by the `set.publisher`.

The `set.tracking.id` and `source.id` fields provide identifiers for the record and the described dataset respectively, but do not themselves provide integrity protection.

## URI Safety {#uri-safety}

Several fields in this specification accept URI values, including `source.location`, `set.publisher.namespace`, `source.id.uris`, `set.acknowledgments[].urls`, and `set.references[].url`.
Implementations that automatically dereference these URIs MUST apply the same defences required for any externally supplied URL, including protection against server-side request forgery (SSRF) and open redirect attacks.
URIs MUST be validated as well-formed before dereferencing.
Implementations SHOULD restrict dereferenceable schemes to `https` and, where appropriate, `http`.

## Sensitive Information in Provenance Records {#sensitive-information}

Provenance records may incidentally contain information that publishers consider sensitive, including internal tool names in `use.data-risk-reducing`, personnel names in `set.acknowledgments`, internal geographic constraints in `use.processing-included` and related fields, and organizational contact details in `set.publisher.contact-details`.

Publishers MUST consider whether information included in a provenance record is appropriate for the audience that will consume it.
Provenance records intended for public distribution SHOULD be reviewed to ensure they do not expose internal operational details beyond what is required to describe the dataset's provenance.

## Data Protection Compliance {#data-protection-compliance}

The `use.classification` field records whether a dataset has been evaluated against confidentiality classifications such as PHI, PI, PCI, SCI, or SPI.
The presence of a classification entry, including the value of the `evaluated` field, does not itself constitute compliance with any applicable law or regulation.
Implementers that process datasets described by provenance records containing such classifications MUST apply the data handling controls required by the relevant regulations in the jurisdictions where the data is processed and stored.

The geographic restriction fields (`use.processing-included`, `use.processing-excluded`, `use.storage-allowed`, `use.storage-forbidden`) express the publisher's stated intent but are not self-enforcing.
Implementers are responsible for establishing technical and organizational controls that honour these restrictions.

---
