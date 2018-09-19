#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdiePreviewPagesModel import FengdiePreviewPagesModel


class FengdiePreviewQueryRespModel(object):

    def __init__(self):
        self._list = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, FengdiePreviewPagesModel):
                    self._list.append(i)
                else:
                    self._list.append(FengdiePreviewPagesModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.list:
            if isinstance(self.list, list):
                for i in range(0, len(self.list)):
                    element = self.list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list[i] = element.to_alipay_dict()
            if hasattr(self.list, 'to_alipay_dict'):
                params['list'] = self.list.to_alipay_dict()
            else:
                params['list'] = self.list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdiePreviewQueryRespModel()
        if 'list' in d:
            o.list = d['list']
        return o


