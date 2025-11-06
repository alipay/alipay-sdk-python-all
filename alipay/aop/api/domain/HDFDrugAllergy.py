#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFDrugAllergy(object):

    def __init__(self):
        self._allergy_desc = None
        self._is_allergy = None

    @property
    def allergy_desc(self):
        return self._allergy_desc

    @allergy_desc.setter
    def allergy_desc(self, value):
        self._allergy_desc = value
    @property
    def is_allergy(self):
        return self._is_allergy

    @is_allergy.setter
    def is_allergy(self, value):
        self._is_allergy = value


    def to_alipay_dict(self):
        params = dict()
        if self.allergy_desc:
            if hasattr(self.allergy_desc, 'to_alipay_dict'):
                params['allergy_desc'] = self.allergy_desc.to_alipay_dict()
            else:
                params['allergy_desc'] = self.allergy_desc
        if self.is_allergy:
            if hasattr(self.is_allergy, 'to_alipay_dict'):
                params['is_allergy'] = self.is_allergy.to_alipay_dict()
            else:
                params['is_allergy'] = self.is_allergy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFDrugAllergy()
        if 'allergy_desc' in d:
            o.allergy_desc = d['allergy_desc']
        if 'is_allergy' in d:
            o.is_allergy = d['is_allergy']
        return o


