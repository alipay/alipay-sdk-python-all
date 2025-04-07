#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorNlinkUrlsecurityVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorNlinkUrlsecurityVerifyResponse, self).__init__()
        self._cost_time = None
        self._msg_info = None
        self._trace_id_info = None
        self._verify_flag = None

    @property
    def cost_time(self):
        return self._cost_time

    @cost_time.setter
    def cost_time(self, value):
        self._cost_time = value
    @property
    def msg_info(self):
        return self._msg_info

    @msg_info.setter
    def msg_info(self, value):
        self._msg_info = value
    @property
    def trace_id_info(self):
        return self._trace_id_info

    @trace_id_info.setter
    def trace_id_info(self, value):
        self._trace_id_info = value
    @property
    def verify_flag(self):
        return self._verify_flag

    @verify_flag.setter
    def verify_flag(self, value):
        self._verify_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorNlinkUrlsecurityVerifyResponse, self).parse_response_content(response_content)
        if 'cost_time' in response:
            self.cost_time = response['cost_time']
        if 'msg_info' in response:
            self.msg_info = response['msg_info']
        if 'trace_id_info' in response:
            self.trace_id_info = response['trace_id_info']
        if 'verify_flag' in response:
            self.verify_flag = response['verify_flag']
