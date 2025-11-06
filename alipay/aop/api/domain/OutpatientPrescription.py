#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TraditionalChineseMedicine import TraditionalChineseMedicine
from alipay.aop.api.domain.WesternMedicine import WesternMedicine


class OutpatientPrescription(object):

    def __init__(self):
        self._data_id = None
        self._date = None
        self._department_name = None
        self._hospital_name = None
        self._result = None
        self._traditional_chinese_medicine = None
        self._type = None
        self._western_medicine = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def traditional_chinese_medicine(self):
        return self._traditional_chinese_medicine

    @traditional_chinese_medicine.setter
    def traditional_chinese_medicine(self, value):
        if isinstance(value, TraditionalChineseMedicine):
            self._traditional_chinese_medicine = value
        else:
            self._traditional_chinese_medicine = TraditionalChineseMedicine.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def western_medicine(self):
        return self._western_medicine

    @western_medicine.setter
    def western_medicine(self, value):
        if isinstance(value, WesternMedicine):
            self._western_medicine = value
        else:
            self._western_medicine = WesternMedicine.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.traditional_chinese_medicine:
            if hasattr(self.traditional_chinese_medicine, 'to_alipay_dict'):
                params['traditional_chinese_medicine'] = self.traditional_chinese_medicine.to_alipay_dict()
            else:
                params['traditional_chinese_medicine'] = self.traditional_chinese_medicine
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.western_medicine:
            if hasattr(self.western_medicine, 'to_alipay_dict'):
                params['western_medicine'] = self.western_medicine.to_alipay_dict()
            else:
                params['western_medicine'] = self.western_medicine
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutpatientPrescription()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'date' in d:
            o.date = d['date']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'result' in d:
            o.result = d['result']
        if 'traditional_chinese_medicine' in d:
            o.traditional_chinese_medicine = d['traditional_chinese_medicine']
        if 'type' in d:
            o.type = d['type']
        if 'western_medicine' in d:
            o.western_medicine = d['western_medicine']
        return o


