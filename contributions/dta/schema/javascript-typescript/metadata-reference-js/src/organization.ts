import { AddressLine } from './address-line';
import { UniqueEntity } from './unique-entity';

export class Organization extends UniqueEntity {
  name: string;
  addressLines: AddressLine[];

  constructor() {
    super();

    this.name = "";
    this.addressLines = [];
  };

  static copy(otherOrganization: Organization) {
    var duplicate = new Organization();
    duplicate.name = otherOrganization.name;
    duplicate.addressLines = otherOrganization.addressLines.map(
      (addressLine) => {
        return AddressLine.copy(addressLine);
      }
    );

    return duplicate;
  };
}
