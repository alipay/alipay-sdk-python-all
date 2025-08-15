#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RealtimeQcDialog import RealtimeQcDialog


class RealtimeTextQc(object):

    def __init__(self):
        self._current_time = None
        self._dialog_id = None
        self._realtime_qc_dialog = None
        self._role = None
        self._service_source = None
        self._start_time = None
        self._text = None

    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
    @property
    def dialog_id(self):
        return self._dialog_id

    @dialog_id.setter
    def dialog_id(self, value):
        self._dialog_id = value
    @property
    def realtime_qc_dialog(self):
        return self._realtime_qc_dialog

    @realtime_qc_dialog.setter
    def realtime_qc_dialog(self, value):
        if isinstance(value, RealtimeQcDialog):
            self._realtime_qc_dialog = value
        else:
            self._realtime_qc_dialog = RealtimeQcDialog.from_alipay_dict(value)
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def service_source(self):
        return self._service_source

    @service_source.setter
    def service_source(self, value):
        self._service_source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_time:
            if hasattr(self.current_time, 'to_alipay_dict'):
                params['current_time'] = self.current_time.to_alipay_dict()
            else:
                params['current_time'] = self.current_time
        if self.dialog_id:
            if hasattr(self.dialog_id, 'to_alipay_dict'):
                params['dialog_id'] = self.dialog_id.to_alipay_dict()
            else:
                params['dialog_id'] = self.dialog_id
        if self.realtime_qc_dialog:
            if hasattr(self.realtime_qc_dialog, 'to_alipay_dict'):
                params['realtime_qc_dialog'] = self.realtime_qc_dialog.to_alipay_dict()
            else:
                params['realtime_qc_dialog'] = self.realtime_qc_dialog
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.service_source:
            if hasattr(self.service_source, 'to_alipay_dict'):
                params['service_source'] = self.service_source.to_alipay_dict()
            else:
                params['service_source'] = self.service_source
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = RealtimeTextQc()
        if 'current_time' in d:
            o.current_time = d['current_time']
        if 'dialog_id' in d:
            o.dialog_id = d['dialog_id']
        if 'realtime_qc_dialog' in d:
            o.realtime_qc_dialog = d['realtime_qc_dialog']
        if 'role' in d:
            o.role = d['role']
        if 'service_source' in d:
            o.service_source = d['service_source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'text' in d:
            o.text = d['text']
        return o


