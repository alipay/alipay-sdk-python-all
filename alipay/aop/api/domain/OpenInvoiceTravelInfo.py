#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenInvoiceTravelInfo(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._destination = None
        self._origin = None
        self._travel_date = None
        self._traveller_name = None
        self._vehicle_level = None
        self._vehicle_type = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
    @property
    def travel_date(self):
        return self._travel_date

    @travel_date.setter
    def travel_date(self, value):
        self._travel_date = value
    @property
    def traveller_name(self):
        return self._traveller_name

    @traveller_name.setter
    def traveller_name(self, value):
        self._traveller_name = value
    @property
    def vehicle_level(self):
        return self._vehicle_level

    @vehicle_level.setter
    def vehicle_level(self, value):
        self._vehicle_level = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.origin:
            if hasattr(self.origin, 'to_alipay_dict'):
                params['origin'] = self.origin.to_alipay_dict()
            else:
                params['origin'] = self.origin
        if self.travel_date:
            if hasattr(self.travel_date, 'to_alipay_dict'):
                params['travel_date'] = self.travel_date.to_alipay_dict()
            else:
                params['travel_date'] = self.travel_date
        if self.traveller_name:
            if hasattr(self.traveller_name, 'to_alipay_dict'):
                params['traveller_name'] = self.traveller_name.to_alipay_dict()
            else:
                params['traveller_name'] = self.traveller_name
        if self.vehicle_level:
            if hasattr(self.vehicle_level, 'to_alipay_dict'):
                params['vehicle_level'] = self.vehicle_level.to_alipay_dict()
            else:
                params['vehicle_level'] = self.vehicle_level
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenInvoiceTravelInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'destination' in d:
            o.destination = d['destination']
        if 'origin' in d:
            o.origin = d['origin']
        if 'travel_date' in d:
            o.travel_date = d['travel_date']
        if 'traveller_name' in d:
            o.traveller_name = d['traveller_name']
        if 'vehicle_level' in d:
            o.vehicle_level = d['vehicle_level']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        return o


