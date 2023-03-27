#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitServingTargetCity import RecruitServingTargetCity


class RecruitServingTarget(object):

    def __init__(self):
        self._city = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, RecruitServingTargetCity):
            self._city = value
        else:
            self._city = RecruitServingTargetCity.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitServingTarget()
        if 'city' in d:
            o.city = d['city']
        return o


