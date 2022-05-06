#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsLGBDomainEvent import InsLGBDomainEvent


class AlipayInsSceneEmploymentEventSendModel(object):

    def __init__(self):
        self._channel = None
        self._domain_event = None
        self._out_biz_no = None
        self._scene_code = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def domain_event(self):
        return self._domain_event

    @domain_event.setter
    def domain_event(self, value):
        if isinstance(value, InsLGBDomainEvent):
            self._domain_event = value
        else:
            self._domain_event = InsLGBDomainEvent.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.domain_event:
            if hasattr(self.domain_event, 'to_alipay_dict'):
                params['domain_event'] = self.domain_event.to_alipay_dict()
            else:
                params['domain_event'] = self.domain_event
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEmploymentEventSendModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'domain_event' in d:
            o.domain_event = d['domain_event']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


