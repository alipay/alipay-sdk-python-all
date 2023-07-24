#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AIDongSubjectSyncDetail import AIDongSubjectSyncDetail


class AlipayCommerceSportsSubjectBackstageSyncModel(object):

    def __init__(self):
        self._list = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, AIDongSubjectSyncDetail):
            self._list = value
        else:
            self._list = AIDongSubjectSyncDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.list:
            if hasattr(self.list, 'to_alipay_dict'):
                params['list'] = self.list.to_alipay_dict()
            else:
                params['list'] = self.list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsSubjectBackstageSyncModel()
        if 'list' in d:
            o.list = d['list']
        return o


