#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyRefinedOilRuleQueryOpenItem import CompanyRefinedOilRuleQueryOpenItem


class AlipayCommerceEcIndustryinvoiceOilconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcIndustryinvoiceOilconfigQueryResponse, self).__init__()
        self._curr_page_size = None
        self._page_num = None
        self._page_size = None
        self._rule_list = None
        self._tax_no = None
        self._total_size = None

    @property
    def curr_page_size(self):
        return self._curr_page_size

    @curr_page_size.setter
    def curr_page_size(self, value):
        self._curr_page_size = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def rule_list(self):
        return self._rule_list

    @rule_list.setter
    def rule_list(self, value):
        if isinstance(value, list):
            self._rule_list = list()
            for i in value:
                if isinstance(i, CompanyRefinedOilRuleQueryOpenItem):
                    self._rule_list.append(i)
                else:
                    self._rule_list.append(CompanyRefinedOilRuleQueryOpenItem.from_alipay_dict(i))
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcIndustryinvoiceOilconfigQueryResponse, self).parse_response_content(response_content)
        if 'curr_page_size' in response:
            self.curr_page_size = response['curr_page_size']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'rule_list' in response:
            self.rule_list = response['rule_list']
        if 'tax_no' in response:
            self.tax_no = response['tax_no']
        if 'total_size' in response:
            self.total_size = response['total_size']
