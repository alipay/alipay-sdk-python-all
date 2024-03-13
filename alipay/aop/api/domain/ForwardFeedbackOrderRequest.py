#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ForwardFeedbackOrderRequest(object):

    def __init__(self):
        self._feedback_desc = None
        self._feedback_type = None
        self._out_order_id = None
        self._self_order_id = None

    @property
    def feedback_desc(self):
        return self._feedback_desc

    @feedback_desc.setter
    def feedback_desc(self, value):
        self._feedback_desc = value
    @property
    def feedback_type(self):
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, value):
        self._feedback_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def self_order_id(self):
        return self._self_order_id

    @self_order_id.setter
    def self_order_id(self, value):
        self._self_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.feedback_desc:
            if hasattr(self.feedback_desc, 'to_alipay_dict'):
                params['feedback_desc'] = self.feedback_desc.to_alipay_dict()
            else:
                params['feedback_desc'] = self.feedback_desc
        if self.feedback_type:
            if hasattr(self.feedback_type, 'to_alipay_dict'):
                params['feedback_type'] = self.feedback_type.to_alipay_dict()
            else:
                params['feedback_type'] = self.feedback_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.self_order_id:
            if hasattr(self.self_order_id, 'to_alipay_dict'):
                params['self_order_id'] = self.self_order_id.to_alipay_dict()
            else:
                params['self_order_id'] = self.self_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ForwardFeedbackOrderRequest()
        if 'feedback_desc' in d:
            o.feedback_desc = d['feedback_desc']
        if 'feedback_type' in d:
            o.feedback_type = d['feedback_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'self_order_id' in d:
            o.self_order_id = d['self_order_id']
        return o


