#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RightNoOpenedList import RightNoOpenedList


class AlipayInsMarketingGiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingGiftQueryResponse, self).__init__()
        self._channel = None
        self._gift_prod_code = None
        self._opened = None
        self._right_no_opened_list = None
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
    def opened(self):
        return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def right_no_opened_list(self):
        return self._right_no_opened_list

    @right_no_opened_list.setter
    def right_no_opened_list(self, value):
        if isinstance(value, list):
            self._right_no_opened_list = list()
            for i in value:
                if isinstance(i, RightNoOpenedList):
                    self._right_no_opened_list.append(i)
                else:
                    self._right_no_opened_list.append(RightNoOpenedList.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingGiftQueryResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'gift_prod_code' in response:
            self.gift_prod_code = response['gift_prod_code']
        if 'opened' in response:
            self.opened = response['opened']
        if 'right_no_opened_list' in response:
            self.right_no_opened_list = response['right_no_opened_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
