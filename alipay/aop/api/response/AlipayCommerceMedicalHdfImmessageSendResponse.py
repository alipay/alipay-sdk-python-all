#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfImmessageSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfImmessageSendResponse, self).__init__()
        self._app_msg_id = None
        self._msg_id = None
        self._send_time = None

    @property
    def app_msg_id(self):
        return self._app_msg_id

    @app_msg_id.setter
    def app_msg_id(self, value):
        self._app_msg_id = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfImmessageSendResponse, self).parse_response_content(response_content)
        if 'app_msg_id' in response:
            self.app_msg_id = response['app_msg_id']
        if 'msg_id' in response:
            self.msg_id = response['msg_id']
        if 'send_time' in response:
            self.send_time = response['send_time']
