#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIndividualBusinessCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIndividualBusinessCertifyResponse, self).__init__()
        self._certify_result = None

    @property
    def certify_result(self):
        return self._certify_result

    @certify_result.setter
    def certify_result(self, value):
        self._certify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIndividualBusinessCertifyResponse, self).parse_response_content(response_content)
        if 'certify_result' in response:
            self.certify_result = response['certify_result']
