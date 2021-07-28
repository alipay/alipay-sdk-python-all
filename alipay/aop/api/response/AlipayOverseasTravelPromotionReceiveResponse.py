#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelPromotionReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelPromotionReceiveResponse, self).__init__()
        self._out_prize_id = None

    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelPromotionReceiveResponse, self).parse_response_content(response_content)
        if 'out_prize_id' in response:
            self.out_prize_id = response['out_prize_id']
