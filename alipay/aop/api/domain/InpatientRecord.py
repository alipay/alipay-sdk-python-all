#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SurgeryInfo import SurgeryInfo


class InpatientRecord(object):

    def __init__(self):
        self._data_id = None
        self._days = None
        self._department_name = None
        self._hospital_name = None
        self._in_date = None
        self._recovery_date = None
        self._recovery_department_name = None
        self._recovery_memo = None
        self._surgery_info = None
        self._traditional_chinese_medicine_diagnosis = None
        self._way = None
        self._western_medicine_diagnosis = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        self._days = value
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
    def in_date(self):
        return self._in_date

    @in_date.setter
    def in_date(self, value):
        self._in_date = value
    @property
    def recovery_date(self):
        return self._recovery_date

    @recovery_date.setter
    def recovery_date(self, value):
        self._recovery_date = value
    @property
    def recovery_department_name(self):
        return self._recovery_department_name

    @recovery_department_name.setter
    def recovery_department_name(self, value):
        self._recovery_department_name = value
    @property
    def recovery_memo(self):
        return self._recovery_memo

    @recovery_memo.setter
    def recovery_memo(self, value):
        self._recovery_memo = value
    @property
    def surgery_info(self):
        return self._surgery_info

    @surgery_info.setter
    def surgery_info(self, value):
        if isinstance(value, SurgeryInfo):
            self._surgery_info = value
        else:
            self._surgery_info = SurgeryInfo.from_alipay_dict(value)
    @property
    def traditional_chinese_medicine_diagnosis(self):
        return self._traditional_chinese_medicine_diagnosis

    @traditional_chinese_medicine_diagnosis.setter
    def traditional_chinese_medicine_diagnosis(self, value):
        self._traditional_chinese_medicine_diagnosis = value
    @property
    def way(self):
        return self._way

    @way.setter
    def way(self, value):
        self._way = value
    @property
    def western_medicine_diagnosis(self):
        return self._western_medicine_diagnosis

    @western_medicine_diagnosis.setter
    def western_medicine_diagnosis(self, value):
        self._western_medicine_diagnosis = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.days:
            if hasattr(self.days, 'to_alipay_dict'):
                params['days'] = self.days.to_alipay_dict()
            else:
                params['days'] = self.days
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
        if self.in_date:
            if hasattr(self.in_date, 'to_alipay_dict'):
                params['in_date'] = self.in_date.to_alipay_dict()
            else:
                params['in_date'] = self.in_date
        if self.recovery_date:
            if hasattr(self.recovery_date, 'to_alipay_dict'):
                params['recovery_date'] = self.recovery_date.to_alipay_dict()
            else:
                params['recovery_date'] = self.recovery_date
        if self.recovery_department_name:
            if hasattr(self.recovery_department_name, 'to_alipay_dict'):
                params['recovery_department_name'] = self.recovery_department_name.to_alipay_dict()
            else:
                params['recovery_department_name'] = self.recovery_department_name
        if self.recovery_memo:
            if hasattr(self.recovery_memo, 'to_alipay_dict'):
                params['recovery_memo'] = self.recovery_memo.to_alipay_dict()
            else:
                params['recovery_memo'] = self.recovery_memo
        if self.surgery_info:
            if hasattr(self.surgery_info, 'to_alipay_dict'):
                params['surgery_info'] = self.surgery_info.to_alipay_dict()
            else:
                params['surgery_info'] = self.surgery_info
        if self.traditional_chinese_medicine_diagnosis:
            if hasattr(self.traditional_chinese_medicine_diagnosis, 'to_alipay_dict'):
                params['traditional_chinese_medicine_diagnosis'] = self.traditional_chinese_medicine_diagnosis.to_alipay_dict()
            else:
                params['traditional_chinese_medicine_diagnosis'] = self.traditional_chinese_medicine_diagnosis
        if self.way:
            if hasattr(self.way, 'to_alipay_dict'):
                params['way'] = self.way.to_alipay_dict()
            else:
                params['way'] = self.way
        if self.western_medicine_diagnosis:
            if hasattr(self.western_medicine_diagnosis, 'to_alipay_dict'):
                params['western_medicine_diagnosis'] = self.western_medicine_diagnosis.to_alipay_dict()
            else:
                params['western_medicine_diagnosis'] = self.western_medicine_diagnosis
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InpatientRecord()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'days' in d:
            o.days = d['days']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'in_date' in d:
            o.in_date = d['in_date']
        if 'recovery_date' in d:
            o.recovery_date = d['recovery_date']
        if 'recovery_department_name' in d:
            o.recovery_department_name = d['recovery_department_name']
        if 'recovery_memo' in d:
            o.recovery_memo = d['recovery_memo']
        if 'surgery_info' in d:
            o.surgery_info = d['surgery_info']
        if 'traditional_chinese_medicine_diagnosis' in d:
            o.traditional_chinese_medicine_diagnosis = d['traditional_chinese_medicine_diagnosis']
        if 'way' in d:
            o.way = d['way']
        if 'western_medicine_diagnosis' in d:
            o.western_medicine_diagnosis = d['western_medicine_diagnosis']
        return o


