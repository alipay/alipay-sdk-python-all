#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScenePayCode import ScenePayCode


class AlipayTradeScenepayTokenExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeScenepayTokenExchangeResponse, self).__init__()
        self._scene_pay_code = None

    @property
    def scene_pay_code(self):
        return self._scene_pay_code

    @scene_pay_code.setter
    def scene_pay_code(self, value):
        if isinstance(value, ScenePayCode):
            self._scene_pay_code = value
        else:
            self._scene_pay_code = ScenePayCode.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradeScenepayTokenExchangeResponse, self).parse_response_content(response_content)
        if 'scene_pay_code' in response:
            self.scene_pay_code = response['scene_pay_code']
