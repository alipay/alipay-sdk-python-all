#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserPeerpayprodAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPeerpayprodAgreementQueryResponse, self).__init__()
        self._quota = None

    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserPeerpayprodAgreementQueryResponse, self).parse_response_content(response_content)
        if 'quota' in response:
            self.quota = response['quota']
