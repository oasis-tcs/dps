# Metadata Reference Library (JavaScript/TypeScript)

Welcome to the metadata reference library for implementations of the Data and Trust Alliance (D&TA) Data Provenance Standards.

## Description

This project contains code references for the JavaScript and TypeScript implementations of data provenance standards entities.
External applications that import these reference implementations will be able to maintain a consistent data structure across different elements of the standards.

Note: Only the TypeScript entities are implemented directly. JavaScript entities are generated from the TypeScript implementation.

## Included Files

### JavaScript

Upon code generation, JavaScript implementations of the data provenance standards will be located in the `/dist` directory.

### TypeScript

TypeScript implementations are located in the `/src` directory. Each entity is defined in its own TypeScript file.

#### TypeScript File Overview

| File                                    | Description                                                                 |
|:----------------------------------------|:----------------------------------------------------------------------------|
| `src/address-line.ts`                   | Defines a single address entry for a given organization.                    |
| `src/concept.ts`                        | Describes an aggregation of code, system location, and concept description. |
| `src/confidentiality-classification.ts` | Describes confidentiality classification entries.                           |
| `src/data-format.ts`                    | Captures details about the dataset's data format.                           |
| `src/index.ts`                          | Export file that consolidates all class definitions.                        |
| `src/intended-data-use.ts`              | Describes intended uses for the dataset.                                    |
| `src/location.ts`                       | Describes geolocation information for dataset storage and processing.       |
| `src/method.ts`                         | Describes methods used to generate the dataset.                             |
| `src/organization.ts`                   | Represents an authority entity associated with the dataset.                 |
| `src/privacy-enhancing-technology.ts`   | Captures privacy-related modifications applied to the dataset.              |
| `src/unique-concept.ts`                 | Provides uniqueness features for concepts.                                  |
| `src/unique-entity.ts`                  | Generic class that provides uniqueness capabilities for entities.           |

## Getting Started

### Dependencies

- Node.js 20+ (other versions may be compatible)
- `iso-3166` npm package, used for building the geolocation lists

### Installing

The library is packaged as an NPM module. While not currently published on npmjs.com, it can be generated and integrated manually.

To generate JavaScript files and build the package:

```sh
./rebuild.sh
```
