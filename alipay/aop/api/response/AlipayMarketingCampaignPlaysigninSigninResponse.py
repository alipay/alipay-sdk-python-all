#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeSendInfo import PrizeSendInfo


class AlipayMarketingCampaignPlaysigninSigninResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPlaysigninSigninResponse, self).__init__()
        self._prize_send_list = None
        self._trigger_error_code = None
        self._trigger_error_message = None
        self._trigger_result = None

    @property
    def prize_send_list(self):
        return self._prize_send_list

    @prize_send_list.setter
    def prize_send_list(self, value):
        if isinstance(value, list):
            self._prize_send_list = list()
            for i in value:
                if isinstance(i, PrizeSendInfo):
                    self._prize_send_list.append(i)
                else:
                    self._prize_send_list.append(PrizeSendInfo.from_alipay_dict(i))
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
        response = super(AlipayMarketingCampaignPlaysigninSigninResponse, self).parse_response_content(response_content)
        if 'prize_send_list' in response:
            self.prize_send_list = response['prize_send_list']
        if 'trigger_error_code' in response:
            self.trigger_error_code = response['trigger_error_code']
        if 'trigger_error_message' in response:
            self.trigger_error_message = response['trigger_error_message']
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
