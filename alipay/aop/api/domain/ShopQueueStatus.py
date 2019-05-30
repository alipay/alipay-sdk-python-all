#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopQueueStatus(object):

    def __init__(self):
        self._queue_id = None
        self._queue_status = None
        self._queue_wait = None
        self._queue_wait_time = None

    @property
    def queue_id(self):
        return self._queue_id

    @queue_id.setter
    def queue_id(self, value):
        self._queue_id = value
    @property
    def queue_status(self):
        return self._queue_status

    @queue_status.setter
    def queue_status(self, value):
        self._queue_status = value
    @property
    def queue_wait(self):
        return self._queue_wait

    @queue_wait.setter
    def queue_wait(self, value):
        self._queue_wait = value
    @property
    def queue_wait_time(self):
        return self._queue_wait_time

    @queue_wait_time.setter
    def queue_wait_time(self, value):
        self._queue_wait_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.queue_id:
            if hasattr(self.queue_id, 'to_alipay_dict'):
                params['queue_id'] = self.queue_id.to_alipay_dict()
            else:
                params['queue_id'] = self.queue_id
        if self.queue_status:
            if hasattr(self.queue_status, 'to_alipay_dict'):
                params['queue_status'] = self.queue_status.to_alipay_dict()
            else:
                params['queue_status'] = self.queue_status
        if self.queue_wait:
            if hasattr(self.queue_wait, 'to_alipay_dict'):
                params['queue_wait'] = self.queue_wait.to_alipay_dict()
            else:
                params['queue_wait'] = self.queue_wait
        if self.queue_wait_time:
            if hasattr(self.queue_wait_time, 'to_alipay_dict'):
                params['queue_wait_time'] = self.queue_wait_time.to_alipay_dict()
            else:
                params['queue_wait_time'] = self.queue_wait_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopQueueStatus()
        if 'queue_id' in d:
            o.queue_id = d['queue_id']
        if 'queue_status' in d:
            o.queue_status = d['queue_status']
        if 'queue_wait' in d:
            o.queue_wait = d['queue_wait']
        if 'queue_wait_time' in d:
            o.queue_wait_time = d['queue_wait_time']
        return o


