#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JTQueryDetails(object):

    def __init__(self):
        self._bill_code = None
        self._desc = None
        self._next_network_area_name = None
        self._next_network_city_name = None
        self._next_network_province_name = None
        self._next_stop_name = None
        self._problem_type = None
        self._remark = None
        self._scan_network_area = None
        self._scan_network_city = None
        self._scan_network_contact = None
        self._scan_network_id = None
        self._scan_network_name = None
        self._scan_network_province = None
        self._scan_time = None
        self._scan_type = None
        self._staff_contact = None
        self._staff_name = None

    @property
    def bill_code(self):
        return self._bill_code

    @bill_code.setter
    def bill_code(self, value):
        self._bill_code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def next_network_area_name(self):
        return self._next_network_area_name

    @next_network_area_name.setter
    def next_network_area_name(self, value):
        self._next_network_area_name = value
    @property
    def next_network_city_name(self):
        return self._next_network_city_name

    @next_network_city_name.setter
    def next_network_city_name(self, value):
        self._next_network_city_name = value
    @property
    def next_network_province_name(self):
        return self._next_network_province_name

    @next_network_province_name.setter
    def next_network_province_name(self, value):
        self._next_network_province_name = value
    @property
    def next_stop_name(self):
        return self._next_stop_name

    @next_stop_name.setter
    def next_stop_name(self, value):
        self._next_stop_name = value
    @property
    def problem_type(self):
        return self._problem_type

    @problem_type.setter
    def problem_type(self, value):
        self._problem_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scan_network_area(self):
        return self._scan_network_area

    @scan_network_area.setter
    def scan_network_area(self, value):
        self._scan_network_area = value
    @property
    def scan_network_city(self):
        return self._scan_network_city

    @scan_network_city.setter
    def scan_network_city(self, value):
        self._scan_network_city = value
    @property
    def scan_network_contact(self):
        return self._scan_network_contact

    @scan_network_contact.setter
    def scan_network_contact(self, value):
        self._scan_network_contact = value
    @property
    def scan_network_id(self):
        return self._scan_network_id

    @scan_network_id.setter
    def scan_network_id(self, value):
        self._scan_network_id = value
    @property
    def scan_network_name(self):
        return self._scan_network_name

    @scan_network_name.setter
    def scan_network_name(self, value):
        self._scan_network_name = value
    @property
    def scan_network_province(self):
        return self._scan_network_province

    @scan_network_province.setter
    def scan_network_province(self, value):
        self._scan_network_province = value
    @property
    def scan_time(self):
        return self._scan_time

    @scan_time.setter
    def scan_time(self, value):
        self._scan_time = value
    @property
    def scan_type(self):
        return self._scan_type

    @scan_type.setter
    def scan_type(self, value):
        self._scan_type = value
    @property
    def staff_contact(self):
        return self._staff_contact

    @staff_contact.setter
    def staff_contact(self, value):
        self._staff_contact = value
    @property
    def staff_name(self):
        return self._staff_name

    @staff_name.setter
    def staff_name(self, value):
        self._staff_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_code:
            if hasattr(self.bill_code, 'to_alipay_dict'):
                params['bill_code'] = self.bill_code.to_alipay_dict()
            else:
                params['bill_code'] = self.bill_code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.next_network_area_name:
            if hasattr(self.next_network_area_name, 'to_alipay_dict'):
                params['next_network_area_name'] = self.next_network_area_name.to_alipay_dict()
            else:
                params['next_network_area_name'] = self.next_network_area_name
        if self.next_network_city_name:
            if hasattr(self.next_network_city_name, 'to_alipay_dict'):
                params['next_network_city_name'] = self.next_network_city_name.to_alipay_dict()
            else:
                params['next_network_city_name'] = self.next_network_city_name
        if self.next_network_province_name:
            if hasattr(self.next_network_province_name, 'to_alipay_dict'):
                params['next_network_province_name'] = self.next_network_province_name.to_alipay_dict()
            else:
                params['next_network_province_name'] = self.next_network_province_name
        if self.next_stop_name:
            if hasattr(self.next_stop_name, 'to_alipay_dict'):
                params['next_stop_name'] = self.next_stop_name.to_alipay_dict()
            else:
                params['next_stop_name'] = self.next_stop_name
        if self.problem_type:
            if hasattr(self.problem_type, 'to_alipay_dict'):
                params['problem_type'] = self.problem_type.to_alipay_dict()
            else:
                params['problem_type'] = self.problem_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scan_network_area:
            if hasattr(self.scan_network_area, 'to_alipay_dict'):
                params['scan_network_area'] = self.scan_network_area.to_alipay_dict()
            else:
                params['scan_network_area'] = self.scan_network_area
        if self.scan_network_city:
            if hasattr(self.scan_network_city, 'to_alipay_dict'):
                params['scan_network_city'] = self.scan_network_city.to_alipay_dict()
            else:
                params['scan_network_city'] = self.scan_network_city
        if self.scan_network_contact:
            if hasattr(self.scan_network_contact, 'to_alipay_dict'):
                params['scan_network_contact'] = self.scan_network_contact.to_alipay_dict()
            else:
                params['scan_network_contact'] = self.scan_network_contact
        if self.scan_network_id:
            if hasattr(self.scan_network_id, 'to_alipay_dict'):
                params['scan_network_id'] = self.scan_network_id.to_alipay_dict()
            else:
                params['scan_network_id'] = self.scan_network_id
        if self.scan_network_name:
            if hasattr(self.scan_network_name, 'to_alipay_dict'):
                params['scan_network_name'] = self.scan_network_name.to_alipay_dict()
            else:
                params['scan_network_name'] = self.scan_network_name
        if self.scan_network_province:
            if hasattr(self.scan_network_province, 'to_alipay_dict'):
                params['scan_network_province'] = self.scan_network_province.to_alipay_dict()
            else:
                params['scan_network_province'] = self.scan_network_province
        if self.scan_time:
            if hasattr(self.scan_time, 'to_alipay_dict'):
                params['scan_time'] = self.scan_time.to_alipay_dict()
            else:
                params['scan_time'] = self.scan_time
        if self.scan_type:
            if hasattr(self.scan_type, 'to_alipay_dict'):
                params['scan_type'] = self.scan_type.to_alipay_dict()
            else:
                params['scan_type'] = self.scan_type
        if self.staff_contact:
            if hasattr(self.staff_contact, 'to_alipay_dict'):
                params['staff_contact'] = self.staff_contact.to_alipay_dict()
            else:
                params['staff_contact'] = self.staff_contact
        if self.staff_name:
            if hasattr(self.staff_name, 'to_alipay_dict'):
                params['staff_name'] = self.staff_name.to_alipay_dict()
            else:
                params['staff_name'] = self.staff_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JTQueryDetails()
        if 'bill_code' in d:
            o.bill_code = d['bill_code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'next_network_area_name' in d:
            o.next_network_area_name = d['next_network_area_name']
        if 'next_network_city_name' in d:
            o.next_network_city_name = d['next_network_city_name']
        if 'next_network_province_name' in d:
            o.next_network_province_name = d['next_network_province_name']
        if 'next_stop_name' in d:
            o.next_stop_name = d['next_stop_name']
        if 'problem_type' in d:
            o.problem_type = d['problem_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scan_network_area' in d:
            o.scan_network_area = d['scan_network_area']
        if 'scan_network_city' in d:
            o.scan_network_city = d['scan_network_city']
        if 'scan_network_contact' in d:
            o.scan_network_contact = d['scan_network_contact']
        if 'scan_network_id' in d:
            o.scan_network_id = d['scan_network_id']
        if 'scan_network_name' in d:
            o.scan_network_name = d['scan_network_name']
        if 'scan_network_province' in d:
            o.scan_network_province = d['scan_network_province']
        if 'scan_time' in d:
            o.scan_time = d['scan_time']
        if 'scan_type' in d:
            o.scan_type = d['scan_type']
        if 'staff_contact' in d:
            o.staff_contact = d['staff_contact']
        if 'staff_name' in d:
            o.staff_name = d['staff_name']
        return o


