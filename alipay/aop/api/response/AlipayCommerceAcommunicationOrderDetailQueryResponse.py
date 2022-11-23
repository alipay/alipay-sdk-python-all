#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationOrderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationOrderDetailQueryResponse, self).__init__()
        self._bill_key = None
        self._create_time = None
        self._detail_url = None
        self._modified_time = None
        self._order_amount = None
        self._order_no = None
        self._trade_no = None
        self._trade_status = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationOrderDetailQueryResponse, self).parse_response_content(response_content)
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'detail_url' in response:
            self.detail_url = response['detail_url']
        if 'modified_time' in response:
            self.modified_time = response['modified_time']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
