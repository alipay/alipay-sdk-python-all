#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Kv import Kv


class AntfortuneStockTrustMessageSendModel(object):

    def __init__(self):
        self._message_id = None
        self._message_params = None
        self._message_type = None
        self._trust_user_id = None

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def message_params(self):
        return self._message_params

    @message_params.setter
    def message_params(self, value):
        if isinstance(value, Kv):
            self._message_params = value
        else:
            self._message_params = Kv.from_alipay_dict(value)
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value
    @property
    def trust_user_id(self):
        return self._trust_user_id

    @trust_user_id.setter
    def trust_user_id(self, value):
        self._trust_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.message_params:
            if hasattr(self.message_params, 'to_alipay_dict'):
                params['message_params'] = self.message_params.to_alipay_dict()
            else:
                params['message_params'] = self.message_params
        if self.message_type:
            if hasattr(self.message_type, 'to_alipay_dict'):
                params['message_type'] = self.message_type.to_alipay_dict()
            else:
                params['message_type'] = self.message_type
        if self.trust_user_id:
            if hasattr(self.trust_user_id, 'to_alipay_dict'):
                params['trust_user_id'] = self.trust_user_id.to_alipay_dict()
            else:
                params['trust_user_id'] = self.trust_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockTrustMessageSendModel()
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'message_params' in d:
            o.message_params = d['message_params']
        if 'message_type' in d:
            o.message_type = d['message_type']
        if 'trust_user_id' in d:
            o.trust_user_id = d['trust_user_id']
        return o


