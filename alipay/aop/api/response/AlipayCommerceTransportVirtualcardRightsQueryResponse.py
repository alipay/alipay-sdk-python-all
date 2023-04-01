#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVirtualcardRightsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVirtualcardRightsQueryResponse, self).__init__()
        self._card_no = None
        self._card_type = None
        self._open_id = None
        self._right_data = None
        self._right_type_list = None
        self._user_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def right_data(self):
        return self._right_data

    @right_data.setter
    def right_data(self, value):
        self._right_data = value
    @property
    def right_type_list(self):
        return self._right_type_list

    @right_type_list.setter
    def right_type_list(self, value):
        if isinstance(value, list):
            self._right_type_list = list()
            for i in value:
                self._right_type_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVirtualcardRightsQueryResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'right_data' in response:
            self.right_data = response['right_data']
        if 'right_type_list' in response:
            self.right_type_list = response['right_type_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
