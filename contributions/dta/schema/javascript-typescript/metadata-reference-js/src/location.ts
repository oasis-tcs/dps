import { v4 as uuid } from 'uuid';

export class Location {
  uuid: string;
  country: string;
  state: string;
  inclusion: boolean;

  constructor(country: string, state: string, inclusion: boolean) {
    this.uuid = uuid();
    this.country = country;
    this.state = state;
    this.inclusion = inclusion;
  };

  static default() {
    return new Location("", "", true);
  };
}
