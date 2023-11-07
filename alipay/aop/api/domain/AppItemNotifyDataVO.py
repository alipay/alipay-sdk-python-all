#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemDataDiffVO import AppItemDataDiffVO
from alipay.aop.api.domain.AppItemDataDiffVO import AppItemDataDiffVO


class AppItemNotifyDataVO(object):

    def __init__(self):
        self._after = None
        self._before = None
        self._event_type = None
        self._source = None

    @property
    def after(self):
        return self._after

    @after.setter
    def after(self, value):
        if isinstance(value, AppItemDataDiffVO):
            self._after = value
        else:
            self._after = AppItemDataDiffVO.from_alipay_dict(value)
    @property
    def before(self):
        return self._before

    @before.setter
    def before(self, value):
        if isinstance(value, AppItemDataDiffVO):
            self._before = value
        else:
            self._before = AppItemDataDiffVO.from_alipay_dict(value)
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.after:
            if hasattr(self.after, 'to_alipay_dict'):
                params['after'] = self.after.to_alipay_dict()
            else:
                params['after'] = self.after
        if self.before:
            if hasattr(self.before, 'to_alipay_dict'):
                params['before'] = self.before.to_alipay_dict()
            else:
                params['before'] = self.before
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemNotifyDataVO()
        if 'after' in d:
            o.after = d['after']
        if 'before' in d:
            o.before = d['before']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'source' in d:
            o.source = d['source']
        return o


