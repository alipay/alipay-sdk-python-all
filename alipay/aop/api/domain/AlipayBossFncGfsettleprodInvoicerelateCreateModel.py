#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RelateInputInvoiceOrderDTO import RelateInputInvoiceOrderDTO


class AlipayBossFncGfsettleprodInvoicerelateCreateModel(object):

    def __init__(self):
        self._relate_input_invoice_order_dto = None

    @property
    def relate_input_invoice_order_dto(self):
        return self._relate_input_invoice_order_dto

    @relate_input_invoice_order_dto.setter
    def relate_input_invoice_order_dto(self, value):
        if isinstance(value, RelateInputInvoiceOrderDTO):
            self._relate_input_invoice_order_dto = value
        else:
            self._relate_input_invoice_order_dto = RelateInputInvoiceOrderDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.relate_input_invoice_order_dto:
            if hasattr(self.relate_input_invoice_order_dto, 'to_alipay_dict'):
                params['relate_input_invoice_order_dto'] = self.relate_input_invoice_order_dto.to_alipay_dict()
            else:
                params['relate_input_invoice_order_dto'] = self.relate_input_invoice_order_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoicerelateCreateModel()
        if 'relate_input_invoice_order_dto' in d:
            o.relate_input_invoice_order_dto = d['relate_input_invoice_order_dto']
        return o


