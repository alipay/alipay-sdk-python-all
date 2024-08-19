#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitOrderInfo import BenefitOrderInfo


class BenefitRecordQueryContent(object):

    def __init__(self):
        self._play_luck_draw_order_infos = None

    @property
    def play_luck_draw_order_infos(self):
        return self._play_luck_draw_order_infos

    @play_luck_draw_order_infos.setter
    def play_luck_draw_order_infos(self, value):
        if isinstance(value, list):
            self._play_luck_draw_order_infos = list()
            for i in value:
                if isinstance(i, BenefitOrderInfo):
                    self._play_luck_draw_order_infos.append(i)
                else:
                    self._play_luck_draw_order_infos.append(BenefitOrderInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.play_luck_draw_order_infos:
            if isinstance(self.play_luck_draw_order_infos, list):
                for i in range(0, len(self.play_luck_draw_order_infos)):
                    element = self.play_luck_draw_order_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.play_luck_draw_order_infos[i] = element.to_alipay_dict()
            if hasattr(self.play_luck_draw_order_infos, 'to_alipay_dict'):
                params['play_luck_draw_order_infos'] = self.play_luck_draw_order_infos.to_alipay_dict()
            else:
                params['play_luck_draw_order_infos'] = self.play_luck_draw_order_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitRecordQueryContent()
        if 'play_luck_draw_order_infos' in d:
            o.play_luck_draw_order_infos = d['play_luck_draw_order_infos']
        return o


