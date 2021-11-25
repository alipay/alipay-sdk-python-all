#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandAssetQrcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetQrcodeQueryResponse, self).__init__()
        self._biz_type = None
        self._code_type = None
        self._dynamic_img_url = None
        self._token_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def dynamic_img_url(self):
        return self._dynamic_img_url

    @dynamic_img_url.setter
    def dynamic_img_url(self, value):
        self._dynamic_img_url = value
    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetQrcodeQueryResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'code_type' in response:
            self.code_type = response['code_type']
        if 'dynamic_img_url' in response:
            self.dynamic_img_url = response['dynamic_img_url']
        if 'token_id' in response:
            self.token_id = response['token_id']
