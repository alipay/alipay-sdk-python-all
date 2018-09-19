#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicTopicDeleteModel(object):

    def __init__(self):
        self._topic_id = None

    @property
    def topic_id(self):
        return self._topic_id

    @topic_id.setter
    def topic_id(self, value):
        self._topic_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.topic_id:
            if hasattr(self.topic_id, 'to_alipay_dict'):
                params['topic_id'] = self.topic_id.to_alipay_dict()
            else:
                params['topic_id'] = self.topic_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicTopicDeleteModel()
        if 'topic_id' in d:
            o.topic_id = d['topic_id']
        return o


