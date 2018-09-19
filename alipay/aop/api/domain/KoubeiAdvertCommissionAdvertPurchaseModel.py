#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionAdvertPurchaseModel(object):

    def __init__(self):
        self._channel_id = None
        self._out_unique_id = None
        self._security_code = None
        self._tag = None
        self._trigger_identifies = None
        self._trigger_identify_type = None
        self._trigger_strategy = None
        self._user_identify = None
        self._user_identify_type = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def out_unique_id(self):
        return self._out_unique_id

    @out_unique_id.setter
    def out_unique_id(self, value):
        self._out_unique_id = value
    @property
    def security_code(self):
        return self._security_code

    @security_code.setter
    def security_code(self, value):
        self._security_code = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def trigger_identifies(self):
        return self._trigger_identifies

    @trigger_identifies.setter
    def trigger_identifies(self, value):
        if isinstance(value, list):
            self._trigger_identifies = list()
            for i in value:
                self._trigger_identifies.append(i)
    @property
    def trigger_identify_type(self):
        return self._trigger_identify_type

    @trigger_identify_type.setter
    def trigger_identify_type(self, value):
        self._trigger_identify_type = value
    @property
    def trigger_strategy(self):
        return self._trigger_strategy

    @trigger_strategy.setter
    def trigger_strategy(self, value):
        self._trigger_strategy = value
    @property
    def user_identify(self):
        return self._user_identify

    @user_identify.setter
    def user_identify(self, value):
        self._user_identify = value
    @property
    def user_identify_type(self):
        return self._user_identify_type

    @user_identify_type.setter
    def user_identify_type(self, value):
        self._user_identify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.out_unique_id:
            if hasattr(self.out_unique_id, 'to_alipay_dict'):
                params['out_unique_id'] = self.out_unique_id.to_alipay_dict()
            else:
                params['out_unique_id'] = self.out_unique_id
        if self.security_code:
            if hasattr(self.security_code, 'to_alipay_dict'):
                params['security_code'] = self.security_code.to_alipay_dict()
            else:
                params['security_code'] = self.security_code
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.trigger_identifies:
            if isinstance(self.trigger_identifies, list):
                for i in range(0, len(self.trigger_identifies)):
                    element = self.trigger_identifies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trigger_identifies[i] = element.to_alipay_dict()
            if hasattr(self.trigger_identifies, 'to_alipay_dict'):
                params['trigger_identifies'] = self.trigger_identifies.to_alipay_dict()
            else:
                params['trigger_identifies'] = self.trigger_identifies
        if self.trigger_identify_type:
            if hasattr(self.trigger_identify_type, 'to_alipay_dict'):
                params['trigger_identify_type'] = self.trigger_identify_type.to_alipay_dict()
            else:
                params['trigger_identify_type'] = self.trigger_identify_type
        if self.trigger_strategy:
            if hasattr(self.trigger_strategy, 'to_alipay_dict'):
                params['trigger_strategy'] = self.trigger_strategy.to_alipay_dict()
            else:
                params['trigger_strategy'] = self.trigger_strategy
        if self.user_identify:
            if hasattr(self.user_identify, 'to_alipay_dict'):
                params['user_identify'] = self.user_identify.to_alipay_dict()
            else:
                params['user_identify'] = self.user_identify
        if self.user_identify_type:
            if hasattr(self.user_identify_type, 'to_alipay_dict'):
                params['user_identify_type'] = self.user_identify_type.to_alipay_dict()
            else:
                params['user_identify_type'] = self.user_identify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionAdvertPurchaseModel()
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'out_unique_id' in d:
            o.out_unique_id = d['out_unique_id']
        if 'security_code' in d:
            o.security_code = d['security_code']
        if 'tag' in d:
            o.tag = d['tag']
        if 'trigger_identifies' in d:
            o.trigger_identifies = d['trigger_identifies']
        if 'trigger_identify_type' in d:
            o.trigger_identify_type = d['trigger_identify_type']
        if 'trigger_strategy' in d:
            o.trigger_strategy = d['trigger_strategy']
        if 'user_identify' in d:
            o.user_identify = d['user_identify']
        if 'user_identify_type' in d:
            o.user_identify_type = d['user_identify_type']
        return o


