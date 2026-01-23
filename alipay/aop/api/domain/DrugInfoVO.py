#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrugInfoVO(object):

    def __init__(self):
        self._drug_cnt = None
        self._drug_spec = None
        self._drug_unit = None
        self._generic_name = None
        self._usage_dosage = None

    @property
    def drug_cnt(self):
        return self._drug_cnt

    @drug_cnt.setter
    def drug_cnt(self, value):
        self._drug_cnt = value
    @property
    def drug_spec(self):
        return self._drug_spec

    @drug_spec.setter
    def drug_spec(self, value):
        self._drug_spec = value
    @property
    def drug_unit(self):
        return self._drug_unit

    @drug_unit.setter
    def drug_unit(self, value):
        self._drug_unit = value
    @property
    def generic_name(self):
        return self._generic_name

    @generic_name.setter
    def generic_name(self, value):
        self._generic_name = value
    @property
    def usage_dosage(self):
        return self._usage_dosage

    @usage_dosage.setter
    def usage_dosage(self, value):
        self._usage_dosage = value


    def to_alipay_dict(self):
        params = dict()
        if self.drug_cnt:
            if hasattr(self.drug_cnt, 'to_alipay_dict'):
                params['drug_cnt'] = self.drug_cnt.to_alipay_dict()
            else:
                params['drug_cnt'] = self.drug_cnt
        if self.drug_spec:
            if hasattr(self.drug_spec, 'to_alipay_dict'):
                params['drug_spec'] = self.drug_spec.to_alipay_dict()
            else:
                params['drug_spec'] = self.drug_spec
        if self.drug_unit:
            if hasattr(self.drug_unit, 'to_alipay_dict'):
                params['drug_unit'] = self.drug_unit.to_alipay_dict()
            else:
                params['drug_unit'] = self.drug_unit
        if self.generic_name:
            if hasattr(self.generic_name, 'to_alipay_dict'):
                params['generic_name'] = self.generic_name.to_alipay_dict()
            else:
                params['generic_name'] = self.generic_name
        if self.usage_dosage:
            if hasattr(self.usage_dosage, 'to_alipay_dict'):
                params['usage_dosage'] = self.usage_dosage.to_alipay_dict()
            else:
                params['usage_dosage'] = self.usage_dosage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrugInfoVO()
        if 'drug_cnt' in d:
            o.drug_cnt = d['drug_cnt']
        if 'drug_spec' in d:
            o.drug_spec = d['drug_spec']
        if 'drug_unit' in d:
            o.drug_unit = d['drug_unit']
        if 'generic_name' in d:
            o.generic_name = d['generic_name']
        if 'usage_dosage' in d:
            o.usage_dosage = d['usage_dosage']
        return o


