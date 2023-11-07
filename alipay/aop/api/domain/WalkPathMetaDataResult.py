#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WalkPathMetaData import WalkPathMetaData


class WalkPathMetaDataResult(object):

    def __init__(self):
        self._paths = None

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, value):
        if isinstance(value, list):
            self._paths = list()
            for i in value:
                if isinstance(i, WalkPathMetaData):
                    self._paths.append(i)
                else:
                    self._paths.append(WalkPathMetaData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.paths:
            if isinstance(self.paths, list):
                for i in range(0, len(self.paths)):
                    element = self.paths[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.paths[i] = element.to_alipay_dict()
            if hasattr(self.paths, 'to_alipay_dict'):
                params['paths'] = self.paths.to_alipay_dict()
            else:
                params['paths'] = self.paths
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalkPathMetaDataResult()
        if 'paths' in d:
            o.paths = d['paths']
        return o


