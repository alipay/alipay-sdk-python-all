#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinancePfPaymentQueryModel(object):

    def __init__(self):
        self._buss_refr_no = None
        self._financing_id = None
        self._platform_id = None

    @property
    def buss_refr_no(self):
        return self._buss_refr_no

    @buss_refr_no.setter
    def buss_refr_no(self, value):
        self._buss_refr_no = value
    @property
    def financing_id(self):
        return self._financing_id

    @financing_id.setter
    def financing_id(self, value):
        self._financing_id = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buss_refr_no:
            if hasattr(self.buss_refr_no, 'to_alipay_dict'):
                params['buss_refr_no'] = self.buss_refr_no.to_alipay_dict()
            else:
                params['buss_refr_no'] = self.buss_refr_no
        if self.financing_id:
            if hasattr(self.financing_id, 'to_alipay_dict'):
                params['financing_id'] = self.financing_id.to_alipay_dict()
            else:
                params['financing_id'] = self.financing_id
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinancePfPaymentQueryModel()
        if 'buss_refr_no' in d:
            o.buss_refr_no = d['buss_refr_no']
        if 'financing_id' in d:
            o.financing_id = d['financing_id']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        return o


