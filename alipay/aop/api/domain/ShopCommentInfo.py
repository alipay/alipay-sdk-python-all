#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopCommentInfo(object):

    def __init__(self):
        self._avg_popularity = None
        self._avg_popularity_name = None
        self._score = None
        self._star = None

    @property
    def avg_popularity(self):
        return self._avg_popularity

    @avg_popularity.setter
    def avg_popularity(self, value):
        self._avg_popularity = value
    @property
    def avg_popularity_name(self):
        return self._avg_popularity_name

    @avg_popularity_name.setter
    def avg_popularity_name(self, value):
        self._avg_popularity_name = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def star(self):
        return self._star

    @star.setter
    def star(self, value):
        self._star = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_popularity:
            if hasattr(self.avg_popularity, 'to_alipay_dict'):
                params['avg_popularity'] = self.avg_popularity.to_alipay_dict()
            else:
                params['avg_popularity'] = self.avg_popularity
        if self.avg_popularity_name:
            if hasattr(self.avg_popularity_name, 'to_alipay_dict'):
                params['avg_popularity_name'] = self.avg_popularity_name.to_alipay_dict()
            else:
                params['avg_popularity_name'] = self.avg_popularity_name
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.star:
            if hasattr(self.star, 'to_alipay_dict'):
                params['star'] = self.star.to_alipay_dict()
            else:
                params['star'] = self.star
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopCommentInfo()
        if 'avg_popularity' in d:
            o.avg_popularity = d['avg_popularity']
        if 'avg_popularity_name' in d:
            o.avg_popularity_name = d['avg_popularity_name']
        if 'score' in d:
            o.score = d['score']
        if 'star' in d:
            o.star = d['star']
        return o


