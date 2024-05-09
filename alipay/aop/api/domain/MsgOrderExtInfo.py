#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgOrderExtInfo(object):

    def __init__(self):
        self._address = None
        self._attachment_info = None
        self._end_time = None
        self._invoke_app_id = None
        self._name = None
        self._queue_number = None
        self._reason = None
        self._start_time = None
        self._take_time = None
        self._tips = None
        self._wait_number = None
        self._window = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def attachment_info(self):
        return self._attachment_info

    @attachment_info.setter
    def attachment_info(self, value):
        self._attachment_info = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def invoke_app_id(self):
        return self._invoke_app_id

    @invoke_app_id.setter
    def invoke_app_id(self, value):
        self._invoke_app_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def queue_number(self):
        return self._queue_number

    @queue_number.setter
    def queue_number(self, value):
        self._queue_number = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def take_time(self):
        return self._take_time

    @take_time.setter
    def take_time(self, value):
        self._take_time = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def wait_number(self):
        return self._wait_number

    @wait_number.setter
    def wait_number(self, value):
        self._wait_number = value
    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, value):
        self._window = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.attachment_info:
            if hasattr(self.attachment_info, 'to_alipay_dict'):
                params['attachment_info'] = self.attachment_info.to_alipay_dict()
            else:
                params['attachment_info'] = self.attachment_info
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.invoke_app_id:
            if hasattr(self.invoke_app_id, 'to_alipay_dict'):
                params['invoke_app_id'] = self.invoke_app_id.to_alipay_dict()
            else:
                params['invoke_app_id'] = self.invoke_app_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.queue_number:
            if hasattr(self.queue_number, 'to_alipay_dict'):
                params['queue_number'] = self.queue_number.to_alipay_dict()
            else:
                params['queue_number'] = self.queue_number
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.take_time:
            if hasattr(self.take_time, 'to_alipay_dict'):
                params['take_time'] = self.take_time.to_alipay_dict()
            else:
                params['take_time'] = self.take_time
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        if self.wait_number:
            if hasattr(self.wait_number, 'to_alipay_dict'):
                params['wait_number'] = self.wait_number.to_alipay_dict()
            else:
                params['wait_number'] = self.wait_number
        if self.window:
            if hasattr(self.window, 'to_alipay_dict'):
                params['window'] = self.window.to_alipay_dict()
            else:
                params['window'] = self.window
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgOrderExtInfo()
        if 'address' in d:
            o.address = d['address']
        if 'attachment_info' in d:
            o.attachment_info = d['attachment_info']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        if 'name' in d:
            o.name = d['name']
        if 'queue_number' in d:
            o.queue_number = d['queue_number']
        if 'reason' in d:
            o.reason = d['reason']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'take_time' in d:
            o.take_time = d['take_time']
        if 'tips' in d:
            o.tips = d['tips']
        if 'wait_number' in d:
            o.wait_number = d['wait_number']
        if 'window' in d:
            o.window = d['window']
        return o


