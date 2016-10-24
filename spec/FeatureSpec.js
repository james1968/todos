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

  it('planes cannot take off if weather is stormy', function(){
    plane.land(airport)
    spyOn(airport, 'isStormy').and.returnValue(true);
    expect(function(){ plane.takeoff();}).toThrowError('cannot takeoff during storm');
    expect(airport.planes()).toContain(plane);
  });

});
