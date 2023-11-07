#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionOrderQueryResponse, self).__init__()
        self._alipay_order_detail_url = None
        self._amount = None
        self._currency = None
        self._order_status = None
        self._order_title = None
        self._out_order_no = None
        self._paid_amount = None
        self._unpaid_amount = None

    @property
    def alipay_order_detail_url(self):
        return self._alipay_order_detail_url

    @alipay_order_detail_url.setter
    def alipay_order_detail_url(self, value):
        self._alipay_order_detail_url = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def unpaid_amount(self):
        return self._unpaid_amount

    @unpaid_amount.setter
    def unpaid_amount(self, value):
        self._unpaid_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionOrderQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_detail_url' in response:
            self.alipay_order_detail_url = response['alipay_order_detail_url']
        if 'amount' in response:
            self.amount = response['amount']
        if 'currency' in response:
            self.currency = response['currency']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_title' in response:
            self.order_title = response['order_title']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'paid_amount' in response:
            self.paid_amount = response['paid_amount']
        if 'unpaid_amount' in response:
            self.unpaid_amount = response['unpaid_amount']
