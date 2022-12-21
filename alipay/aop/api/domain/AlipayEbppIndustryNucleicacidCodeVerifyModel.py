#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryNucleicacidCodeVerifyModel(object):

    def __init__(self):
        self._nucleic_acid_code = None

    @property
    def nucleic_acid_code(self):
        return self._nucleic_acid_code

    @nucleic_acid_code.setter
    def nucleic_acid_code(self, value):
        self._nucleic_acid_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.nucleic_acid_code:
            if hasattr(self.nucleic_acid_code, 'to_alipay_dict'):
                params['nucleic_acid_code'] = self.nucleic_acid_code.to_alipay_dict()
            else:
                params['nucleic_acid_code'] = self.nucleic_acid_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryNucleicacidCodeVerifyModel()
        if 'nucleic_acid_code' in d:
            o.nucleic_acid_code = d['nucleic_acid_code']
        return o


