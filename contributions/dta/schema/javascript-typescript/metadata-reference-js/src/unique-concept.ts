import { v4 as uuid } from 'uuid';

import { Concept } from './concept';

export class UniqueConcept extends Concept {
  uuid: string;

  constructor(code: string, system: string, description: string) {
    super(code, system, description);

    this.uuid = uuid();
  };

  static override default() {
    return new UniqueConcept("", "", "");
  };
}
