#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceContactInfo import InvoiceContactInfo
from alipay.aop.api.domain.InvoiceCompanyInfo import InvoiceCompanyInfo
from alipay.aop.api.domain.InvoiceOrderInfo import InvoiceOrderInfo


class AlipayEbppInvoiceRegisterCreateModel(object):

    def __init__(self):
        self._contact_info = None
        self._ext_json = None
        self._invoice_company = None
        self._invoice_order = None
        self._m_short_name = None
        self._outer_id = None
        self._platform_code = None
        self._platform_user_id = None
        self._register_type = None
        self._sub_m_short_name = None

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, InvoiceContactInfo):
            self._contact_info = value
        else:
            self._contact_info = InvoiceContactInfo.from_alipay_dict(value)
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def invoice_company(self):
        return self._invoice_company

    @invoice_company.setter
    def invoice_company(self, value):
        if isinstance(value, InvoiceCompanyInfo):
            self._invoice_company = value
        else:
            self._invoice_company = InvoiceCompanyInfo.from_alipay_dict(value)
    @property
    def invoice_order(self):
        return self._invoice_order

    @invoice_order.setter
    def invoice_order(self, value):
        if isinstance(value, list):
            self._invoice_order = list()
            for i in value:
                if isinstance(i, InvoiceOrderInfo):
                    self._invoice_order.append(i)
                else:
                    self._invoice_order.append(InvoiceOrderInfo.from_alipay_dict(i))
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
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
    def register_type(self):
        return self._register_type

    @register_type.setter
    def register_type(self, value):
        self._register_type = value
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.invoice_company:
            if hasattr(self.invoice_company, 'to_alipay_dict'):
                params['invoice_company'] = self.invoice_company.to_alipay_dict()
            else:
                params['invoice_company'] = self.invoice_company
        if self.invoice_order:
            if isinstance(self.invoice_order, list):
                for i in range(0, len(self.invoice_order)):
                    element = self.invoice_order[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_order[i] = element.to_alipay_dict()
            if hasattr(self.invoice_order, 'to_alipay_dict'):
                params['invoice_order'] = self.invoice_order.to_alipay_dict()
            else:
                params['invoice_order'] = self.invoice_order
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
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
        if self.register_type:
            if hasattr(self.register_type, 'to_alipay_dict'):
                params['register_type'] = self.register_type.to_alipay_dict()
            else:
                params['register_type'] = self.register_type
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceRegisterCreateModel()
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'invoice_company' in d:
            o.invoice_company = d['invoice_company']
        if 'invoice_order' in d:
            o.invoice_order = d['invoice_order']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_user_id' in d:
            o.platform_user_id = d['platform_user_id']
        if 'register_type' in d:
            o.register_type = d['register_type']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


