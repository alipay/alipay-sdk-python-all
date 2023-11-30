#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserKabaoVoucherCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserKabaoVoucherCreateResponse, self).__init__()
        self._error_msg = None
        self._instance_id = None
        self._out_instance_id = None

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def out_instance_id(self):
        return self._out_instance_id

    @out_instance_id.setter
    def out_instance_id(self, value):
        self._out_instance_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserKabaoVoucherCreateResponse, self).parse_response_content(response_content)
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'instance_id' in response:
            self.instance_id = response['instance_id']
        if 'out_instance_id' in response:
            self.out_instance_id = response['out_instance_id']
