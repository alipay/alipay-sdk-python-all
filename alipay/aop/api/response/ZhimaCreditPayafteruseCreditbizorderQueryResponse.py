#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseCreditbizorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseCreditbizorderQueryResponse, self).__init__()
        self._create_time = None
        self._credit_agreement_id = None
        self._credit_biz_order_id = None
        self._order_status = None
        self._product_code = None
        self._total_amount = None
        self._trade_no = None
        self._zm_service_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
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
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseCreditbizorderQueryResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'credit_agreement_id' in response:
            self.credit_agreement_id = response['credit_agreement_id']
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'zm_service_id' in response:
            self.zm_service_id = response['zm_service_id']
