#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditbenefitHuabeijinCancelModel(object):

    def __init__(self):
        self._activity_id = None
        self._activity_order_id = None
        self._cancel_reason = None
        self._cancel_time = None
        self._industry_value = None
        self._open_id = None
        self._operation_seq_id = None
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
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def industry_value(self):
        return self._industry_value

    @industry_value.setter
    def industry_value(self, value):
        self._industry_value = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_seq_id(self):
        return self._operation_seq_id

    @operation_seq_id.setter
    def operation_seq_id(self, value):
        self._operation_seq_id = value
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
        if self.activity_order_id:
            if hasattr(self.activity_order_id, 'to_alipay_dict'):
                params['activity_order_id'] = self.activity_order_id.to_alipay_dict()
            else:
                params['activity_order_id'] = self.activity_order_id
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.industry_value:
            if hasattr(self.industry_value, 'to_alipay_dict'):
                params['industry_value'] = self.industry_value.to_alipay_dict()
            else:
                params['industry_value'] = self.industry_value
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_seq_id:
            if hasattr(self.operation_seq_id, 'to_alipay_dict'):
                params['operation_seq_id'] = self.operation_seq_id.to_alipay_dict()
            else:
                params['operation_seq_id'] = self.operation_seq_id
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
        o = AlipayPcreditHuabeiPcreditbenefitHuabeijinCancelModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_order_id' in d:
            o.activity_order_id = d['activity_order_id']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'industry_value' in d:
            o.industry_value = d['industry_value']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_seq_id' in d:
            o.operation_seq_id = d['operation_seq_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


