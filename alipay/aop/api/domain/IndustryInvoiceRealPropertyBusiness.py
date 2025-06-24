#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoiceRealPropertyBusiness(object):

    def __init__(self):
        self._cross_city_flag = None
        self._end_time = None
        self._plate_no_list = None
        self._real_property_address = None
        self._real_property_area = None
        self._real_property_cert_no = None
        self._real_property_city = None
        self._real_property_code = None
        self._real_property_province = None
        self._serial_no = None
        self._start_time = None

    @property
    def cross_city_flag(self):
        return self._cross_city_flag

    @cross_city_flag.setter
    def cross_city_flag(self, value):
        self._cross_city_flag = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def plate_no_list(self):
        return self._plate_no_list

    @plate_no_list.setter
    def plate_no_list(self, value):
        if isinstance(value, list):
            self._plate_no_list = list()
            for i in value:
                self._plate_no_list.append(i)
    @property
    def real_property_address(self):
        return self._real_property_address

    @real_property_address.setter
    def real_property_address(self, value):
        self._real_property_address = value
    @property
    def real_property_area(self):
        return self._real_property_area

    @real_property_area.setter
    def real_property_area(self, value):
        self._real_property_area = value
    @property
    def real_property_cert_no(self):
        return self._real_property_cert_no

    @real_property_cert_no.setter
    def real_property_cert_no(self, value):
        self._real_property_cert_no = value
    @property
    def real_property_city(self):
        return self._real_property_city

    @real_property_city.setter
    def real_property_city(self, value):
        self._real_property_city = value
    @property
    def real_property_code(self):
        return self._real_property_code

    @real_property_code.setter
    def real_property_code(self, value):
        self._real_property_code = value
    @property
    def real_property_province(self):
        return self._real_property_province

    @real_property_province.setter
    def real_property_province(self, value):
        self._real_property_province = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.cross_city_flag:
            if hasattr(self.cross_city_flag, 'to_alipay_dict'):
                params['cross_city_flag'] = self.cross_city_flag.to_alipay_dict()
            else:
                params['cross_city_flag'] = self.cross_city_flag
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.plate_no_list:
            if isinstance(self.plate_no_list, list):
                for i in range(0, len(self.plate_no_list)):
                    element = self.plate_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plate_no_list[i] = element.to_alipay_dict()
            if hasattr(self.plate_no_list, 'to_alipay_dict'):
                params['plate_no_list'] = self.plate_no_list.to_alipay_dict()
            else:
                params['plate_no_list'] = self.plate_no_list
        if self.real_property_address:
            if hasattr(self.real_property_address, 'to_alipay_dict'):
                params['real_property_address'] = self.real_property_address.to_alipay_dict()
            else:
                params['real_property_address'] = self.real_property_address
        if self.real_property_area:
            if hasattr(self.real_property_area, 'to_alipay_dict'):
                params['real_property_area'] = self.real_property_area.to_alipay_dict()
            else:
                params['real_property_area'] = self.real_property_area
        if self.real_property_cert_no:
            if hasattr(self.real_property_cert_no, 'to_alipay_dict'):
                params['real_property_cert_no'] = self.real_property_cert_no.to_alipay_dict()
            else:
                params['real_property_cert_no'] = self.real_property_cert_no
        if self.real_property_city:
            if hasattr(self.real_property_city, 'to_alipay_dict'):
                params['real_property_city'] = self.real_property_city.to_alipay_dict()
            else:
                params['real_property_city'] = self.real_property_city
        if self.real_property_code:
            if hasattr(self.real_property_code, 'to_alipay_dict'):
                params['real_property_code'] = self.real_property_code.to_alipay_dict()
            else:
                params['real_property_code'] = self.real_property_code
        if self.real_property_province:
            if hasattr(self.real_property_province, 'to_alipay_dict'):
                params['real_property_province'] = self.real_property_province.to_alipay_dict()
            else:
                params['real_property_province'] = self.real_property_province
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceRealPropertyBusiness()
        if 'cross_city_flag' in d:
            o.cross_city_flag = d['cross_city_flag']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'plate_no_list' in d:
            o.plate_no_list = d['plate_no_list']
        if 'real_property_address' in d:
            o.real_property_address = d['real_property_address']
        if 'real_property_area' in d:
            o.real_property_area = d['real_property_area']
        if 'real_property_cert_no' in d:
            o.real_property_cert_no = d['real_property_cert_no']
        if 'real_property_city' in d:
            o.real_property_city = d['real_property_city']
        if 'real_property_code' in d:
            o.real_property_code = d['real_property_code']
        if 'real_property_province' in d:
            o.real_property_province = d['real_property_province']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


