#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantshopCommentStatistic(object):

    def __init__(self):
        self._comment_count = None
        self._score = None

    @property
    def comment_count(self):
        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        self._comment_count = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment_count:
            if hasattr(self.comment_count, 'to_alipay_dict'):
                params['comment_count'] = self.comment_count.to_alipay_dict()
            else:
                params['comment_count'] = self.comment_count
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantshopCommentStatistic()
        if 'comment_count' in d:
            o.comment_count = d['comment_count']
        if 'score' in d:
            o.score = d['score']
        return o


