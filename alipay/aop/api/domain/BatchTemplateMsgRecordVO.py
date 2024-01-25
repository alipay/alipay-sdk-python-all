#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgTemplateContentVO import MsgTemplateContentVO


class BatchTemplateMsgRecordVO(object):

    def __init__(self):
        self._batch_msg_id = None
        self._crowd_code = None
        self._msg_content = None
        self._msg_send_count = None
        self._msg_send_status = None
        self._msg_send_time = None
        self._template_id = None

    @property
    def batch_msg_id(self):
        return self._batch_msg_id

    @batch_msg_id.setter
    def batch_msg_id(self, value):
        self._batch_msg_id = value
    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        if isinstance(value, MsgTemplateContentVO):
            self._msg_content = value
        else:
            self._msg_content = MsgTemplateContentVO.from_alipay_dict(value)
    @property
    def msg_send_count(self):
        return self._msg_send_count

    @msg_send_count.setter
    def msg_send_count(self, value):
        self._msg_send_count = value
    @property
    def msg_send_status(self):
        return self._msg_send_status

    @msg_send_status.setter
    def msg_send_status(self, value):
        self._msg_send_status = value
    @property
    def msg_send_time(self):
        return self._msg_send_time

    @msg_send_time.setter
    def msg_send_time(self, value):
        self._msg_send_time = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_msg_id:
            if hasattr(self.batch_msg_id, 'to_alipay_dict'):
                params['batch_msg_id'] = self.batch_msg_id.to_alipay_dict()
            else:
                params['batch_msg_id'] = self.batch_msg_id
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.msg_send_count:
            if hasattr(self.msg_send_count, 'to_alipay_dict'):
                params['msg_send_count'] = self.msg_send_count.to_alipay_dict()
            else:
                params['msg_send_count'] = self.msg_send_count
        if self.msg_send_status:
            if hasattr(self.msg_send_status, 'to_alipay_dict'):
                params['msg_send_status'] = self.msg_send_status.to_alipay_dict()
            else:
                params['msg_send_status'] = self.msg_send_status
        if self.msg_send_time:
            if hasattr(self.msg_send_time, 'to_alipay_dict'):
                params['msg_send_time'] = self.msg_send_time.to_alipay_dict()
            else:
                params['msg_send_time'] = self.msg_send_time
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchTemplateMsgRecordVO()
        if 'batch_msg_id' in d:
            o.batch_msg_id = d['batch_msg_id']
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'msg_send_count' in d:
            o.msg_send_count = d['msg_send_count']
        if 'msg_send_status' in d:
            o.msg_send_status = d['msg_send_status']
        if 'msg_send_time' in d:
            o.msg_send_time = d['msg_send_time']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


