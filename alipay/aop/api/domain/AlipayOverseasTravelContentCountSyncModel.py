#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CountInfo import CountInfo


class AlipayOverseasTravelContentCountSyncModel(object):

    def __init__(self):
        self._count_infos = None

    @property
    def count_infos(self):
        return self._count_infos

    @count_infos.setter
    def count_infos(self, value):
        if isinstance(value, list):
            self._count_infos = list()
            for i in value:
                if isinstance(i, CountInfo):
                    self._count_infos.append(i)
                else:
                    self._count_infos.append(CountInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.count_infos:
            if isinstance(self.count_infos, list):
                for i in range(0, len(self.count_infos)):
                    element = self.count_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.count_infos[i] = element.to_alipay_dict()
            if hasattr(self.count_infos, 'to_alipay_dict'):
                params['count_infos'] = self.count_infos.to_alipay_dict()
            else:
                params['count_infos'] = self.count_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelContentCountSyncModel()
        if 'count_infos' in d:
            o.count_infos = d['count_infos']
        return o


