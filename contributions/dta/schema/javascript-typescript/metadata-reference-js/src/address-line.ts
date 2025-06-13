import { UniqueEntity } from './unique-entity';

export class AddressLine extends UniqueEntity {
  address: string;

  constructor() {
    super();

    this.address = "";
  };

  static copy(otherAddressLine: AddressLine) {
    var duplicate = new AddressLine();
    duplicate.address = otherAddressLine.address;

    return duplicate;
  };
}
