#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExpenseCtrlEmployeeRuleInfo import ExpenseCtrlEmployeeRuleInfo


class AlipayEbppInvoiceExpenserulesEmployeerulesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpenserulesEmployeerulesQueryResponse, self).__init__()
        self._employee_rules = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def employee_rules(self):
        return self._employee_rules

    @employee_rules.setter
    def employee_rules(self, value):
        if isinstance(value, list):
            self._employee_rules = list()
            for i in value:
                if isinstance(i, ExpenseCtrlEmployeeRuleInfo):
                    self._employee_rules.append(i)
                else:
                    self._employee_rules.append(ExpenseCtrlEmployeeRuleInfo.from_alipay_dict(i))
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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpenserulesEmployeerulesQueryResponse, self).parse_response_content(response_content)
        if 'employee_rules' in response:
            self.employee_rules = response['employee_rules']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
