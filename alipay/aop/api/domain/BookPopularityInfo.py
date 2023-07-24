#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookPopularityInfo(object):

    def __init__(self):
        self._buy_count = None
        self._collect_count = None
        self._read_count = None
        self._score = None
        self._share_count = None

    @property
    def buy_count(self):
        return self._buy_count

    @buy_count.setter
    def buy_count(self, value):
        self._buy_count = value
    @property
    def collect_count(self):
        return self._collect_count

    @collect_count.setter
    def collect_count(self, value):
        self._collect_count = value
    @property
    def read_count(self):
        return self._read_count

    @read_count.setter
    def read_count(self, value):
        self._read_count = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def share_count(self):
        return self._share_count

    @share_count.setter
    def share_count(self, value):
        self._share_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_count:
            if hasattr(self.buy_count, 'to_alipay_dict'):
                params['buy_count'] = self.buy_count.to_alipay_dict()
            else:
                params['buy_count'] = self.buy_count
        if self.collect_count:
            if hasattr(self.collect_count, 'to_alipay_dict'):
                params['collect_count'] = self.collect_count.to_alipay_dict()
            else:
                params['collect_count'] = self.collect_count
        if self.read_count:
            if hasattr(self.read_count, 'to_alipay_dict'):
                params['read_count'] = self.read_count.to_alipay_dict()
            else:
                params['read_count'] = self.read_count
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.share_count:
            if hasattr(self.share_count, 'to_alipay_dict'):
                params['share_count'] = self.share_count.to_alipay_dict()
            else:
                params['share_count'] = self.share_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookPopularityInfo()
        if 'buy_count' in d:
            o.buy_count = d['buy_count']
        if 'collect_count' in d:
            o.collect_count = d['collect_count']
        if 'read_count' in d:
            o.read_count = d['read_count']
        if 'score' in d:
            o.score = d['score']
        if 'share_count' in d:
            o.share_count = d['share_count']
        return o


