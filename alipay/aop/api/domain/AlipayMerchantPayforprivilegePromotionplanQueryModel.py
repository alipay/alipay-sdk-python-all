#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantPayforprivilegePromotionplanQueryModel(object):

    def __init__(self):
        self._promotion_plan_id = None

    @property
    def promotion_plan_id(self):
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, value):
        self._promotion_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.promotion_plan_id:
            if hasattr(self.promotion_plan_id, 'to_alipay_dict'):
                params['promotion_plan_id'] = self.promotion_plan_id.to_alipay_dict()
            else:
                params['promotion_plan_id'] = self.promotion_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantPayforprivilegePromotionplanQueryModel()
        if 'promotion_plan_id' in d:
            o.promotion_plan_id = d['promotion_plan_id']
        return o


