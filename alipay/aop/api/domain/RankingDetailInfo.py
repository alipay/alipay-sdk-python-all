#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RankingDetailInfo(object):

    def __init__(self):
        self._point = None

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value


    def to_alipay_dict(self):
        params = dict()
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RankingDetailInfo()
        if 'point' in d:
            o.point = d['point']
        return o


