#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinDataserviceRegioninfoQueryModel(object):

    def __init__(self):
        self._region_codes = None
        self._region_type = None

    @property
    def region_codes(self):
        return self._region_codes

    @region_codes.setter
    def region_codes(self, value):
        if isinstance(value, list):
            self._region_codes = list()
            for i in value:
                self._region_codes.append(i)
    @property
    def region_type(self):
        return self._region_type

    @region_type.setter
    def region_type(self, value):
        self._region_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.region_codes:
            if isinstance(self.region_codes, list):
                for i in range(0, len(self.region_codes)):
                    element = self.region_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_codes[i] = element.to_alipay_dict()
            if hasattr(self.region_codes, 'to_alipay_dict'):
                params['region_codes'] = self.region_codes.to_alipay_dict()
            else:
                params['region_codes'] = self.region_codes
        if self.region_type:
            if hasattr(self.region_type, 'to_alipay_dict'):
                params['region_type'] = self.region_type.to_alipay_dict()
            else:
                params['region_type'] = self.region_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinDataserviceRegioninfoQueryModel()
        if 'region_codes' in d:
            o.region_codes = d['region_codes']
        if 'region_type' in d:
            o.region_type = d['region_type']
        return o


