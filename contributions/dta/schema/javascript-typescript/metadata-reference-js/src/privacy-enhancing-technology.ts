import { v4 as uuid } from 'uuid';

import { Concept } from './concept';

export class PrivacyEnhancingTechnology {
  uuid: string;
  tool: Concept;
  parameters: string;
  result: string;

  constructor(tool: Concept, parameters: string, result: string) {
    this.uuid = uuid();
    this.tool = tool;
    this.parameters = parameters;
    this.result = result;
  };

  static default() {
    return new PrivacyEnhancingTechnology(Concept.default(), "", "");
  };

  static defaultOptions = [
    {
      code: "data-anonymization",
      description: "Data Anonymization"
    }, {
      code: "data-encryption",
      description: "Data Encryption"
    }, {
      code: "data-masking",
      description: "Data Masking"
    }, {
      code: "data-minimization",
      description: "Data Minimization"
    }, {
      code: "data-redaction",
      description: "Data Redaction"
    }, {
      code: "differential-privacy",
      description: "Differential Privacy"
    }, {
      code: "federated-learning",
      description: "Federated Learning"
    }, {
      code: "homomorphic-encryption",
      description: "Homomorphic Encryption"
    }, {
      code: "k-anonymity",
      description: "K-anonymity"
    }, {
      code: "l-diversity",
      description: "L-diversity"
    }, {
      code: "pseudonymization",
      description: "Pseudonymization"
    }, {
      code: "secure-multi-party-computation",
      description: "Secure Multi-party Computation (SMC)"
    }, {
      code: "t-closeness",
      description: "T-closeness"
    }, {
      code: "tokenization",
      description: "Tokenization"
    }
  ];

  static defaultSystem = "https://dataandtrustalliance.org/DPS/CodeSystem/PET";

  static getDescriptions() {
    return new Set(PrivacyEnhancingTechnology.defaultOptions.map((defaultOption) => defaultOption.description));
  };
}
