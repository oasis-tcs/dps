### Member `proof` {#member-proof}

The `proof` member is reserved for the proof material of an external integrity or signing envelope, such as a signature over the record.
Its internal structure is opaque to this specification: a record defines only where such material is carried, not how it is produced or verified
(see section [sec](#integrity-and-authenticity)).

```{.yaml json-path="$.properties.proof"}
DataProvenance:
  # ...
  proof: Mapping  # optional
```

The value of `proof`, when present, MUST be a JSON object.

---
