#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelInfo import ChannelInfo


class AlipayPayAppChannelConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppChannelConsultResponse, self).__init__()
        self._channel_info_list = None
        self._pre_consult_id = None
        self._real_alipay_account_id = None
        self._real_alipay_open_id = None
        self._virtual_alipay_open_id = None
        self._virtual_alipay_user_id = None

    @property
    def channel_info_list(self):
        return self._channel_info_list

    @channel_info_list.setter
    def channel_info_list(self, value):
        if isinstance(value, list):
            self._channel_info_list = list()
            for i in value:
                if isinstance(i, ChannelInfo):
                    self._channel_info_list.append(i)
                else:
                    self._channel_info_list.append(ChannelInfo.from_alipay_dict(i))
    @property
    def pre_consult_id(self):
        return self._pre_consult_id

    @pre_consult_id.setter
    def pre_consult_id(self, value):
        self._pre_consult_id = value
    @property
    def real_alipay_account_id(self):
        return self._real_alipay_account_id

    @real_alipay_account_id.setter
    def real_alipay_account_id(self, value):
        self._real_alipay_account_id = value
    @property
    def real_alipay_open_id(self):
        return self._real_alipay_open_id

    @real_alipay_open_id.setter
    def real_alipay_open_id(self, value):
        self._real_alipay_open_id = value
    @property
    def virtual_alipay_open_id(self):
        return self._virtual_alipay_open_id

    @virtual_alipay_open_id.setter
    def virtual_alipay_open_id(self, value):
        self._virtual_alipay_open_id = value
    @property
    def virtual_alipay_user_id(self):
        return self._virtual_alipay_user_id

    @virtual_alipay_user_id.setter
    def virtual_alipay_user_id(self, value):
        self._virtual_alipay_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppChannelConsultResponse, self).parse_response_content(response_content)
        if 'channel_info_list' in response:
            self.channel_info_list = response['channel_info_list']
        if 'pre_consult_id' in response:
            self.pre_consult_id = response['pre_consult_id']
        if 'real_alipay_account_id' in response:
            self.real_alipay_account_id = response['real_alipay_account_id']
        if 'real_alipay_open_id' in response:
            self.real_alipay_open_id = response['real_alipay_open_id']
        if 'virtual_alipay_open_id' in response:
            self.virtual_alipay_open_id = response['virtual_alipay_open_id']
        if 'virtual_alipay_user_id' in response:
            self.virtual_alipay_user_id = response['virtual_alipay_user_id']
