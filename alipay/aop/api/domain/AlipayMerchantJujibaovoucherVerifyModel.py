#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChinaMobileContractRoot import ChinaMobileContractRoot


class AlipayMerchantJujibaovoucherVerifyModel(object):

    def __init__(self):
        self._contract_root = None

    @property
    def contract_root(self):
        return self._contract_root

    @contract_root.setter
    def contract_root(self, value):
        if isinstance(value, ChinaMobileContractRoot):
            self._contract_root = value
        else:
            self._contract_root = ChinaMobileContractRoot.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.contract_root:
            if hasattr(self.contract_root, 'to_alipay_dict'):
                params['contract_root'] = self.contract_root.to_alipay_dict()
            else:
                params['contract_root'] = self.contract_root
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantJujibaovoucherVerifyModel()
        if 'contract_root' in d:
            o.contract_root = d['contract_root']
        return o


