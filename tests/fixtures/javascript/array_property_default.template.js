// @flow

export class Test {
  x: Array<*>;

  constructor(data: Object = {}) {
    this.x = Array.isArray(data.x) ? data.x : [42];
  }
}
