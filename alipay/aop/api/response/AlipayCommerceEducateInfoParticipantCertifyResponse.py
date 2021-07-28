#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateInfoParticipantCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateInfoParticipantCertifyResponse, self).__init__()
        self._out_payid = None

    @property
    def out_payid(self):
        return self._out_payid

    @out_payid.setter
    def out_payid(self, value):
        self._out_payid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateInfoParticipantCertifyResponse, self).parse_response_content(response_content)
        if 'out_payid' in response:
            self.out_payid = response['out_payid']
