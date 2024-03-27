#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpSiriusApplyCallbackResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSiriusApplyCallbackResponse, self).__init__()
        self._biz_id = None
        self._message = None
        self._request_id = None
        self._resp_code = None
        self._site_user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def resp_code(self):
        return self._resp_code

    @resp_code.setter
    def resp_code(self, value):
        self._resp_code = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSiriusApplyCallbackResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'message' in response:
            self.message = response['message']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'resp_code' in response:
            self.resp_code = response['resp_code']
        if 'site_user_id' in response:
            self.site_user_id = response['site_user_id']
