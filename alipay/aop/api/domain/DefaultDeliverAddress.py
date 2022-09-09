#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DefaultDeliverAddress(object):

    def __init__(self):
        self._address = None
        self._area = None
        self._city = None
        self._fullname = None
        self._mobile = None
        self._prov = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, value):
        self._prov = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.fullname:
            if hasattr(self.fullname, 'to_alipay_dict'):
                params['fullname'] = self.fullname.to_alipay_dict()
            else:
                params['fullname'] = self.fullname
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.prov:
            if hasattr(self.prov, 'to_alipay_dict'):
                params['prov'] = self.prov.to_alipay_dict()
            else:
                params['prov'] = self.prov
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DefaultDeliverAddress()
        if 'address' in d:
            o.address = d['address']
        if 'area' in d:
            o.area = d['area']
        if 'city' in d:
            o.city = d['city']
        if 'fullname' in d:
            o.fullname = d['fullname']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'prov' in d:
            o.prov = d['prov']
        return o


