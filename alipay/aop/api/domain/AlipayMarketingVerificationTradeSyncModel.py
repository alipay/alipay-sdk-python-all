#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVerificationTradeSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._alipay_refund_no = None
        self._alipay_trade_no = None
        self._biz_info = None
        self._operation_time = None
        self._out_trade_no = None
        self._scene_code = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def alipay_refund_no(self):
        return self._alipay_refund_no

    @alipay_refund_no.setter
    def alipay_refund_no(self, value):
        self._alipay_refund_no = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.alipay_refund_no:
            if hasattr(self.alipay_refund_no, 'to_alipay_dict'):
                params['alipay_refund_no'] = self.alipay_refund_no.to_alipay_dict()
            else:
                params['alipay_refund_no'] = self.alipay_refund_no
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVerificationTradeSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'alipay_refund_no' in d:
            o.alipay_refund_no = d['alipay_refund_no']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


