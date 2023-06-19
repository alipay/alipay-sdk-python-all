#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JsonParamDemo import JsonParamDemo


class AlipayOpenOpenbizmockHexidemoQueryModel(object):

    def __init__(self):
        self._child_nodes = None
        self._file_param = None
        self._open_id = None
        self._other_open_id = None
        self._other_user_id = None
        self._out_biz_no = None
        self._pattern_param = None
        self._req_num = None
        self._user_id = None

    @property
    def child_nodes(self):
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, value):
        if isinstance(value, JsonParamDemo):
            self._child_nodes = value
        else:
            self._child_nodes = JsonParamDemo.from_alipay_dict(value)
    @property
    def file_param(self):
        return self._file_param

    @file_param.setter
    def file_param(self, value):
        self._file_param = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def other_open_id(self):
        return self._other_open_id

    @other_open_id.setter
    def other_open_id(self, value):
        self._other_open_id = value
    @property
    def other_user_id(self):
        return self._other_user_id

    @other_user_id.setter
    def other_user_id(self, value):
        self._other_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        if isinstance(value, list):
            self._out_biz_no = list()
            for i in value:
                self._out_biz_no.append(i)
    @property
    def pattern_param(self):
        return self._pattern_param

    @pattern_param.setter
    def pattern_param(self, value):
        self._pattern_param = value
    @property
    def req_num(self):
        return self._req_num

    @req_num.setter
    def req_num(self, value):
        self._req_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.child_nodes:
            if hasattr(self.child_nodes, 'to_alipay_dict'):
                params['child_nodes'] = self.child_nodes.to_alipay_dict()
            else:
                params['child_nodes'] = self.child_nodes
        if self.file_param:
            if hasattr(self.file_param, 'to_alipay_dict'):
                params['file_param'] = self.file_param.to_alipay_dict()
            else:
                params['file_param'] = self.file_param
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.other_open_id:
            if hasattr(self.other_open_id, 'to_alipay_dict'):
                params['other_open_id'] = self.other_open_id.to_alipay_dict()
            else:
                params['other_open_id'] = self.other_open_id
        if self.other_user_id:
            if hasattr(self.other_user_id, 'to_alipay_dict'):
                params['other_user_id'] = self.other_user_id.to_alipay_dict()
            else:
                params['other_user_id'] = self.other_user_id
        if self.out_biz_no:
            if isinstance(self.out_biz_no, list):
                for i in range(0, len(self.out_biz_no)):
                    element = self.out_biz_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_no[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pattern_param:
            if hasattr(self.pattern_param, 'to_alipay_dict'):
                params['pattern_param'] = self.pattern_param.to_alipay_dict()
            else:
                params['pattern_param'] = self.pattern_param
        if self.req_num:
            if hasattr(self.req_num, 'to_alipay_dict'):
                params['req_num'] = self.req_num.to_alipay_dict()
            else:
                params['req_num'] = self.req_num
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOpenbizmockHexidemoQueryModel()
        if 'child_nodes' in d:
            o.child_nodes = d['child_nodes']
        if 'file_param' in d:
            o.file_param = d['file_param']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'other_open_id' in d:
            o.other_open_id = d['other_open_id']
        if 'other_user_id' in d:
            o.other_user_id = d['other_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pattern_param' in d:
            o.pattern_param = d['pattern_param']
        if 'req_num' in d:
            o.req_num = d['req_num']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


