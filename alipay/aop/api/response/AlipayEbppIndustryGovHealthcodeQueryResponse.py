#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryGovHealthcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryGovHealthcodeQueryResponse, self).__init__()
        self._code_color = None
        self._code_content = None
        self._refresh_time = None
        self._user_name = None

    @property
    def code_color(self):
        return self._code_color

    @code_color.setter
    def code_color(self, value):
        self._code_color = value
    @property
    def code_content(self):
        return self._code_content

    @code_content.setter
    def code_content(self, value):
        self._code_content = value
    @property
    def refresh_time(self):
        return self._refresh_time

    @refresh_time.setter
    def refresh_time(self, value):
        self._refresh_time = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryGovHealthcodeQueryResponse, self).parse_response_content(response_content)
        if 'code_color' in response:
            self.code_color = response['code_color']
        if 'code_content' in response:
            self.code_content = response['code_content']
        if 'refresh_time' in response:
            self.refresh_time = response['refresh_time']
        if 'user_name' in response:
            self.user_name = response['user_name']
