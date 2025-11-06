#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicationGuidanceItem(object):

    def __init__(self):
        self._cautions_desc = None
        self._drug_name = None
        self._drug_specifications = None

    @property
    def cautions_desc(self):
        return self._cautions_desc

    @cautions_desc.setter
    def cautions_desc(self, value):
        self._cautions_desc = value
    @property
    def drug_name(self):
        return self._drug_name

    @drug_name.setter
    def drug_name(self, value):
        self._drug_name = value
    @property
    def drug_specifications(self):
        return self._drug_specifications

    @drug_specifications.setter
    def drug_specifications(self, value):
        self._drug_specifications = value


    def to_alipay_dict(self):
        params = dict()
        if self.cautions_desc:
            if hasattr(self.cautions_desc, 'to_alipay_dict'):
                params['cautions_desc'] = self.cautions_desc.to_alipay_dict()
            else:
                params['cautions_desc'] = self.cautions_desc
        if self.drug_name:
            if hasattr(self.drug_name, 'to_alipay_dict'):
                params['drug_name'] = self.drug_name.to_alipay_dict()
            else:
                params['drug_name'] = self.drug_name
        if self.drug_specifications:
            if hasattr(self.drug_specifications, 'to_alipay_dict'):
                params['drug_specifications'] = self.drug_specifications.to_alipay_dict()
            else:
                params['drug_specifications'] = self.drug_specifications
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicationGuidanceItem()
        if 'cautions_desc' in d:
            o.cautions_desc = d['cautions_desc']
        if 'drug_name' in d:
            o.drug_name = d['drug_name']
        if 'drug_specifications' in d:
            o.drug_specifications = d['drug_specifications']
        return o


