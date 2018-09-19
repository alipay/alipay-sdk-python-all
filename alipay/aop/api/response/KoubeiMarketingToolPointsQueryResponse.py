#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingToolPointsQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingToolPointsQueryResponse, self).__init__()
        self._available_points = None
        self._freezed_points = None
        self._total_points = None

    @property
    def available_points(self):
        return self._available_points

    @available_points.setter
    def available_points(self, value):
        self._available_points = value
    @property
    def freezed_points(self):
        return self._freezed_points

    @freezed_points.setter
    def freezed_points(self, value):
        self._freezed_points = value
    @property
    def total_points(self):
        return self._total_points

    @total_points.setter
    def total_points(self, value):
        self._total_points = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingToolPointsQueryResponse, self).parse_response_content(response_content)
        if 'available_points' in response:
            self.available_points = response['available_points']
        if 'freezed_points' in response:
            self.freezed_points = response['freezed_points']
        if 'total_points' in response:
            self.total_points = response['total_points']
