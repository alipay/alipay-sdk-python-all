#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceSearchDetailInfo(object):

    def __init__(self):
        self._city_code = None
        self._out_data_id = None
        self._score = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def out_data_id(self):
        return self._out_data_id

    @out_data_id.setter
    def out_data_id(self, value):
        self._out_data_id = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.out_data_id:
            if hasattr(self.out_data_id, 'to_alipay_dict'):
                params['out_data_id'] = self.out_data_id.to_alipay_dict()
            else:
                params['out_data_id'] = self.out_data_id
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
        o = ServiceSearchDetailInfo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'out_data_id' in d:
            o.out_data_id = d['out_data_id']
        if 'score' in d:
            o.score = d['score']
        return o


