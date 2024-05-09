#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmSubscribe(object):

    def __init__(self):
        self._group_id = None
        self._id = None
        self._subscribe_types = None
        self._subscriber = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def subscribe_types(self):
        return self._subscribe_types

    @subscribe_types.setter
    def subscribe_types(self, value):
        if isinstance(value, list):
            self._subscribe_types = list()
            for i in value:
                self._subscribe_types.append(i)
    @property
    def subscriber(self):
        return self._subscriber

    @subscriber.setter
    def subscriber(self, value):
        self._subscriber = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.subscribe_types:
            if isinstance(self.subscribe_types, list):
                for i in range(0, len(self.subscribe_types)):
                    element = self.subscribe_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subscribe_types[i] = element.to_alipay_dict()
            if hasattr(self.subscribe_types, 'to_alipay_dict'):
                params['subscribe_types'] = self.subscribe_types.to_alipay_dict()
            else:
                params['subscribe_types'] = self.subscribe_types
        if self.subscriber:
            if hasattr(self.subscriber, 'to_alipay_dict'):
                params['subscriber'] = self.subscriber.to_alipay_dict()
            else:
                params['subscriber'] = self.subscriber
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmSubscribe()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'id' in d:
            o.id = d['id']
        if 'subscribe_types' in d:
            o.subscribe_types = d['subscribe_types']
        if 'subscriber' in d:
            o.subscriber = d['subscriber']
        return o


