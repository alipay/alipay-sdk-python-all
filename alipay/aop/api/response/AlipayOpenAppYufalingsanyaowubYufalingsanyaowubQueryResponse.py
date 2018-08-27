#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppYufalingsanyaowubYufalingsanyaowubQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppYufalingsanyaowubYufalingsanyaowubQueryResponse, self).__init__()
        self._yufaa = None

    @property
    def yufaa(self):
        return self._yufaa

    @yufaa.setter
    def yufaa(self, value):
        self._yufaa = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppYufalingsanyaowubYufalingsanyaowubQueryResponse, self).parse_response_content(response_content)
        if 'yufaa' in response:
            self.yufaa = response['yufaa']
