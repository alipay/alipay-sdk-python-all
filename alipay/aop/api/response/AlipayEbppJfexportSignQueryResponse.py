#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfexportSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfexportSignQueryResponse, self).__init__()
        self._asset_id = None
        self._assigned_channel = None
        self._bank_id = None
        self._channel_full_name = None
        self._current_user_sign = None
        self._status = None
        self._user_direct_sign = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def assigned_channel(self):
        return self._assigned_channel

    @assigned_channel.setter
    def assigned_channel(self, value):
        self._assigned_channel = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def channel_full_name(self):
        return self._channel_full_name

    @channel_full_name.setter
    def channel_full_name(self, value):
        self._channel_full_name = value
    @property
    def current_user_sign(self):
        return self._current_user_sign

    @current_user_sign.setter
    def current_user_sign(self, value):
        self._current_user_sign = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_direct_sign(self):
        return self._user_direct_sign

    @user_direct_sign.setter
    def user_direct_sign(self, value):
        self._user_direct_sign = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfexportSignQueryResponse, self).parse_response_content(response_content)
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'assigned_channel' in response:
            self.assigned_channel = response['assigned_channel']
        if 'bank_id' in response:
            self.bank_id = response['bank_id']
        if 'channel_full_name' in response:
            self.channel_full_name = response['channel_full_name']
        if 'current_user_sign' in response:
            self.current_user_sign = response['current_user_sign']
        if 'status' in response:
            self.status = response['status']
        if 'user_direct_sign' in response:
            self.user_direct_sign = response['user_direct_sign']
