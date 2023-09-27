#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractOrderSendLogDTO(object):

    def __init__(self):
        self._files = None
        self._log_id = None
        self._remark = None
        self._send_time = None
        self._sender = None
        self._status = None

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value
    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.files:
            if hasattr(self.files, 'to_alipay_dict'):
                params['files'] = self.files.to_alipay_dict()
            else:
                params['files'] = self.files
        if self.log_id:
            if hasattr(self.log_id, 'to_alipay_dict'):
                params['log_id'] = self.log_id.to_alipay_dict()
            else:
                params['log_id'] = self.log_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.sender:
            if hasattr(self.sender, 'to_alipay_dict'):
                params['sender'] = self.sender.to_alipay_dict()
            else:
                params['sender'] = self.sender
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractOrderSendLogDTO()
        if 'files' in d:
            o.files = d['files']
        if 'log_id' in d:
            o.log_id = d['log_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'sender' in d:
            o.sender = d['sender']
        if 'status' in d:
            o.status = d['status']
        return o


