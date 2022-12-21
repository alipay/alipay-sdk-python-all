#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NodeOperateDTO(object):

    def __init__(self):
        self._ant_process_puid = None
        self._biz_app = None
        self._biz_id = None
        self._biz_type = None
        self._memo = None
        self._node_display_name = None
        self._node_duration = None
        self._node_name = None
        self._operate_detail = None
        self._operate_duration = None
        self._operate_time = None
        self._operate_type = None
        self._operator = None
        self._operator_name = None
        self._operator_work_no = None
        self._ticket_state = None
        self._title = None

    @property
    def ant_process_puid(self):
        return self._ant_process_puid

    @ant_process_puid.setter
    def ant_process_puid(self, value):
        self._ant_process_puid = value
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
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def node_display_name(self):
        return self._node_display_name

    @node_display_name.setter
    def node_display_name(self, value):
        self._node_display_name = value
    @property
    def node_duration(self):
        return self._node_duration

    @node_duration.setter
    def node_duration(self, value):
        self._node_duration = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def operate_detail(self):
        return self._operate_detail

    @operate_detail.setter
    def operate_detail(self, value):
        self._operate_detail = value
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
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
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
    def operator_work_no(self):
        return self._operator_work_no

    @operator_work_no.setter
    def operator_work_no(self, value):
        self._operator_work_no = value
    @property
    def ticket_state(self):
        return self._ticket_state

    @ticket_state.setter
    def ticket_state(self, value):
        self._ticket_state = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_process_puid:
            if hasattr(self.ant_process_puid, 'to_alipay_dict'):
                params['ant_process_puid'] = self.ant_process_puid.to_alipay_dict()
            else:
                params['ant_process_puid'] = self.ant_process_puid
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
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.node_display_name:
            if hasattr(self.node_display_name, 'to_alipay_dict'):
                params['node_display_name'] = self.node_display_name.to_alipay_dict()
            else:
                params['node_display_name'] = self.node_display_name
        if self.node_duration:
            if hasattr(self.node_duration, 'to_alipay_dict'):
                params['node_duration'] = self.node_duration.to_alipay_dict()
            else:
                params['node_duration'] = self.node_duration
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.operate_detail:
            if hasattr(self.operate_detail, 'to_alipay_dict'):
                params['operate_detail'] = self.operate_detail.to_alipay_dict()
            else:
                params['operate_detail'] = self.operate_detail
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
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
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
        if self.operator_work_no:
            if hasattr(self.operator_work_no, 'to_alipay_dict'):
                params['operator_work_no'] = self.operator_work_no.to_alipay_dict()
            else:
                params['operator_work_no'] = self.operator_work_no
        if self.ticket_state:
            if hasattr(self.ticket_state, 'to_alipay_dict'):
                params['ticket_state'] = self.ticket_state.to_alipay_dict()
            else:
                params['ticket_state'] = self.ticket_state
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NodeOperateDTO()
        if 'ant_process_puid' in d:
            o.ant_process_puid = d['ant_process_puid']
        if 'biz_app' in d:
            o.biz_app = d['biz_app']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'node_display_name' in d:
            o.node_display_name = d['node_display_name']
        if 'node_duration' in d:
            o.node_duration = d['node_duration']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'operate_detail' in d:
            o.operate_detail = d['operate_detail']
        if 'operate_duration' in d:
            o.operate_duration = d['operate_duration']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'operator_work_no' in d:
            o.operator_work_no = d['operator_work_no']
        if 'ticket_state' in d:
            o.ticket_state = d['ticket_state']
        if 'title' in d:
            o.title = d['title']
        return o


