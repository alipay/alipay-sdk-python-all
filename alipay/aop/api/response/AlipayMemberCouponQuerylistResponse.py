#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Coupon import Coupon


class AlipayMemberCouponQuerylistResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMemberCouponQuerylistResponse, self).__init__()
        self._coupon_list = None
        self._error_code = None
        self._error_msg = None
        self._list_size = None
        self._success_code = None
        self._total_num = None

    @property
    def coupon_list(self):
        return self._coupon_list

    @coupon_list.setter
    def coupon_list(self, value):
        if isinstance(value, list):
            self._coupon_list = list()
            for i in value:
                if isinstance(i, Coupon):
                    self._coupon_list.append(i)
                else:
                    self._coupon_list.append(Coupon.from_alipay_dict(i))
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def list_size(self):
        return self._list_size

    @list_size.setter
    def list_size(self, value):
        self._list_size = value
    @property
    def success_code(self):
        return self._success_code

    @success_code.setter
    def success_code(self, value):
        self._success_code = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayMemberCouponQuerylistResponse, self).parse_response_content(response_content)
        if 'coupon_list' in response:
            self.coupon_list = response['coupon_list']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'list_size' in response:
            self.list_size = response['list_size']
        if 'success_code' in response:
            self.success_code = response['success_code']
        if 'total_num' in response:
            self.total_num = response['total_num']
