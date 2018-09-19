#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileCodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileCodeCreateResponse, self).__init__()
        self._biz_linked_id = None
        self._biz_type = None
        self._code_status = None
        self._context_str = None
        self._dynamic_img_url = None
        self._expire_date = None
        self._is_direct = None
        self._memo = None
        self._qr_code = None
        self._qr_token = None
        self._source_id = None
        self._start_date = None
        self._user_id = None

    @property
    def biz_linked_id(self):
        return self._biz_linked_id

    @biz_linked_id.setter
    def biz_linked_id(self, value):
        self._biz_linked_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def code_status(self):
        return self._code_status

    @code_status.setter
    def code_status(self, value):
        self._code_status = value
    @property
    def context_str(self):
        return self._context_str

    @context_str.setter
    def context_str(self, value):
        self._context_str = value
    @property
    def dynamic_img_url(self):
        return self._dynamic_img_url

    @dynamic_img_url.setter
    def dynamic_img_url(self, value):
        self._dynamic_img_url = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def is_direct(self):
        return self._is_direct

    @is_direct.setter
    def is_direct(self, value):
        self._is_direct = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def qr_token(self):
        return self._qr_token

    @qr_token.setter
    def qr_token(self, value):
        self._qr_token = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileCodeCreateResponse, self).parse_response_content(response_content)
        if 'biz_linked_id' in response:
            self.biz_linked_id = response['biz_linked_id']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'code_status' in response:
            self.code_status = response['code_status']
        if 'context_str' in response:
            self.context_str = response['context_str']
        if 'dynamic_img_url' in response:
            self.dynamic_img_url = response['dynamic_img_url']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'is_direct' in response:
            self.is_direct = response['is_direct']
        if 'memo' in response:
            self.memo = response['memo']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'qr_token' in response:
            self.qr_token = response['qr_token']
        if 'source_id' in response:
            self.source_id = response['source_id']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'user_id' in response:
            self.user_id = response['user_id']
