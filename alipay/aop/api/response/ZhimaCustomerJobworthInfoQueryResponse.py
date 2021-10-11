#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthInfoQueryResponse, self).__init__()
        self._acceptance_id = None
        self._auth_token = None
        self._picture_url = None
        self._sub_code = None
        self._sub_msg = None
        self._update_url = None
        self._url = None

    @property
    def acceptance_id(self):
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, value):
        self._acceptance_id = value
    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
    @property
    def picture_url(self):
        return self._picture_url

    @picture_url.setter
    def picture_url(self, value):
        self._picture_url = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_msg(self):
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, value):
        self._sub_msg = value
    @property
    def update_url(self):
        return self._update_url

    @update_url.setter
    def update_url(self, value):
        self._update_url = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthInfoQueryResponse, self).parse_response_content(response_content)
        if 'acceptance_id' in response:
            self.acceptance_id = response['acceptance_id']
        if 'auth_token' in response:
            self.auth_token = response['auth_token']
        if 'picture_url' in response:
            self.picture_url = response['picture_url']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
        if 'update_url' in response:
            self.update_url = response['update_url']
        if 'url' in response:
            self.url = response['url']
