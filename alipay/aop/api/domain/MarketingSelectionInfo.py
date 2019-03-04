#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketingItemSelection import MarketingItemSelection


class MarketingSelectionInfo(object):

    def __init__(self):
        self._selection_list = None
        self._use_mode = None

    @property
    def selection_list(self):
        return self._selection_list

    @selection_list.setter
    def selection_list(self, value):
        if isinstance(value, list):
            self._selection_list = list()
            for i in value:
                if isinstance(i, MarketingItemSelection):
                    self._selection_list.append(i)
                else:
                    self._selection_list.append(MarketingItemSelection.from_alipay_dict(i))
    @property
    def use_mode(self):
        return self._use_mode

    @use_mode.setter
    def use_mode(self, value):
        self._use_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.selection_list:
            if isinstance(self.selection_list, list):
                for i in range(0, len(self.selection_list)):
                    element = self.selection_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.selection_list[i] = element.to_alipay_dict()
            if hasattr(self.selection_list, 'to_alipay_dict'):
                params['selection_list'] = self.selection_list.to_alipay_dict()
            else:
                params['selection_list'] = self.selection_list
        if self.use_mode:
            if hasattr(self.use_mode, 'to_alipay_dict'):
                params['use_mode'] = self.use_mode.to_alipay_dict()
            else:
                params['use_mode'] = self.use_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketingSelectionInfo()
        if 'selection_list' in d:
            o.selection_list = d['selection_list']
        if 'use_mode' in d:
            o.use_mode = d['use_mode']
        return o


