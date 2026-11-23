#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterNumber(object):

    def __init__(self):
        self._department_id = None
        self._doctor_id = None
        self._hospital_id = None
        self._isv_code = None
        self._number_ids = None
        self._number_seq_nos = None
        self._number_tag_desc = None
        self._period = None
        self._platform_code = None
        self._register_date = None
        self._register_fee = None
        self._register_id = None
        self._register_time = None
        self._unit = None
        self._visit_type = None
        self._visit_type_desc = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def number_ids(self):
        return self._number_ids

    @number_ids.setter
    def number_ids(self, value):
        if isinstance(value, list):
            self._number_ids = list()
            for i in value:
                self._number_ids.append(i)
    @property
    def number_seq_nos(self):
        return self._number_seq_nos

    @number_seq_nos.setter
    def number_seq_nos(self, value):
        if isinstance(value, list):
            self._number_seq_nos = list()
            for i in value:
                self._number_seq_nos.append(i)
    @property
    def number_tag_desc(self):
        return self._number_tag_desc

    @number_tag_desc.setter
    def number_tag_desc(self, value):
        self._number_tag_desc = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def register_fee(self):
        return self._register_fee

    @register_fee.setter
    def register_fee(self, value):
        self._register_fee = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value
    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def visit_type(self):
        return self._visit_type

    @visit_type.setter
    def visit_type(self, value):
        self._visit_type = value
    @property
    def visit_type_desc(self):
        return self._visit_type_desc

    @visit_type_desc.setter
    def visit_type_desc(self, value):
        self._visit_type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.number_ids:
            if isinstance(self.number_ids, list):
                for i in range(0, len(self.number_ids)):
                    element = self.number_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.number_ids[i] = element.to_alipay_dict()
            if hasattr(self.number_ids, 'to_alipay_dict'):
                params['number_ids'] = self.number_ids.to_alipay_dict()
            else:
                params['number_ids'] = self.number_ids
        if self.number_seq_nos:
            if isinstance(self.number_seq_nos, list):
                for i in range(0, len(self.number_seq_nos)):
                    element = self.number_seq_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.number_seq_nos[i] = element.to_alipay_dict()
            if hasattr(self.number_seq_nos, 'to_alipay_dict'):
                params['number_seq_nos'] = self.number_seq_nos.to_alipay_dict()
            else:
                params['number_seq_nos'] = self.number_seq_nos
        if self.number_tag_desc:
            if hasattr(self.number_tag_desc, 'to_alipay_dict'):
                params['number_tag_desc'] = self.number_tag_desc.to_alipay_dict()
            else:
                params['number_tag_desc'] = self.number_tag_desc
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.register_fee:
            if hasattr(self.register_fee, 'to_alipay_dict'):
                params['register_fee'] = self.register_fee.to_alipay_dict()
            else:
                params['register_fee'] = self.register_fee
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.visit_type:
            if hasattr(self.visit_type, 'to_alipay_dict'):
                params['visit_type'] = self.visit_type.to_alipay_dict()
            else:
                params['visit_type'] = self.visit_type
        if self.visit_type_desc:
            if hasattr(self.visit_type_desc, 'to_alipay_dict'):
                params['visit_type_desc'] = self.visit_type_desc.to_alipay_dict()
            else:
                params['visit_type_desc'] = self.visit_type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterNumber()
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'number_ids' in d:
            o.number_ids = d['number_ids']
        if 'number_seq_nos' in d:
            o.number_seq_nos = d['number_seq_nos']
        if 'number_tag_desc' in d:
            o.number_tag_desc = d['number_tag_desc']
        if 'period' in d:
            o.period = d['period']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'register_fee' in d:
            o.register_fee = d['register_fee']
        if 'register_id' in d:
            o.register_id = d['register_id']
        if 'register_time' in d:
            o.register_time = d['register_time']
        if 'unit' in d:
            o.unit = d['unit']
        if 'visit_type' in d:
            o.visit_type = d['visit_type']
        if 'visit_type_desc' in d:
            o.visit_type_desc = d['visit_type_desc']
        return o


