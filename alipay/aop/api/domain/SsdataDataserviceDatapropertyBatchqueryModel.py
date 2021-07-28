#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceDatapropertyBatchqueryModel(object):

    def __init__(self):
        self._action = None
        self._action_param = None
        self._base = None
        self._data_channel = None
        self._visit_ac = None
        self._visit_biz_line = None
        self._visit_bu = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def action_param(self):
        return self._action_param

    @action_param.setter
    def action_param(self, value):
        self._action_param = value
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value
    @property
    def data_channel(self):
        return self._data_channel

    @data_channel.setter
    def data_channel(self, value):
        self._data_channel = value
    @property
    def visit_ac(self):
        return self._visit_ac

    @visit_ac.setter
    def visit_ac(self, value):
        self._visit_ac = value
    @property
    def visit_biz_line(self):
        return self._visit_biz_line

    @visit_biz_line.setter
    def visit_biz_line(self, value):
        self._visit_biz_line = value
    @property
    def visit_bu(self):
        return self._visit_bu

    @visit_bu.setter
    def visit_bu(self, value):
        self._visit_bu = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.action_param:
            if hasattr(self.action_param, 'to_alipay_dict'):
                params['action_param'] = self.action_param.to_alipay_dict()
            else:
                params['action_param'] = self.action_param
        if self.base:
            if hasattr(self.base, 'to_alipay_dict'):
                params['base'] = self.base.to_alipay_dict()
            else:
                params['base'] = self.base
        if self.data_channel:
            if hasattr(self.data_channel, 'to_alipay_dict'):
                params['data_channel'] = self.data_channel.to_alipay_dict()
            else:
                params['data_channel'] = self.data_channel
        if self.visit_ac:
            if hasattr(self.visit_ac, 'to_alipay_dict'):
                params['visit_ac'] = self.visit_ac.to_alipay_dict()
            else:
                params['visit_ac'] = self.visit_ac
        if self.visit_biz_line:
            if hasattr(self.visit_biz_line, 'to_alipay_dict'):
                params['visit_biz_line'] = self.visit_biz_line.to_alipay_dict()
            else:
                params['visit_biz_line'] = self.visit_biz_line
        if self.visit_bu:
            if hasattr(self.visit_bu, 'to_alipay_dict'):
                params['visit_bu'] = self.visit_bu.to_alipay_dict()
            else:
                params['visit_bu'] = self.visit_bu
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceDatapropertyBatchqueryModel()
        if 'action' in d:
            o.action = d['action']
        if 'action_param' in d:
            o.action_param = d['action_param']
        if 'base' in d:
            o.base = d['base']
        if 'data_channel' in d:
            o.data_channel = d['data_channel']
        if 'visit_ac' in d:
            o.visit_ac = d['visit_ac']
        if 'visit_biz_line' in d:
            o.visit_biz_line = d['visit_biz_line']
        if 'visit_bu' in d:
            o.visit_bu = d['visit_bu']
        return o


