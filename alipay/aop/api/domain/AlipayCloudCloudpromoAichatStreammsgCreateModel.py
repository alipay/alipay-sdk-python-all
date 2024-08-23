#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoAichatStreammsgCreateModel(object):

    def __init__(self):
        self._biz_trans_data = None
        self._chat_type = None
        self._customer_id = None
        self._question = None
        self._request_id = None
        self._retry = None
        self._scene_id = None
        self._session_id = None
        self._source_id = None

    @property
    def biz_trans_data(self):
        return self._biz_trans_data

    @biz_trans_data.setter
    def biz_trans_data(self, value):
        self._biz_trans_data = value
    @property
    def chat_type(self):
        return self._chat_type

    @chat_type.setter
    def chat_type(self, value):
        self._chat_type = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trans_data:
            if hasattr(self.biz_trans_data, 'to_alipay_dict'):
                params['biz_trans_data'] = self.biz_trans_data.to_alipay_dict()
            else:
                params['biz_trans_data'] = self.biz_trans_data
        if self.chat_type:
            if hasattr(self.chat_type, 'to_alipay_dict'):
                params['chat_type'] = self.chat_type.to_alipay_dict()
            else:
                params['chat_type'] = self.chat_type
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.retry:
            if hasattr(self.retry, 'to_alipay_dict'):
                params['retry'] = self.retry.to_alipay_dict()
            else:
                params['retry'] = self.retry
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAichatStreammsgCreateModel()
        if 'biz_trans_data' in d:
            o.biz_trans_data = d['biz_trans_data']
        if 'chat_type' in d:
            o.chat_type = d['chat_type']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'question' in d:
            o.question = d['question']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'retry' in d:
            o.retry = d['retry']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


