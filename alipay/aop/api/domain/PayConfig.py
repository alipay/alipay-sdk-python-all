#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayConfig(object):

    def __init__(self):
        self._bank_channel_mode = None
        self._card_holder_name = None
        self._card_no = None
        self._open_asset_role = None
        self._use_bank_channel = None

    @property
    def bank_channel_mode(self):
        return self._bank_channel_mode

    @bank_channel_mode.setter
    def bank_channel_mode(self, value):
        self._bank_channel_mode = value
    @property
    def card_holder_name(self):
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value):
        self._card_holder_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def open_asset_role(self):
        return self._open_asset_role

    @open_asset_role.setter
    def open_asset_role(self, value):
        self._open_asset_role = value
    @property
    def use_bank_channel(self):
        return self._use_bank_channel

    @use_bank_channel.setter
    def use_bank_channel(self, value):
        self._use_bank_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_channel_mode:
            if hasattr(self.bank_channel_mode, 'to_alipay_dict'):
                params['bank_channel_mode'] = self.bank_channel_mode.to_alipay_dict()
            else:
                params['bank_channel_mode'] = self.bank_channel_mode
        if self.card_holder_name:
            if hasattr(self.card_holder_name, 'to_alipay_dict'):
                params['card_holder_name'] = self.card_holder_name.to_alipay_dict()
            else:
                params['card_holder_name'] = self.card_holder_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.open_asset_role:
            if hasattr(self.open_asset_role, 'to_alipay_dict'):
                params['open_asset_role'] = self.open_asset_role.to_alipay_dict()
            else:
                params['open_asset_role'] = self.open_asset_role
        if self.use_bank_channel:
            if hasattr(self.use_bank_channel, 'to_alipay_dict'):
                params['use_bank_channel'] = self.use_bank_channel.to_alipay_dict()
            else:
                params['use_bank_channel'] = self.use_bank_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayConfig()
        if 'bank_channel_mode' in d:
            o.bank_channel_mode = d['bank_channel_mode']
        if 'card_holder_name' in d:
            o.card_holder_name = d['card_holder_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'open_asset_role' in d:
            o.open_asset_role = d['open_asset_role']
        if 'use_bank_channel' in d:
            o.use_bank_channel = d['use_bank_channel']
        return o


