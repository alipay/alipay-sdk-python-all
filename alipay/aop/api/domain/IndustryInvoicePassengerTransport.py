#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoicePassengerTransport(object):

    def __init__(self):
        self._departure = None
        self._destination = None
        self._passenger_cert_no = None
        self._passenger_cert_type = None
        self._passenger_name = None
        self._seat_class = None
        self._serial_no = None
        self._travel_date = None
        self._travel_method = None

    @property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        self._departure = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def passenger_cert_no(self):
        return self._passenger_cert_no

    @passenger_cert_no.setter
    def passenger_cert_no(self, value):
        self._passenger_cert_no = value
    @property
    def passenger_cert_type(self):
        return self._passenger_cert_type

    @passenger_cert_type.setter
    def passenger_cert_type(self, value):
        self._passenger_cert_type = value
    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self._passenger_name = value
    @property
    def seat_class(self):
        return self._seat_class

    @seat_class.setter
    def seat_class(self, value):
        self._seat_class = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def travel_date(self):
        return self._travel_date

    @travel_date.setter
    def travel_date(self, value):
        self._travel_date = value
    @property
    def travel_method(self):
        return self._travel_method

    @travel_method.setter
    def travel_method(self, value):
        self._travel_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.departure:
            if hasattr(self.departure, 'to_alipay_dict'):
                params['departure'] = self.departure.to_alipay_dict()
            else:
                params['departure'] = self.departure
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.passenger_cert_no:
            if hasattr(self.passenger_cert_no, 'to_alipay_dict'):
                params['passenger_cert_no'] = self.passenger_cert_no.to_alipay_dict()
            else:
                params['passenger_cert_no'] = self.passenger_cert_no
        if self.passenger_cert_type:
            if hasattr(self.passenger_cert_type, 'to_alipay_dict'):
                params['passenger_cert_type'] = self.passenger_cert_type.to_alipay_dict()
            else:
                params['passenger_cert_type'] = self.passenger_cert_type
        if self.passenger_name:
            if hasattr(self.passenger_name, 'to_alipay_dict'):
                params['passenger_name'] = self.passenger_name.to_alipay_dict()
            else:
                params['passenger_name'] = self.passenger_name
        if self.seat_class:
            if hasattr(self.seat_class, 'to_alipay_dict'):
                params['seat_class'] = self.seat_class.to_alipay_dict()
            else:
                params['seat_class'] = self.seat_class
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.travel_date:
            if hasattr(self.travel_date, 'to_alipay_dict'):
                params['travel_date'] = self.travel_date.to_alipay_dict()
            else:
                params['travel_date'] = self.travel_date
        if self.travel_method:
            if hasattr(self.travel_method, 'to_alipay_dict'):
                params['travel_method'] = self.travel_method.to_alipay_dict()
            else:
                params['travel_method'] = self.travel_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoicePassengerTransport()
        if 'departure' in d:
            o.departure = d['departure']
        if 'destination' in d:
            o.destination = d['destination']
        if 'passenger_cert_no' in d:
            o.passenger_cert_no = d['passenger_cert_no']
        if 'passenger_cert_type' in d:
            o.passenger_cert_type = d['passenger_cert_type']
        if 'passenger_name' in d:
            o.passenger_name = d['passenger_name']
        if 'seat_class' in d:
            o.seat_class = d['seat_class']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'travel_date' in d:
            o.travel_date = d['travel_date']
        if 'travel_method' in d:
            o.travel_method = d['travel_method']
        return o


