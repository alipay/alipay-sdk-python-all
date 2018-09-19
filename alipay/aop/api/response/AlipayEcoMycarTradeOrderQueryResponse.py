#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarTradeOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarTradeOrderQueryResponse, self).__init__()
        self._biz_trade_no = None
        self._buyer_id = None
        self._buyer_logon_id = None
        self._gmt_closed = None
        self._gmt_created = None
        self._gmt_payment = None
        self._gmt_payment_success = None
        self._gmt_refund = None
        self._gmt_refund_success = None
        self._gmt_updated = None
        self._out_biz_trade_no = None
        self._send_back_fee = None
        self._shop_id = None
        self._subject = None
        self._summary = None
        self._total_fee = None
        self._trade_no = None
        self._trade_status = None
        self._trade_type = None

    @property
    def biz_trade_no(self):
        return self._biz_trade_no

    @biz_trade_no.setter
    def biz_trade_no(self, value):
        self._biz_trade_no = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def gmt_closed(self):
        return self._gmt_closed

    @gmt_closed.setter
    def gmt_closed(self, value):
        self._gmt_closed = value
    @property
    def gmt_created(self):
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, value):
        self._gmt_created = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def gmt_payment_success(self):
        return self._gmt_payment_success

    @gmt_payment_success.setter
    def gmt_payment_success(self, value):
        self._gmt_payment_success = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def gmt_refund_success(self):
        return self._gmt_refund_success

    @gmt_refund_success.setter
    def gmt_refund_success(self, value):
        self._gmt_refund_success = value
    @property
    def gmt_updated(self):
        return self._gmt_updated

    @gmt_updated.setter
    def gmt_updated(self, value):
        self._gmt_updated = value
    @property
    def out_biz_trade_no(self):
        return self._out_biz_trade_no

    @out_biz_trade_no.setter
    def out_biz_trade_no(self, value):
        self._out_biz_trade_no = value
    @property
    def send_back_fee(self):
        return self._send_back_fee

    @send_back_fee.setter
    def send_back_fee(self, value):
        self._send_back_fee = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
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
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarTradeOrderQueryResponse, self).parse_response_content(response_content)
        if 'biz_trade_no' in response:
            self.biz_trade_no = response['biz_trade_no']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'gmt_closed' in response:
            self.gmt_closed = response['gmt_closed']
        if 'gmt_created' in response:
            self.gmt_created = response['gmt_created']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'gmt_payment_success' in response:
            self.gmt_payment_success = response['gmt_payment_success']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'gmt_refund_success' in response:
            self.gmt_refund_success = response['gmt_refund_success']
        if 'gmt_updated' in response:
            self.gmt_updated = response['gmt_updated']
        if 'out_biz_trade_no' in response:
            self.out_biz_trade_no = response['out_biz_trade_no']
        if 'send_back_fee' in response:
            self.send_back_fee = response['send_back_fee']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'subject' in response:
            self.subject = response['subject']
        if 'summary' in response:
            self.summary = response['summary']
        if 'total_fee' in response:
            self.total_fee = response['total_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
        if 'trade_type' in response:
            self.trade_type = response['trade_type']
