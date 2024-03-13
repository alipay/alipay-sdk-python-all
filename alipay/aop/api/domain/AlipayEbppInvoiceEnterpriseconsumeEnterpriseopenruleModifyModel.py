#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._enterprise_id = None
        self._invoice_rule_id = None
        self._invoice_rule_name = None
        self._invoice_title_id = None
        self._receive_address = None
        self._receive_name = None
        self._receive_phone = None
        self._seller_type = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def invoice_rule_id(self):
        return self._invoice_rule_id

    @invoice_rule_id.setter
    def invoice_rule_id(self, value):
        self._invoice_rule_id = value
    @property
    def invoice_rule_name(self):
        return self._invoice_rule_name

    @invoice_rule_name.setter
    def invoice_rule_name(self, value):
        self._invoice_rule_name = value
    @property
    def invoice_title_id(self):
        return self._invoice_title_id

    @invoice_title_id.setter
    def invoice_title_id(self, value):
        self._invoice_title_id = value
    @property
    def receive_address(self):
        return self._receive_address

    @receive_address.setter
    def receive_address(self, value):
        self._receive_address = value
    @property
    def receive_name(self):
        return self._receive_name

    @receive_name.setter
    def receive_name(self, value):
        self._receive_name = value
    @property
    def receive_phone(self):
        return self._receive_phone

    @receive_phone.setter
    def receive_phone(self, value):
        self._receive_phone = value
    @property
    def seller_type(self):
        return self._seller_type

    @seller_type.setter
    def seller_type(self, value):
        self._seller_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.invoice_rule_id:
            if hasattr(self.invoice_rule_id, 'to_alipay_dict'):
                params['invoice_rule_id'] = self.invoice_rule_id.to_alipay_dict()
            else:
                params['invoice_rule_id'] = self.invoice_rule_id
        if self.invoice_rule_name:
            if hasattr(self.invoice_rule_name, 'to_alipay_dict'):
                params['invoice_rule_name'] = self.invoice_rule_name.to_alipay_dict()
            else:
                params['invoice_rule_name'] = self.invoice_rule_name
        if self.invoice_title_id:
            if hasattr(self.invoice_title_id, 'to_alipay_dict'):
                params['invoice_title_id'] = self.invoice_title_id.to_alipay_dict()
            else:
                params['invoice_title_id'] = self.invoice_title_id
        if self.receive_address:
            if hasattr(self.receive_address, 'to_alipay_dict'):
                params['receive_address'] = self.receive_address.to_alipay_dict()
            else:
                params['receive_address'] = self.receive_address
        if self.receive_name:
            if hasattr(self.receive_name, 'to_alipay_dict'):
                params['receive_name'] = self.receive_name.to_alipay_dict()
            else:
                params['receive_name'] = self.receive_name
        if self.receive_phone:
            if hasattr(self.receive_phone, 'to_alipay_dict'):
                params['receive_phone'] = self.receive_phone.to_alipay_dict()
            else:
                params['receive_phone'] = self.receive_phone
        if self.seller_type:
            if hasattr(self.seller_type, 'to_alipay_dict'):
                params['seller_type'] = self.seller_type.to_alipay_dict()
            else:
                params['seller_type'] = self.seller_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'invoice_rule_id' in d:
            o.invoice_rule_id = d['invoice_rule_id']
        if 'invoice_rule_name' in d:
            o.invoice_rule_name = d['invoice_rule_name']
        if 'invoice_title_id' in d:
            o.invoice_title_id = d['invoice_title_id']
        if 'receive_address' in d:
            o.receive_address = d['receive_address']
        if 'receive_name' in d:
            o.receive_name = d['receive_name']
        if 'receive_phone' in d:
            o.receive_phone = d['receive_phone']
        if 'seller_type' in d:
            o.seller_type = d['seller_type']
        return o


