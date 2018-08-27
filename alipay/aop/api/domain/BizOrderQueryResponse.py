#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizOrderQueryResponse(object):

    def __init__(self):
        self._action = None
        self._action_mode = None
        self._apply_id = None
        self._biz_context_info = None
        self._biz_id = None
        self._biz_type = None
        self._create_time = None
        self._op_id = None
        self._request_id = None
        self._result_code = None
        self._result_desc = None
        self._status = None
        self._sub_status = None
        self._update_time = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def action_mode(self):
        return self._action_mode

    @action_mode.setter
    def action_mode(self, value):
        self._action_mode = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def biz_context_info(self):
        return self._biz_context_info

    @biz_context_info.setter
    def biz_context_info(self, value):
        self._biz_context_info = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def op_id(self):
        return self._op_id

    @op_id.setter
    def op_id(self, value):
        self._op_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.action_mode:
            if hasattr(self.action_mode, 'to_alipay_dict'):
                params['action_mode'] = self.action_mode.to_alipay_dict()
            else:
                params['action_mode'] = self.action_mode
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.biz_context_info:
            if hasattr(self.biz_context_info, 'to_alipay_dict'):
                params['biz_context_info'] = self.biz_context_info.to_alipay_dict()
            else:
                params['biz_context_info'] = self.biz_context_info
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.op_id:
            if hasattr(self.op_id, 'to_alipay_dict'):
                params['op_id'] = self.op_id.to_alipay_dict()
            else:
                params['op_id'] = self.op_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_desc:
            if hasattr(self.result_desc, 'to_alipay_dict'):
                params['result_desc'] = self.result_desc.to_alipay_dict()
            else:
                params['result_desc'] = self.result_desc
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizOrderQueryResponse()
        if 'action' in d:
            o.action = d['action']
        if 'action_mode' in d:
            o.action_mode = d['action_mode']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'biz_context_info' in d:
            o.biz_context_info = d['biz_context_info']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'op_id' in d:
            o.op_id = d['op_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_desc' in d:
            o.result_desc = d['result_desc']
        if 'status' in d:
            o.status = d['status']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


