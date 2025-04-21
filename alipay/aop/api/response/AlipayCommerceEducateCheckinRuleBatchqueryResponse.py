#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduCheckInRule import EduCheckInRule


class AlipayCommerceEducateCheckinRuleBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCheckinRuleBatchqueryResponse, self).__init__()
        self._rule_info_list = None
        self._total_num = None

    @property
    def rule_info_list(self):
        return self._rule_info_list

    @rule_info_list.setter
    def rule_info_list(self, value):
        if isinstance(value, list):
            self._rule_info_list = list()
            for i in value:
                if isinstance(i, EduCheckInRule):
                    self._rule_info_list.append(i)
                else:
                    self._rule_info_list.append(EduCheckInRule.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCheckinRuleBatchqueryResponse, self).parse_response_content(response_content)
        if 'rule_info_list' in response:
            self.rule_info_list = response['rule_info_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
