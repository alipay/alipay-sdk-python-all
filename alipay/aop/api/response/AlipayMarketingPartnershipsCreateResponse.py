#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingPartnershipsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingPartnershipsCreateResponse, self).__init__()
        self._create_time = None
        self._status = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingPartnershipsCreateResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'status' in response:
            self.status = response['status']
