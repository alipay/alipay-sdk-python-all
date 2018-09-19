#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoLogisticsExpressNonserviceQueryModel(object):

    def __init__(self):
        self._logis_merch_code = None

    @property
    def logis_merch_code(self):
        return self._logis_merch_code

    @logis_merch_code.setter
    def logis_merch_code(self, value):
        self._logis_merch_code = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayEcoLogisticsExpressNonserviceQueryModel()
        if 'logis_merch_code' in d:
            o.logis_merch_code = d['logis_merch_code']
        return o


