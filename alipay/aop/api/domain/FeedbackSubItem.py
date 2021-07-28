#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeedbackSubItem(object):

    def __init__(self):
        self._score = None
        self._sub_item_desc = None
        self._sub_item_key = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def sub_item_desc(self):
        return self._sub_item_desc

    @sub_item_desc.setter
    def sub_item_desc(self, value):
        self._sub_item_desc = value
    @property
    def sub_item_key(self):
        return self._sub_item_key

    @sub_item_key.setter
    def sub_item_key(self, value):
        self._sub_item_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.sub_item_desc:
            if hasattr(self.sub_item_desc, 'to_alipay_dict'):
                params['sub_item_desc'] = self.sub_item_desc.to_alipay_dict()
            else:
                params['sub_item_desc'] = self.sub_item_desc
        if self.sub_item_key:
            if hasattr(self.sub_item_key, 'to_alipay_dict'):
                params['sub_item_key'] = self.sub_item_key.to_alipay_dict()
            else:
                params['sub_item_key'] = self.sub_item_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeedbackSubItem()
        if 'score' in d:
            o.score = d['score']
        if 'sub_item_desc' in d:
            o.sub_item_desc = d['sub_item_desc']
        if 'sub_item_key' in d:
            o.sub_item_key = d['sub_item_key']
        return o


