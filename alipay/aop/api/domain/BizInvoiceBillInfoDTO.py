#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyInfoRequestDTO import CompanyInfoRequestDTO
from alipay.aop.api.domain.GfsmartpayExtInfo import GfsmartpayExtInfo
from alipay.aop.api.domain.BizInvoiceDTO import BizInvoiceDTO


class BizInvoiceBillInfoDTO(object):

    def __init__(self):
        self._amount = None
        self._bill_desc = None
        self._biz_code = None
        self._biz_document_nos = None
        self._company_info = None
        self._create_invoice_notify = None
        self._currency_code = None
        self._deduct_strategy = None
        self._ext_info = None
        self._idempotent_id = None
        self._invoices = None
        self._is_async = None
        self._operator = None
        self._related_document_nos = None
        self._source_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_desc(self):
        return self._bill_desc

    @bill_desc.setter
    def bill_desc(self, value):
        self._bill_desc = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_document_nos(self):
        return self._biz_document_nos

    @biz_document_nos.setter
    def biz_document_nos(self, value):
        if isinstance(value, list):
            self._biz_document_nos = list()
            for i in value:
                self._biz_document_nos.append(i)
    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, value):
        if isinstance(value, CompanyInfoRequestDTO):
            self._company_info = value
        else:
            self._company_info = CompanyInfoRequestDTO.from_alipay_dict(value)
    @property
    def create_invoice_notify(self):
        return self._create_invoice_notify

    @create_invoice_notify.setter
    def create_invoice_notify(self, value):
        self._create_invoice_notify = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def deduct_strategy(self):
        return self._deduct_strategy

    @deduct_strategy.setter
    def deduct_strategy(self, value):
        self._deduct_strategy = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, GfsmartpayExtInfo):
            self._ext_info = value
        else:
            self._ext_info = GfsmartpayExtInfo.from_alipay_dict(value)
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
    @property
    def invoices(self):
        return self._invoices

    @invoices.setter
    def invoices(self, value):
        if isinstance(value, list):
            self._invoices = list()
            for i in value:
                if isinstance(i, BizInvoiceDTO):
                    self._invoices.append(i)
                else:
                    self._invoices.append(BizInvoiceDTO.from_alipay_dict(i))
    @property
    def is_async(self):
        return self._is_async

    @is_async.setter
    def is_async(self, value):
        self._is_async = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def related_document_nos(self):
        return self._related_document_nos

    @related_document_nos.setter
    def related_document_nos(self, value):
        if isinstance(value, list):
            self._related_document_nos = list()
            for i in value:
                self._related_document_nos.append(i)
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_desc:
            if hasattr(self.bill_desc, 'to_alipay_dict'):
                params['bill_desc'] = self.bill_desc.to_alipay_dict()
            else:
                params['bill_desc'] = self.bill_desc
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_document_nos:
            if isinstance(self.biz_document_nos, list):
                for i in range(0, len(self.biz_document_nos)):
                    element = self.biz_document_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_document_nos[i] = element.to_alipay_dict()
            if hasattr(self.biz_document_nos, 'to_alipay_dict'):
                params['biz_document_nos'] = self.biz_document_nos.to_alipay_dict()
            else:
                params['biz_document_nos'] = self.biz_document_nos
        if self.company_info:
            if hasattr(self.company_info, 'to_alipay_dict'):
                params['company_info'] = self.company_info.to_alipay_dict()
            else:
                params['company_info'] = self.company_info
        if self.create_invoice_notify:
            if hasattr(self.create_invoice_notify, 'to_alipay_dict'):
                params['create_invoice_notify'] = self.create_invoice_notify.to_alipay_dict()
            else:
                params['create_invoice_notify'] = self.create_invoice_notify
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.deduct_strategy:
            if hasattr(self.deduct_strategy, 'to_alipay_dict'):
                params['deduct_strategy'] = self.deduct_strategy.to_alipay_dict()
            else:
                params['deduct_strategy'] = self.deduct_strategy
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        if self.invoices:
            if isinstance(self.invoices, list):
                for i in range(0, len(self.invoices)):
                    element = self.invoices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoices[i] = element.to_alipay_dict()
            if hasattr(self.invoices, 'to_alipay_dict'):
                params['invoices'] = self.invoices.to_alipay_dict()
            else:
                params['invoices'] = self.invoices
        if self.is_async:
            if hasattr(self.is_async, 'to_alipay_dict'):
                params['is_async'] = self.is_async.to_alipay_dict()
            else:
                params['is_async'] = self.is_async
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.related_document_nos:
            if isinstance(self.related_document_nos, list):
                for i in range(0, len(self.related_document_nos)):
                    element = self.related_document_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_document_nos[i] = element.to_alipay_dict()
            if hasattr(self.related_document_nos, 'to_alipay_dict'):
                params['related_document_nos'] = self.related_document_nos.to_alipay_dict()
            else:
                params['related_document_nos'] = self.related_document_nos
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizInvoiceBillInfoDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_desc' in d:
            o.bill_desc = d['bill_desc']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_document_nos' in d:
            o.biz_document_nos = d['biz_document_nos']
        if 'company_info' in d:
            o.company_info = d['company_info']
        if 'create_invoice_notify' in d:
            o.create_invoice_notify = d['create_invoice_notify']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'deduct_strategy' in d:
            o.deduct_strategy = d['deduct_strategy']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'invoices' in d:
            o.invoices = d['invoices']
        if 'is_async' in d:
            o.is_async = d['is_async']
        if 'operator' in d:
            o.operator = d['operator']
        if 'related_document_nos' in d:
            o.related_document_nos = d['related_document_nos']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


