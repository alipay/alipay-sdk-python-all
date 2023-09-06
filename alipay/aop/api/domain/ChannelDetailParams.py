#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelDetailParams(object):

    def __init__(self):
        self._card_group_name = None
        self._marketing_flag = None
        self._refuse_code = None

    @property
    def card_group_name(self):
        return self._card_group_name

    @card_group_name.setter
    def card_group_name(self, value):
        self._card_group_name = value
    @property
    def marketing_flag(self):
        return self._marketing_flag

    @marketing_flag.setter
    def marketing_flag(self, value):
        self._marketing_flag = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_group_name:
            if hasattr(self.card_group_name, 'to_alipay_dict'):
                params['card_group_name'] = self.card_group_name.to_alipay_dict()
            else:
                params['card_group_name'] = self.card_group_name
        if self.marketing_flag:
            if hasattr(self.marketing_flag, 'to_alipay_dict'):
                params['marketing_flag'] = self.marketing_flag.to_alipay_dict()
            else:
                params['marketing_flag'] = self.marketing_flag
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelDetailParams()
        if 'card_group_name' in d:
            o.card_group_name = d['card_group_name']
        if 'marketing_flag' in d:
            o.marketing_flag = d['marketing_flag']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        return o


