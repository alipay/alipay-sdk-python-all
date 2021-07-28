#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayGuideVO(object):

    def __init__(self):
        self._guide_param = None
        self._need_guide = None

    @property
    def guide_param(self):
        return self._guide_param

    @guide_param.setter
    def guide_param(self, value):
        self._guide_param = value
    @property
    def need_guide(self):
        return self._need_guide

    @need_guide.setter
    def need_guide(self, value):
        self._need_guide = value


    def to_alipay_dict(self):
        params = dict()
        if self.guide_param:
            if hasattr(self.guide_param, 'to_alipay_dict'):
                params['guide_param'] = self.guide_param.to_alipay_dict()
            else:
                params['guide_param'] = self.guide_param
        if self.need_guide:
            if hasattr(self.need_guide, 'to_alipay_dict'):
                params['need_guide'] = self.need_guide.to_alipay_dict()
            else:
                params['need_guide'] = self.need_guide
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayGuideVO()
        if 'guide_param' in d:
            o.guide_param = d['guide_param']
        if 'need_guide' in d:
            o.need_guide = d['need_guide']
        return o


