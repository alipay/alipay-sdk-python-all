#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpensecontrolAggregationCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._aggregation_name = None
        self._agreement_no = None
        self._standard_id_list = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def aggregation_name(self):
        return self._aggregation_name

    @aggregation_name.setter
    def aggregation_name(self, value):
        self._aggregation_name = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
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
        if self.aggregation_name:
            if hasattr(self.aggregation_name, 'to_alipay_dict'):
                params['aggregation_name'] = self.aggregation_name.to_alipay_dict()
            else:
                params['aggregation_name'] = self.aggregation_name
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
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
        o = AlipayEbppInvoiceExpensecontrolAggregationCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'aggregation_name' in d:
            o.aggregation_name = d['aggregation_name']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'standard_id_list' in d:
            o.standard_id_list = d['standard_id_list']
        return o


