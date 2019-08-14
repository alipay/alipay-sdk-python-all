#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveClassificationFeedbackSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._biz_code = None
        self._cognition_content = None
        self._cognition_type = None
        self._feedback_category = None
        self._feedback_rubbish = None
        self._predict_category = None
        self._predict_rubbish = None
        self._trace_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def cognition_content(self):
        return self._cognition_content

    @cognition_content.setter
    def cognition_content(self, value):
        self._cognition_content = value
    @property
    def cognition_type(self):
        return self._cognition_type

    @cognition_type.setter
    def cognition_type(self, value):
        self._cognition_type = value
    @property
    def feedback_category(self):
        return self._feedback_category

    @feedback_category.setter
    def feedback_category(self, value):
        self._feedback_category = value
    @property
    def feedback_rubbish(self):
        return self._feedback_rubbish

    @feedback_rubbish.setter
    def feedback_rubbish(self, value):
        self._feedback_rubbish = value
    @property
    def predict_category(self):
        return self._predict_category

    @predict_category.setter
    def predict_category(self, value):
        self._predict_category = value
    @property
    def predict_rubbish(self):
        return self._predict_rubbish

    @predict_rubbish.setter
    def predict_rubbish(self, value):
        self._predict_rubbish = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.cognition_content:
            if hasattr(self.cognition_content, 'to_alipay_dict'):
                params['cognition_content'] = self.cognition_content.to_alipay_dict()
            else:
                params['cognition_content'] = self.cognition_content
        if self.cognition_type:
            if hasattr(self.cognition_type, 'to_alipay_dict'):
                params['cognition_type'] = self.cognition_type.to_alipay_dict()
            else:
                params['cognition_type'] = self.cognition_type
        if self.feedback_category:
            if hasattr(self.feedback_category, 'to_alipay_dict'):
                params['feedback_category'] = self.feedback_category.to_alipay_dict()
            else:
                params['feedback_category'] = self.feedback_category
        if self.feedback_rubbish:
            if hasattr(self.feedback_rubbish, 'to_alipay_dict'):
                params['feedback_rubbish'] = self.feedback_rubbish.to_alipay_dict()
            else:
                params['feedback_rubbish'] = self.feedback_rubbish
        if self.predict_category:
            if hasattr(self.predict_category, 'to_alipay_dict'):
                params['predict_category'] = self.predict_category.to_alipay_dict()
            else:
                params['predict_category'] = self.predict_category
        if self.predict_rubbish:
            if hasattr(self.predict_rubbish, 'to_alipay_dict'):
                params['predict_rubbish'] = self.predict_rubbish.to_alipay_dict()
            else:
                params['predict_rubbish'] = self.predict_rubbish
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveClassificationFeedbackSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'cognition_content' in d:
            o.cognition_content = d['cognition_content']
        if 'cognition_type' in d:
            o.cognition_type = d['cognition_type']
        if 'feedback_category' in d:
            o.feedback_category = d['feedback_category']
        if 'feedback_rubbish' in d:
            o.feedback_rubbish = d['feedback_rubbish']
        if 'predict_category' in d:
            o.predict_category = d['predict_category']
        if 'predict_rubbish' in d:
            o.predict_rubbish = d['predict_rubbish']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


