#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayAbilityAssetInfo(object):

    def __init__(self):
        self._asset_type_code = None
        self._channel_code = None
        self._enough = None
        self._has_history_pay_success = None
        self._inst_id = None
        self._inst_name = None

    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def enough(self):
        return self._enough

    @enough.setter
    def enough(self, value):
        self._enough = value
    @property
    def has_history_pay_success(self):
        return self._has_history_pay_success

    @has_history_pay_success.setter
    def has_history_pay_success(self, value):
        self._has_history_pay_success = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.enough:
            if hasattr(self.enough, 'to_alipay_dict'):
                params['enough'] = self.enough.to_alipay_dict()
            else:
                params['enough'] = self.enough
        if self.has_history_pay_success:
            if hasattr(self.has_history_pay_success, 'to_alipay_dict'):
                params['has_history_pay_success'] = self.has_history_pay_success.to_alipay_dict()
            else:
                params['has_history_pay_success'] = self.has_history_pay_success
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayAbilityAssetInfo()
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'enough' in d:
            o.enough = d['enough']
        if 'has_history_pay_success' in d:
            o.has_history_pay_success = d['has_history_pay_success']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        return o


