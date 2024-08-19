#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiStepTransOrderDetailResponse import MultiStepTransOrderDetailResponse


class AlipayFundTransMultistepQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransMultistepQueryResponse, self).__init__()
        self._order_details = None
        self._order_id = None
        self._out_biz_no = None
        self._remark = None
        self._request_user_id = None
        self._total_amount = None
        self._total_count = None

    @property
    def order_details(self):
        return self._order_details

    @order_details.setter
    def order_details(self, value):
        if isinstance(value, list):
            self._order_details = list()
            for i in value:
                if isinstance(i, MultiStepTransOrderDetailResponse):
                    self._order_details.append(i)
                else:
                    self._order_details.append(MultiStepTransOrderDetailResponse.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_user_id(self):
        return self._request_user_id

    @request_user_id.setter
    def request_user_id(self, value):
        self._request_user_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransMultistepQueryResponse, self).parse_response_content(response_content)
        if 'order_details' in response:
            self.order_details = response['order_details']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'remark' in response:
            self.remark = response['remark']
        if 'request_user_id' in response:
            self.request_user_id = response['request_user_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_count' in response:
            self.total_count = response['total_count']
