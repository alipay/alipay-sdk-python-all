#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeDeviceInfo import AmpeDeviceInfo


class AlipayOpenMiniAmpeChatSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeChatSendResponse, self).__init__()
        self._content = None
        self._device_info = None
        self._req_no = None
        self._session_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, AmpeDeviceInfo):
            self._device_info = value
        else:
            self._device_info = AmpeDeviceInfo.from_alipay_dict(value)
    @property
    def req_no(self):
        return self._req_no

    @req_no.setter
    def req_no(self, value):
        self._req_no = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeChatSendResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'device_info' in response:
            self.device_info = response['device_info']
        if 'req_no' in response:
            self.req_no = response['req_no']
        if 'session_id' in response:
            self.session_id = response['session_id']
