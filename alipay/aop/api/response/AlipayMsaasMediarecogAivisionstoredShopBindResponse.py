#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAivisionstoredShopBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAivisionstoredShopBindResponse, self).__init__()
        self._ai_service_status = None

    @property
    def ai_service_status(self):
        return self._ai_service_status

    @ai_service_status.setter
    def ai_service_status(self, value):
        self._ai_service_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAivisionstoredShopBindResponse, self).parse_response_content(response_content)
        if 'ai_service_status' in response:
            self.ai_service_status = response['ai_service_status']
