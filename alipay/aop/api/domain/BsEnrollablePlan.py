#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsBrandPlanDetail import BsBrandPlanDetail
from alipay.aop.api.domain.BsSupplyInfo import BsSupplyInfo


class BsEnrollablePlan(object):

    def __init__(self):
        self._plan_detail = None
        self._supply_info_list = None

    @property
    def plan_detail(self):
        return self._plan_detail

    @plan_detail.setter
    def plan_detail(self, value):
        if isinstance(value, BsBrandPlanDetail):
            self._plan_detail = value
        else:
            self._plan_detail = BsBrandPlanDetail.from_alipay_dict(value)
    @property
    def supply_info_list(self):
        return self._supply_info_list

    @supply_info_list.setter
    def supply_info_list(self, value):
        if isinstance(value, list):
            self._supply_info_list = list()
            for i in value:
                if isinstance(i, BsSupplyInfo):
                    self._supply_info_list.append(i)
                else:
                    self._supply_info_list.append(BsSupplyInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.plan_detail:
            if hasattr(self.plan_detail, 'to_alipay_dict'):
                params['plan_detail'] = self.plan_detail.to_alipay_dict()
            else:
                params['plan_detail'] = self.plan_detail
        if self.supply_info_list:
            if isinstance(self.supply_info_list, list):
                for i in range(0, len(self.supply_info_list)):
                    element = self.supply_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supply_info_list[i] = element.to_alipay_dict()
            if hasattr(self.supply_info_list, 'to_alipay_dict'):
                params['supply_info_list'] = self.supply_info_list.to_alipay_dict()
            else:
                params['supply_info_list'] = self.supply_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsEnrollablePlan()
        if 'plan_detail' in d:
            o.plan_detail = d['plan_detail']
        if 'supply_info_list' in d:
            o.supply_info_list = d['supply_info_list']
        return o


