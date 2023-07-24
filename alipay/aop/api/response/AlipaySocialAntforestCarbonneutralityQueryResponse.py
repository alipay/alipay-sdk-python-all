#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestCarbonneutralityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestCarbonneutralityQueryResponse, self).__init__()
        self._carbon_neutrality_biz_count = None
        self._carbon_neutrality_people_count = None
        self._green_life_tick_times = None

    @property
    def carbon_neutrality_biz_count(self):
        return self._carbon_neutrality_biz_count

    @carbon_neutrality_biz_count.setter
    def carbon_neutrality_biz_count(self, value):
        self._carbon_neutrality_biz_count = value
    @property
    def carbon_neutrality_people_count(self):
        return self._carbon_neutrality_people_count

    @carbon_neutrality_people_count.setter
    def carbon_neutrality_people_count(self, value):
        self._carbon_neutrality_people_count = value
    @property
    def green_life_tick_times(self):
        return self._green_life_tick_times

    @green_life_tick_times.setter
    def green_life_tick_times(self, value):
        self._green_life_tick_times = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestCarbonneutralityQueryResponse, self).parse_response_content(response_content)
        if 'carbon_neutrality_biz_count' in response:
            self.carbon_neutrality_biz_count = response['carbon_neutrality_biz_count']
        if 'carbon_neutrality_people_count' in response:
            self.carbon_neutrality_people_count = response['carbon_neutrality_people_count']
        if 'green_life_tick_times' in response:
            self.green_life_tick_times = response['green_life_tick_times']
