#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Member import Member
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpayTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpayTradeQueryResponse, self).__init__()
        self._buyer = None
        self._buyer_scene_id = None
        self._confirm_amt = None
        self._create_date = None
        self._effect_date = None
        self._out_order_no = None
        self._refund_amt = None
        self._seller = None
        self._seller_scene_id = None
        self._source_order_no = None
        self._status = None
        self._trace_id = None
        self._trade_amt = None
        self._trade_no = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def buyer_scene_id(self):
        return self._buyer_scene_id

    @buyer_scene_id.setter
    def buyer_scene_id(self, value):
        self._buyer_scene_id = value
    @property
    def confirm_amt(self):
        return self._confirm_amt

    @confirm_amt.setter
    def confirm_amt(self, value):
        self._confirm_amt = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refund_amt(self):
        return self._refund_amt

    @refund_amt.setter
    def refund_amt(self, value):
        self._refund_amt = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, Member):
            self._seller = value
        else:
            self._seller = Member.from_alipay_dict(value)
    @property
    def seller_scene_id(self):
        return self._seller_scene_id

    @seller_scene_id.setter
    def seller_scene_id(self, value):
        self._seller_scene_id = value
    @property
    def source_order_no(self):
        return self._source_order_no

    @source_order_no.setter
    def source_order_no(self, value):
        self._source_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def trade_amt(self):
        return self._trade_amt

    @trade_amt.setter
    def trade_amt(self, value):
        self._trade_amt = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpayTradeQueryResponse, self).parse_response_content(response_content)
        if 'buyer' in response:
            self.buyer = response['buyer']
        if 'buyer_scene_id' in response:
            self.buyer_scene_id = response['buyer_scene_id']
        if 'confirm_amt' in response:
            self.confirm_amt = response['confirm_amt']
        if 'create_date' in response:
            self.create_date = response['create_date']
        if 'effect_date' in response:
            self.effect_date = response['effect_date']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'refund_amt' in response:
            self.refund_amt = response['refund_amt']
        if 'seller' in response:
            self.seller = response['seller']
        if 'seller_scene_id' in response:
            self.seller_scene_id = response['seller_scene_id']
        if 'source_order_no' in response:
            self.source_order_no = response['source_order_no']
        if 'status' in response:
            self.status = response['status']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'trade_amt' in response:
            self.trade_amt = response['trade_amt']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
