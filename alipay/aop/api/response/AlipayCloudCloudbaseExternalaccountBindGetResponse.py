#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseExternalaccountBindGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseExternalaccountBindGetResponse, self).__init__()
        self._access_token = None
        self._biz_app_id = None
        self._shadow_wallet_id = None
        self._status = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def shadow_wallet_id(self):
        return self._shadow_wallet_id

    @shadow_wallet_id.setter
    def shadow_wallet_id(self, value):
        self._shadow_wallet_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseExternalaccountBindGetResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'biz_app_id' in response:
            self.biz_app_id = response['biz_app_id']
        if 'shadow_wallet_id' in response:
            self.shadow_wallet_id = response['shadow_wallet_id']
        if 'status' in response:
            self.status = response['status']
