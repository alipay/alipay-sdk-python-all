#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PBCHitDetail import PBCHitDetail


class PBCScanResult(object):

    def __init__(self):
        self._hit_details = None

    @property
    def hit_details(self):
        return self._hit_details

    @hit_details.setter
    def hit_details(self, value):
        if isinstance(value, list):
            self._hit_details = list()
            for i in value:
                if isinstance(i, PBCHitDetail):
                    self._hit_details.append(i)
                else:
                    self._hit_details.append(PBCHitDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.hit_details:
            if isinstance(self.hit_details, list):
                for i in range(0, len(self.hit_details)):
                    element = self.hit_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hit_details[i] = element.to_alipay_dict()
            if hasattr(self.hit_details, 'to_alipay_dict'):
                params['hit_details'] = self.hit_details.to_alipay_dict()
            else:
                params['hit_details'] = self.hit_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PBCScanResult()
        if 'hit_details' in d:
            o.hit_details = d['hit_details']
        return o


