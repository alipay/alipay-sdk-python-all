#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantInvoiceUKDTO import MerchantInvoiceUKDTO


class AlipayEbppInvoiceMerchantApplyModifyModel(object):

    def __init__(self):
        self._apply_id = None
        self._apply_result_memo = None
        self._apply_status = None
        self._attach_invoices = None
        self._batch_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_result_memo(self):
        return self._apply_result_memo

    @apply_result_memo.setter
    def apply_result_memo(self, value):
        self._apply_result_memo = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def attach_invoices(self):
        return self._attach_invoices

    @attach_invoices.setter
    def attach_invoices(self, value):
        if isinstance(value, list):
            self._attach_invoices = list()
            for i in value:
                if isinstance(i, MerchantInvoiceUKDTO):
                    self._attach_invoices.append(i)
                else:
                    self._attach_invoices.append(MerchantInvoiceUKDTO.from_alipay_dict(i))
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_result_memo:
            if hasattr(self.apply_result_memo, 'to_alipay_dict'):
                params['apply_result_memo'] = self.apply_result_memo.to_alipay_dict()
            else:
                params['apply_result_memo'] = self.apply_result_memo
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.attach_invoices:
            if isinstance(self.attach_invoices, list):
                for i in range(0, len(self.attach_invoices)):
                    element = self.attach_invoices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attach_invoices[i] = element.to_alipay_dict()
            if hasattr(self.attach_invoices, 'to_alipay_dict'):
                params['attach_invoices'] = self.attach_invoices.to_alipay_dict()
            else:
                params['attach_invoices'] = self.attach_invoices
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceMerchantApplyModifyModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_result_memo' in d:
            o.apply_result_memo = d['apply_result_memo']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'attach_invoices' in d:
            o.attach_invoices = d['attach_invoices']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        return o


