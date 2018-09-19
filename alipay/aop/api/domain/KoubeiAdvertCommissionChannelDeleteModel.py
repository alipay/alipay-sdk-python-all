#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionChannelDeleteModel(object):

    def __init__(self):
        self._channel_ids = None

    @property
    def channel_ids(self):
        return self._channel_ids

    @channel_ids.setter
    def channel_ids(self, value):
        if isinstance(value, list):
            self._channel_ids = list()
            for i in value:
                self._channel_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.channel_ids:
            if isinstance(self.channel_ids, list):
                for i in range(0, len(self.channel_ids)):
                    element = self.channel_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_ids[i] = element.to_alipay_dict()
            if hasattr(self.channel_ids, 'to_alipay_dict'):
                params['channel_ids'] = self.channel_ids.to_alipay_dict()
            else:
                params['channel_ids'] = self.channel_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionChannelDeleteModel()
        if 'channel_ids' in d:
            o.channel_ids = d['channel_ids']
        return o


