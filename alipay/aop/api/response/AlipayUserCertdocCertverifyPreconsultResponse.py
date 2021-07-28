#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertdocCertverifyPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertdocCertverifyPreconsultResponse, self).__init__()
        self._verify_id = None

    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertdocCertverifyPreconsultResponse, self).parse_response_content(response_content)
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
