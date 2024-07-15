#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsTradeEventSyncModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._expressman_open_id = None
        self._expressman_user_id = None
        self._logistics_code = None
        self._pay_open_id = None
        self._pay_user_id = None
        self._waybill_no = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def expressman_open_id(self):
        return self._expressman_open_id

    @expressman_open_id.setter
    def expressman_open_id(self, value):
        self._expressman_open_id = value
    @property
    def expressman_user_id(self):
        return self._expressman_user_id

    @expressman_user_id.setter
    def expressman_user_id(self, value):
        self._expressman_user_id = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def pay_open_id(self):
        return self._pay_open_id

    @pay_open_id.setter
    def pay_open_id(self, value):
        self._pay_open_id = value
    @property
    def pay_user_id(self):
        return self._pay_user_id

    @pay_user_id.setter
    def pay_user_id(self, value):
        self._pay_user_id = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.expressman_open_id:
            if hasattr(self.expressman_open_id, 'to_alipay_dict'):
                params['expressman_open_id'] = self.expressman_open_id.to_alipay_dict()
            else:
                params['expressman_open_id'] = self.expressman_open_id
        if self.expressman_user_id:
            if hasattr(self.expressman_user_id, 'to_alipay_dict'):
                params['expressman_user_id'] = self.expressman_user_id.to_alipay_dict()
            else:
                params['expressman_user_id'] = self.expressman_user_id
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.pay_open_id:
            if hasattr(self.pay_open_id, 'to_alipay_dict'):
                params['pay_open_id'] = self.pay_open_id.to_alipay_dict()
            else:
                params['pay_open_id'] = self.pay_open_id
        if self.pay_user_id:
            if hasattr(self.pay_user_id, 'to_alipay_dict'):
                params['pay_user_id'] = self.pay_user_id.to_alipay_dict()
            else:
                params['pay_user_id'] = self.pay_user_id
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsTradeEventSyncModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'expressman_open_id' in d:
            o.expressman_open_id = d['expressman_open_id']
        if 'expressman_user_id' in d:
            o.expressman_user_id = d['expressman_user_id']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'pay_open_id' in d:
            o.pay_open_id = d['pay_open_id']
        if 'pay_user_id' in d:
            o.pay_user_id = d['pay_user_id']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


