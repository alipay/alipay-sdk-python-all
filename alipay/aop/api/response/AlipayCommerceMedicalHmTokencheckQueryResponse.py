#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHmTokencheckQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmTokencheckQueryResponse, self).__init__()
        self._hmuid = None

    @property
    def hmuid(self):
        return self._hmuid

    @hmuid.setter
    def hmuid(self, value):
        self._hmuid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmTokencheckQueryResponse, self).parse_response_content(response_content)
        if 'hmuid' in response:
            self.hmuid = response['hmuid']
