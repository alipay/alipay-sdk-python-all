#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringOrderPayResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderPayResponse, self).__init__()
        self._biz_type = None
        self._merchant_pid = None
        self._shop_id = None
        self._table_num = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderPayResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'table_num' in response:
            self.table_num = response['table_num']
        if 'user_id' in response:
            self.user_id = response['user_id']
