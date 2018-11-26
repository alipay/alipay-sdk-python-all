#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeInfo import PrizeInfo


class AlipayOverseasTravelGkaCampaignApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelGkaCampaignApplyResponse, self).__init__()
        self._prize_info = None
        self._result_code = None
        self._result_msg = None

    @property
    def prize_info(self):
        return self._prize_info

    @prize_info.setter
    def prize_info(self, value):
        if isinstance(value, PrizeInfo):
            self._prize_info = value
        else:
            self._prize_info = PrizeInfo.from_alipay_dict(value)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelGkaCampaignApplyResponse, self).parse_response_content(response_content)
        if 'prize_info' in response:
            self.prize_info = response['prize_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
