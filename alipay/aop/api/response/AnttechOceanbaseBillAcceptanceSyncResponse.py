#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseBillAcceptanceSyncResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseBillAcceptanceSyncResponse, self).__init__()
        self._error_msg = None

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseBillAcceptanceSyncResponse, self).parse_response_content(response_content)
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
