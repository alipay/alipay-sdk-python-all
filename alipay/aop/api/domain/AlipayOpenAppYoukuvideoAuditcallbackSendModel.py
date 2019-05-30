#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppYoukuvideoAuditcallbackSendModel(object):

    def __init__(self):
        self._action = None
        self._old_action = None
        self._source = None
        self._vid = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def old_action(self):
        return self._old_action

    @old_action.setter
    def old_action(self, value):
        self._old_action = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.old_action:
            if hasattr(self.old_action, 'to_alipay_dict'):
                params['old_action'] = self.old_action.to_alipay_dict()
            else:
                params['old_action'] = self.old_action
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.vid:
            if hasattr(self.vid, 'to_alipay_dict'):
                params['vid'] = self.vid.to_alipay_dict()
            else:
                params['vid'] = self.vid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppYoukuvideoAuditcallbackSendModel()
        if 'action' in d:
            o.action = d['action']
        if 'old_action' in d:
            o.old_action = d['old_action']
        if 'source' in d:
            o.source = d['source']
        if 'vid' in d:
            o.vid = d['vid']
        return o


