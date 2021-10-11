#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchProductOrientedRuleOpenApi import SearchProductOrientedRuleOpenApi
from alipay.aop.api.domain.SearchProductPeriod import SearchProductPeriod
from alipay.aop.api.domain.SearchProductRegion import SearchProductRegion


class SearchBoxExclusiveMarketingInfoRequest(object):

    def __init__(self):
        self._action = None
        self._action_type = None
        self._action_url = None
        self._applier_id = None
        self._brand_id = None
        self._item_id = None
        self._material_link = None
        self._material_type = None
        self._oriented_rules = None
        self._serv_code = None
        self._target_period = None
        self._target_region = None
        self._title = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def applier_id(self):
        return self._applier_id

    @applier_id.setter
    def applier_id(self, value):
        self._applier_id = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def material_link(self):
        return self._material_link

    @material_link.setter
    def material_link(self, value):
        self._material_link = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def oriented_rules(self):
        return self._oriented_rules

    @oriented_rules.setter
    def oriented_rules(self, value):
        if isinstance(value, SearchProductOrientedRuleOpenApi):
            self._oriented_rules = value
        else:
            self._oriented_rules = SearchProductOrientedRuleOpenApi.from_alipay_dict(value)
    @property
    def serv_code(self):
        return self._serv_code

    @serv_code.setter
    def serv_code(self, value):
        self._serv_code = value
    @property
    def target_period(self):
        return self._target_period

    @target_period.setter
    def target_period(self, value):
        if isinstance(value, SearchProductPeriod):
            self._target_period = value
        else:
            self._target_period = SearchProductPeriod.from_alipay_dict(value)
    @property
    def target_region(self):
        return self._target_region

    @target_region.setter
    def target_region(self, value):
        if isinstance(value, list):
            self._target_region = list()
            for i in value:
                if isinstance(i, SearchProductRegion):
                    self._target_region.append(i)
                else:
                    self._target_region.append(SearchProductRegion.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.applier_id:
            if hasattr(self.applier_id, 'to_alipay_dict'):
                params['applier_id'] = self.applier_id.to_alipay_dict()
            else:
                params['applier_id'] = self.applier_id
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.material_link:
            if hasattr(self.material_link, 'to_alipay_dict'):
                params['material_link'] = self.material_link.to_alipay_dict()
            else:
                params['material_link'] = self.material_link
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.oriented_rules:
            if hasattr(self.oriented_rules, 'to_alipay_dict'):
                params['oriented_rules'] = self.oriented_rules.to_alipay_dict()
            else:
                params['oriented_rules'] = self.oriented_rules
        if self.serv_code:
            if hasattr(self.serv_code, 'to_alipay_dict'):
                params['serv_code'] = self.serv_code.to_alipay_dict()
            else:
                params['serv_code'] = self.serv_code
        if self.target_period:
            if hasattr(self.target_period, 'to_alipay_dict'):
                params['target_period'] = self.target_period.to_alipay_dict()
            else:
                params['target_period'] = self.target_period
        if self.target_region:
            if isinstance(self.target_region, list):
                for i in range(0, len(self.target_region)):
                    element = self.target_region[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_region[i] = element.to_alipay_dict()
            if hasattr(self.target_region, 'to_alipay_dict'):
                params['target_region'] = self.target_region.to_alipay_dict()
            else:
                params['target_region'] = self.target_region
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxExclusiveMarketingInfoRequest()
        if 'action' in d:
            o.action = d['action']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'applier_id' in d:
            o.applier_id = d['applier_id']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'material_link' in d:
            o.material_link = d['material_link']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'oriented_rules' in d:
            o.oriented_rules = d['oriented_rules']
        if 'serv_code' in d:
            o.serv_code = d['serv_code']
        if 'target_period' in d:
            o.target_period = d['target_period']
        if 'target_region' in d:
            o.target_region = d['target_region']
        if 'title' in d:
            o.title = d['title']
        return o


