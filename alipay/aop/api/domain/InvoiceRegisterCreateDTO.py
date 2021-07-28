#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceCompanyDTO import InvoiceCompanyDTO
from alipay.aop.api.domain.InvoiceContactDTO import InvoiceContactDTO
from alipay.aop.api.domain.InvoiceOrderDTO import InvoiceOrderDTO


class InvoiceRegisterCreateDTO(object):

    def __init__(self):
        self._invoice_company_dto = None
        self._invoice_contact_dto = None
        self._invoice_order_dto_list = None
        self._outer_id = None
        self._platform_code = None
        self._platform_user_id = None
        self._product_code = None
        self._register_type = None

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
    def invoice_contact_dto(self):
        return self._invoice_contact_dto

    @invoice_contact_dto.setter
    def invoice_contact_dto(self, value):
        if isinstance(value, InvoiceContactDTO):
            self._invoice_contact_dto = value
        else:
            self._invoice_contact_dto = InvoiceContactDTO.from_alipay_dict(value)
    @property
    def invoice_order_dto_list(self):
        return self._invoice_order_dto_list

    @invoice_order_dto_list.setter
    def invoice_order_dto_list(self, value):
        if isinstance(value, list):
            self._invoice_order_dto_list = list()
            for i in value:
                if isinstance(i, InvoiceOrderDTO):
                    self._invoice_order_dto_list.append(i)
                else:
                    self._invoice_order_dto_list.append(InvoiceOrderDTO.from_alipay_dict(i))
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def platform_user_id(self):
        return self._platform_user_id

    @platform_user_id.setter
    def platform_user_id(self, value):
        self._platform_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def register_type(self):
        return self._register_type

    @register_type.setter
    def register_type(self, value):
        self._register_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_company_dto:
            if hasattr(self.invoice_company_dto, 'to_alipay_dict'):
                params['invoice_company_dto'] = self.invoice_company_dto.to_alipay_dict()
            else:
                params['invoice_company_dto'] = self.invoice_company_dto
        if self.invoice_contact_dto:
            if hasattr(self.invoice_contact_dto, 'to_alipay_dict'):
                params['invoice_contact_dto'] = self.invoice_contact_dto.to_alipay_dict()
            else:
                params['invoice_contact_dto'] = self.invoice_contact_dto
        if self.invoice_order_dto_list:
            if isinstance(self.invoice_order_dto_list, list):
                for i in range(0, len(self.invoice_order_dto_list)):
                    element = self.invoice_order_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_order_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_order_dto_list, 'to_alipay_dict'):
                params['invoice_order_dto_list'] = self.invoice_order_dto_list.to_alipay_dict()
            else:
                params['invoice_order_dto_list'] = self.invoice_order_dto_list
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.platform_user_id:
            if hasattr(self.platform_user_id, 'to_alipay_dict'):
                params['platform_user_id'] = self.platform_user_id.to_alipay_dict()
            else:
                params['platform_user_id'] = self.platform_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.register_type:
            if hasattr(self.register_type, 'to_alipay_dict'):
                params['register_type'] = self.register_type.to_alipay_dict()
            else:
                params['register_type'] = self.register_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceRegisterCreateDTO()
        if 'invoice_company_dto' in d:
            o.invoice_company_dto = d['invoice_company_dto']
        if 'invoice_contact_dto' in d:
            o.invoice_contact_dto = d['invoice_contact_dto']
        if 'invoice_order_dto_list' in d:
            o.invoice_order_dto_list = d['invoice_order_dto_list']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_user_id' in d:
            o.platform_user_id = d['platform_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'register_type' in d:
            o.register_type = d['register_type']
        return o


