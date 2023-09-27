#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntifloodRule import AntifloodRule


class AlipayCloudCloudbaseAntifloodRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseAntifloodRuleQueryResponse, self).__init__()
        self._page_index = None
        self._page_size = None
        self._rules = None
        self._total = None

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        if isinstance(value, list):
            self._rules = list()
            for i in value:
                if isinstance(i, AntifloodRule):
                    self._rules.append(i)
                else:
                    self._rules.append(AntifloodRule.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseAntifloodRuleQueryResponse, self).parse_response_content(response_content)
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'rules' in response:
            self.rules = response['rules']
        if 'total' in response:
            self.total = response['total']
