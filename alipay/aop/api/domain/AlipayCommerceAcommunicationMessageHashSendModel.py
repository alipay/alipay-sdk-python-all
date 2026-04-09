#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationMessageHashSendModel(object):

    def __init__(self):
        self._context = None
        self._inst_message_id = None
        self._open_id = None
        self._to_mobile_hash = None
        self._trigger_condition = None
        self._user_id = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def inst_message_id(self):
        return self._inst_message_id

    @inst_message_id.setter
    def inst_message_id(self, value):
        self._inst_message_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def to_mobile_hash(self):
        return self._to_mobile_hash

    @to_mobile_hash.setter
    def to_mobile_hash(self, value):
        self._to_mobile_hash = value
    @property
    def trigger_condition(self):
        return self._trigger_condition

    @trigger_condition.setter
    def trigger_condition(self, value):
        self._trigger_condition = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.inst_message_id:
            if hasattr(self.inst_message_id, 'to_alipay_dict'):
                params['inst_message_id'] = self.inst_message_id.to_alipay_dict()
            else:
                params['inst_message_id'] = self.inst_message_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.to_mobile_hash:
            if hasattr(self.to_mobile_hash, 'to_alipay_dict'):
                params['to_mobile_hash'] = self.to_mobile_hash.to_alipay_dict()
            else:
                params['to_mobile_hash'] = self.to_mobile_hash
        if self.trigger_condition:
            if hasattr(self.trigger_condition, 'to_alipay_dict'):
                params['trigger_condition'] = self.trigger_condition.to_alipay_dict()
            else:
                params['trigger_condition'] = self.trigger_condition
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
        o = AlipayCommerceAcommunicationMessageHashSendModel()
        if 'context' in d:
            o.context = d['context']
        if 'inst_message_id' in d:
            o.inst_message_id = d['inst_message_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'to_mobile_hash' in d:
            o.to_mobile_hash = d['to_mobile_hash']
        if 'trigger_condition' in d:
            o.trigger_condition = d['trigger_condition']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


