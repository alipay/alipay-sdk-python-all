#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceSyncCheckDTO import InvoiceSyncCheckDTO


class AlipayBossFncInputInvoiceCheckModel(object):

    def __init__(self):
        self._invoice_sync_check_dto = None

    @property
    def invoice_sync_check_dto(self):
        return self._invoice_sync_check_dto

    @invoice_sync_check_dto.setter
    def invoice_sync_check_dto(self, value):
        if isinstance(value, InvoiceSyncCheckDTO):
            self._invoice_sync_check_dto = value
        else:
            self._invoice_sync_check_dto = InvoiceSyncCheckDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_sync_check_dto:
            if hasattr(self.invoice_sync_check_dto, 'to_alipay_dict'):
                params['invoice_sync_check_dto'] = self.invoice_sync_check_dto.to_alipay_dict()
            else:
                params['invoice_sync_check_dto'] = self.invoice_sync_check_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInputInvoiceCheckModel()
        if 'invoice_sync_check_dto' in d:
            o.invoice_sync_check_dto = d['invoice_sync_check_dto']
        return o


