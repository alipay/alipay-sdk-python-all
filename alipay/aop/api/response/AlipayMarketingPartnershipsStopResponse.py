#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingPartnershipsStopResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingPartnershipsStopResponse, self).__init__()
        self._status = None
        self._stop_time = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stop_time(self):
        return self._stop_time

    @stop_time.setter
    def stop_time(self, value):
        self._stop_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingPartnershipsStopResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'stop_time' in response:
            self.stop_time = response['stop_time']
