#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFMedicineCondition(object):

    def __init__(self):
        self._medicine_desc = None
        self._medicine_name = None
        self._patient_attachment_ids = None

    @property
    def medicine_desc(self):
        return self._medicine_desc

    @medicine_desc.setter
    def medicine_desc(self, value):
        self._medicine_desc = value
    @property
    def medicine_name(self):
        return self._medicine_name

    @medicine_name.setter
    def medicine_name(self, value):
        self._medicine_name = value
    @property
    def patient_attachment_ids(self):
        return self._patient_attachment_ids

    @patient_attachment_ids.setter
    def patient_attachment_ids(self, value):
        if isinstance(value, list):
            self._patient_attachment_ids = list()
            for i in value:
                self._patient_attachment_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.medicine_desc:
            if hasattr(self.medicine_desc, 'to_alipay_dict'):
                params['medicine_desc'] = self.medicine_desc.to_alipay_dict()
            else:
                params['medicine_desc'] = self.medicine_desc
        if self.medicine_name:
            if hasattr(self.medicine_name, 'to_alipay_dict'):
                params['medicine_name'] = self.medicine_name.to_alipay_dict()
            else:
                params['medicine_name'] = self.medicine_name
        if self.patient_attachment_ids:
            if isinstance(self.patient_attachment_ids, list):
                for i in range(0, len(self.patient_attachment_ids)):
                    element = self.patient_attachment_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.patient_attachment_ids[i] = element.to_alipay_dict()
            if hasattr(self.patient_attachment_ids, 'to_alipay_dict'):
                params['patient_attachment_ids'] = self.patient_attachment_ids.to_alipay_dict()
            else:
                params['patient_attachment_ids'] = self.patient_attachment_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFMedicineCondition()
        if 'medicine_desc' in d:
            o.medicine_desc = d['medicine_desc']
        if 'medicine_name' in d:
            o.medicine_name = d['medicine_name']
        if 'patient_attachment_ids' in d:
            o.patient_attachment_ids = d['patient_attachment_ids']
        return o


