#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTuitioncodeOrderdetailQueryModel(object):

    def __init__(self):
        self._include_plans = None
        self._out_order_no = None
        self._scene = None
        self._smid = None

    @property
    def include_plans(self):
        return self._include_plans

    @include_plans.setter
    def include_plans(self, value):
        self._include_plans = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.include_plans:
            if hasattr(self.include_plans, 'to_alipay_dict'):
                params['include_plans'] = self.include_plans.to_alipay_dict()
            else:
                params['include_plans'] = self.include_plans
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTuitioncodeOrderdetailQueryModel()
        if 'include_plans' in d:
            o.include_plans = d['include_plans']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'smid' in d:
            o.smid = d['smid']
        return o


