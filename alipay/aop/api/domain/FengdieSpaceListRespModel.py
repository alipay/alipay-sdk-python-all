#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieSpaceDetailModel import FengdieSpaceDetailModel
from alipay.aop.api.domain.FengdieListPaginator import FengdieListPaginator


class FengdieSpaceListRespModel(object):

    def __init__(self):
        self._list = None
        self._paginator = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, FengdieSpaceDetailModel):
                    self._list.append(i)
                else:
                    self._list.append(FengdieSpaceDetailModel.from_alipay_dict(i))
    @property
    def paginator(self):
        return self._paginator

    @paginator.setter
    def paginator(self, value):
        if isinstance(value, FengdieListPaginator):
            self._paginator = value
        else:
            self._paginator = FengdieListPaginator.from_alipay_dict(value)


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
        if self.paginator:
            if hasattr(self.paginator, 'to_alipay_dict'):
                params['paginator'] = self.paginator.to_alipay_dict()
            else:
                params['paginator'] = self.paginator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieSpaceListRespModel()
        if 'list' in d:
            o.list = d['list']
        if 'paginator' in d:
            o.paginator = d['paginator']
        return o


