#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoDoctemplateSettingurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoDoctemplateSettingurlQueryResponse, self).__init__()
        self._setting_url = None

    @property
    def setting_url(self):
        return self._setting_url

    @setting_url.setter
    def setting_url(self, value):
        self._setting_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoDoctemplateSettingurlQueryResponse, self).parse_response_content(response_content)
        if 'setting_url' in response:
            self.setting_url = response['setting_url']
