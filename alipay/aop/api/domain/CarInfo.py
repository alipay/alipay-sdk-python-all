#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarInfo(object):

    def __init__(self):
        self._address = None
        self._car_brand = None
        self._car_license = None
        self._car_series = None
        self._car_type = None
        self._car_vin = None
        self._engine_no = None
        self._first_register_date = None
        self._issue_date = None
        self._owner = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def car_brand(self):
        return self._car_brand

    @car_brand.setter
    def car_brand(self, value):
        self._car_brand = value
    @property
    def car_license(self):
        return self._car_license

    @car_license.setter
    def car_license(self, value):
        self._car_license = value
    @property
    def car_series(self):
        return self._car_series

    @car_series.setter
    def car_series(self, value):
        self._car_series = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def car_vin(self):
        return self._car_vin

    @car_vin.setter
    def car_vin(self, value):
        self._car_vin = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def first_register_date(self):
        return self._first_register_date

    @first_register_date.setter
    def first_register_date(self, value):
        self._first_register_date = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.car_brand:
            if hasattr(self.car_brand, 'to_alipay_dict'):
                params['car_brand'] = self.car_brand.to_alipay_dict()
            else:
                params['car_brand'] = self.car_brand
        if self.car_license:
            if hasattr(self.car_license, 'to_alipay_dict'):
                params['car_license'] = self.car_license.to_alipay_dict()
            else:
                params['car_license'] = self.car_license
        if self.car_series:
            if hasattr(self.car_series, 'to_alipay_dict'):
                params['car_series'] = self.car_series.to_alipay_dict()
            else:
                params['car_series'] = self.car_series
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.car_vin:
            if hasattr(self.car_vin, 'to_alipay_dict'):
                params['car_vin'] = self.car_vin.to_alipay_dict()
            else:
                params['car_vin'] = self.car_vin
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.first_register_date:
            if hasattr(self.first_register_date, 'to_alipay_dict'):
                params['first_register_date'] = self.first_register_date.to_alipay_dict()
            else:
                params['first_register_date'] = self.first_register_date
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarInfo()
        if 'address' in d:
            o.address = d['address']
        if 'car_brand' in d:
            o.car_brand = d['car_brand']
        if 'car_license' in d:
            o.car_license = d['car_license']
        if 'car_series' in d:
            o.car_series = d['car_series']
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'car_vin' in d:
            o.car_vin = d['car_vin']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'first_register_date' in d:
            o.first_register_date = d['first_register_date']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'owner' in d:
            o.owner = d['owner']
        return o


