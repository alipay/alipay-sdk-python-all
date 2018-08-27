#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BPOpenApiTask(object):

    def __init__(self):
        self._deal_url = None
        self._detail_url = None
        self._display_name = None
        self._gmt_operate = None
        self._memo = None
        self._name = None
        self._operate = None
        self._operate_transition = None
        self._operator = None
        self._operator_name = None
        self._sign_type = None
        self._state = None
        self._type = None

    @property
    def deal_url(self):
        return self._deal_url

    @deal_url.setter
    def deal_url(self, value):
        self._deal_url = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def gmt_operate(self):
        return self._gmt_operate

    @gmt_operate.setter
    def gmt_operate(self, value):
        self._gmt_operate = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def operate_transition(self):
        return self._operate_transition

    @operate_transition.setter
    def operate_transition(self, value):
        self._operate_transition = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def sign_type(self):
        return self._sign_type

    @sign_type.setter
    def sign_type(self, value):
        self._sign_type = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.deal_url:
            if hasattr(self.deal_url, 'to_alipay_dict'):
                params['deal_url'] = self.deal_url.to_alipay_dict()
            else:
                params['deal_url'] = self.deal_url
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.gmt_operate:
            if hasattr(self.gmt_operate, 'to_alipay_dict'):
                params['gmt_operate'] = self.gmt_operate.to_alipay_dict()
            else:
                params['gmt_operate'] = self.gmt_operate
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.operate_transition:
            if hasattr(self.operate_transition, 'to_alipay_dict'):
                params['operate_transition'] = self.operate_transition.to_alipay_dict()
            else:
                params['operate_transition'] = self.operate_transition
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.sign_type:
            if hasattr(self.sign_type, 'to_alipay_dict'):
                params['sign_type'] = self.sign_type.to_alipay_dict()
            else:
                params['sign_type'] = self.sign_type
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiTask()
        if 'deal_url' in d:
            o.deal_url = d['deal_url']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'gmt_operate' in d:
            o.gmt_operate = d['gmt_operate']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'operate' in d:
            o.operate = d['operate']
        if 'operate_transition' in d:
            o.operate_transition = d['operate_transition']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'sign_type' in d:
            o.sign_type = d['sign_type']
        if 'state' in d:
            o.state = d['state']
        if 'type' in d:
            o.type = d['type']
        return o


