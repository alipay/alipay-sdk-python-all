#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WidgetDataAuditRejectResult(object):

    def __init__(self):
        self._audit_memo = None
        self._audit_result = None
        self._data_id = None
        self._mini_app_id = None
        self._reject_field_list = None
        self._widget_id = None

    @property
    def audit_memo(self):
        return self._audit_memo

    @audit_memo.setter
    def audit_memo(self, value):
        self._audit_memo = value
    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def reject_field_list(self):
        return self._reject_field_list

    @reject_field_list.setter
    def reject_field_list(self, value):
        if isinstance(value, list):
            self._reject_field_list = list()
            for i in value:
                self._reject_field_list.append(i)
    @property
    def widget_id(self):
        return self._widget_id

    @widget_id.setter
    def widget_id(self, value):
        self._widget_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_memo:
            if hasattr(self.audit_memo, 'to_alipay_dict'):
                params['audit_memo'] = self.audit_memo.to_alipay_dict()
            else:
                params['audit_memo'] = self.audit_memo
        if self.audit_result:
            if hasattr(self.audit_result, 'to_alipay_dict'):
                params['audit_result'] = self.audit_result.to_alipay_dict()
            else:
                params['audit_result'] = self.audit_result
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.reject_field_list:
            if isinstance(self.reject_field_list, list):
                for i in range(0, len(self.reject_field_list)):
                    element = self.reject_field_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reject_field_list[i] = element.to_alipay_dict()
            if hasattr(self.reject_field_list, 'to_alipay_dict'):
                params['reject_field_list'] = self.reject_field_list.to_alipay_dict()
            else:
                params['reject_field_list'] = self.reject_field_list
        if self.widget_id:
            if hasattr(self.widget_id, 'to_alipay_dict'):
                params['widget_id'] = self.widget_id.to_alipay_dict()
            else:
                params['widget_id'] = self.widget_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WidgetDataAuditRejectResult()
        if 'audit_memo' in d:
            o.audit_memo = d['audit_memo']
        if 'audit_result' in d:
            o.audit_result = d['audit_result']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'reject_field_list' in d:
            o.reject_field_list = d['reject_field_list']
        if 'widget_id' in d:
            o.widget_id = d['widget_id']
        return o


