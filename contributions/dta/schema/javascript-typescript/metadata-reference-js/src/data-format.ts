import { UniqueEntity } from './unique-entity';

export class DataFormat extends UniqueEntity {
  value: string;

  constructor(value: string) {
    super();

    this.value = value;
  };

  static default() {
    return new DataFormat("");
  };

  static defaultOptions = [
    "application/json",
    "application/jsonld",
    "application/zip",
    "application/msword",
    "application/vnd.ms-excel",
    "image/bmp",
    "image/jpeg",
    "image/x-png",
    "image/png",
    "image/gif",
    "text/csv",
    "text/plain"
  ];
}
