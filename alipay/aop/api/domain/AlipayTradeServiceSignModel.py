#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeServiceSignModel(object):

    def __init__(self):
        self._access_channel = None
        self._alipay_user_id = None
        self._biz_type = None
        self._external_logon_id = None
        self._external_user_id = None
        self._sub_biz_type = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.external_logon_id:
            if hasattr(self.external_logon_id, 'to_alipay_dict'):
                params['external_logon_id'] = self.external_logon_id.to_alipay_dict()
            else:
                params['external_logon_id'] = self.external_logon_id
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeServiceSignModel()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


