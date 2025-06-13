export class Concept {
  code: string;
  system: string;
  description: string;

  constructor(code: string, system: string, description: string) {
    this.code = code;
    this.system = system;
    this.description = description;
  };

  static default() {
    return new Concept("", "", "");
  };

  static generateCode(value: string) {
    const delimiter = "-";
    const pattern = /[^a-zA-Z0-9]+/g

    // Replace all strings of non-alphanumeric characters with hyphens.
    var tempValue = value.replaceAll(pattern, delimiter);

    // Convert to lower case.
    tempValue = tempValue.toLowerCase();

    // Remove leading/trailing hyphens.
    while(tempValue.length > 0 && tempValue.charAt(0) === delimiter) {
      tempValue = tempValue.substring(1);
    }

    while(tempValue.length > 0 && tempValue.charAt(tempValue.length - 1) === delimiter) {
      tempValue = tempValue.slice(0, tempValue.length - 1);
    }

    return tempValue;
  };
}
