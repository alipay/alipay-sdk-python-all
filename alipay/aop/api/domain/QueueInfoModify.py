#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueueInfoModify(object):

    def __init__(self):
        self._queue_id = None
        self._queue_no = None
        self._queue_wait = None
        self._queue_wait_time = None

    @property
    def queue_id(self):
        return self._queue_id

    @queue_id.setter
    def queue_id(self, value):
        self._queue_id = value
    @property
    def queue_no(self):
        return self._queue_no

    @queue_no.setter
    def queue_no(self, value):
        self._queue_no = value
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
        if self.queue_no:
            if hasattr(self.queue_no, 'to_alipay_dict'):
                params['queue_no'] = self.queue_no.to_alipay_dict()
            else:
                params['queue_no'] = self.queue_no
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
        o = QueueInfoModify()
        if 'queue_id' in d:
            o.queue_id = d['queue_id']
        if 'queue_no' in d:
            o.queue_no = d['queue_no']
        if 'queue_wait' in d:
            o.queue_wait = d['queue_wait']
        if 'queue_wait_time' in d:
            o.queue_wait_time = d['queue_wait_time']
        return o


