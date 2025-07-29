#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestFreeplantApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestFreeplantApplyResponse, self).__init__()
        self._certificate_id = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestFreeplantApplyResponse, self).parse_response_content(response_content)
        if 'certificate_id' in response:
            self.certificate_id = response['certificate_id']
