#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._bill_month_day = None
        self._bill_scope = None
        self._combined_pay_mode = None
        self._default_invoice_kind = None
        self._enterprise_id = None
        self._invoice_remark_value_rule = None
        self._invoice_rule_name = None
        self._invoice_title_id = None
        self._open_mode = None
        self._receive_address = None
        self._receive_name = None
        self._receive_phone = None
        self._seller_type = None
        self._tag = None

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
    def bill_month_day(self):
        return self._bill_month_day

    @bill_month_day.setter
    def bill_month_day(self, value):
        self._bill_month_day = value
    @property
    def bill_scope(self):
        return self._bill_scope

    @bill_scope.setter
    def bill_scope(self, value):
        self._bill_scope = value
    @property
    def combined_pay_mode(self):
        return self._combined_pay_mode

    @combined_pay_mode.setter
    def combined_pay_mode(self, value):
        self._combined_pay_mode = value
    @property
    def default_invoice_kind(self):
        return self._default_invoice_kind

    @default_invoice_kind.setter
    def default_invoice_kind(self, value):
        self._default_invoice_kind = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def invoice_remark_value_rule(self):
        return self._invoice_remark_value_rule

    @invoice_remark_value_rule.setter
    def invoice_remark_value_rule(self, value):
        self._invoice_remark_value_rule = value
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
    def open_mode(self):
        return self._open_mode

    @open_mode.setter
    def open_mode(self, value):
        self._open_mode = value
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
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value


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
        if self.bill_month_day:
            if hasattr(self.bill_month_day, 'to_alipay_dict'):
                params['bill_month_day'] = self.bill_month_day.to_alipay_dict()
            else:
                params['bill_month_day'] = self.bill_month_day
        if self.bill_scope:
            if hasattr(self.bill_scope, 'to_alipay_dict'):
                params['bill_scope'] = self.bill_scope.to_alipay_dict()
            else:
                params['bill_scope'] = self.bill_scope
        if self.combined_pay_mode:
            if hasattr(self.combined_pay_mode, 'to_alipay_dict'):
                params['combined_pay_mode'] = self.combined_pay_mode.to_alipay_dict()
            else:
                params['combined_pay_mode'] = self.combined_pay_mode
        if self.default_invoice_kind:
            if hasattr(self.default_invoice_kind, 'to_alipay_dict'):
                params['default_invoice_kind'] = self.default_invoice_kind.to_alipay_dict()
            else:
                params['default_invoice_kind'] = self.default_invoice_kind
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.invoice_remark_value_rule:
            if hasattr(self.invoice_remark_value_rule, 'to_alipay_dict'):
                params['invoice_remark_value_rule'] = self.invoice_remark_value_rule.to_alipay_dict()
            else:
                params['invoice_remark_value_rule'] = self.invoice_remark_value_rule
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
        if self.open_mode:
            if hasattr(self.open_mode, 'to_alipay_dict'):
                params['open_mode'] = self.open_mode.to_alipay_dict()
            else:
                params['open_mode'] = self.open_mode
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
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'bill_month_day' in d:
            o.bill_month_day = d['bill_month_day']
        if 'bill_scope' in d:
            o.bill_scope = d['bill_scope']
        if 'combined_pay_mode' in d:
            o.combined_pay_mode = d['combined_pay_mode']
        if 'default_invoice_kind' in d:
            o.default_invoice_kind = d['default_invoice_kind']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'invoice_remark_value_rule' in d:
            o.invoice_remark_value_rule = d['invoice_remark_value_rule']
        if 'invoice_rule_name' in d:
            o.invoice_rule_name = d['invoice_rule_name']
        if 'invoice_title_id' in d:
            o.invoice_title_id = d['invoice_title_id']
        if 'open_mode' in d:
            o.open_mode = d['open_mode']
        if 'receive_address' in d:
            o.receive_address = d['receive_address']
        if 'receive_name' in d:
            o.receive_name = d['receive_name']
        if 'receive_phone' in d:
            o.receive_phone = d['receive_phone']
        if 'seller_type' in d:
            o.seller_type = d['seller_type']
        if 'tag' in d:
            o.tag = d['tag']
        return o


