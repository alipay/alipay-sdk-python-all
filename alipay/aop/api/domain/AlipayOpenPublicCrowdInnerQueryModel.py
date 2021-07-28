#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicCrowdInnerQueryModel(object):

    def __init__(self):
        self._channel = None
        self._crowd_id = None
        self._group_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicCrowdInnerQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'group_id' in d:
            o.group_id = d['group_id']
        return o


