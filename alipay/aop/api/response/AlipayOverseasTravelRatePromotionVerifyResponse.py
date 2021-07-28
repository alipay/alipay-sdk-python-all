#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelRatePromotionVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelRatePromotionVerifyResponse, self).__init__()
        self._biz_result_code = None
        self._biz_result_msg = None

    @property
    def biz_result_code(self):
        return self._biz_result_code

    @biz_result_code.setter
    def biz_result_code(self, value):
        self._biz_result_code = value
    @property
    def biz_result_msg(self):
        return self._biz_result_msg

    @biz_result_msg.setter
    def biz_result_msg(self, value):
        self._biz_result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelRatePromotionVerifyResponse, self).parse_response_content(response_content)
        if 'biz_result_code' in response:
            self.biz_result_code = response['biz_result_code']
        if 'biz_result_msg' in response:
            self.biz_result_msg = response['biz_result_msg']
