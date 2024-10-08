#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentDetail(object):

    def __init__(self):
        self._actual_amount = None
        self._actual_pay_time = None
        self._actual_royalty_price = None
        self._installment_id = None
        self._pay_channel = None
        self._period = None
        self._royalty_deliver_type = None
        self._royalty_time = None
        self._royalty_trade_no = None
        self._stage = None
        self._status = None
        self._trade_no = None
        self._type = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def actual_pay_time(self):
        return self._actual_pay_time

    @actual_pay_time.setter
    def actual_pay_time(self, value):
        self._actual_pay_time = value
    @property
    def actual_royalty_price(self):
        return self._actual_royalty_price

    @actual_royalty_price.setter
    def actual_royalty_price(self, value):
        self._actual_royalty_price = value
    @property
    def installment_id(self):
        return self._installment_id

    @installment_id.setter
    def installment_id(self, value):
        self._installment_id = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def royalty_deliver_type(self):
        return self._royalty_deliver_type

    @royalty_deliver_type.setter
    def royalty_deliver_type(self, value):
        self._royalty_deliver_type = value
    @property
    def royalty_time(self):
        return self._royalty_time

    @royalty_time.setter
    def royalty_time(self, value):
        self._royalty_time = value
    @property
    def royalty_trade_no(self):
        return self._royalty_trade_no

    @royalty_trade_no.setter
    def royalty_trade_no(self, value):
        self._royalty_trade_no = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.actual_pay_time:
            if hasattr(self.actual_pay_time, 'to_alipay_dict'):
                params['actual_pay_time'] = self.actual_pay_time.to_alipay_dict()
            else:
                params['actual_pay_time'] = self.actual_pay_time
        if self.actual_royalty_price:
            if hasattr(self.actual_royalty_price, 'to_alipay_dict'):
                params['actual_royalty_price'] = self.actual_royalty_price.to_alipay_dict()
            else:
                params['actual_royalty_price'] = self.actual_royalty_price
        if self.installment_id:
            if hasattr(self.installment_id, 'to_alipay_dict'):
                params['installment_id'] = self.installment_id.to_alipay_dict()
            else:
                params['installment_id'] = self.installment_id
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.royalty_deliver_type:
            if hasattr(self.royalty_deliver_type, 'to_alipay_dict'):
                params['royalty_deliver_type'] = self.royalty_deliver_type.to_alipay_dict()
            else:
                params['royalty_deliver_type'] = self.royalty_deliver_type
        if self.royalty_time:
            if hasattr(self.royalty_time, 'to_alipay_dict'):
                params['royalty_time'] = self.royalty_time.to_alipay_dict()
            else:
                params['royalty_time'] = self.royalty_time
        if self.royalty_trade_no:
            if hasattr(self.royalty_trade_no, 'to_alipay_dict'):
                params['royalty_trade_no'] = self.royalty_trade_no.to_alipay_dict()
            else:
                params['royalty_trade_no'] = self.royalty_trade_no
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentDetail()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'actual_pay_time' in d:
            o.actual_pay_time = d['actual_pay_time']
        if 'actual_royalty_price' in d:
            o.actual_royalty_price = d['actual_royalty_price']
        if 'installment_id' in d:
            o.installment_id = d['installment_id']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'period' in d:
            o.period = d['period']
        if 'royalty_deliver_type' in d:
            o.royalty_deliver_type = d['royalty_deliver_type']
        if 'royalty_time' in d:
            o.royalty_time = d['royalty_time']
        if 'royalty_trade_no' in d:
            o.royalty_trade_no = d['royalty_trade_no']
        if 'stage' in d:
            o.stage = d['stage']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'type' in d:
            o.type = d['type']
        return o


