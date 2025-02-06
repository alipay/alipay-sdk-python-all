#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerSegmentOfPassengersInfo import VoyagerSegmentOfPassengersInfo
from alipay.aop.api.domain.VoyagerSegmentOfPassengersInfo import VoyagerSegmentOfPassengersInfo


class VoyagerOrderRebookInfo(object):

    def __init__(self):
        self._after_rebook = None
        self._before_rebook = None

    @property
    def after_rebook(self):
        return self._after_rebook

    @after_rebook.setter
    def after_rebook(self, value):
        if isinstance(value, list):
            self._after_rebook = list()
            for i in value:
                if isinstance(i, VoyagerSegmentOfPassengersInfo):
                    self._after_rebook.append(i)
                else:
                    self._after_rebook.append(VoyagerSegmentOfPassengersInfo.from_alipay_dict(i))
    @property
    def before_rebook(self):
        return self._before_rebook

    @before_rebook.setter
    def before_rebook(self, value):
        if isinstance(value, list):
            self._before_rebook = list()
            for i in value:
                if isinstance(i, VoyagerSegmentOfPassengersInfo):
                    self._before_rebook.append(i)
                else:
                    self._before_rebook.append(VoyagerSegmentOfPassengersInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.after_rebook:
            if isinstance(self.after_rebook, list):
                for i in range(0, len(self.after_rebook)):
                    element = self.after_rebook[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.after_rebook[i] = element.to_alipay_dict()
            if hasattr(self.after_rebook, 'to_alipay_dict'):
                params['after_rebook'] = self.after_rebook.to_alipay_dict()
            else:
                params['after_rebook'] = self.after_rebook
        if self.before_rebook:
            if isinstance(self.before_rebook, list):
                for i in range(0, len(self.before_rebook)):
                    element = self.before_rebook[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.before_rebook[i] = element.to_alipay_dict()
            if hasattr(self.before_rebook, 'to_alipay_dict'):
                params['before_rebook'] = self.before_rebook.to_alipay_dict()
            else:
                params['before_rebook'] = self.before_rebook
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerOrderRebookInfo()
        if 'after_rebook' in d:
            o.after_rebook = d['after_rebook']
        if 'before_rebook' in d:
            o.before_rebook = d['before_rebook']
        return o


