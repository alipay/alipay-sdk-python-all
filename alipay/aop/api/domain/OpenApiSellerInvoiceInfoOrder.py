#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiSellerInvoiceInfoOrder(object):

    def __init__(self):
        self._drawer = None
        self._inst_id = None
        self._invoice_title = None
        self._payee = None
        self._registered_address = None
        self._registered_phone_no = None
        self._reviewer = None
        self._tax_no = None
        self._taxpayer_type = None

    @property
    def drawer(self):
        return self._drawer

    @drawer.setter
    def drawer(self, value):
        self._drawer = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        self._invoice_title = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def registered_phone_no(self):
        return self._registered_phone_no

    @registered_phone_no.setter
    def registered_phone_no(self, value):
        self._registered_phone_no = value
    @property
    def reviewer(self):
        return self._reviewer

    @reviewer.setter
    def reviewer(self, value):
        self._reviewer = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def taxpayer_type(self):
        return self._taxpayer_type

    @taxpayer_type.setter
    def taxpayer_type(self, value):
        self._taxpayer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.drawer:
            if hasattr(self.drawer, 'to_alipay_dict'):
                params['drawer'] = self.drawer.to_alipay_dict()
            else:
                params['drawer'] = self.drawer
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.registered_address:
            if hasattr(self.registered_address, 'to_alipay_dict'):
                params['registered_address'] = self.registered_address.to_alipay_dict()
            else:
                params['registered_address'] = self.registered_address
        if self.registered_phone_no:
            if hasattr(self.registered_phone_no, 'to_alipay_dict'):
                params['registered_phone_no'] = self.registered_phone_no.to_alipay_dict()
            else:
                params['registered_phone_no'] = self.registered_phone_no
        if self.reviewer:
            if hasattr(self.reviewer, 'to_alipay_dict'):
                params['reviewer'] = self.reviewer.to_alipay_dict()
            else:
                params['reviewer'] = self.reviewer
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.taxpayer_type:
            if hasattr(self.taxpayer_type, 'to_alipay_dict'):
                params['taxpayer_type'] = self.taxpayer_type.to_alipay_dict()
            else:
                params['taxpayer_type'] = self.taxpayer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiSellerInvoiceInfoOrder()
        if 'drawer' in d:
            o.drawer = d['drawer']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'payee' in d:
            o.payee = d['payee']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registered_phone_no' in d:
            o.registered_phone_no = d['registered_phone_no']
        if 'reviewer' in d:
            o.reviewer = d['reviewer']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'taxpayer_type' in d:
            o.taxpayer_type = d['taxpayer_type']
        return o


