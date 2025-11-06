#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NotifyRecord(object):

    def __init__(self):
        self._acid = None
        self._belong_data_code = None
        self._belong_data_id = None
        self._content = None
        self._customer_id = None
        self._customer_name = None
        self._receiver = None
        self._send_time = None
        self._send_type = None
        self._sender = None
        self._task_code = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def belong_data_code(self):
        return self._belong_data_code

    @belong_data_code.setter
    def belong_data_code(self, value):
        self._belong_data_code = value
    @property
    def belong_data_id(self):
        return self._belong_data_id

    @belong_data_id.setter
    def belong_data_id(self, value):
        self._belong_data_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def send_type(self):
        return self._send_type

    @send_type.setter
    def send_type(self, value):
        self._send_type = value
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.belong_data_code:
            if hasattr(self.belong_data_code, 'to_alipay_dict'):
                params['belong_data_code'] = self.belong_data_code.to_alipay_dict()
            else:
                params['belong_data_code'] = self.belong_data_code
        if self.belong_data_id:
            if hasattr(self.belong_data_id, 'to_alipay_dict'):
                params['belong_data_id'] = self.belong_data_id.to_alipay_dict()
            else:
                params['belong_data_id'] = self.belong_data_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.send_type:
            if hasattr(self.send_type, 'to_alipay_dict'):
                params['send_type'] = self.send_type.to_alipay_dict()
            else:
                params['send_type'] = self.send_type
        if self.sender:
            if hasattr(self.sender, 'to_alipay_dict'):
                params['sender'] = self.sender.to_alipay_dict()
            else:
                params['sender'] = self.sender
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NotifyRecord()
        if 'acid' in d:
            o.acid = d['acid']
        if 'belong_data_code' in d:
            o.belong_data_code = d['belong_data_code']
        if 'belong_data_id' in d:
            o.belong_data_id = d['belong_data_id']
        if 'content' in d:
            o.content = d['content']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'send_type' in d:
            o.send_type = d['send_type']
        if 'sender' in d:
            o.sender = d['sender']
        if 'task_code' in d:
            o.task_code = d['task_code']
        return o


