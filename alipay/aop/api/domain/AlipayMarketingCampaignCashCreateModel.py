#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignCashCreateModel(object):

    def __init__(self):
        self._coupon_name = None
        self._end_time = None
        self._merchant_link = None
        self._prize_msg = None
        self._prize_type = None
        self._send_freqency = None
        self._start_time = None
        self._total_money = None
        self._total_num = None

    @property
    def coupon_name(self):
        return self._coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self._coupon_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def merchant_link(self):
        return self._merchant_link

    @merchant_link.setter
    def merchant_link(self, value):
        self._merchant_link = value
    @property
    def prize_msg(self):
        return self._prize_msg

    @prize_msg.setter
    def prize_msg(self, value):
        self._prize_msg = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def send_freqency(self):
        return self._send_freqency

    @send_freqency.setter
    def send_freqency(self, value):
        self._send_freqency = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_money(self):
        return self._total_money

    @total_money.setter
    def total_money(self, value):
        self._total_money = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_name:
            if hasattr(self.coupon_name, 'to_alipay_dict'):
                params['coupon_name'] = self.coupon_name.to_alipay_dict()
            else:
                params['coupon_name'] = self.coupon_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.merchant_link:
            if hasattr(self.merchant_link, 'to_alipay_dict'):
                params['merchant_link'] = self.merchant_link.to_alipay_dict()
            else:
                params['merchant_link'] = self.merchant_link
        if self.prize_msg:
            if hasattr(self.prize_msg, 'to_alipay_dict'):
                params['prize_msg'] = self.prize_msg.to_alipay_dict()
            else:
                params['prize_msg'] = self.prize_msg
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.send_freqency:
            if hasattr(self.send_freqency, 'to_alipay_dict'):
                params['send_freqency'] = self.send_freqency.to_alipay_dict()
            else:
                params['send_freqency'] = self.send_freqency
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.total_money:
            if hasattr(self.total_money, 'to_alipay_dict'):
                params['total_money'] = self.total_money.to_alipay_dict()
            else:
                params['total_money'] = self.total_money
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignCashCreateModel()
        if 'coupon_name' in d:
            o.coupon_name = d['coupon_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'merchant_link' in d:
            o.merchant_link = d['merchant_link']
        if 'prize_msg' in d:
            o.prize_msg = d['prize_msg']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'send_freqency' in d:
            o.send_freqency = d['send_freqency']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_money' in d:
            o.total_money = d['total_money']
        if 'total_num' in d:
            o.total_num = d['total_num']
        return o


