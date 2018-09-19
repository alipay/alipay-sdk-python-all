#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneSellerActivityUnsignModel(object):

    def __init__(self):
        self._channel_account_id = None
        self._channel_account_type = None
        self._sp_code = None

    @property
    def channel_account_id(self):
        return self._channel_account_id

    @channel_account_id.setter
    def channel_account_id(self, value):
        self._channel_account_id = value
    @property
    def channel_account_type(self):
        return self._channel_account_type

    @channel_account_type.setter
    def channel_account_type(self, value):
        self._channel_account_type = value
    @property
    def sp_code(self):
        return self._sp_code

    @sp_code.setter
    def sp_code(self, value):
        self._sp_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_account_id:
            if hasattr(self.channel_account_id, 'to_alipay_dict'):
                params['channel_account_id'] = self.channel_account_id.to_alipay_dict()
            else:
                params['channel_account_id'] = self.channel_account_id
        if self.channel_account_type:
            if hasattr(self.channel_account_type, 'to_alipay_dict'):
                params['channel_account_type'] = self.channel_account_type.to_alipay_dict()
            else:
                params['channel_account_type'] = self.channel_account_type
        if self.sp_code:
            if hasattr(self.sp_code, 'to_alipay_dict'):
                params['sp_code'] = self.sp_code.to_alipay_dict()
            else:
                params['sp_code'] = self.sp_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneSellerActivityUnsignModel()
        if 'channel_account_id' in d:
            o.channel_account_id = d['channel_account_id']
        if 'channel_account_type' in d:
            o.channel_account_type = d['channel_account_type']
        if 'sp_code' in d:
            o.sp_code = d['sp_code']
        return o


