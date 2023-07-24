#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelDetailParams(object):

    def __init__(self):
        self._card_group_name = None

    @property
    def card_group_name(self):
        return self._card_group_name

    @card_group_name.setter
    def card_group_name(self, value):
        self._card_group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_group_name:
            if hasattr(self.card_group_name, 'to_alipay_dict'):
                params['card_group_name'] = self.card_group_name.to_alipay_dict()
            else:
                params['card_group_name'] = self.card_group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelDetailParams()
        if 'card_group_name' in d:
            o.card_group_name = d['card_group_name']
        return o


