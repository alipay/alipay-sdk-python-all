#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayContractBaseDTO import PayContractBaseDTO


class AlipayBossFncGfsettlePaycontractConfirmModel(object):

    def __init__(self):
        self._paycontractbasedto = None

    @property
    def paycontractbasedto(self):
        return self._paycontractbasedto

    @paycontractbasedto.setter
    def paycontractbasedto(self, value):
        if isinstance(value, PayContractBaseDTO):
            self._paycontractbasedto = value
        else:
            self._paycontractbasedto = PayContractBaseDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.paycontractbasedto:
            if hasattr(self.paycontractbasedto, 'to_alipay_dict'):
                params['paycontractbasedto'] = self.paycontractbasedto.to_alipay_dict()
            else:
                params['paycontractbasedto'] = self.paycontractbasedto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettlePaycontractConfirmModel()
        if 'paycontractbasedto' in d:
            o.paycontractbasedto = d['paycontractbasedto']
        return o


