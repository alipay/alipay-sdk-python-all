#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityGoodsBenefit import ActivityGoodsBenefit


class ActivityOperateContext(object):

    def __init__(self):
        self._activity_goods_benefit = None
        self._activity_status = None

    @property
    def activity_goods_benefit(self):
        return self._activity_goods_benefit

    @activity_goods_benefit.setter
    def activity_goods_benefit(self, value):
        if isinstance(value, ActivityGoodsBenefit):
            self._activity_goods_benefit = value
        else:
            self._activity_goods_benefit = ActivityGoodsBenefit.from_alipay_dict(value)
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_goods_benefit:
            if hasattr(self.activity_goods_benefit, 'to_alipay_dict'):
                params['activity_goods_benefit'] = self.activity_goods_benefit.to_alipay_dict()
            else:
                params['activity_goods_benefit'] = self.activity_goods_benefit
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityOperateContext()
        if 'activity_goods_benefit' in d:
            o.activity_goods_benefit = d['activity_goods_benefit']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        return o


