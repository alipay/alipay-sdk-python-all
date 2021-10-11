#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StandardRuleInfo import StandardRuleInfo


class AlipayEbppInvoiceExpenserulesSceneruleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpenserulesSceneruleQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._standard_rule_info_list = None
        self._total_page_count = None

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
    def standard_rule_info_list(self):
        return self._standard_rule_info_list

    @standard_rule_info_list.setter
    def standard_rule_info_list(self, value):
        if isinstance(value, list):
            self._standard_rule_info_list = list()
            for i in value:
                if isinstance(i, StandardRuleInfo):
                    self._standard_rule_info_list.append(i)
                else:
                    self._standard_rule_info_list.append(StandardRuleInfo.from_alipay_dict(i))
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpenserulesSceneruleQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'standard_rule_info_list' in response:
            self.standard_rule_info_list = response['standard_rule_info_list']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
