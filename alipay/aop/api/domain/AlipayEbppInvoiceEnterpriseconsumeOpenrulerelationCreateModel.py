#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseconsumeOpenrulerelationCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._invoice_rule_id = None
        self._standard_id_list = None

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
    def invoice_rule_id(self):
        return self._invoice_rule_id

    @invoice_rule_id.setter
    def invoice_rule_id(self, value):
        self._invoice_rule_id = value
    @property
    def standard_id_list(self):
        return self._standard_id_list

    @standard_id_list.setter
    def standard_id_list(self, value):
        if isinstance(value, list):
            self._standard_id_list = list()
            for i in value:
                self._standard_id_list.append(i)


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
        if self.invoice_rule_id:
            if hasattr(self.invoice_rule_id, 'to_alipay_dict'):
                params['invoice_rule_id'] = self.invoice_rule_id.to_alipay_dict()
            else:
                params['invoice_rule_id'] = self.invoice_rule_id
        if self.standard_id_list:
            if isinstance(self.standard_id_list, list):
                for i in range(0, len(self.standard_id_list)):
                    element = self.standard_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_id_list[i] = element.to_alipay_dict()
            if hasattr(self.standard_id_list, 'to_alipay_dict'):
                params['standard_id_list'] = self.standard_id_list.to_alipay_dict()
            else:
                params['standard_id_list'] = self.standard_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEnterpriseconsumeOpenrulerelationCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'invoice_rule_id' in d:
            o.invoice_rule_id = d['invoice_rule_id']
        if 'standard_id_list' in d:
            o.standard_id_list = d['standard_id_list']
        return o


