#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVehicleownerCampaignPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerCampaignPublishResponse, self).__init__()
        self._activity_id = None
        self._status = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerCampaignPublishResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'status' in response:
            self.status = response['status']
