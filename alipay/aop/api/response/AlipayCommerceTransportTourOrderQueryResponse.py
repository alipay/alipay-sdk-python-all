#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TourVoucherInfoQueryopenapiResult import TourVoucherInfoQueryopenapiResult


class AlipayCommerceTransportTourOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourOrderQueryResponse, self).__init__()
        self._amount = None
        self._order_id = None
        self._order_status = None
        self._order_time = None
        self._total_amount = None
        self._trade_no = None
        self._voucher_list = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, TourVoucherInfoQueryopenapiResult):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(TourVoucherInfoQueryopenapiResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourOrderQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_time' in response:
            self.order_time = response['order_time']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'voucher_list' in response:
            self.voucher_list = response['voucher_list']
