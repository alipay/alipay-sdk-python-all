#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizInvoiceBillInfoDTO import BizInvoiceBillInfoDTO


class AlipayBossFncGfsmartpaySyncinvoicebillinfoCreateModel(object):

    def __init__(self):
        self._invoice_bill_info_dto = None

    @property
    def invoice_bill_info_dto(self):
        return self._invoice_bill_info_dto

    @invoice_bill_info_dto.setter
    def invoice_bill_info_dto(self, value):
        if isinstance(value, BizInvoiceBillInfoDTO):
            self._invoice_bill_info_dto = value
        else:
            self._invoice_bill_info_dto = BizInvoiceBillInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_bill_info_dto:
            if hasattr(self.invoice_bill_info_dto, 'to_alipay_dict'):
                params['invoice_bill_info_dto'] = self.invoice_bill_info_dto.to_alipay_dict()
            else:
                params['invoice_bill_info_dto'] = self.invoice_bill_info_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsmartpaySyncinvoicebillinfoCreateModel()
        if 'invoice_bill_info_dto' in d:
            o.invoice_bill_info_dto = d['invoice_bill_info_dto']
        return o


