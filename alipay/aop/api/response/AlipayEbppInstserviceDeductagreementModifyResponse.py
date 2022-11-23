#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceDeductagreementModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceDeductagreementModifyResponse, self).__init__()
        self._result = None
        self._result_code = None
        self._result_msg = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceDeductagreementModifyResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
