#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinancePfApplySendModel(object):

    def __init__(self):
        self._biz_type = None
        self._channel = None
        self._financing_id = None
        self._parm = None
        self._platform_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def financing_id(self):
        return self._financing_id

    @financing_id.setter
    def financing_id(self, value):
        self._financing_id = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.financing_id:
            if hasattr(self.financing_id, 'to_alipay_dict'):
                params['financing_id'] = self.financing_id.to_alipay_dict()
            else:
                params['financing_id'] = self.financing_id
        if self.parm:
            if hasattr(self.parm, 'to_alipay_dict'):
                params['parm'] = self.parm.to_alipay_dict()
            else:
                params['parm'] = self.parm
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinancePfApplySendModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'financing_id' in d:
            o.financing_id = d['financing_id']
        if 'parm' in d:
            o.parm = d['parm']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        return o


