'use strict';

describe('Feature Test',function() {
  var plane;
  var airport;

  beforeEach(function() {
    plane = new Plane();
    airport = new Airport();
  });

  it('planes can land at the airport',function() {
    plane.land(airport)
    expect(airport.planes()).toContain(plane);
  });

  it('planes can be inastructed to take off', function(){
    plane.land(airport)
    plane.takeoff();
    expect(airport.planes()).not.toContain(plane);
  });
});
