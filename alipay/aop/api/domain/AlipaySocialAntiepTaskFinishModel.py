#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntiepTaskFinishModel(object):

    def __init__(self):
        self._condition_for_variable_award = None
        self._finish_business_info = None
        self._request_mode = None
        self._request_type = None
        self._scene_code = None
        self._source = None
        self._task_token = None
        self._task_type = None
        self._unique_id = None
        self._zone_id = None

    @property
    def condition_for_variable_award(self):
        return self._condition_for_variable_award

    @condition_for_variable_award.setter
    def condition_for_variable_award(self, value):
        self._condition_for_variable_award = value
    @property
    def finish_business_info(self):
        return self._finish_business_info

    @finish_business_info.setter
    def finish_business_info(self, value):
        self._finish_business_info = value
    @property
    def request_mode(self):
        return self._request_mode

    @request_mode.setter
    def request_mode(self, value):
        self._request_mode = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def task_token(self):
        return self._task_token

    @task_token.setter
    def task_token(self, value):
        self._task_token = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def zone_id(self):
        return self._zone_id

    @zone_id.setter
    def zone_id(self, value):
        self._zone_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_for_variable_award:
            if hasattr(self.condition_for_variable_award, 'to_alipay_dict'):
                params['condition_for_variable_award'] = self.condition_for_variable_award.to_alipay_dict()
            else:
                params['condition_for_variable_award'] = self.condition_for_variable_award
        if self.finish_business_info:
            if hasattr(self.finish_business_info, 'to_alipay_dict'):
                params['finish_business_info'] = self.finish_business_info.to_alipay_dict()
            else:
                params['finish_business_info'] = self.finish_business_info
        if self.request_mode:
            if hasattr(self.request_mode, 'to_alipay_dict'):
                params['request_mode'] = self.request_mode.to_alipay_dict()
            else:
                params['request_mode'] = self.request_mode
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.task_token:
            if hasattr(self.task_token, 'to_alipay_dict'):
                params['task_token'] = self.task_token.to_alipay_dict()
            else:
                params['task_token'] = self.task_token
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        if self.zone_id:
            if hasattr(self.zone_id, 'to_alipay_dict'):
                params['zone_id'] = self.zone_id.to_alipay_dict()
            else:
                params['zone_id'] = self.zone_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntiepTaskFinishModel()
        if 'condition_for_variable_award' in d:
            o.condition_for_variable_award = d['condition_for_variable_award']
        if 'finish_business_info' in d:
            o.finish_business_info = d['finish_business_info']
        if 'request_mode' in d:
            o.request_mode = d['request_mode']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'source' in d:
            o.source = d['source']
        if 'task_token' in d:
            o.task_token = d['task_token']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        if 'zone_id' in d:
            o.zone_id = d['zone_id']
        return o


