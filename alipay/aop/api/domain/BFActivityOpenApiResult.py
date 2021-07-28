#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BFActivityOpenApiInfo import BFActivityOpenApiInfo


class BFActivityOpenApiResult(object):

    def __init__(self):
        self._activity_infos = None

    @property
    def activity_infos(self):
        return self._activity_infos

    @activity_infos.setter
    def activity_infos(self, value):
        if isinstance(value, list):
            self._activity_infos = list()
            for i in value:
                if isinstance(i, BFActivityOpenApiInfo):
                    self._activity_infos.append(i)
                else:
                    self._activity_infos.append(BFActivityOpenApiInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_infos:
            if isinstance(self.activity_infos, list):
                for i in range(0, len(self.activity_infos)):
                    element = self.activity_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_infos[i] = element.to_alipay_dict()
            if hasattr(self.activity_infos, 'to_alipay_dict'):
                params['activity_infos'] = self.activity_infos.to_alipay_dict()
            else:
                params['activity_infos'] = self.activity_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BFActivityOpenApiResult()
        if 'activity_infos' in d:
            o.activity_infos = d['activity_infos']
        return o


