#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InfoSecHitDetectItem import InfoSecHitDetectItem


class AlipaySecurityRiskContentResultGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskContentResultGetResponse, self).__init__()
        self._hit_detect_items = None
        self._result_action = None

    @property
    def hit_detect_items(self):
        return self._hit_detect_items

    @hit_detect_items.setter
    def hit_detect_items(self, value):
        if isinstance(value, list):
            self._hit_detect_items = list()
            for i in value:
                if isinstance(i, InfoSecHitDetectItem):
                    self._hit_detect_items.append(i)
                else:
                    self._hit_detect_items.append(InfoSecHitDetectItem.from_alipay_dict(i))
    @property
    def result_action(self):
        return self._result_action

    @result_action.setter
    def result_action(self, value):
        self._result_action = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskContentResultGetResponse, self).parse_response_content(response_content)
        if 'hit_detect_items' in response:
            self.hit_detect_items = response['hit_detect_items']
        if 'result_action' in response:
            self.result_action = response['result_action']
