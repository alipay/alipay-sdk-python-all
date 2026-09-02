#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenSimplestIssueCustomParamDTO import InsOpenSimplestIssueCustomParamDTO
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO


class AlipayInsSceneSimplestPolicyApplyModel(object):

    def __init__(self):
        self._custom_param = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._holder = None
        self._insureds = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._period = None
        self._product_plan_id = None
        self._scene_code = None

    @property
    def custom_param(self):
        return self._custom_param

    @custom_param.setter
    def custom_param(self, value):
        if isinstance(value, InsOpenSimplestIssueCustomParamDTO):
            self._custom_param = value
        else:
            self._custom_param = InsOpenSimplestIssueCustomParamDTO.from_alipay_dict(value)
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._holder = value
        else:
            self._holder = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def insureds(self):
        return self._insureds

    @insureds.setter
    def insureds(self, value):
        if isinstance(value, list):
            self._insureds = list()
            for i in value:
                if isinstance(i, InsOpenUserDTO):
                    self._insureds.append(i)
                else:
                    self._insureds.append(InsOpenUserDTO.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_param:
            if hasattr(self.custom_param, 'to_alipay_dict'):
                params['custom_param'] = self.custom_param.to_alipay_dict()
            else:
                params['custom_param'] = self.custom_param
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.holder:
            if hasattr(self.holder, 'to_alipay_dict'):
                params['holder'] = self.holder.to_alipay_dict()
            else:
                params['holder'] = self.holder
        if self.insureds:
            if isinstance(self.insureds, list):
                for i in range(0, len(self.insureds)):
                    element = self.insureds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insureds[i] = element.to_alipay_dict()
            if hasattr(self.insureds, 'to_alipay_dict'):
                params['insureds'] = self.insureds.to_alipay_dict()
            else:
                params['insureds'] = self.insureds
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneSimplestPolicyApplyModel()
        if 'custom_param' in d:
            o.custom_param = d['custom_param']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'holder' in d:
            o.holder = d['holder']
        if 'insureds' in d:
            o.insureds = d['insureds']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'period' in d:
            o.period = d['period']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


