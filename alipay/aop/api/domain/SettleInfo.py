#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo


class SettleInfo(object):

    def __init__(self):
        self._settle_detail_infos = None
        self._settle_period_time = None

    @property
    def settle_detail_infos(self):
        return self._settle_detail_infos

    @settle_detail_infos.setter
    def settle_detail_infos(self, value):
        if isinstance(value, list):
            self._settle_detail_infos = list()
            for i in value:
                if isinstance(i, SettleDetailInfo):
                    self._settle_detail_infos.append(i)
                else:
                    self._settle_detail_infos.append(SettleDetailInfo.from_alipay_dict(i))
    @property
    def settle_period_time(self):
        return self._settle_period_time

    @settle_period_time.setter
    def settle_period_time(self, value):
        self._settle_period_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.settle_detail_infos:
            if isinstance(self.settle_detail_infos, list):
                for i in range(0, len(self.settle_detail_infos)):
                    element = self.settle_detail_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_detail_infos[i] = element.to_alipay_dict()
            if hasattr(self.settle_detail_infos, 'to_alipay_dict'):
                params['settle_detail_infos'] = self.settle_detail_infos.to_alipay_dict()
            else:
                params['settle_detail_infos'] = self.settle_detail_infos
        if self.settle_period_time:
            if hasattr(self.settle_period_time, 'to_alipay_dict'):
                params['settle_period_time'] = self.settle_period_time.to_alipay_dict()
            else:
                params['settle_period_time'] = self.settle_period_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleInfo()
        if 'settle_detail_infos' in d:
            o.settle_detail_infos = d['settle_detail_infos']
        if 'settle_period_time' in d:
            o.settle_period_time = d['settle_period_time']
        return o


