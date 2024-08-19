#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitOrderInfo import BenefitOrderInfo
from alipay.aop.api.domain.BenefitPlayLuckDrawTemplateInfo import BenefitPlayLuckDrawTemplateInfo


class BenefitLuckDrawTemplate(object):

    def __init__(self):
        self._have_participated = None
        self._play_luck_draw_order_info = None
        self._play_luck_draw_template_info = None

    @property
    def have_participated(self):
        return self._have_participated

    @have_participated.setter
    def have_participated(self, value):
        self._have_participated = value
    @property
    def play_luck_draw_order_info(self):
        return self._play_luck_draw_order_info

    @play_luck_draw_order_info.setter
    def play_luck_draw_order_info(self, value):
        if isinstance(value, BenefitOrderInfo):
            self._play_luck_draw_order_info = value
        else:
            self._play_luck_draw_order_info = BenefitOrderInfo.from_alipay_dict(value)
    @property
    def play_luck_draw_template_info(self):
        return self._play_luck_draw_template_info

    @play_luck_draw_template_info.setter
    def play_luck_draw_template_info(self, value):
        if isinstance(value, BenefitPlayLuckDrawTemplateInfo):
            self._play_luck_draw_template_info = value
        else:
            self._play_luck_draw_template_info = BenefitPlayLuckDrawTemplateInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.have_participated:
            if hasattr(self.have_participated, 'to_alipay_dict'):
                params['have_participated'] = self.have_participated.to_alipay_dict()
            else:
                params['have_participated'] = self.have_participated
        if self.play_luck_draw_order_info:
            if hasattr(self.play_luck_draw_order_info, 'to_alipay_dict'):
                params['play_luck_draw_order_info'] = self.play_luck_draw_order_info.to_alipay_dict()
            else:
                params['play_luck_draw_order_info'] = self.play_luck_draw_order_info
        if self.play_luck_draw_template_info:
            if hasattr(self.play_luck_draw_template_info, 'to_alipay_dict'):
                params['play_luck_draw_template_info'] = self.play_luck_draw_template_info.to_alipay_dict()
            else:
                params['play_luck_draw_template_info'] = self.play_luck_draw_template_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitLuckDrawTemplate()
        if 'have_participated' in d:
            o.have_participated = d['have_participated']
        if 'play_luck_draw_order_info' in d:
            o.play_luck_draw_order_info = d['play_luck_draw_order_info']
        if 'play_luck_draw_template_info' in d:
            o.play_luck_draw_template_info = d['play_luck_draw_template_info']
        return o


