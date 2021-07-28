#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayContractBaseDTO import PayContractBaseDTO


class AlipayBossFncGfsettlePaycontractQueryModel(object):

    def __init__(self):
        self._pay_contract_base_dto = None

    @property
    def pay_contract_base_dto(self):
        return self._pay_contract_base_dto

    @pay_contract_base_dto.setter
    def pay_contract_base_dto(self, value):
        if isinstance(value, PayContractBaseDTO):
            self._pay_contract_base_dto = value
        else:
            self._pay_contract_base_dto = PayContractBaseDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.pay_contract_base_dto:
            if hasattr(self.pay_contract_base_dto, 'to_alipay_dict'):
                params['pay_contract_base_dto'] = self.pay_contract_base_dto.to_alipay_dict()
            else:
                params['pay_contract_base_dto'] = self.pay_contract_base_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettlePaycontractQueryModel()
        if 'pay_contract_base_dto' in d:
            o.pay_contract_base_dto = d['pay_contract_base_dto']
        return o


