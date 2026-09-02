#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalRecord(object):

    def __init__(self):
        self._md_date = None
        self._mdtrt_id = None
        self._med_type = None
        self._medical_org_campus_id = None
        self._medical_org_id = None

    @property
    def md_date(self):
        return self._md_date

    @md_date.setter
    def md_date(self, value):
        self._md_date = value
    @property
    def mdtrt_id(self):
        return self._mdtrt_id

    @mdtrt_id.setter
    def mdtrt_id(self, value):
        self._mdtrt_id = value
    @property
    def med_type(self):
        return self._med_type

    @med_type.setter
    def med_type(self, value):
        self._med_type = value
    @property
    def medical_org_campus_id(self):
        return self._medical_org_campus_id

    @medical_org_campus_id.setter
    def medical_org_campus_id(self, value):
        self._medical_org_campus_id = value
    @property
    def medical_org_id(self):
        return self._medical_org_id

    @medical_org_id.setter
    def medical_org_id(self, value):
        self._medical_org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.md_date:
            if hasattr(self.md_date, 'to_alipay_dict'):
                params['md_date'] = self.md_date.to_alipay_dict()
            else:
                params['md_date'] = self.md_date
        if self.mdtrt_id:
            if hasattr(self.mdtrt_id, 'to_alipay_dict'):
                params['mdtrt_id'] = self.mdtrt_id.to_alipay_dict()
            else:
                params['mdtrt_id'] = self.mdtrt_id
        if self.med_type:
            if hasattr(self.med_type, 'to_alipay_dict'):
                params['med_type'] = self.med_type.to_alipay_dict()
            else:
                params['med_type'] = self.med_type
        if self.medical_org_campus_id:
            if hasattr(self.medical_org_campus_id, 'to_alipay_dict'):
                params['medical_org_campus_id'] = self.medical_org_campus_id.to_alipay_dict()
            else:
                params['medical_org_campus_id'] = self.medical_org_campus_id
        if self.medical_org_id:
            if hasattr(self.medical_org_id, 'to_alipay_dict'):
                params['medical_org_id'] = self.medical_org_id.to_alipay_dict()
            else:
                params['medical_org_id'] = self.medical_org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRecord()
        if 'md_date' in d:
            o.md_date = d['md_date']
        if 'mdtrt_id' in d:
            o.mdtrt_id = d['mdtrt_id']
        if 'med_type' in d:
            o.med_type = d['med_type']
        if 'medical_org_campus_id' in d:
            o.medical_org_campus_id = d['medical_org_campus_id']
        if 'medical_org_id' in d:
            o.medical_org_id = d['medical_org_id']
        return o


