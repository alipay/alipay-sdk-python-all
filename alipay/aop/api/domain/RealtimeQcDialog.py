#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RealtimeQcDialog(object):

    def __init__(self):
        self._begin_time = None
        self._dialog_id = None
        self._owner_type = None
        self._text = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def dialog_id(self):
        return self._dialog_id

    @dialog_id.setter
    def dialog_id(self, value):
        self._dialog_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.dialog_id:
            if hasattr(self.dialog_id, 'to_alipay_dict'):
                params['dialog_id'] = self.dialog_id.to_alipay_dict()
            else:
                params['dialog_id'] = self.dialog_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RealtimeQcDialog()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'dialog_id' in d:
            o.dialog_id = d['dialog_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'text' in d:
            o.text = d['text']
        return o


