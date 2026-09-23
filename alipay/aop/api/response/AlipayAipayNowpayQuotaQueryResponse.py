#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpayQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayQuotaQueryResponse, self).__init__()
        self._as_of_time = None
        self._quota_unit = None
        self._remaining = None
        self._total = None
        self._used = None

    @property
    def as_of_time(self):
        return self._as_of_time

    @as_of_time.setter
    def as_of_time(self, value):
        self._as_of_time = value
    @property
    def quota_unit(self):
        return self._quota_unit

    @quota_unit.setter
    def quota_unit(self, value):
        self._quota_unit = value
    @property
    def remaining(self):
        return self._remaining

    @remaining.setter
    def remaining(self, value):
        self._remaining = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def used(self):
        return self._used

    @used.setter
    def used(self, value):
        self._used = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayQuotaQueryResponse, self).parse_response_content(response_content)
        if 'as_of_time' in response:
            self.as_of_time = response['as_of_time']
        if 'quota_unit' in response:
            self.quota_unit = response['quota_unit']
        if 'remaining' in response:
            self.remaining = response['remaining']
        if 'total' in response:
            self.total = response['total']
        if 'used' in response:
            self.used = response['used']
