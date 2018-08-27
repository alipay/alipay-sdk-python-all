#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PointsExchangeInfo import PointsExchangeInfo


class MemberPointsScene(object):

    def __init__(self):
        self._exchange_info = None
        self._kb_trade_no = None
        self._mall_id = None
        self._modify_time = None
        self._oper_type = None
        self._out_biz_no = None
        self._points_balance = None

    @property
    def exchange_info(self):
        return self._exchange_info

    @exchange_info.setter
    def exchange_info(self, value):
        if isinstance(value, PointsExchangeInfo):
            self._exchange_info = value
        else:
            self._exchange_info = PointsExchangeInfo.from_alipay_dict(value)
    @property
    def kb_trade_no(self):
        return self._kb_trade_no

    @kb_trade_no.setter
    def kb_trade_no(self, value):
        self._kb_trade_no = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def oper_type(self):
        return self._oper_type

    @oper_type.setter
    def oper_type(self, value):
        self._oper_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def points_balance(self):
        return self._points_balance

    @points_balance.setter
    def points_balance(self, value):
        self._points_balance = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_info:
            if hasattr(self.exchange_info, 'to_alipay_dict'):
                params['exchange_info'] = self.exchange_info.to_alipay_dict()
            else:
                params['exchange_info'] = self.exchange_info
        if self.kb_trade_no:
            if hasattr(self.kb_trade_no, 'to_alipay_dict'):
                params['kb_trade_no'] = self.kb_trade_no.to_alipay_dict()
            else:
                params['kb_trade_no'] = self.kb_trade_no
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.oper_type:
            if hasattr(self.oper_type, 'to_alipay_dict'):
                params['oper_type'] = self.oper_type.to_alipay_dict()
            else:
                params['oper_type'] = self.oper_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.points_balance:
            if hasattr(self.points_balance, 'to_alipay_dict'):
                params['points_balance'] = self.points_balance.to_alipay_dict()
            else:
                params['points_balance'] = self.points_balance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberPointsScene()
        if 'exchange_info' in d:
            o.exchange_info = d['exchange_info']
        if 'kb_trade_no' in d:
            o.kb_trade_no = d['kb_trade_no']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'oper_type' in d:
            o.oper_type = d['oper_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'points_balance' in d:
            o.points_balance = d['points_balance']
        return o


