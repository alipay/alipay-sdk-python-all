#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BcClusterMsgRecord(object):

    def __init__(self):
        self._biz_id = None
        self._msg_name = None
        self._send_cluster_ids = None
        self._send_time = None
        self._status = None
        self._template_code = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def msg_name(self):
        return self._msg_name

    @msg_name.setter
    def msg_name(self, value):
        self._msg_name = value
    @property
    def send_cluster_ids(self):
        return self._send_cluster_ids

    @send_cluster_ids.setter
    def send_cluster_ids(self, value):
        if isinstance(value, list):
            self._send_cluster_ids = list()
            for i in value:
                self._send_cluster_ids.append(i)
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
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.msg_name:
            if hasattr(self.msg_name, 'to_alipay_dict'):
                params['msg_name'] = self.msg_name.to_alipay_dict()
            else:
                params['msg_name'] = self.msg_name
        if self.send_cluster_ids:
            if isinstance(self.send_cluster_ids, list):
                for i in range(0, len(self.send_cluster_ids)):
                    element = self.send_cluster_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.send_cluster_ids[i] = element.to_alipay_dict()
            if hasattr(self.send_cluster_ids, 'to_alipay_dict'):
                params['send_cluster_ids'] = self.send_cluster_ids.to_alipay_dict()
            else:
                params['send_cluster_ids'] = self.send_cluster_ids
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
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BcClusterMsgRecord()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'msg_name' in d:
            o.msg_name = d['msg_name']
        if 'send_cluster_ids' in d:
            o.send_cluster_ids = d['send_cluster_ids']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'status' in d:
            o.status = d['status']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


