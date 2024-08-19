#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitLuckDrawTemplate import BenefitLuckDrawTemplate


class BenefitQueryContent(object):

    def __init__(self):
        self._luck_draw_templates = None

    @property
    def luck_draw_templates(self):
        return self._luck_draw_templates

    @luck_draw_templates.setter
    def luck_draw_templates(self, value):
        if isinstance(value, list):
            self._luck_draw_templates = list()
            for i in value:
                if isinstance(i, BenefitLuckDrawTemplate):
                    self._luck_draw_templates.append(i)
                else:
                    self._luck_draw_templates.append(BenefitLuckDrawTemplate.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.luck_draw_templates:
            if isinstance(self.luck_draw_templates, list):
                for i in range(0, len(self.luck_draw_templates)):
                    element = self.luck_draw_templates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.luck_draw_templates[i] = element.to_alipay_dict()
            if hasattr(self.luck_draw_templates, 'to_alipay_dict'):
                params['luck_draw_templates'] = self.luck_draw_templates.to_alipay_dict()
            else:
                params['luck_draw_templates'] = self.luck_draw_templates
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitQueryContent()
        if 'luck_draw_templates' in d:
            o.luck_draw_templates = d['luck_draw_templates']
        return o


