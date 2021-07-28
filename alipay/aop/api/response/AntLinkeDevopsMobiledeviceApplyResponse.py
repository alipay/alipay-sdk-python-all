#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntLinkeDevopsMobiledeviceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AntLinkeDevopsMobiledeviceApplyResponse, self).__init__()
        self._access_token = None
        self._device_id = None
        self._device_info = None
        self._device_status = None
        self._expire_time = None
        self._image_info = None
        self._remote_port = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        self._device_info = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def image_info(self):
        return self._image_info

    @image_info.setter
    def image_info(self, value):
        self._image_info = value
    @property
    def remote_port(self):
        return self._remote_port

    @remote_port.setter
    def remote_port(self, value):
        self._remote_port = value

    def parse_response_content(self, response_content):
        response = super(AntLinkeDevopsMobiledeviceApplyResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'device_info' in response:
            self.device_info = response['device_info']
        if 'device_status' in response:
            self.device_status = response['device_status']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'image_info' in response:
            self.image_info = response['image_info']
        if 'remote_port' in response:
            self.remote_port = response['remote_port']
