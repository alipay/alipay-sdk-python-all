#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IoTBPaaSDeviceApplyBindInfo import IoTBPaaSDeviceApplyBindInfo


class AlipayOpenIotbpaasDevicebindApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotbpaasDevicebindApplyResponse, self).__init__()
        self._bind_info = None
        self._bind_status = None
        self._bind_token = None
        self._bind_url = None

    @property
    def bind_info(self):
        return self._bind_info

    @bind_info.setter
    def bind_info(self, value):
        if isinstance(value, IoTBPaaSDeviceApplyBindInfo):
            self._bind_info = value
        else:
            self._bind_info = IoTBPaaSDeviceApplyBindInfo.from_alipay_dict(value)
    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def bind_token(self):
        return self._bind_token

    @bind_token.setter
    def bind_token(self, value):
        self._bind_token = value
    @property
    def bind_url(self):
        return self._bind_url

    @bind_url.setter
    def bind_url(self, value):
        self._bind_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotbpaasDevicebindApplyResponse, self).parse_response_content(response_content)
        if 'bind_info' in response:
            self.bind_info = response['bind_info']
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'bind_token' in response:
            self.bind_token = response['bind_token']
        if 'bind_url' in response:
            self.bind_url = response['bind_url']
