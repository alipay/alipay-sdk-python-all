#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleVO import RuleVO


class DatadigitalFincloudFinsaasInsuranceInstanceruleSaveModel(object):

    def __init__(self):
        self._instance_id = None
        self._out_tenant_id = None
        self._outer_product_id = None
        self._rule_items = None

    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def out_tenant_id(self):
        return self._out_tenant_id

    @out_tenant_id.setter
    def out_tenant_id(self, value):
        self._out_tenant_id = value
    @property
    def outer_product_id(self):
        return self._outer_product_id

    @outer_product_id.setter
    def outer_product_id(self, value):
        self._outer_product_id = value
    @property
    def rule_items(self):
        return self._rule_items

    @rule_items.setter
    def rule_items(self, value):
        if isinstance(value, list):
            self._rule_items = list()
            for i in value:
                if isinstance(i, RuleVO):
                    self._rule_items.append(i)
                else:
                    self._rule_items.append(RuleVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.out_tenant_id:
            if hasattr(self.out_tenant_id, 'to_alipay_dict'):
                params['out_tenant_id'] = self.out_tenant_id.to_alipay_dict()
            else:
                params['out_tenant_id'] = self.out_tenant_id
        if self.outer_product_id:
            if hasattr(self.outer_product_id, 'to_alipay_dict'):
                params['outer_product_id'] = self.outer_product_id.to_alipay_dict()
            else:
                params['outer_product_id'] = self.outer_product_id
        if self.rule_items:
            if isinstance(self.rule_items, list):
                for i in range(0, len(self.rule_items)):
                    element = self.rule_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_items[i] = element.to_alipay_dict()
            if hasattr(self.rule_items, 'to_alipay_dict'):
                params['rule_items'] = self.rule_items.to_alipay_dict()
            else:
                params['rule_items'] = self.rule_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasInsuranceInstanceruleSaveModel()
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'out_tenant_id' in d:
            o.out_tenant_id = d['out_tenant_id']
        if 'outer_product_id' in d:
            o.outer_product_id = d['outer_product_id']
        if 'rule_items' in d:
            o.rule_items = d['rule_items']
        return o


