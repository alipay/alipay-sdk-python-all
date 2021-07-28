#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantOrderExternalPaychannelSyncModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_status = None
        self._buyer_pay_amount = None
        self._discount_amount = None
        self._fund_bill_list = None
        self._gmt_payment = None
        self._mdiscount_amount = None
        self._notify_time = None
        self._notify_type = None
        self._origin_trade_no = None
        self._out_biz_no = None
        self._out_request_no = None
        self._pay_channel = None
        self._receipt_amount = None
        self._refund_amount = None
        self._refund_total_amount = None
        self._total_amount = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        self._fund_bill_list = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def mdiscount_amount(self):
        return self._mdiscount_amount

    @mdiscount_amount.setter
    def mdiscount_amount(self, value):
        self._mdiscount_amount = value
    @property
    def notify_time(self):
        return self._notify_time

    @notify_time.setter
    def notify_time(self, value):
        self._notify_time = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def origin_trade_no(self):
        return self._origin_trade_no

    @origin_trade_no.setter
    def origin_trade_no(self, value):
        self._origin_trade_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_total_amount(self):
        return self._refund_total_amount

    @refund_total_amount.setter
    def refund_total_amount(self, value):
        self._refund_total_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.buyer_pay_amount:
            if hasattr(self.buyer_pay_amount, 'to_alipay_dict'):
                params['buyer_pay_amount'] = self.buyer_pay_amount.to_alipay_dict()
            else:
                params['buyer_pay_amount'] = self.buyer_pay_amount
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.fund_bill_list:
            if hasattr(self.fund_bill_list, 'to_alipay_dict'):
                params['fund_bill_list'] = self.fund_bill_list.to_alipay_dict()
            else:
                params['fund_bill_list'] = self.fund_bill_list
        if self.gmt_payment:
            if hasattr(self.gmt_payment, 'to_alipay_dict'):
                params['gmt_payment'] = self.gmt_payment.to_alipay_dict()
            else:
                params['gmt_payment'] = self.gmt_payment
        if self.mdiscount_amount:
            if hasattr(self.mdiscount_amount, 'to_alipay_dict'):
                params['mdiscount_amount'] = self.mdiscount_amount.to_alipay_dict()
            else:
                params['mdiscount_amount'] = self.mdiscount_amount
        if self.notify_time:
            if hasattr(self.notify_time, 'to_alipay_dict'):
                params['notify_time'] = self.notify_time.to_alipay_dict()
            else:
                params['notify_time'] = self.notify_time
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.origin_trade_no:
            if hasattr(self.origin_trade_no, 'to_alipay_dict'):
                params['origin_trade_no'] = self.origin_trade_no.to_alipay_dict()
            else:
                params['origin_trade_no'] = self.origin_trade_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_total_amount:
            if hasattr(self.refund_total_amount, 'to_alipay_dict'):
                params['refund_total_amount'] = self.refund_total_amount.to_alipay_dict()
            else:
                params['refund_total_amount'] = self.refund_total_amount
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderExternalPaychannelSyncModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'buyer_pay_amount' in d:
            o.buyer_pay_amount = d['buyer_pay_amount']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'fund_bill_list' in d:
            o.fund_bill_list = d['fund_bill_list']
        if 'gmt_payment' in d:
            o.gmt_payment = d['gmt_payment']
        if 'mdiscount_amount' in d:
            o.mdiscount_amount = d['mdiscount_amount']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'origin_trade_no' in d:
            o.origin_trade_no = d['origin_trade_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_total_amount' in d:
            o.refund_total_amount = d['refund_total_amount']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


