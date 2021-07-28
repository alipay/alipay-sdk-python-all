#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayContractDTO import PayContractDTO


class AlipayBossProdGfsettlePaycontractModifyModel(object):

    def __init__(self):
        self._paycontract = None

    @property
    def paycontract(self):
        return self._paycontract

    @paycontract.setter
    def paycontract(self, value):
        if isinstance(value, PayContractDTO):
            self._paycontract = value
        else:
            self._paycontract = PayContractDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.paycontract:
            if hasattr(self.paycontract, 'to_alipay_dict'):
                params['paycontract'] = self.paycontract.to_alipay_dict()
            else:
                params['paycontract'] = self.paycontract
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdGfsettlePaycontractModifyModel()
        if 'paycontract' in d:
            o.paycontract = d['paycontract']
        return o


