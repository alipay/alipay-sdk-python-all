#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstSigConfigInfo import InstSigConfigInfo


class AntfortuneFinresearchInstSignalSyncModel(object):

    def __init__(self):
        self._datas = None
        self._inst_id = None

    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, value):
        if isinstance(value, list):
            self._datas = list()
            for i in value:
                if isinstance(i, InstSigConfigInfo):
                    self._datas.append(i)
                else:
                    self._datas.append(InstSigConfigInfo.from_alipay_dict(i))
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.datas:
            if isinstance(self.datas, list):
                for i in range(0, len(self.datas)):
                    element = self.datas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.datas[i] = element.to_alipay_dict()
            if hasattr(self.datas, 'to_alipay_dict'):
                params['datas'] = self.datas.to_alipay_dict()
            else:
                params['datas'] = self.datas
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchInstSignalSyncModel()
        if 'datas' in d:
            o.datas = d['datas']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        return o


