#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtCrowdappEntityMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtCrowdappEntityMatchResponse, self).__init__()
        self._hit_crowd_app_ids = None
        self._not_hit_crowd_app_ids = None

    @property
    def hit_crowd_app_ids(self):
        return self._hit_crowd_app_ids

    @hit_crowd_app_ids.setter
    def hit_crowd_app_ids(self, value):
        if isinstance(value, list):
            self._hit_crowd_app_ids = list()
            for i in value:
                self._hit_crowd_app_ids.append(i)
    @property
    def not_hit_crowd_app_ids(self):
        return self._not_hit_crowd_app_ids

    @not_hit_crowd_app_ids.setter
    def not_hit_crowd_app_ids(self, value):
        if isinstance(value, list):
            self._not_hit_crowd_app_ids = list()
            for i in value:
                self._not_hit_crowd_app_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtCrowdappEntityMatchResponse, self).parse_response_content(response_content)
        if 'hit_crowd_app_ids' in response:
            self.hit_crowd_app_ids = response['hit_crowd_app_ids']
        if 'not_hit_crowd_app_ids' in response:
            self.not_hit_crowd_app_ids = response['not_hit_crowd_app_ids']
