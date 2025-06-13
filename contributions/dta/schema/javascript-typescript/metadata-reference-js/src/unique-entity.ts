import { v4 as uuid } from 'uuid';

export class UniqueEntity {
  uuid: string;

  constructor() {
    this.uuid = uuid();
  };
}
