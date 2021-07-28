#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiverIstd(object):

    def __init__(self):
        self._address = None
        self._address_detail = None
        self._city = None
        self._coordinate_type = None
        self._lat = None
        self._lng = None
        self._mobile_no = None
        self._name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_detail(self):
        return self._address_detail

    @address_detail.setter
    def address_detail(self, value):
        self._address_detail = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def coordinate_type(self):
        return self._coordinate_type

    @coordinate_type.setter
    def coordinate_type(self, value):
        self._coordinate_type = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, value):
        self._lng = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_detail:
            if hasattr(self.address_detail, 'to_alipay_dict'):
                params['address_detail'] = self.address_detail.to_alipay_dict()
            else:
                params['address_detail'] = self.address_detail
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.coordinate_type:
            if hasattr(self.coordinate_type, 'to_alipay_dict'):
                params['coordinate_type'] = self.coordinate_type.to_alipay_dict()
            else:
                params['coordinate_type'] = self.coordinate_type
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lng:
            if hasattr(self.lng, 'to_alipay_dict'):
                params['lng'] = self.lng.to_alipay_dict()
            else:
                params['lng'] = self.lng
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiverIstd()
        if 'address' in d:
            o.address = d['address']
        if 'address_detail' in d:
            o.address_detail = d['address_detail']
        if 'city' in d:
            o.city = d['city']
        if 'coordinate_type' in d:
            o.coordinate_type = d['coordinate_type']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lng' in d:
            o.lng = d['lng']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'name' in d:
            o.name = d['name']
        return o


