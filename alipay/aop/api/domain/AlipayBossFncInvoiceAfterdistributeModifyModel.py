#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceModifyAfterDistributeDTO import InputInvoiceModifyAfterDistributeDTO


class AlipayBossFncInvoiceAfterdistributeModifyModel(object):

    def __init__(self):
        self._input_invoice_modify_after_distribute_dto = None

    @property
    def input_invoice_modify_after_distribute_dto(self):
        return self._input_invoice_modify_after_distribute_dto

    @input_invoice_modify_after_distribute_dto.setter
    def input_invoice_modify_after_distribute_dto(self, value):
        if isinstance(value, InputInvoiceModifyAfterDistributeDTO):
            self._input_invoice_modify_after_distribute_dto = value
        else:
            self._input_invoice_modify_after_distribute_dto = InputInvoiceModifyAfterDistributeDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.input_invoice_modify_after_distribute_dto:
            if hasattr(self.input_invoice_modify_after_distribute_dto, 'to_alipay_dict'):
                params['input_invoice_modify_after_distribute_dto'] = self.input_invoice_modify_after_distribute_dto.to_alipay_dict()
            else:
                params['input_invoice_modify_after_distribute_dto'] = self.input_invoice_modify_after_distribute_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoiceAfterdistributeModifyModel()
        if 'input_invoice_modify_after_distribute_dto' in d:
            o.input_invoice_modify_after_distribute_dto = d['input_invoice_modify_after_distribute_dto']
        return o


