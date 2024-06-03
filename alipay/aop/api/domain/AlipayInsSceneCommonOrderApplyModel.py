#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO


class AlipayInsSceneCommonOrderApplyModel(object):

    def __init__(self):
        self._biz_time = None
        self._holder_user = None
        self._insured_user = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._pre_order_id = None
        self._product_plan_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def holder_user(self):
        return self._holder_user

    @holder_user.setter
    def holder_user(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._holder_user = value
        else:
            self._holder_user = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def insured_user(self):
        return self._insured_user

    @insured_user.setter
    def insured_user(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._insured_user = value
        else:
            self._insured_user = InsOpenUserDTO.from_alipay_dict(value)
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
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.holder_user:
            if hasattr(self.holder_user, 'to_alipay_dict'):
                params['holder_user'] = self.holder_user.to_alipay_dict()
            else:
                params['holder_user'] = self.holder_user
        if self.insured_user:
            if hasattr(self.insured_user, 'to_alipay_dict'):
                params['insured_user'] = self.insured_user.to_alipay_dict()
            else:
                params['insured_user'] = self.insured_user
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
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCommonOrderApplyModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'holder_user' in d:
            o.holder_user = d['holder_user']
        if 'insured_user' in d:
            o.insured_user = d['insured_user']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        return o


