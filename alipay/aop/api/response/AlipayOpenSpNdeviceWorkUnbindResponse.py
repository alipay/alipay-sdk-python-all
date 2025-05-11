#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNdeviceWorkUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNdeviceWorkUnbindResponse, self).__init__()
        self._out_biz_id = None
        self._unbind_result = None

    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def unbind_result(self):
        return self._unbind_result

    @unbind_result.setter
    def unbind_result(self, value):
        self._unbind_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNdeviceWorkUnbindResponse, self).parse_response_content(response_content)
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'unbind_result' in response:
            self.unbind_result = response['unbind_result']
