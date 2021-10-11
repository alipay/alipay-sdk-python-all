#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NotifyInfo(object):

    def __init__(self):
        self._biz_id = None
        self._biz_no = None
        self._notify_id = None
        self._send_result = None
        self._send_times = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def notify_id(self):
        return self._notify_id

    @notify_id.setter
    def notify_id(self, value):
        self._notify_id = value
    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value
    @property
    def send_times(self):
        return self._send_times

    @send_times.setter
    def send_times(self, value):
        self._send_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.notify_id:
            if hasattr(self.notify_id, 'to_alipay_dict'):
                params['notify_id'] = self.notify_id.to_alipay_dict()
            else:
                params['notify_id'] = self.notify_id
        if self.send_result:
            if hasattr(self.send_result, 'to_alipay_dict'):
                params['send_result'] = self.send_result.to_alipay_dict()
            else:
                params['send_result'] = self.send_result
        if self.send_times:
            if hasattr(self.send_times, 'to_alipay_dict'):
                params['send_times'] = self.send_times.to_alipay_dict()
            else:
                params['send_times'] = self.send_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NotifyInfo()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'notify_id' in d:
            o.notify_id = d['notify_id']
        if 'send_result' in d:
            o.send_result = d['send_result']
        if 'send_times' in d:
            o.send_times = d['send_times']
        return o


