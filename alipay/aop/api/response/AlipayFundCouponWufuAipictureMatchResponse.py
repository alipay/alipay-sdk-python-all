#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponWufuAipictureMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuAipictureMatchResponse, self).__init__()
        self._pass = None

    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuAipictureMatchResponse, self).parse_response_content(response_content)
        if 'pass' in response:
            self.pass = response['pass']
