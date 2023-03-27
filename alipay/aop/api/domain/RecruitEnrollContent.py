#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitContentAppItem import RecruitContentAppItem


class RecruitEnrollContent(object):

    def __init__(self):
        self._app_items = None

    @property
    def app_items(self):
        return self._app_items

    @app_items.setter
    def app_items(self, value):
        if isinstance(value, list):
            self._app_items = list()
            for i in value:
                if isinstance(i, RecruitContentAppItem):
                    self._app_items.append(i)
                else:
                    self._app_items.append(RecruitContentAppItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_items:
            if isinstance(self.app_items, list):
                for i in range(0, len(self.app_items)):
                    element = self.app_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_items[i] = element.to_alipay_dict()
            if hasattr(self.app_items, 'to_alipay_dict'):
                params['app_items'] = self.app_items.to_alipay_dict()
            else:
                params['app_items'] = self.app_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollContent()
        if 'app_items' in d:
            o.app_items = d['app_items']
        return o


