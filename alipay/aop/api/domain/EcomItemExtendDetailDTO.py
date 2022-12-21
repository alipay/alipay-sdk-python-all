#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcomItemExtendDetailDTO(object):

    def __init__(self):
        self._card_type = None
        self._card_use_amount = None
        self._card_use_count = None
        self._card_use_period = None
        self._ext_info = None
        self._game_account = None
        self._game_account_client = None
        self._game_account_client_id = None
        self._game_id = None
        self._game_name = None
        self._lockable_device = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def card_use_amount(self):
        return self._card_use_amount

    @card_use_amount.setter
    def card_use_amount(self, value):
        self._card_use_amount = value
    @property
    def card_use_count(self):
        return self._card_use_count

    @card_use_count.setter
    def card_use_count(self, value):
        self._card_use_count = value
    @property
    def card_use_period(self):
        return self._card_use_period

    @card_use_period.setter
    def card_use_period(self, value):
        self._card_use_period = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def game_account(self):
        return self._game_account

    @game_account.setter
    def game_account(self, value):
        self._game_account = value
    @property
    def game_account_client(self):
        return self._game_account_client

    @game_account_client.setter
    def game_account_client(self, value):
        self._game_account_client = value
    @property
    def game_account_client_id(self):
        return self._game_account_client_id

    @game_account_client_id.setter
    def game_account_client_id(self, value):
        self._game_account_client_id = value
    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value
    @property
    def game_name(self):
        return self._game_name

    @game_name.setter
    def game_name(self, value):
        self._game_name = value
    @property
    def lockable_device(self):
        return self._lockable_device

    @lockable_device.setter
    def lockable_device(self, value):
        self._lockable_device = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.card_use_amount:
            if hasattr(self.card_use_amount, 'to_alipay_dict'):
                params['card_use_amount'] = self.card_use_amount.to_alipay_dict()
            else:
                params['card_use_amount'] = self.card_use_amount
        if self.card_use_count:
            if hasattr(self.card_use_count, 'to_alipay_dict'):
                params['card_use_count'] = self.card_use_count.to_alipay_dict()
            else:
                params['card_use_count'] = self.card_use_count
        if self.card_use_period:
            if hasattr(self.card_use_period, 'to_alipay_dict'):
                params['card_use_period'] = self.card_use_period.to_alipay_dict()
            else:
                params['card_use_period'] = self.card_use_period
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.game_account:
            if hasattr(self.game_account, 'to_alipay_dict'):
                params['game_account'] = self.game_account.to_alipay_dict()
            else:
                params['game_account'] = self.game_account
        if self.game_account_client:
            if hasattr(self.game_account_client, 'to_alipay_dict'):
                params['game_account_client'] = self.game_account_client.to_alipay_dict()
            else:
                params['game_account_client'] = self.game_account_client
        if self.game_account_client_id:
            if hasattr(self.game_account_client_id, 'to_alipay_dict'):
                params['game_account_client_id'] = self.game_account_client_id.to_alipay_dict()
            else:
                params['game_account_client_id'] = self.game_account_client_id
        if self.game_id:
            if hasattr(self.game_id, 'to_alipay_dict'):
                params['game_id'] = self.game_id.to_alipay_dict()
            else:
                params['game_id'] = self.game_id
        if self.game_name:
            if hasattr(self.game_name, 'to_alipay_dict'):
                params['game_name'] = self.game_name.to_alipay_dict()
            else:
                params['game_name'] = self.game_name
        if self.lockable_device:
            if hasattr(self.lockable_device, 'to_alipay_dict'):
                params['lockable_device'] = self.lockable_device.to_alipay_dict()
            else:
                params['lockable_device'] = self.lockable_device
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomItemExtendDetailDTO()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'card_use_amount' in d:
            o.card_use_amount = d['card_use_amount']
        if 'card_use_count' in d:
            o.card_use_count = d['card_use_count']
        if 'card_use_period' in d:
            o.card_use_period = d['card_use_period']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'game_account' in d:
            o.game_account = d['game_account']
        if 'game_account_client' in d:
            o.game_account_client = d['game_account_client']
        if 'game_account_client_id' in d:
            o.game_account_client_id = d['game_account_client_id']
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'game_name' in d:
            o.game_name = d['game_name']
        if 'lockable_device' in d:
            o.lockable_device = d['lockable_device']
        return o


