#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyRefinedOilRuleItem import CompanyRefinedOilRuleItem


class AlipayCommerceEcIndustryinvoiceOilconfigSaveModel(object):

    def __init__(self):
        self._rule_list = None
        self._tax_no = None

    @property
    def rule_list(self):
        return self._rule_list

    @rule_list.setter
    def rule_list(self, value):
        if isinstance(value, list):
            self._rule_list = list()
            for i in value:
                if isinstance(i, CompanyRefinedOilRuleItem):
                    self._rule_list.append(i)
                else:
                    self._rule_list.append(CompanyRefinedOilRuleItem.from_alipay_dict(i))
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_list:
            if isinstance(self.rule_list, list):
                for i in range(0, len(self.rule_list)):
                    element = self.rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_list[i] = element.to_alipay_dict()
            if hasattr(self.rule_list, 'to_alipay_dict'):
                params['rule_list'] = self.rule_list.to_alipay_dict()
            else:
                params['rule_list'] = self.rule_list
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcIndustryinvoiceOilconfigSaveModel()
        if 'rule_list' in d:
            o.rule_list = d['rule_list']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


