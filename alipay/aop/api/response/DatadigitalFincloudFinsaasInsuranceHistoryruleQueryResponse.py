#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HistoryRuleVO import HistoryRuleVO


class DatadigitalFincloudFinsaasInsuranceHistoryruleQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasInsuranceHistoryruleQueryResponse, self).__init__()
        self._history_rule_items = None
        self._total_count = None

    @property
    def history_rule_items(self):
        return self._history_rule_items

    @history_rule_items.setter
    def history_rule_items(self, value):
        if isinstance(value, list):
            self._history_rule_items = list()
            for i in value:
                if isinstance(i, HistoryRuleVO):
                    self._history_rule_items.append(i)
                else:
                    self._history_rule_items.append(HistoryRuleVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasInsuranceHistoryruleQueryResponse, self).parse_response_content(response_content)
        if 'history_rule_items' in response:
            self.history_rule_items = response['history_rule_items']
        if 'total_count' in response:
            self.total_count = response['total_count']
