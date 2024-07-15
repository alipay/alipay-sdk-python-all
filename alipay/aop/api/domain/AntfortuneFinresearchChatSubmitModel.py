#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchChatSubmitModel(object):

    def __init__(self):
        self._bu_unique_id = None
        self._business_type = None
        self._file_ids = None
        self._file_type = None
        self._interpret_mode = None
        self._question = None
        self._session_id = None
        self._tenant_id = None
        self._urls = None
        self._user_framework_code = None

    @property
    def bu_unique_id(self):
        return self._bu_unique_id

    @bu_unique_id.setter
    def bu_unique_id(self, value):
        self._bu_unique_id = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def file_ids(self):
        return self._file_ids

    @file_ids.setter
    def file_ids(self, value):
        if isinstance(value, list):
            self._file_ids = list()
            for i in value:
                self._file_ids.append(i)
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def interpret_mode(self):
        return self._interpret_mode

    @interpret_mode.setter
    def interpret_mode(self, value):
        self._interpret_mode = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, value):
        if isinstance(value, list):
            self._urls = list()
            for i in value:
                self._urls.append(i)
    @property
    def user_framework_code(self):
        return self._user_framework_code

    @user_framework_code.setter
    def user_framework_code(self, value):
        self._user_framework_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bu_unique_id:
            if hasattr(self.bu_unique_id, 'to_alipay_dict'):
                params['bu_unique_id'] = self.bu_unique_id.to_alipay_dict()
            else:
                params['bu_unique_id'] = self.bu_unique_id
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.file_ids:
            if isinstance(self.file_ids, list):
                for i in range(0, len(self.file_ids)):
                    element = self.file_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_ids[i] = element.to_alipay_dict()
            if hasattr(self.file_ids, 'to_alipay_dict'):
                params['file_ids'] = self.file_ids.to_alipay_dict()
            else:
                params['file_ids'] = self.file_ids
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.interpret_mode:
            if hasattr(self.interpret_mode, 'to_alipay_dict'):
                params['interpret_mode'] = self.interpret_mode.to_alipay_dict()
            else:
                params['interpret_mode'] = self.interpret_mode
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.urls:
            if isinstance(self.urls, list):
                for i in range(0, len(self.urls)):
                    element = self.urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.urls[i] = element.to_alipay_dict()
            if hasattr(self.urls, 'to_alipay_dict'):
                params['urls'] = self.urls.to_alipay_dict()
            else:
                params['urls'] = self.urls
        if self.user_framework_code:
            if hasattr(self.user_framework_code, 'to_alipay_dict'):
                params['user_framework_code'] = self.user_framework_code.to_alipay_dict()
            else:
                params['user_framework_code'] = self.user_framework_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchChatSubmitModel()
        if 'bu_unique_id' in d:
            o.bu_unique_id = d['bu_unique_id']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'file_ids' in d:
            o.file_ids = d['file_ids']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'interpret_mode' in d:
            o.interpret_mode = d['interpret_mode']
        if 'question' in d:
            o.question = d['question']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'urls' in d:
            o.urls = d['urls']
        if 'user_framework_code' in d:
            o.user_framework_code = d['user_framework_code']
        return o


