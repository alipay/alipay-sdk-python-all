#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProjectRuleInfo import ProjectRuleInfo


class AlipayEbppInvoiceExpenserulesProjectruleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpenserulesProjectruleQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._project_rule_info_list = None
        self._total_count = None
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
    def project_rule_info_list(self):
        return self._project_rule_info_list

    @project_rule_info_list.setter
    def project_rule_info_list(self, value):
        if isinstance(value, list):
            self._project_rule_info_list = list()
            for i in value:
                if isinstance(i, ProjectRuleInfo):
                    self._project_rule_info_list.append(i)
                else:
                    self._project_rule_info_list.append(ProjectRuleInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpenserulesProjectruleQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'project_rule_info_list' in response:
            self.project_rule_info_list = response['project_rule_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
