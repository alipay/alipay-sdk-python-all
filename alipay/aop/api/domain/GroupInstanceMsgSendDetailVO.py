#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupInstanceMsgSendDetailVO(object):

    def __init__(self):
        self._group_instance_id = None
        self._group_instance_name = None
        self._group_instance_record_id = None
        self._send_time = None
        self._status = None
        self._tips = None

    @property
    def group_instance_id(self):
        return self._group_instance_id

    @group_instance_id.setter
    def group_instance_id(self, value):
        self._group_instance_id = value
    @property
    def group_instance_name(self):
        return self._group_instance_name

    @group_instance_name.setter
    def group_instance_name(self, value):
        self._group_instance_name = value
    @property
    def group_instance_record_id(self):
        return self._group_instance_record_id

    @group_instance_record_id.setter
    def group_instance_record_id(self, value):
        self._group_instance_record_id = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_instance_id:
            if hasattr(self.group_instance_id, 'to_alipay_dict'):
                params['group_instance_id'] = self.group_instance_id.to_alipay_dict()
            else:
                params['group_instance_id'] = self.group_instance_id
        if self.group_instance_name:
            if hasattr(self.group_instance_name, 'to_alipay_dict'):
                params['group_instance_name'] = self.group_instance_name.to_alipay_dict()
            else:
                params['group_instance_name'] = self.group_instance_name
        if self.group_instance_record_id:
            if hasattr(self.group_instance_record_id, 'to_alipay_dict'):
                params['group_instance_record_id'] = self.group_instance_record_id.to_alipay_dict()
            else:
                params['group_instance_record_id'] = self.group_instance_record_id
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupInstanceMsgSendDetailVO()
        if 'group_instance_id' in d:
            o.group_instance_id = d['group_instance_id']
        if 'group_instance_name' in d:
            o.group_instance_name = d['group_instance_name']
        if 'group_instance_record_id' in d:
            o.group_instance_record_id = d['group_instance_record_id']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'status' in d:
            o.status = d['status']
        if 'tips' in d:
            o.tips = d['tips']
        return o


