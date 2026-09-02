#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditbenefitHuabeijinSendModel(object):

    def __init__(self):
        self._activity_id = None
        self._actual_amount = None
        self._industry_value = None
        self._memo = None
        self._open_id = None
        self._order_desc = None
        self._order_time = None
        self._out_biz_no = None
        self._trade_no = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def industry_value(self):
        return self._industry_value

    @industry_value.setter
    def industry_value(self, value):
        self._industry_value = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_desc(self):
        return self._order_desc

    @order_desc.setter
    def order_desc(self, value):
        self._order_desc = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.industry_value:
            if hasattr(self.industry_value, 'to_alipay_dict'):
                params['industry_value'] = self.industry_value.to_alipay_dict()
            else:
                params['industry_value'] = self.industry_value
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_desc:
            if hasattr(self.order_desc, 'to_alipay_dict'):
                params['order_desc'] = self.order_desc.to_alipay_dict()
            else:
                params['order_desc'] = self.order_desc
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditbenefitHuabeijinSendModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'industry_value' in d:
            o.industry_value = d['industry_value']
        if 'memo' in d:
            o.memo = d['memo']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_desc' in d:
            o.order_desc = d['order_desc']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


