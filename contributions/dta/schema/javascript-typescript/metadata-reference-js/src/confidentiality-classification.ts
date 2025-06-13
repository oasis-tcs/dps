import { UniqueConcept } from './unique-concept';

export class ConfidentialityClassification extends UniqueConcept {
  enabled: boolean = false;

  constructor(code: string, system: string, description: string, enabled: boolean) {
    super(code, system, description);

    this.enabled = enabled;
  };

  static override default() {
    return new ConfidentialityClassification("", "", "", true);
  };

  static dataProvenanceStandardsEntry(code: string, description: string) {
    return new ConfidentialityClassification(code, ConfidentialityClassification.defaultSystem, description, false);
  };

  static defaultOptions = [
    {
      code: "pi",
      description: "Personal Information (PI)/Demographic"
    }, {
      code: "pci",
      description: "Payment Card Industry (PCI)"
    }, {
      code: "pfi",
      description: "Personal Financial Information (PFI)"
    }, {
      code: "pii",
      description: "Personally Identifiable Information (PII)"
    }, {
      code: "phi",
      description: "Personal Health Information (PHI)"
    }, {
      code: "spi",
      description: "Sensitive Personal Information (SPI)"
    }
  ];

  static defaultSystem = "https://dataandtrustalliance.org/DPS/CodeSystem/Regulations";
}
