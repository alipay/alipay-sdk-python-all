#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAvailableVoucher import UserAvailableVoucher
from alipay.aop.api.domain.UserAvailableVoucher import UserAvailableVoucher


class AlipayCommerceTransportUservoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportUservoucherQueryResponse, self).__init__()
        self._best_voucher = None
        self._user_available_voucher_list = None

    @property
    def best_voucher(self):
        return self._best_voucher

    @best_voucher.setter
    def best_voucher(self, value):
        if isinstance(value, UserAvailableVoucher):
            self._best_voucher = value
        else:
            self._best_voucher = UserAvailableVoucher.from_alipay_dict(value)
    @property
    def user_available_voucher_list(self):
        return self._user_available_voucher_list

    @user_available_voucher_list.setter
    def user_available_voucher_list(self, value):
        if isinstance(value, list):
            self._user_available_voucher_list = list()
            for i in value:
                if isinstance(i, UserAvailableVoucher):
                    self._user_available_voucher_list.append(i)
                else:
                    self._user_available_voucher_list.append(UserAvailableVoucher.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportUservoucherQueryResponse, self).parse_response_content(response_content)
        if 'best_voucher' in response:
            self.best_voucher = response['best_voucher']
        if 'user_available_voucher_list' in response:
            self.user_available_voucher_list = response['user_available_voucher_list']
