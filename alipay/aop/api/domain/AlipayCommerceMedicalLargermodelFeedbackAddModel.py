#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelFeedbackAddModel(object):

    def __init__(self):
        self._chat_id = None
        self._feed_back_tags = None
        self._feedback = None
        self._open_id = None
        self._out_user_id = None
        self._out_user_type = None
        self._session_id = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def feed_back_tags(self):
        return self._feed_back_tags

    @feed_back_tags.setter
    def feed_back_tags(self, value):
        if isinstance(value, list):
            self._feed_back_tags = list()
            for i in value:
                self._feed_back_tags.append(i)
    @property
    def feedback(self):
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        self._feedback = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_type(self):
        return self._out_user_type

    @out_user_type.setter
    def out_user_type(self, value):
        self._out_user_type = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.feed_back_tags:
            if isinstance(self.feed_back_tags, list):
                for i in range(0, len(self.feed_back_tags)):
                    element = self.feed_back_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feed_back_tags[i] = element.to_alipay_dict()
            if hasattr(self.feed_back_tags, 'to_alipay_dict'):
                params['feed_back_tags'] = self.feed_back_tags.to_alipay_dict()
            else:
                params['feed_back_tags'] = self.feed_back_tags
        if self.feedback:
            if hasattr(self.feedback, 'to_alipay_dict'):
                params['feedback'] = self.feedback.to_alipay_dict()
            else:
                params['feedback'] = self.feedback
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_type:
            if hasattr(self.out_user_type, 'to_alipay_dict'):
                params['out_user_type'] = self.out_user_type.to_alipay_dict()
            else:
                params['out_user_type'] = self.out_user_type
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelFeedbackAddModel()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'feed_back_tags' in d:
            o.feed_back_tags = d['feed_back_tags']
        if 'feedback' in d:
            o.feedback = d['feedback']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_type' in d:
            o.out_user_type = d['out_user_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


