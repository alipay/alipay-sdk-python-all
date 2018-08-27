#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserVirtualcardPageSignModel(object):

    def __init__(self):
        self._balance = None
        self._card_data = None
        self._card_no = None
        self._card_sign_mode = None
        self._card_type = None
        self._disabled = None
        self._disabled_tips = None
        self._disabled_url = None
        self._ext_info = None

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
    def card_sign_mode(self):
        return self._card_sign_mode

    @card_sign_mode.setter
    def card_sign_mode(self, value):
        self._card_sign_mode = value
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
    def disabled_tips(self):
        return self._disabled_tips

    @disabled_tips.setter
    def disabled_tips(self, value):
        self._disabled_tips = value
    @property
    def disabled_url(self):
        return self._disabled_url

    @disabled_url.setter
    def disabled_url(self, value):
        self._disabled_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.card_sign_mode:
            if hasattr(self.card_sign_mode, 'to_alipay_dict'):
                params['card_sign_mode'] = self.card_sign_mode.to_alipay_dict()
            else:
                params['card_sign_mode'] = self.card_sign_mode
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
        if self.disabled_tips:
            if hasattr(self.disabled_tips, 'to_alipay_dict'):
                params['disabled_tips'] = self.disabled_tips.to_alipay_dict()
            else:
                params['disabled_tips'] = self.disabled_tips
        if self.disabled_url:
            if hasattr(self.disabled_url, 'to_alipay_dict'):
                params['disabled_url'] = self.disabled_url.to_alipay_dict()
            else:
                params['disabled_url'] = self.disabled_url
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserVirtualcardPageSignModel()
        if 'balance' in d:
            o.balance = d['balance']
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_sign_mode' in d:
            o.card_sign_mode = d['card_sign_mode']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'disabled' in d:
            o.disabled = d['disabled']
        if 'disabled_tips' in d:
            o.disabled_tips = d['disabled_tips']
        if 'disabled_url' in d:
            o.disabled_url = d['disabled_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


