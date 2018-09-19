#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserStepcounterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserStepcounterQueryResponse, self).__init__()
        self._count = None
        self._count_date = None
        self._time_zone = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def count_date(self):
        return self._count_date

    @count_date.setter
    def count_date(self, value):
        self._count_date = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserStepcounterQueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'count_date' in response:
            self.count_date = response['count_date']
        if 'time_zone' in response:
            self.time_zone = response['time_zone']
