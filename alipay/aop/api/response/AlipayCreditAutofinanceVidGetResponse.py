#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCreditAutofinanceVidGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditAutofinanceVidGetResponse, self).__init__()
        self._verifyid = None

    @property
    def verifyid(self):
        return self._verifyid

    @verifyid.setter
    def verifyid(self, value):
        self._verifyid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCreditAutofinanceVidGetResponse, self).parse_response_content(response_content)
        if 'verifyid' in response:
            self.verifyid = response['verifyid']
