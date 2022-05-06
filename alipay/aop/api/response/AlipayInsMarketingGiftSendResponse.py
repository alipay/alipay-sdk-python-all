#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RightNoSendList import RightNoSendList


class AlipayInsMarketingGiftSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingGiftSendResponse, self).__init__()
        self._channel = None
        self._gift_prod_code = None
        self._right_no_send_list = None
        self._send_sum_insured = None
        self._success = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def gift_prod_code(self):
        return self._gift_prod_code

    @gift_prod_code.setter
    def gift_prod_code(self, value):
        self._gift_prod_code = value
    @property
    def right_no_send_list(self):
        return self._right_no_send_list

    @right_no_send_list.setter
    def right_no_send_list(self, value):
        if isinstance(value, list):
            self._right_no_send_list = list()
            for i in value:
                if isinstance(i, RightNoSendList):
                    self._right_no_send_list.append(i)
                else:
                    self._right_no_send_list.append(RightNoSendList.from_alipay_dict(i))
    @property
    def send_sum_insured(self):
        return self._send_sum_insured

    @send_sum_insured.setter
    def send_sum_insured(self, value):
        self._send_sum_insured = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingGiftSendResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'gift_prod_code' in response:
            self.gift_prod_code = response['gift_prod_code']
        if 'right_no_send_list' in response:
            self.right_no_send_list = response['right_no_send_list']
        if 'send_sum_insured' in response:
            self.send_sum_insured = response['send_sum_insured']
        if 'success' in response:
            self.success = response['success']
        if 'user_id' in response:
            self.user_id = response['user_id']
