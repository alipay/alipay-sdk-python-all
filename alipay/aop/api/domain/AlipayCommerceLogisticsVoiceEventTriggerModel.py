#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsVoiceEventTriggerModel(object):

    def __init__(self):
        self._msg_type = None
        self._sn_id = None

    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def sn_id(self):
        return self._sn_id

    @sn_id.setter
    def sn_id(self, value):
        self._sn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.sn_id:
            if hasattr(self.sn_id, 'to_alipay_dict'):
                params['sn_id'] = self.sn_id.to_alipay_dict()
            else:
                params['sn_id'] = self.sn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsVoiceEventTriggerModel()
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'sn_id' in d:
            o.sn_id = d['sn_id']
        return o


