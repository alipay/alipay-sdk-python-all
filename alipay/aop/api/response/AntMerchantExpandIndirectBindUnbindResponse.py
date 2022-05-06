#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectBindUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectBindUnbindResponse, self).__init__()
        self._alipay_account = None
        self._handle_result = None
        self._has_apply = None
        self._order_id = None
        self._user_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def handle_result(self):
        return self._handle_result

    @handle_result.setter
    def handle_result(self, value):
        self._handle_result = value
    @property
    def has_apply(self):
        return self._has_apply

    @has_apply.setter
    def has_apply(self, value):
        self._has_apply = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectBindUnbindResponse, self).parse_response_content(response_content)
        if 'alipay_account' in response:
            self.alipay_account = response['alipay_account']
        if 'handle_result' in response:
            self.handle_result = response['handle_result']
        if 'has_apply' in response:
            self.has_apply = response['has_apply']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
