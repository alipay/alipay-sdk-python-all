#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoTravelPartnerTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelPartnerTriggerResponse, self).__init__()
        self._assist_status = None

    @property
    def assist_status(self):
        return self._assist_status

    @assist_status.setter
    def assist_status(self, value):
        self._assist_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelPartnerTriggerResponse, self).parse_response_content(response_content)
        if 'assist_status' in response:
            self.assist_status = response['assist_status']
