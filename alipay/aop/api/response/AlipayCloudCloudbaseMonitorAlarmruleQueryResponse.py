#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlarmRule import AlarmRule


class AlipayCloudCloudbaseMonitorAlarmruleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorAlarmruleQueryResponse, self).__init__()
        self._alarm_rules = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def alarm_rules(self):
        return self._alarm_rules

    @alarm_rules.setter
    def alarm_rules(self, value):
        if isinstance(value, list):
            self._alarm_rules = list()
            for i in value:
                if isinstance(i, AlarmRule):
                    self._alarm_rules.append(i)
                else:
                    self._alarm_rules.append(AlarmRule.from_alipay_dict(i))
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorAlarmruleQueryResponse, self).parse_response_content(response_content)
        if 'alarm_rules' in response:
            self.alarm_rules = response['alarm_rules']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
