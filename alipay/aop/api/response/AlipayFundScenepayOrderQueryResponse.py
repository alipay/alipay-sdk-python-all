#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScenePayBusinessParamDTO import ScenePayBusinessParamDTO


class AlipayFundScenepayOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundScenepayOrderQueryResponse, self).__init__()
        self._biz_amount = None
        self._biz_no = None
        self._business_params = None
        self._buyer_id = None
        self._gmt_payment = None
        self._is_use_expected_discount = None
        self._order_status = None
        self._out_biz_no = None
        self._out_trade_no = None
        self._refund_detail_list = None
        self._total_amount = None
        self._trade_no = None

    @property
    def biz_amount(self):
        return self._biz_amount

    @biz_amount.setter
    def biz_amount(self, value):
        self._biz_amount = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, ScenePayBusinessParamDTO):
            self._business_params = value
        else:
            self._business_params = ScenePayBusinessParamDTO.from_alipay_dict(value)
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def is_use_expected_discount(self):
        return self._is_use_expected_discount

    @is_use_expected_discount.setter
    def is_use_expected_discount(self, value):
        self._is_use_expected_discount = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_detail_list(self):
        return self._refund_detail_list

    @refund_detail_list.setter
    def refund_detail_list(self, value):
        self._refund_detail_list = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayFundScenepayOrderQueryResponse, self).parse_response_content(response_content)
        if 'biz_amount' in response:
            self.biz_amount = response['biz_amount']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'business_params' in response:
            self.business_params = response['business_params']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'is_use_expected_discount' in response:
            self.is_use_expected_discount = response['is_use_expected_discount']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_detail_list' in response:
            self.refund_detail_list = response['refund_detail_list']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
