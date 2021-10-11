#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EvaluateInfo(object):

    def __init__(self):
        self._content = None
        self._driver_score = None
        self._id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def driver_score(self):
        return self._driver_score

    @driver_score.setter
    def driver_score(self, value):
        self._driver_score = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.driver_score:
            if hasattr(self.driver_score, 'to_alipay_dict'):
                params['driver_score'] = self.driver_score.to_alipay_dict()
            else:
                params['driver_score'] = self.driver_score
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvaluateInfo()
        if 'content' in d:
            o.content = d['content']
        if 'driver_score' in d:
            o.driver_score = d['driver_score']
        if 'id' in d:
            o.id = d['id']
        return o


