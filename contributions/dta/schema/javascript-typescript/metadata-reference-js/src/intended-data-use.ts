import { UniqueConcept } from './unique-concept';

export class IntendedDataUse extends UniqueConcept {
  descriptionDisplayText: string;
  enabled: boolean;

  constructor(code: string, system: string, description: string, descriptionDisplayText: string, enabled: boolean) {
    super(code, system, description);

    this.descriptionDisplayText = descriptionDisplayText;
    this.enabled = enabled;
  };

  static override default() {
    return new IntendedDataUse("", "", "", "", true);
  };

  static dataProvenanceStandardsEntry(code: string, description: string, descriptionDisplayText: string) {
    return new IntendedDataUse(code, IntendedDataUse.defaultSystem, description, descriptionDisplayText, false);
  };

  static customNonAiEntry() {
    return new IntendedDataUse("non-ai-other", "", "", "", true);
  };

  static customAiEntry() {
    return new IntendedDataUse("ai-other", "", "", "", true);
  };

  static defaultNonAiOptions = [
    {
      code: "non-ai-staging",
      description: "Non-AI Staging/testing",
      descriptionText: "Staging/testing"
    }, {
      code: "non-ai-production",
      description: "Non-AI Production",
      descriptionText: "Production"
    }, {
      code: "non-ai-quality",
      description: "Non-AI Quality assurance",
      descriptionText: "Quality assurance"
    }
  ];

  static defaultAiOptions = [
    {
      code: "ai-pre-training",
      description: "AI Pre-Training",
      descriptionText: "Pre-Training"
    }, {
      code: "ai-alignment",
      description: "AI Alignment",
      descriptionText: "Alignment"
    }, {
      code: "ai-evaluation",
      description: "AI Evaluation",
      descriptionText: "Evaluation"
    }, {
      code: "ai-synthetic",
      description: "AI Sythentic Data Generation",
      descriptionText: "Sythentic Data Generation"
    }
  ];

  static defaultSystem = "https://dataandtrustalliance.org/DPS/CodeSystem/Use";
}
