#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNdeviceWorkBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNdeviceWorkBindResponse, self).__init__()
        self._bind_result = None
        self._device_sn = None
        self._device_type = None
        self._out_biz_id = None

    @property
    def bind_result(self):
        return self._bind_result

    @bind_result.setter
    def bind_result(self, value):
        self._bind_result = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNdeviceWorkBindResponse, self).parse_response_content(response_content)
        if 'bind_result' in response:
            self.bind_result = response['bind_result']
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'device_type' in response:
            self.device_type = response['device_type']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
