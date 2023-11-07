#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignPlaysigninSignupResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPlaysigninSignupResponse, self).__init__()
        self._trigger_error_code = None
        self._trigger_error_message = None
        self._trigger_result = None

    @property
    def trigger_error_code(self):
        return self._trigger_error_code

    @trigger_error_code.setter
    def trigger_error_code(self, value):
        self._trigger_error_code = value
    @property
    def trigger_error_message(self):
        return self._trigger_error_message

    @trigger_error_message.setter
    def trigger_error_message(self, value):
        self._trigger_error_message = value
    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPlaysigninSignupResponse, self).parse_response_content(response_content)
        if 'trigger_error_code' in response:
            self.trigger_error_code = response['trigger_error_code']
        if 'trigger_error_message' in response:
            self.trigger_error_message = response['trigger_error_message']
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
