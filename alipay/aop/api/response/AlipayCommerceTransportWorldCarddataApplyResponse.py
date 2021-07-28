#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorldBaseRPCResponseInfo import WorldBaseRPCResponseInfo
from alipay.aop.api.domain.WorldOfflineDataInfo import WorldOfflineDataInfo


class AlipayCommerceTransportWorldCarddataApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportWorldCarddataApplyResponse, self).__init__()
        self._card_no = None
        self._card_timestamp = None
        self._card_type = None
        self._error_message = None
        self._first_use_time = None
        self._sub_error_code = None
        self._user_id = None
        self._world_base_rpc_response_info = None
        self._world_offline_data_info = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_timestamp(self):
        return self._card_timestamp

    @card_timestamp.setter
    def card_timestamp(self, value):
        self._card_timestamp = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def first_use_time(self):
        return self._first_use_time

    @first_use_time.setter
    def first_use_time(self, value):
        self._first_use_time = value
    @property
    def sub_error_code(self):
        return self._sub_error_code

    @sub_error_code.setter
    def sub_error_code(self, value):
        self._sub_error_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def world_base_rpc_response_info(self):
        return self._world_base_rpc_response_info

    @world_base_rpc_response_info.setter
    def world_base_rpc_response_info(self, value):
        if isinstance(value, WorldBaseRPCResponseInfo):
            self._world_base_rpc_response_info = value
        else:
            self._world_base_rpc_response_info = WorldBaseRPCResponseInfo.from_alipay_dict(value)
    @property
    def world_offline_data_info(self):
        return self._world_offline_data_info

    @world_offline_data_info.setter
    def world_offline_data_info(self, value):
        if isinstance(value, WorldOfflineDataInfo):
            self._world_offline_data_info = value
        else:
            self._world_offline_data_info = WorldOfflineDataInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportWorldCarddataApplyResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'card_timestamp' in response:
            self.card_timestamp = response['card_timestamp']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'first_use_time' in response:
            self.first_use_time = response['first_use_time']
        if 'sub_error_code' in response:
            self.sub_error_code = response['sub_error_code']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'world_base_rpc_response_info' in response:
            self.world_base_rpc_response_info = response['world_base_rpc_response_info']
        if 'world_offline_data_info' in response:
            self.world_offline_data_info = response['world_offline_data_info']
