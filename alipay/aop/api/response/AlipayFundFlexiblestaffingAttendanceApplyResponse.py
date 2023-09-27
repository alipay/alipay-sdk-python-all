#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingAttendanceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingAttendanceApplyResponse, self).__init__()
        self._apply_link = None
        self._flow_token = None

    @property
    def apply_link(self):
        return self._apply_link

    @apply_link.setter
    def apply_link(self, value):
        self._apply_link = value
    @property
    def flow_token(self):
        return self._flow_token

    @flow_token.setter
    def flow_token(self, value):
        self._flow_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingAttendanceApplyResponse, self).parse_response_content(response_content)
        if 'apply_link' in response:
            self.apply_link = response['apply_link']
        if 'flow_token' in response:
            self.flow_token = response['flow_token']
