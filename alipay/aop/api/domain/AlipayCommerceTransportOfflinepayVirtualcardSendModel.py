#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportOfflinepayVirtualcardSendModel(object):

    def __init__(self):
        self._action = None
        self._balance = None
        self._card_data = None
        self._card_no = None
        self._card_type = None
        self._disabled = None
        self._disabled_code = None
        self._disabled_tips = None
        self._ext_info = None
        self._last_update_time = None
        self._sub_action = None
        self._trade_scene = None
        self._user_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def card_data(self):
        return self._card_data

    @card_data.setter
    def card_data(self, value):
        self._card_data = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        self._disabled = value
    @property
    def disabled_code(self):
        return self._disabled_code

    @disabled_code.setter
    def disabled_code(self, value):
        self._disabled_code = value
    @property
    def disabled_tips(self):
        return self._disabled_tips

    @disabled_tips.setter
    def disabled_tips(self, value):
        self._disabled_tips = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def last_update_time(self):
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        self._last_update_time = value
    @property
    def sub_action(self):
        return self._sub_action

    @sub_action.setter
    def sub_action(self, value):
        self._sub_action = value
    @property
    def trade_scene(self):
        return self._trade_scene

    @trade_scene.setter
    def trade_scene(self, value):
        self._trade_scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.card_data:
            if hasattr(self.card_data, 'to_alipay_dict'):
                params['card_data'] = self.card_data.to_alipay_dict()
            else:
                params['card_data'] = self.card_data
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.disabled:
            if hasattr(self.disabled, 'to_alipay_dict'):
                params['disabled'] = self.disabled.to_alipay_dict()
            else:
                params['disabled'] = self.disabled
        if self.disabled_code:
            if hasattr(self.disabled_code, 'to_alipay_dict'):
                params['disabled_code'] = self.disabled_code.to_alipay_dict()
            else:
                params['disabled_code'] = self.disabled_code
        if self.disabled_tips:
            if hasattr(self.disabled_tips, 'to_alipay_dict'):
                params['disabled_tips'] = self.disabled_tips.to_alipay_dict()
            else:
                params['disabled_tips'] = self.disabled_tips
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.last_update_time:
            if hasattr(self.last_update_time, 'to_alipay_dict'):
                params['last_update_time'] = self.last_update_time.to_alipay_dict()
            else:
                params['last_update_time'] = self.last_update_time
        if self.sub_action:
            if hasattr(self.sub_action, 'to_alipay_dict'):
                params['sub_action'] = self.sub_action.to_alipay_dict()
            else:
                params['sub_action'] = self.sub_action
        if self.trade_scene:
            if hasattr(self.trade_scene, 'to_alipay_dict'):
                params['trade_scene'] = self.trade_scene.to_alipay_dict()
            else:
                params['trade_scene'] = self.trade_scene
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
        o = AlipayCommerceTransportOfflinepayVirtualcardSendModel()
        if 'action' in d:
            o.action = d['action']
        if 'balance' in d:
            o.balance = d['balance']
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'disabled' in d:
            o.disabled = d['disabled']
        if 'disabled_code' in d:
            o.disabled_code = d['disabled_code']
        if 'disabled_tips' in d:
            o.disabled_tips = d['disabled_tips']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'last_update_time' in d:
            o.last_update_time = d['last_update_time']
        if 'sub_action' in d:
            o.sub_action = d['sub_action']
        if 'trade_scene' in d:
            o.trade_scene = d['trade_scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


