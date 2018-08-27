#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AreaCode import AreaCode


class AlipayEcoLogisticsExpressNonserviceModifyModel(object):

    def __init__(self):
        self._area_codes = None
        self._logis_merch_code = None

    @property
    def area_codes(self):
        return self._area_codes

    @area_codes.setter
    def area_codes(self, value):
        if isinstance(value, list):
            self._area_codes = list()
            for i in value:
                if isinstance(i, AreaCode):
                    self._area_codes.append(i)
                else:
                    self._area_codes.append(AreaCode.from_alipay_dict(i))
    @property
    def logis_merch_code(self):
        return self._logis_merch_code

    @logis_merch_code.setter
    def logis_merch_code(self, value):
        self._logis_merch_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_codes:
            if isinstance(self.area_codes, list):
                for i in range(0, len(self.area_codes)):
                    element = self.area_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.area_codes[i] = element.to_alipay_dict()
            if hasattr(self.area_codes, 'to_alipay_dict'):
                params['area_codes'] = self.area_codes.to_alipay_dict()
            else:
                params['area_codes'] = self.area_codes
        if self.logis_merch_code:
            if hasattr(self.logis_merch_code, 'to_alipay_dict'):
                params['logis_merch_code'] = self.logis_merch_code.to_alipay_dict()
            else:
                params['logis_merch_code'] = self.logis_merch_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoLogisticsExpressNonserviceModifyModel()
        if 'area_codes' in d:
            o.area_codes = d['area_codes']
        if 'logis_merch_code' in d:
            o.logis_merch_code = d['logis_merch_code']
        return o


