#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._bill_month_day = None
        self._invoice_rule_name = None
        self._invoice_title_id = None
        self._open_mode = None
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
    def bill_month_day(self):
        return self._bill_month_day

    @bill_month_day.setter
    def bill_month_day(self, value):
        self._bill_month_day = value
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
        if self.bill_month_day:
            if hasattr(self.bill_month_day, 'to_alipay_dict'):
                params['bill_month_day'] = self.bill_month_day.to_alipay_dict()
            else:
                params['bill_month_day'] = self.bill_month_day
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
        o = AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'bill_month_day' in d:
            o.bill_month_day = d['bill_month_day']
        if 'invoice_rule_name' in d:
            o.invoice_rule_name = d['invoice_rule_name']
        if 'invoice_title_id' in d:
            o.invoice_title_id = d['invoice_title_id']
        if 'open_mode' in d:
            o.open_mode = d['open_mode']
        if 'seller_type' in d:
            o.seller_type = d['seller_type']
        return o


