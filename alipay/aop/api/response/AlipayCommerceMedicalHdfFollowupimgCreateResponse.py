#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfFollowupimgCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfFollowupimgCreateResponse, self).__init__()
        self._image_url = None
        self._open_agent_flag = None
        self._qr_image_url = None
        self._redirect_url = None
        self._source_type = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def open_agent_flag(self):
        return self._open_agent_flag

    @open_agent_flag.setter
    def open_agent_flag(self, value):
        self._open_agent_flag = value
    @property
    def qr_image_url(self):
        return self._qr_image_url

    @qr_image_url.setter
    def qr_image_url(self, value):
        self._qr_image_url = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfFollowupimgCreateResponse, self).parse_response_content(response_content)
        if 'image_url' in response:
            self.image_url = response['image_url']
        if 'open_agent_flag' in response:
            self.open_agent_flag = response['open_agent_flag']
        if 'qr_image_url' in response:
            self.qr_image_url = response['qr_image_url']
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']
        if 'source_type' in response:
            self.source_type = response['source_type']
