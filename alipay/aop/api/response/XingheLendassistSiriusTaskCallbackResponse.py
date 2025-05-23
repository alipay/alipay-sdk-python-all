#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistSiriusTaskCallbackResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistSiriusTaskCallbackResponse, self).__init__()
        self._biz_id = None
        self._channel_code = None
        self._message = None
        self._mode_code = None
        self._op_token = None
        self._request_id = None
        self._resp_code = None
        self._scene_code = None
        self._sirius_app_id = None
        self._sirius_code = None
        self._sirius_env = None
        self._site_user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def mode_code(self):
        return self._mode_code

    @mode_code.setter
    def mode_code(self, value):
        self._mode_code = value
    @property
    def op_token(self):
        return self._op_token

    @op_token.setter
    def op_token(self, value):
        self._op_token = value
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
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sirius_app_id(self):
        return self._sirius_app_id

    @sirius_app_id.setter
    def sirius_app_id(self, value):
        self._sirius_app_id = value
    @property
    def sirius_code(self):
        return self._sirius_code

    @sirius_code.setter
    def sirius_code(self, value):
        self._sirius_code = value
    @property
    def sirius_env(self):
        return self._sirius_env

    @sirius_env.setter
    def sirius_env(self, value):
        self._sirius_env = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistSiriusTaskCallbackResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'channel_code' in response:
            self.channel_code = response['channel_code']
        if 'message' in response:
            self.message = response['message']
        if 'mode_code' in response:
            self.mode_code = response['mode_code']
        if 'op_token' in response:
            self.op_token = response['op_token']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'resp_code' in response:
            self.resp_code = response['resp_code']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'sirius_app_id' in response:
            self.sirius_app_id = response['sirius_app_id']
        if 'sirius_code' in response:
            self.sirius_code = response['sirius_code']
        if 'sirius_env' in response:
            self.sirius_env = response['sirius_env']
        if 'site_user_id' in response:
            self.site_user_id = response['site_user_id']
