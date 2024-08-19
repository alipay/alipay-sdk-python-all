#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitDisplayInfoResponse import BenefitDisplayInfoResponse


class BenefitRight(object):

    def __init__(self):
        self._display_info = None

    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        if isinstance(value, BenefitDisplayInfoResponse):
            self._display_info = value
        else:
            self._display_info = BenefitDisplayInfoResponse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.display_info:
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitRight()
        if 'display_info' in d:
            o.display_info = d['display_info']
        return o


