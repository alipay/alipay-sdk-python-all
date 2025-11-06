#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicineFrequency import MedicineFrequency


class MedicineHistory(object):

    def __init__(self):
        self._medication_end_date = None
        self._medication_start_date = None
        self._medicine_frequency = None
        self._medicine_name = None

    @property
    def medication_end_date(self):
        return self._medication_end_date

    @medication_end_date.setter
    def medication_end_date(self, value):
        self._medication_end_date = value
    @property
    def medication_start_date(self):
        return self._medication_start_date

    @medication_start_date.setter
    def medication_start_date(self, value):
        self._medication_start_date = value
    @property
    def medicine_frequency(self):
        return self._medicine_frequency

    @medicine_frequency.setter
    def medicine_frequency(self, value):
        if isinstance(value, MedicineFrequency):
            self._medicine_frequency = value
        else:
            self._medicine_frequency = MedicineFrequency.from_alipay_dict(value)
    @property
    def medicine_name(self):
        return self._medicine_name

    @medicine_name.setter
    def medicine_name(self, value):
        self._medicine_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.medication_end_date:
            if hasattr(self.medication_end_date, 'to_alipay_dict'):
                params['medication_end_date'] = self.medication_end_date.to_alipay_dict()
            else:
                params['medication_end_date'] = self.medication_end_date
        if self.medication_start_date:
            if hasattr(self.medication_start_date, 'to_alipay_dict'):
                params['medication_start_date'] = self.medication_start_date.to_alipay_dict()
            else:
                params['medication_start_date'] = self.medication_start_date
        if self.medicine_frequency:
            if hasattr(self.medicine_frequency, 'to_alipay_dict'):
                params['medicine_frequency'] = self.medicine_frequency.to_alipay_dict()
            else:
                params['medicine_frequency'] = self.medicine_frequency
        if self.medicine_name:
            if hasattr(self.medicine_name, 'to_alipay_dict'):
                params['medicine_name'] = self.medicine_name.to_alipay_dict()
            else:
                params['medicine_name'] = self.medicine_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicineHistory()
        if 'medication_end_date' in d:
            o.medication_end_date = d['medication_end_date']
        if 'medication_start_date' in d:
            o.medication_start_date = d['medication_start_date']
        if 'medicine_frequency' in d:
            o.medicine_frequency = d['medicine_frequency']
        if 'medicine_name' in d:
            o.medicine_name = d['medicine_name']
        return o


