#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LeaseSkuSubmitDTO import LeaseSkuSubmitDTO


class AlipayCommerceLeaseEnrollSubmitModel(object):

    def __init__(self):
        self._plan_id = None
        self._sku_submit_list = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def sku_submit_list(self):
        return self._sku_submit_list

    @sku_submit_list.setter
    def sku_submit_list(self, value):
        if isinstance(value, list):
            self._sku_submit_list = list()
            for i in value:
                if isinstance(i, LeaseSkuSubmitDTO):
                    self._sku_submit_list.append(i)
                else:
                    self._sku_submit_list.append(LeaseSkuSubmitDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.sku_submit_list:
            if isinstance(self.sku_submit_list, list):
                for i in range(0, len(self.sku_submit_list)):
                    element = self.sku_submit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_submit_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_submit_list, 'to_alipay_dict'):
                params['sku_submit_list'] = self.sku_submit_list.to_alipay_dict()
            else:
                params['sku_submit_list'] = self.sku_submit_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLeaseEnrollSubmitModel()
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'sku_submit_list' in d:
            o.sku_submit_list = d['sku_submit_list']
        return o


