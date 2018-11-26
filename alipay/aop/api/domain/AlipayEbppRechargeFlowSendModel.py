#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppRechargeFlowSendModel(object):

    def __init__(self):
        self._bind_mobile = None
        self._ext_msg = None
        self._trade_code = None
        self._trade_id = None
        self._trade_time = None
        self._user_id = None

    @property
    def bind_mobile(self):
        return self._bind_mobile

    @bind_mobile.setter
    def bind_mobile(self, value):
        self._bind_mobile = value
    @property
    def ext_msg(self):
        return self._ext_msg

    @ext_msg.setter
    def ext_msg(self, value):
        self._ext_msg = value
    @property
    def trade_code(self):
        return self._trade_code

    @trade_code.setter
    def trade_code(self, value):
        self._trade_code = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_mobile:
            if hasattr(self.bind_mobile, 'to_alipay_dict'):
                params['bind_mobile'] = self.bind_mobile.to_alipay_dict()
            else:
                params['bind_mobile'] = self.bind_mobile
        if self.ext_msg:
            if hasattr(self.ext_msg, 'to_alipay_dict'):
                params['ext_msg'] = self.ext_msg.to_alipay_dict()
            else:
                params['ext_msg'] = self.ext_msg
        if self.trade_code:
            if hasattr(self.trade_code, 'to_alipay_dict'):
                params['trade_code'] = self.trade_code.to_alipay_dict()
            else:
                params['trade_code'] = self.trade_code
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
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
        o = AlipayEbppRechargeFlowSendModel()
        if 'bind_mobile' in d:
            o.bind_mobile = d['bind_mobile']
        if 'ext_msg' in d:
            o.ext_msg = d['ext_msg']
        if 'trade_code' in d:
            o.trade_code = d['trade_code']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


