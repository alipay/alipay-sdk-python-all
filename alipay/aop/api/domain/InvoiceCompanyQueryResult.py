#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceAmountLimitDTO import InvoiceAmountLimitDTO
from alipay.aop.api.domain.InvoiceCompanyDTO import InvoiceCompanyDTO
from alipay.aop.api.domain.InvoiceOpenProductDTO import InvoiceOpenProductDTO


class InvoiceCompanyQueryResult(object):

    def __init__(self):
        self._amount_limit_dto_list = None
        self._invoice_company_dto = None
        self._invoice_open_product_dto_list = None
        self._register_id = None
        self._register_status = None

    @property
    def amount_limit_dto_list(self):
        return self._amount_limit_dto_list

    @amount_limit_dto_list.setter
    def amount_limit_dto_list(self, value):
        if isinstance(value, list):
            self._amount_limit_dto_list = list()
            for i in value:
                if isinstance(i, InvoiceAmountLimitDTO):
                    self._amount_limit_dto_list.append(i)
                else:
                    self._amount_limit_dto_list.append(InvoiceAmountLimitDTO.from_alipay_dict(i))
    @property
    def invoice_company_dto(self):
        return self._invoice_company_dto

    @invoice_company_dto.setter
    def invoice_company_dto(self, value):
        if isinstance(value, InvoiceCompanyDTO):
            self._invoice_company_dto = value
        else:
            self._invoice_company_dto = InvoiceCompanyDTO.from_alipay_dict(value)
    @property
    def invoice_open_product_dto_list(self):
        return self._invoice_open_product_dto_list

    @invoice_open_product_dto_list.setter
    def invoice_open_product_dto_list(self, value):
        if isinstance(value, list):
            self._invoice_open_product_dto_list = list()
            for i in value:
                if isinstance(i, InvoiceOpenProductDTO):
                    self._invoice_open_product_dto_list.append(i)
                else:
                    self._invoice_open_product_dto_list.append(InvoiceOpenProductDTO.from_alipay_dict(i))
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value
    @property
    def register_status(self):
        return self._register_status

    @register_status.setter
    def register_status(self, value):
        self._register_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_limit_dto_list:
            if isinstance(self.amount_limit_dto_list, list):
                for i in range(0, len(self.amount_limit_dto_list)):
                    element = self.amount_limit_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.amount_limit_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.amount_limit_dto_list, 'to_alipay_dict'):
                params['amount_limit_dto_list'] = self.amount_limit_dto_list.to_alipay_dict()
            else:
                params['amount_limit_dto_list'] = self.amount_limit_dto_list
        if self.invoice_company_dto:
            if hasattr(self.invoice_company_dto, 'to_alipay_dict'):
                params['invoice_company_dto'] = self.invoice_company_dto.to_alipay_dict()
            else:
                params['invoice_company_dto'] = self.invoice_company_dto
        if self.invoice_open_product_dto_list:
            if isinstance(self.invoice_open_product_dto_list, list):
                for i in range(0, len(self.invoice_open_product_dto_list)):
                    element = self.invoice_open_product_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_open_product_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_open_product_dto_list, 'to_alipay_dict'):
                params['invoice_open_product_dto_list'] = self.invoice_open_product_dto_list.to_alipay_dict()
            else:
                params['invoice_open_product_dto_list'] = self.invoice_open_product_dto_list
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
        if self.register_status:
            if hasattr(self.register_status, 'to_alipay_dict'):
                params['register_status'] = self.register_status.to_alipay_dict()
            else:
                params['register_status'] = self.register_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceCompanyQueryResult()
        if 'amount_limit_dto_list' in d:
            o.amount_limit_dto_list = d['amount_limit_dto_list']
        if 'invoice_company_dto' in d:
            o.invoice_company_dto = d['invoice_company_dto']
        if 'invoice_open_product_dto_list' in d:
            o.invoice_open_product_dto_list = d['invoice_open_product_dto_list']
        if 'register_id' in d:
            o.register_id = d['register_id']
        if 'register_status' in d:
            o.register_status = d['register_status']
        return o


