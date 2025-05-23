#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdcampaignGroupBatchqueryModel(object):

    def __init__(self):
        self._bid_type = None
        self._current = None
        self._first_market_target_code = None
        self._group_status_list = None
        self._market_target_code = None
        self._page_size = None
        self._plan_id = None
        self._principal_tag = None
        self._scene_code = None
        self._search_keywords = None

    @property
    def bid_type(self):
        return self._bid_type

    @bid_type.setter
    def bid_type(self, value):
        self._bid_type = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def first_market_target_code(self):
        return self._first_market_target_code

    @first_market_target_code.setter
    def first_market_target_code(self, value):
        self._first_market_target_code = value
    @property
    def group_status_list(self):
        return self._group_status_list

    @group_status_list.setter
    def group_status_list(self, value):
        if isinstance(value, list):
            self._group_status_list = list()
            for i in value:
                self._group_status_list.append(i)
    @property
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def search_keywords(self):
        return self._search_keywords

    @search_keywords.setter
    def search_keywords(self, value):
        self._search_keywords = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid_type:
            if hasattr(self.bid_type, 'to_alipay_dict'):
                params['bid_type'] = self.bid_type.to_alipay_dict()
            else:
                params['bid_type'] = self.bid_type
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.first_market_target_code:
            if hasattr(self.first_market_target_code, 'to_alipay_dict'):
                params['first_market_target_code'] = self.first_market_target_code.to_alipay_dict()
            else:
                params['first_market_target_code'] = self.first_market_target_code
        if self.group_status_list:
            if isinstance(self.group_status_list, list):
                for i in range(0, len(self.group_status_list)):
                    element = self.group_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_status_list[i] = element.to_alipay_dict()
            if hasattr(self.group_status_list, 'to_alipay_dict'):
                params['group_status_list'] = self.group_status_list.to_alipay_dict()
            else:
                params['group_status_list'] = self.group_status_list
        if self.market_target_code:
            if hasattr(self.market_target_code, 'to_alipay_dict'):
                params['market_target_code'] = self.market_target_code.to_alipay_dict()
            else:
                params['market_target_code'] = self.market_target_code
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.search_keywords:
            if hasattr(self.search_keywords, 'to_alipay_dict'):
                params['search_keywords'] = self.search_keywords.to_alipay_dict()
            else:
                params['search_keywords'] = self.search_keywords
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdcampaignGroupBatchqueryModel()
        if 'bid_type' in d:
            o.bid_type = d['bid_type']
        if 'current' in d:
            o.current = d['current']
        if 'first_market_target_code' in d:
            o.first_market_target_code = d['first_market_target_code']
        if 'group_status_list' in d:
            o.group_status_list = d['group_status_list']
        if 'market_target_code' in d:
            o.market_target_code = d['market_target_code']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'search_keywords' in d:
            o.search_keywords = d['search_keywords']
        return o


