#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AsrTtsSlsMessage(object):

    def __init__(self):
        self._acid = None
        self._call_session_start_time = None
        self._contact_id = None
        self._content = None
        self._device_session_start_time = None
        self._device_type = None
        self._end_time = None
        self._interrupted = None
        self._seq = None
        self._start_time = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def call_session_start_time(self):
        return self._call_session_start_time

    @call_session_start_time.setter
    def call_session_start_time(self, value):
        self._call_session_start_time = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def device_session_start_time(self):
        return self._device_session_start_time

    @device_session_start_time.setter
    def device_session_start_time(self, value):
        self._device_session_start_time = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def interrupted(self):
        return self._interrupted

    @interrupted.setter
    def interrupted(self, value):
        self._interrupted = value
    @property
    def seq(self):
        return self._seq

    @seq.setter
    def seq(self, value):
        self._seq = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.call_session_start_time:
            if hasattr(self.call_session_start_time, 'to_alipay_dict'):
                params['call_session_start_time'] = self.call_session_start_time.to_alipay_dict()
            else:
                params['call_session_start_time'] = self.call_session_start_time
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.device_session_start_time:
            if hasattr(self.device_session_start_time, 'to_alipay_dict'):
                params['device_session_start_time'] = self.device_session_start_time.to_alipay_dict()
            else:
                params['device_session_start_time'] = self.device_session_start_time
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.interrupted:
            if hasattr(self.interrupted, 'to_alipay_dict'):
                params['interrupted'] = self.interrupted.to_alipay_dict()
            else:
                params['interrupted'] = self.interrupted
        if self.seq:
            if hasattr(self.seq, 'to_alipay_dict'):
                params['seq'] = self.seq.to_alipay_dict()
            else:
                params['seq'] = self.seq
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AsrTtsSlsMessage()
        if 'acid' in d:
            o.acid = d['acid']
        if 'call_session_start_time' in d:
            o.call_session_start_time = d['call_session_start_time']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'content' in d:
            o.content = d['content']
        if 'device_session_start_time' in d:
            o.device_session_start_time = d['device_session_start_time']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'interrupted' in d:
            o.interrupted = d['interrupted']
        if 'seq' in d:
            o.seq = d['seq']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


