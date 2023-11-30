#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyValueMap import KeyValueMap


class AlipaySecurityRiskGuardrailsAskDetectModel(object):

    def __init__(self):
        self._business_properties = None
        self._model_code = None
        self._question = None
        self._question_format = None
        self._request_id = None
        self._scene_code = None
        self._service_name = None
        self._session_id = None
        self._user_id = None

    @property
    def business_properties(self):
        return self._business_properties

    @business_properties.setter
    def business_properties(self, value):
        if isinstance(value, KeyValueMap):
            self._business_properties = value
        else:
            self._business_properties = KeyValueMap.from_alipay_dict(value)
    @property
    def model_code(self):
        return self._model_code

    @model_code.setter
    def model_code(self, value):
        self._model_code = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def question_format(self):
        return self._question_format

    @question_format.setter
    def question_format(self, value):
        self._question_format = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_properties:
            if hasattr(self.business_properties, 'to_alipay_dict'):
                params['business_properties'] = self.business_properties.to_alipay_dict()
            else:
                params['business_properties'] = self.business_properties
        if self.model_code:
            if hasattr(self.model_code, 'to_alipay_dict'):
                params['model_code'] = self.model_code.to_alipay_dict()
            else:
                params['model_code'] = self.model_code
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.question_format:
            if hasattr(self.question_format, 'to_alipay_dict'):
                params['question_format'] = self.question_format.to_alipay_dict()
            else:
                params['question_format'] = self.question_format
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = AlipaySecurityRiskGuardrailsAskDetectModel()
        if 'business_properties' in d:
            o.business_properties = d['business_properties']
        if 'model_code' in d:
            o.model_code = d['model_code']
        if 'question' in d:
            o.question = d['question']
        if 'question_format' in d:
            o.question_format = d['question_format']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


