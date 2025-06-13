#!/bin/bash

rm -rf data-and-trust-alliance-metadata-reference-*.tgz ./dist/ *.d.ts
npm run ts:js
npm run ts:defs
npm pack
