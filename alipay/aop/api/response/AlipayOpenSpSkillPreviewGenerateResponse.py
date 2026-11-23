#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpSkillPreviewGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillPreviewGenerateResponse, self).__init__()
        self._ability_code = None
        self._ability_version = None
        self._expire_seconds = None
        self._expire_time = None
        self._preview_url = None
        self._qr_code_url = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def ability_version(self):
        return self._ability_version

    @ability_version.setter
    def ability_version(self, value):
        self._ability_version = value
    @property
    def expire_seconds(self):
        return self._expire_seconds

    @expire_seconds.setter
    def expire_seconds(self, value):
        self._expire_seconds = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillPreviewGenerateResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'ability_version' in response:
            self.ability_version = response['ability_version']
        if 'expire_seconds' in response:
            self.expire_seconds = response['expire_seconds']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'preview_url' in response:
            self.preview_url = response['preview_url']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
