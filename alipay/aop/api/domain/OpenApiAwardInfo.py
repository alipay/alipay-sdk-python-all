#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiAwardInfo(object):

    def __init__(self):
        self._current_award = None
        self._detail_list = None
        self._total_award = None

    @property
    def current_award(self):
        return self._current_award

    @current_award.setter
    def current_award(self, value):
        self._current_award = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                self._detail_list.append(i)
    @property
    def total_award(self):
        return self._total_award

    @total_award.setter
    def total_award(self, value):
        self._total_award = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_award:
            if hasattr(self.current_award, 'to_alipay_dict'):
                params['current_award'] = self.current_award.to_alipay_dict()
            else:
                params['current_award'] = self.current_award
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.total_award:
            if hasattr(self.total_award, 'to_alipay_dict'):
                params['total_award'] = self.total_award.to_alipay_dict()
            else:
                params['total_award'] = self.total_award
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiAwardInfo()
        if 'current_award' in d:
            o.current_award = d['current_award']
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'total_award' in d:
            o.total_award = d['total_award']
        return o


