#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpPromoTargetInfo import VcpPromoTargetInfo


class VcpBizInfo(object):

    def __init__(self):
        self._biz_tags = None
        self._promo_target = None

    @property
    def biz_tags(self):
        return self._biz_tags

    @biz_tags.setter
    def biz_tags(self, value):
        if isinstance(value, list):
            self._biz_tags = list()
            for i in value:
                self._biz_tags.append(i)
    @property
    def promo_target(self):
        return self._promo_target

    @promo_target.setter
    def promo_target(self, value):
        if isinstance(value, VcpPromoTargetInfo):
            self._promo_target = value
        else:
            self._promo_target = VcpPromoTargetInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tags:
            if isinstance(self.biz_tags, list):
                for i in range(0, len(self.biz_tags)):
                    element = self.biz_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_tags[i] = element.to_alipay_dict()
            if hasattr(self.biz_tags, 'to_alipay_dict'):
                params['biz_tags'] = self.biz_tags.to_alipay_dict()
            else:
                params['biz_tags'] = self.biz_tags
        if self.promo_target:
            if hasattr(self.promo_target, 'to_alipay_dict'):
                params['promo_target'] = self.promo_target.to_alipay_dict()
            else:
                params['promo_target'] = self.promo_target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpBizInfo()
        if 'biz_tags' in d:
            o.biz_tags = d['biz_tags']
        if 'promo_target' in d:
            o.promo_target = d['promo_target']
        return o


