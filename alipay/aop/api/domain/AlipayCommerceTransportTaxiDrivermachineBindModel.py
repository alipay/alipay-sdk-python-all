#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GPSLocationInfo import GPSLocationInfo


class AlipayCommerceTransportTaxiDrivermachineBindModel(object):

    def __init__(self):
        self._car_no = None
        self._city_code = None
        self._driver_open_id = None
        self._driver_user_id = None
        self._gmt_signin = None
        self._location_info = None
        self._machine_sn = None
        self._machine_supplier_id = None
        self._request_id = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def driver_open_id(self):
        return self._driver_open_id

    @driver_open_id.setter
    def driver_open_id(self, value):
        self._driver_open_id = value
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
    @property
    def gmt_signin(self):
        return self._gmt_signin

    @gmt_signin.setter
    def gmt_signin(self, value):
        self._gmt_signin = value
    @property
    def location_info(self):
        return self._location_info

    @location_info.setter
    def location_info(self, value):
        if isinstance(value, GPSLocationInfo):
            self._location_info = value
        else:
            self._location_info = GPSLocationInfo.from_alipay_dict(value)
    @property
    def machine_sn(self):
        return self._machine_sn

    @machine_sn.setter
    def machine_sn(self, value):
        self._machine_sn = value
    @property
    def machine_supplier_id(self):
        return self._machine_supplier_id

    @machine_supplier_id.setter
    def machine_supplier_id(self, value):
        self._machine_supplier_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.driver_open_id:
            if hasattr(self.driver_open_id, 'to_alipay_dict'):
                params['driver_open_id'] = self.driver_open_id.to_alipay_dict()
            else:
                params['driver_open_id'] = self.driver_open_id
        if self.driver_user_id:
            if hasattr(self.driver_user_id, 'to_alipay_dict'):
                params['driver_user_id'] = self.driver_user_id.to_alipay_dict()
            else:
                params['driver_user_id'] = self.driver_user_id
        if self.gmt_signin:
            if hasattr(self.gmt_signin, 'to_alipay_dict'):
                params['gmt_signin'] = self.gmt_signin.to_alipay_dict()
            else:
                params['gmt_signin'] = self.gmt_signin
        if self.location_info:
            if hasattr(self.location_info, 'to_alipay_dict'):
                params['location_info'] = self.location_info.to_alipay_dict()
            else:
                params['location_info'] = self.location_info
        if self.machine_sn:
            if hasattr(self.machine_sn, 'to_alipay_dict'):
                params['machine_sn'] = self.machine_sn.to_alipay_dict()
            else:
                params['machine_sn'] = self.machine_sn
        if self.machine_supplier_id:
            if hasattr(self.machine_supplier_id, 'to_alipay_dict'):
                params['machine_supplier_id'] = self.machine_supplier_id.to_alipay_dict()
            else:
                params['machine_supplier_id'] = self.machine_supplier_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiDrivermachineBindModel()
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'driver_open_id' in d:
            o.driver_open_id = d['driver_open_id']
        if 'driver_user_id' in d:
            o.driver_user_id = d['driver_user_id']
        if 'gmt_signin' in d:
            o.gmt_signin = d['gmt_signin']
        if 'location_info' in d:
            o.location_info = d['location_info']
        if 'machine_sn' in d:
            o.machine_sn = d['machine_sn']
        if 'machine_supplier_id' in d:
            o.machine_supplier_id = d['machine_supplier_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


