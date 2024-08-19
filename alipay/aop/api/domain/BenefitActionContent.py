#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitLuckDrawInfo import BenefitLuckDrawInfo


class BenefitActionContent(object):

    def __init__(self):
        self._luck_draw_info = None

    @property
    def luck_draw_info(self):
        return self._luck_draw_info

    @luck_draw_info.setter
    def luck_draw_info(self, value):
        if isinstance(value, BenefitLuckDrawInfo):
            self._luck_draw_info = value
        else:
            self._luck_draw_info = BenefitLuckDrawInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.luck_draw_info:
            if hasattr(self.luck_draw_info, 'to_alipay_dict'):
                params['luck_draw_info'] = self.luck_draw_info.to_alipay_dict()
            else:
                params['luck_draw_info'] = self.luck_draw_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitActionContent()
        if 'luck_draw_info' in d:
            o.luck_draw_info = d['luck_draw_info']
        return o


