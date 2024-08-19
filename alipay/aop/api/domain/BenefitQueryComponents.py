#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitQueryComponent import BenefitQueryComponent


class BenefitQueryComponents(object):

    def __init__(self):
        self._luck_draw_query_component = None

    @property
    def luck_draw_query_component(self):
        return self._luck_draw_query_component

    @luck_draw_query_component.setter
    def luck_draw_query_component(self, value):
        if isinstance(value, BenefitQueryComponent):
            self._luck_draw_query_component = value
        else:
            self._luck_draw_query_component = BenefitQueryComponent.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.luck_draw_query_component:
            if hasattr(self.luck_draw_query_component, 'to_alipay_dict'):
                params['luck_draw_query_component'] = self.luck_draw_query_component.to_alipay_dict()
            else:
                params['luck_draw_query_component'] = self.luck_draw_query_component
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitQueryComponents()
        if 'luck_draw_query_component' in d:
            o.luck_draw_query_component = d['luck_draw_query_component']
        return o


