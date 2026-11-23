#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppTransferTransferbillkeyModifyModel(object):

    def __init__(self):
        self._bill_key = None
        self._inst_id = None
        self._open_id = None
        self._owner_name = None
        self._second_level_keys = None
        self._third_party_address = None
        self._user_id = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def second_level_keys(self):
        return self._second_level_keys

    @second_level_keys.setter
    def second_level_keys(self, value):
        self._second_level_keys = value
    @property
    def third_party_address(self):
        return self._third_party_address

    @third_party_address.setter
    def third_party_address(self, value):
        self._third_party_address = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.second_level_keys:
            if hasattr(self.second_level_keys, 'to_alipay_dict'):
                params['second_level_keys'] = self.second_level_keys.to_alipay_dict()
            else:
                params['second_level_keys'] = self.second_level_keys
        if self.third_party_address:
            if hasattr(self.third_party_address, 'to_alipay_dict'):
                params['third_party_address'] = self.third_party_address.to_alipay_dict()
            else:
                params['third_party_address'] = self.third_party_address
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
        o = AlipayEbppEbppTransferTransferbillkeyModifyModel()
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'second_level_keys' in d:
            o.second_level_keys = d['second_level_keys']
        if 'third_party_address' in d:
            o.third_party_address = d['third_party_address']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


