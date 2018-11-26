#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPortraitQueryModel(object):

    def __init__(self):
        self._havana_id = None

    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        if isinstance(value, list):
            self._havana_id = list()
            for i in value:
                self._havana_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.havana_id:
            if isinstance(self.havana_id, list):
                for i in range(0, len(self.havana_id)):
                    element = self.havana_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.havana_id[i] = element.to_alipay_dict()
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPortraitQueryModel()
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        return o


