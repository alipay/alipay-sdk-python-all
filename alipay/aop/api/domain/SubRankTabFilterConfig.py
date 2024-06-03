#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubRankTabFilterConfig(object):

    def __init__(self):
        self._min_version_code = None
        self._rank_data_type = None
        self._title = None
        self._winter_eval = None

    @property
    def min_version_code(self):
        return self._min_version_code

    @min_version_code.setter
    def min_version_code(self, value):
        self._min_version_code = value
    @property
    def rank_data_type(self):
        return self._rank_data_type

    @rank_data_type.setter
    def rank_data_type(self, value):
        self._rank_data_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def winter_eval(self):
        return self._winter_eval

    @winter_eval.setter
    def winter_eval(self, value):
        self._winter_eval = value


    def to_alipay_dict(self):
        params = dict()
        if self.min_version_code:
            if hasattr(self.min_version_code, 'to_alipay_dict'):
                params['min_version_code'] = self.min_version_code.to_alipay_dict()
            else:
                params['min_version_code'] = self.min_version_code
        if self.rank_data_type:
            if hasattr(self.rank_data_type, 'to_alipay_dict'):
                params['rank_data_type'] = self.rank_data_type.to_alipay_dict()
            else:
                params['rank_data_type'] = self.rank_data_type
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.winter_eval:
            if hasattr(self.winter_eval, 'to_alipay_dict'):
                params['winter_eval'] = self.winter_eval.to_alipay_dict()
            else:
                params['winter_eval'] = self.winter_eval
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubRankTabFilterConfig()
        if 'min_version_code' in d:
            o.min_version_code = d['min_version_code']
        if 'rank_data_type' in d:
            o.rank_data_type = d['rank_data_type']
        if 'title' in d:
            o.title = d['title']
        if 'winter_eval' in d:
            o.winter_eval = d['winter_eval']
        return o


