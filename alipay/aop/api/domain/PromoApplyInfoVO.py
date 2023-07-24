#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoApplyItemInfoVO import PromoApplyItemInfoVO
from alipay.aop.api.domain.PromoApplySummaryInfoVO import PromoApplySummaryInfoVO


class PromoApplyInfoVO(object):

    def __init__(self):
        self._promo_apply_item_infos = None
        self._promo_apply_summary_infos = None

    @property
    def promo_apply_item_infos(self):
        return self._promo_apply_item_infos

    @promo_apply_item_infos.setter
    def promo_apply_item_infos(self, value):
        if isinstance(value, list):
            self._promo_apply_item_infos = list()
            for i in value:
                if isinstance(i, PromoApplyItemInfoVO):
                    self._promo_apply_item_infos.append(i)
                else:
                    self._promo_apply_item_infos.append(PromoApplyItemInfoVO.from_alipay_dict(i))
    @property
    def promo_apply_summary_infos(self):
        return self._promo_apply_summary_infos

    @promo_apply_summary_infos.setter
    def promo_apply_summary_infos(self, value):
        if isinstance(value, list):
            self._promo_apply_summary_infos = list()
            for i in value:
                if isinstance(i, PromoApplySummaryInfoVO):
                    self._promo_apply_summary_infos.append(i)
                else:
                    self._promo_apply_summary_infos.append(PromoApplySummaryInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.promo_apply_item_infos:
            if isinstance(self.promo_apply_item_infos, list):
                for i in range(0, len(self.promo_apply_item_infos)):
                    element = self.promo_apply_item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_apply_item_infos[i] = element.to_alipay_dict()
            if hasattr(self.promo_apply_item_infos, 'to_alipay_dict'):
                params['promo_apply_item_infos'] = self.promo_apply_item_infos.to_alipay_dict()
            else:
                params['promo_apply_item_infos'] = self.promo_apply_item_infos
        if self.promo_apply_summary_infos:
            if isinstance(self.promo_apply_summary_infos, list):
                for i in range(0, len(self.promo_apply_summary_infos)):
                    element = self.promo_apply_summary_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_apply_summary_infos[i] = element.to_alipay_dict()
            if hasattr(self.promo_apply_summary_infos, 'to_alipay_dict'):
                params['promo_apply_summary_infos'] = self.promo_apply_summary_infos.to_alipay_dict()
            else:
                params['promo_apply_summary_infos'] = self.promo_apply_summary_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoApplyInfoVO()
        if 'promo_apply_item_infos' in d:
            o.promo_apply_item_infos = d['promo_apply_item_infos']
        if 'promo_apply_summary_infos' in d:
            o.promo_apply_summary_infos = d['promo_apply_summary_infos']
        return o


