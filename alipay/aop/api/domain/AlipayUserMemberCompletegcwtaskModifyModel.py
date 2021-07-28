#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserMemberCompletegcwtaskModifyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._application_id = None
        self._biz_date = None
        self._biz_type = None
        self._biz_value = None
        self._flow_id = None
        self._task_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def biz_value(self):
        return self._biz_value

    @biz_value.setter
    def biz_value(self, value):
        self._biz_value = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.biz_value:
            if hasattr(self.biz_value, 'to_alipay_dict'):
                params['biz_value'] = self.biz_value.to_alipay_dict()
            else:
                params['biz_value'] = self.biz_value
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserMemberCompletegcwtaskModifyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'biz_value' in d:
            o.biz_value = d['biz_value']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


