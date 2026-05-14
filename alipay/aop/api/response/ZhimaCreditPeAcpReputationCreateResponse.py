#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeAcpReputationCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeAcpReputationCreateResponse, self).__init__()
        self._reputation_id = None

    @property
    def reputation_id(self):
        return self._reputation_id

    @reputation_id.setter
    def reputation_id(self, value):
        self._reputation_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeAcpReputationCreateResponse, self).parse_response_content(response_content)
        if 'reputation_id' in response:
            self.reputation_id = response['reputation_id']
