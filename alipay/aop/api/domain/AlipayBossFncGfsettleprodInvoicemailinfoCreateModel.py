#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceMailInfoOrderDTO import InvoiceMailInfoOrderDTO


class AlipayBossFncGfsettleprodInvoicemailinfoCreateModel(object):

    def __init__(self):
        self._invoice_mail_info_orde_dto = None

    @property
    def invoice_mail_info_orde_dto(self):
        return self._invoice_mail_info_orde_dto

    @invoice_mail_info_orde_dto.setter
    def invoice_mail_info_orde_dto(self, value):
        if isinstance(value, InvoiceMailInfoOrderDTO):
            self._invoice_mail_info_orde_dto = value
        else:
            self._invoice_mail_info_orde_dto = InvoiceMailInfoOrderDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_mail_info_orde_dto:
            if hasattr(self.invoice_mail_info_orde_dto, 'to_alipay_dict'):
                params['invoice_mail_info_orde_dto'] = self.invoice_mail_info_orde_dto.to_alipay_dict()
            else:
                params['invoice_mail_info_orde_dto'] = self.invoice_mail_info_orde_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoicemailinfoCreateModel()
        if 'invoice_mail_info_orde_dto' in d:
            o.invoice_mail_info_orde_dto = d['invoice_mail_info_orde_dto']
        return o


