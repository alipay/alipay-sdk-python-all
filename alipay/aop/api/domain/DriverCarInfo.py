#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DriverCarInfo(object):

    def __init__(self):
        self._aggregate_code_flag = None
        self._bind_time = None
        self._car_brand = None
        self._car_color = None
        self._car_no = None
        self._car_no_color = None
        self._car_operation_no = None
        self._car_type = None
        self._cert_no = None
        self._channel = None
        self._city_code = None
        self._city_name = None
        self._company = None
        self._driver_id = None
        self._driver_name = None
        self._driver_sex = None
        self._driver_user_id = None
        self._tele_no = None

    @property
    def aggregate_code_flag(self):
        return self._aggregate_code_flag

    @aggregate_code_flag.setter
    def aggregate_code_flag(self, value):
        self._aggregate_code_flag = value
    @property
    def bind_time(self):
        return self._bind_time

    @bind_time.setter
    def bind_time(self, value):
        self._bind_time = value
    @property
    def car_brand(self):
        return self._car_brand

    @car_brand.setter
    def car_brand(self, value):
        self._car_brand = value
    @property
    def car_color(self):
        return self._car_color

    @car_color.setter
    def car_color(self, value):
        self._car_color = value
    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def car_no_color(self):
        return self._car_no_color

    @car_no_color.setter
    def car_no_color(self, value):
        self._car_no_color = value
    @property
    def car_operation_no(self):
        return self._car_operation_no

    @car_operation_no.setter
    def car_operation_no(self, value):
        self._car_operation_no = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        self._driver_id = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_sex(self):
        return self._driver_sex

    @driver_sex.setter
    def driver_sex(self, value):
        self._driver_sex = value
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
    @property
    def tele_no(self):
        return self._tele_no

    @tele_no.setter
    def tele_no(self, value):
        self._tele_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregate_code_flag:
            if hasattr(self.aggregate_code_flag, 'to_alipay_dict'):
                params['aggregate_code_flag'] = self.aggregate_code_flag.to_alipay_dict()
            else:
                params['aggregate_code_flag'] = self.aggregate_code_flag
        if self.bind_time:
            if hasattr(self.bind_time, 'to_alipay_dict'):
                params['bind_time'] = self.bind_time.to_alipay_dict()
            else:
                params['bind_time'] = self.bind_time
        if self.car_brand:
            if hasattr(self.car_brand, 'to_alipay_dict'):
                params['car_brand'] = self.car_brand.to_alipay_dict()
            else:
                params['car_brand'] = self.car_brand
        if self.car_color:
            if hasattr(self.car_color, 'to_alipay_dict'):
                params['car_color'] = self.car_color.to_alipay_dict()
            else:
                params['car_color'] = self.car_color
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.car_no_color:
            if hasattr(self.car_no_color, 'to_alipay_dict'):
                params['car_no_color'] = self.car_no_color.to_alipay_dict()
            else:
                params['car_no_color'] = self.car_no_color
        if self.car_operation_no:
            if hasattr(self.car_operation_no, 'to_alipay_dict'):
                params['car_operation_no'] = self.car_operation_no.to_alipay_dict()
            else:
                params['car_operation_no'] = self.car_operation_no
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.driver_id:
            if hasattr(self.driver_id, 'to_alipay_dict'):
                params['driver_id'] = self.driver_id.to_alipay_dict()
            else:
                params['driver_id'] = self.driver_id
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driver_sex:
            if hasattr(self.driver_sex, 'to_alipay_dict'):
                params['driver_sex'] = self.driver_sex.to_alipay_dict()
            else:
                params['driver_sex'] = self.driver_sex
        if self.driver_user_id:
            if hasattr(self.driver_user_id, 'to_alipay_dict'):
                params['driver_user_id'] = self.driver_user_id.to_alipay_dict()
            else:
                params['driver_user_id'] = self.driver_user_id
        if self.tele_no:
            if hasattr(self.tele_no, 'to_alipay_dict'):
                params['tele_no'] = self.tele_no.to_alipay_dict()
            else:
                params['tele_no'] = self.tele_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DriverCarInfo()
        if 'aggregate_code_flag' in d:
            o.aggregate_code_flag = d['aggregate_code_flag']
        if 'bind_time' in d:
            o.bind_time = d['bind_time']
        if 'car_brand' in d:
            o.car_brand = d['car_brand']
        if 'car_color' in d:
            o.car_color = d['car_color']
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'car_no_color' in d:
            o.car_no_color = d['car_no_color']
        if 'car_operation_no' in d:
            o.car_operation_no = d['car_operation_no']
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'company' in d:
            o.company = d['company']
        if 'driver_id' in d:
            o.driver_id = d['driver_id']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driver_sex' in d:
            o.driver_sex = d['driver_sex']
        if 'driver_user_id' in d:
            o.driver_user_id = d['driver_user_id']
        if 'tele_no' in d:
            o.tele_no = d['tele_no']
        return o


