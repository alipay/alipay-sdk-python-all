#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceAirplaneItinerary(object):

    def __init__(self):
        self._baggage = None
        self._carrier = None
        self._departure = None
        self._departure_date = None
        self._departure_time = None
        self._destination = None
        self._expiry_date = None
        self._flight_no = None
        self._passenger_class = None
        self._seat_class = None
        self._valid_date = None

    @property
    def baggage(self):
        return self._baggage

    @baggage.setter
    def baggage(self, value):
        self._baggage = value
    @property
    def carrier(self):
        return self._carrier

    @carrier.setter
    def carrier(self, value):
        self._carrier = value
    @property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        self._departure = value
    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        self._departure_date = value
    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        self._departure_time = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def passenger_class(self):
        return self._passenger_class

    @passenger_class.setter
    def passenger_class(self, value):
        self._passenger_class = value
    @property
    def seat_class(self):
        return self._seat_class

    @seat_class.setter
    def seat_class(self, value):
        self._seat_class = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.baggage:
            if hasattr(self.baggage, 'to_alipay_dict'):
                params['baggage'] = self.baggage.to_alipay_dict()
            else:
                params['baggage'] = self.baggage
        if self.carrier:
            if hasattr(self.carrier, 'to_alipay_dict'):
                params['carrier'] = self.carrier.to_alipay_dict()
            else:
                params['carrier'] = self.carrier
        if self.departure:
            if hasattr(self.departure, 'to_alipay_dict'):
                params['departure'] = self.departure.to_alipay_dict()
            else:
                params['departure'] = self.departure
        if self.departure_date:
            if hasattr(self.departure_date, 'to_alipay_dict'):
                params['departure_date'] = self.departure_date.to_alipay_dict()
            else:
                params['departure_date'] = self.departure_date
        if self.departure_time:
            if hasattr(self.departure_time, 'to_alipay_dict'):
                params['departure_time'] = self.departure_time.to_alipay_dict()
            else:
                params['departure_time'] = self.departure_time
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.expiry_date:
            if hasattr(self.expiry_date, 'to_alipay_dict'):
                params['expiry_date'] = self.expiry_date.to_alipay_dict()
            else:
                params['expiry_date'] = self.expiry_date
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.passenger_class:
            if hasattr(self.passenger_class, 'to_alipay_dict'):
                params['passenger_class'] = self.passenger_class.to_alipay_dict()
            else:
                params['passenger_class'] = self.passenger_class
        if self.seat_class:
            if hasattr(self.seat_class, 'to_alipay_dict'):
                params['seat_class'] = self.seat_class.to_alipay_dict()
            else:
                params['seat_class'] = self.seat_class
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceAirplaneItinerary()
        if 'baggage' in d:
            o.baggage = d['baggage']
        if 'carrier' in d:
            o.carrier = d['carrier']
        if 'departure' in d:
            o.departure = d['departure']
        if 'departure_date' in d:
            o.departure_date = d['departure_date']
        if 'departure_time' in d:
            o.departure_time = d['departure_time']
        if 'destination' in d:
            o.destination = d['destination']
        if 'expiry_date' in d:
            o.expiry_date = d['expiry_date']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'passenger_class' in d:
            o.passenger_class = d['passenger_class']
        if 'seat_class' in d:
            o.seat_class = d['seat_class']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


