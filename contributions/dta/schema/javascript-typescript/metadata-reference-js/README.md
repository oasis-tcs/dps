# Metadata Reference Library (Javascript/TypeScript)

Welcome to the metadata reference libary used for implementations of the Data and Trust Alliance (D&TA) Data Provenance Standards.

## Description

This project contains code references for the JavaScript and TypeScript implementations of data provenance standards entities.  External applications that import these reference implementations will be able to maintain data structure between different elements of the data provenance standards.

Note that only the TypeScript entities are implemented directly.  JavaScript entities are generated based on the TypeScript implementation.

## Included files

### Javascript

Upon code generation, JavaScript implementations of the data provenance standards will be found under the `/dist` generated directory.

### Typescript

TypeScript implementations of the data provenance standards are found under the `/src` directory.  Each entity class is captured in its own TypeScript implementation file.

A list of TypeScript files is provided below:
- src/address-line.ts
    - Class to describe a single address entry for a given Organization.
- src/concept.ts
    - Class to describe an aggregation pattern of code, system location, and description for various abstract concepts in the Data Provenance Standards.
- src/confidentiality-classification.ts
    - Class to describe confidentiality classifications entries.
- src/data-format.ts
    - Class to capture details about the data format of the provided dataset.
- src/index.ts
    - Export file for class files.
- src/intended-data-use.ts
    - Class to describe intended data uses for the provided dataset.
- src/location.ts
    - Class to describe geolocation information for processing and storage requirements of the dataset.
- src/method.ts
    - Class to describe methods used for generating the dataset.
- src/organization.ts
    - Class to describe a single authority entity related to the dataset.
- src/privacy-enhancing-technology.ts
    - Class to capture privacy-related customizations performed on the dataset prior to distribution.
- src/unique-concept.ts
    - Class providing uniqueness capabilities to concepts.
- src/unique-entity.ts
    - Generic class providing uniqueness capabilities.

## Getting Started

### Dependencies

The JavaScript and TypeScript Data Provenance Standards implementations have been trialed against Node 20+ for packaging.  Similar versions of `node` may also be compatible.

A dependency on `npm` package `iso-3166` is used for building the lists of geolocations used for storage and processing regions.

### Installing

The JavaScript and TypeScript Data Provenance Standards implementations are packaged as an NPM module.  In the future, these would be distributed using a package manager site such as `npmjs`.  For now, the code can be generated and integrated directly using `npm` commands and scripts.

To generate the JavaScript files as well as a consolidated `npm` package for both TypeScript and Javascript, execute the provided shell script `rebuild.sh` to generate the files from the TypeScript sources.  This will generate a file `data-and-trust-alliance-metadata-reference-1.0.0.tgz` that can be imported into existing `npm` projects.
