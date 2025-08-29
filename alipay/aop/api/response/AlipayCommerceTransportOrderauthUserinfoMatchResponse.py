#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportOrderauthUserinfoMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOrderauthUserinfoMatchResponse, self).__init__()
        self._matched_open_id = None
        self._matched_user_id = None
        self._matched_user_risk_level = None
        self._matched_user_risk_reason = None

    @property
    def matched_open_id(self):
        return self._matched_open_id

    @matched_open_id.setter
    def matched_open_id(self, value):
        self._matched_open_id = value
    @property
    def matched_user_id(self):
        return self._matched_user_id

    @matched_user_id.setter
    def matched_user_id(self, value):
        self._matched_user_id = value
    @property
    def matched_user_risk_level(self):
        return self._matched_user_risk_level

    @matched_user_risk_level.setter
    def matched_user_risk_level(self, value):
        self._matched_user_risk_level = value
    @property
    def matched_user_risk_reason(self):
        return self._matched_user_risk_reason

    @matched_user_risk_reason.setter
    def matched_user_risk_reason(self, value):
        self._matched_user_risk_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOrderauthUserinfoMatchResponse, self).parse_response_content(response_content)
        if 'matched_open_id' in response:
            self.matched_open_id = response['matched_open_id']
        if 'matched_user_id' in response:
            self.matched_user_id = response['matched_user_id']
        if 'matched_user_risk_level' in response:
            self.matched_user_risk_level = response['matched_user_risk_level']
        if 'matched_user_risk_reason' in response:
            self.matched_user_risk_reason = response['matched_user_risk_reason']
