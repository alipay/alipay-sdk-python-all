#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHdfServicerightCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHdfServicerightCheckResponse, self).__init__()
        self._biz_identity = None
        self._has_right = None
        self._open_partner_user_id = None
        self._right_cnt = None
        self._right_end_time = None
        self._right_start_time = None
        self._right_total_cnt = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def has_right(self):
        return self._has_right

    @has_right.setter
    def has_right(self, value):
        self._has_right = value
    @property
    def open_partner_user_id(self):
        return self._open_partner_user_id

    @open_partner_user_id.setter
    def open_partner_user_id(self, value):
        self._open_partner_user_id = value
    @property
    def right_cnt(self):
        return self._right_cnt

    @right_cnt.setter
    def right_cnt(self, value):
        self._right_cnt = value
    @property
    def right_end_time(self):
        return self._right_end_time

    @right_end_time.setter
    def right_end_time(self, value):
        self._right_end_time = value
    @property
    def right_start_time(self):
        return self._right_start_time

    @right_start_time.setter
    def right_start_time(self, value):
        self._right_start_time = value
    @property
    def right_total_cnt(self):
        return self._right_total_cnt

    @right_total_cnt.setter
    def right_total_cnt(self, value):
        self._right_total_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHdfServicerightCheckResponse, self).parse_response_content(response_content)
        if 'biz_identity' in response:
            self.biz_identity = response['biz_identity']
        if 'has_right' in response:
            self.has_right = response['has_right']
        if 'open_partner_user_id' in response:
            self.open_partner_user_id = response['open_partner_user_id']
        if 'right_cnt' in response:
            self.right_cnt = response['right_cnt']
        if 'right_end_time' in response:
            self.right_end_time = response['right_end_time']
        if 'right_start_time' in response:
            self.right_start_time = response['right_start_time']
        if 'right_total_cnt' in response:
            self.right_total_cnt = response['right_total_cnt']
