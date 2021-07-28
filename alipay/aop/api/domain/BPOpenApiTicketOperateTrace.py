#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BPOpenApiTicketOperateTrace(object):

    def __init__(self):
        self._action = None
        self._biz_app = None
        self._biz_id = None
        self._display_name = None
        self._memo = None
        self._name = None
        self._next_display_name = None
        self._next_name = None
        self._node_duration = None
        self._operate = None
        self._operate_duration = None
        self._operate_time = None
        self._operator = None
        self._operator_name = None
        self._origin_operator = None
        self._origin_operator_name = None
        self._ticket_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def biz_app(self):
        return self._biz_app

    @biz_app.setter
    def biz_app(self, value):
        self._biz_app = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
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
    def next_display_name(self):
        return self._next_display_name

    @next_display_name.setter
    def next_display_name(self, value):
        self._next_display_name = value
    @property
    def next_name(self):
        return self._next_name

    @next_name.setter
    def next_name(self, value):
        self._next_name = value
    @property
    def node_duration(self):
        return self._node_duration

    @node_duration.setter
    def node_duration(self, value):
        self._node_duration = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def operate_duration(self):
        return self._operate_duration

    @operate_duration.setter
    def operate_duration(self, value):
        self._operate_duration = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
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
    def origin_operator(self):
        return self._origin_operator

    @origin_operator.setter
    def origin_operator(self, value):
        self._origin_operator = value
    @property
    def origin_operator_name(self):
        return self._origin_operator_name

    @origin_operator_name.setter
    def origin_operator_name(self, value):
        self._origin_operator_name = value
    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.biz_app:
            if hasattr(self.biz_app, 'to_alipay_dict'):
                params['biz_app'] = self.biz_app.to_alipay_dict()
            else:
                params['biz_app'] = self.biz_app
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
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
        if self.next_display_name:
            if hasattr(self.next_display_name, 'to_alipay_dict'):
                params['next_display_name'] = self.next_display_name.to_alipay_dict()
            else:
                params['next_display_name'] = self.next_display_name
        if self.next_name:
            if hasattr(self.next_name, 'to_alipay_dict'):
                params['next_name'] = self.next_name.to_alipay_dict()
            else:
                params['next_name'] = self.next_name
        if self.node_duration:
            if hasattr(self.node_duration, 'to_alipay_dict'):
                params['node_duration'] = self.node_duration.to_alipay_dict()
            else:
                params['node_duration'] = self.node_duration
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.operate_duration:
            if hasattr(self.operate_duration, 'to_alipay_dict'):
                params['operate_duration'] = self.operate_duration.to_alipay_dict()
            else:
                params['operate_duration'] = self.operate_duration
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
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
        if self.origin_operator:
            if hasattr(self.origin_operator, 'to_alipay_dict'):
                params['origin_operator'] = self.origin_operator.to_alipay_dict()
            else:
                params['origin_operator'] = self.origin_operator
        if self.origin_operator_name:
            if hasattr(self.origin_operator_name, 'to_alipay_dict'):
                params['origin_operator_name'] = self.origin_operator_name.to_alipay_dict()
            else:
                params['origin_operator_name'] = self.origin_operator_name
        if self.ticket_id:
            if hasattr(self.ticket_id, 'to_alipay_dict'):
                params['ticket_id'] = self.ticket_id.to_alipay_dict()
            else:
                params['ticket_id'] = self.ticket_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiTicketOperateTrace()
        if 'action' in d:
            o.action = d['action']
        if 'biz_app' in d:
            o.biz_app = d['biz_app']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'next_display_name' in d:
            o.next_display_name = d['next_display_name']
        if 'next_name' in d:
            o.next_name = d['next_name']
        if 'node_duration' in d:
            o.node_duration = d['node_duration']
        if 'operate' in d:
            o.operate = d['operate']
        if 'operate_duration' in d:
            o.operate_duration = d['operate_duration']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'origin_operator' in d:
            o.origin_operator = d['origin_operator']
        if 'origin_operator_name' in d:
            o.origin_operator_name = d['origin_operator_name']
        if 'ticket_id' in d:
            o.ticket_id = d['ticket_id']
        return o


