#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobResumeauthloginurlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobResumeauthloginurlGetResponse, self).__init__()
        self._resume_auth_login_url = None

    @property
    def resume_auth_login_url(self):
        return self._resume_auth_login_url

    @resume_auth_login_url.setter
    def resume_auth_login_url(self, value):
        self._resume_auth_login_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobResumeauthloginurlGetResponse, self).parse_response_content(response_content)
        if 'resume_auth_login_url' in response:
            self.resume_auth_login_url = response['resume_auth_login_url']
