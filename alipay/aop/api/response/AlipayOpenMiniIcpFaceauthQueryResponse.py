#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIcpFaceauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpFaceauthQueryResponse, self).__init__()
        self._certify_result_desc = None
        self._certify_result_status = None

    @property
    def certify_result_desc(self):
        return self._certify_result_desc

    @certify_result_desc.setter
    def certify_result_desc(self, value):
        self._certify_result_desc = value
    @property
    def certify_result_status(self):
        return self._certify_result_status

    @certify_result_status.setter
    def certify_result_status(self, value):
        self._certify_result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpFaceauthQueryResponse, self).parse_response_content(response_content)
        if 'certify_result_desc' in response:
            self.certify_result_desc = response['certify_result_desc']
        if 'certify_result_status' in response:
            self.certify_result_status = response['certify_result_status']
