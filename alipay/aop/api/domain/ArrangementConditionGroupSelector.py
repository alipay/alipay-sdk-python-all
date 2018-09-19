#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArrangementConditionGroupSelector(object):

    def __init__(self):
        self._select_latest_pd_cd = None

    @property
    def select_latest_pd_cd(self):
        return self._select_latest_pd_cd

    @select_latest_pd_cd.setter
    def select_latest_pd_cd(self, value):
        self._select_latest_pd_cd = value


    def to_alipay_dict(self):
        params = dict()
        if self.select_latest_pd_cd:
            if hasattr(self.select_latest_pd_cd, 'to_alipay_dict'):
                params['select_latest_pd_cd'] = self.select_latest_pd_cd.to_alipay_dict()
            else:
                params['select_latest_pd_cd'] = self.select_latest_pd_cd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArrangementConditionGroupSelector()
        if 'select_latest_pd_cd' in d:
            o.select_latest_pd_cd = d['select_latest_pd_cd']
        return o


