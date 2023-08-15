#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TrafficRule import TrafficRule


class AlipayCloudCloudbaseFunctionTrafficconfigGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionTrafficconfigGetResponse, self).__init__()
        self._traffic_rules = None

    @property
    def traffic_rules(self):
        return self._traffic_rules

    @traffic_rules.setter
    def traffic_rules(self, value):
        if isinstance(value, list):
            self._traffic_rules = list()
            for i in value:
                if isinstance(i, TrafficRule):
                    self._traffic_rules.append(i)
                else:
                    self._traffic_rules.append(TrafficRule.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionTrafficconfigGetResponse, self).parse_response_content(response_content)
        if 'traffic_rules' in response:
            self.traffic_rules = response['traffic_rules']
