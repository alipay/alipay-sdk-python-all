#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LivePlaySecurityPocketInfo import LivePlaySecurityPocketInfo


class AlipayContentLivePlaySecuritySubmitModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._domain = None
        self._out_biz_id = None
        self._pocket_item_list = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def pocket_item_list(self):
        return self._pocket_item_list

    @pocket_item_list.setter
    def pocket_item_list(self, value):
        if isinstance(value, list):
            self._pocket_item_list = list()
            for i in value:
                if isinstance(i, LivePlaySecurityPocketInfo):
                    self._pocket_item_list.append(i)
                else:
                    self._pocket_item_list.append(LivePlaySecurityPocketInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.pocket_item_list:
            if isinstance(self.pocket_item_list, list):
                for i in range(0, len(self.pocket_item_list)):
                    element = self.pocket_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pocket_item_list[i] = element.to_alipay_dict()
            if hasattr(self.pocket_item_list, 'to_alipay_dict'):
                params['pocket_item_list'] = self.pocket_item_list.to_alipay_dict()
            else:
                params['pocket_item_list'] = self.pocket_item_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLivePlaySecuritySubmitModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'domain' in d:
            o.domain = d['domain']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'pocket_item_list' in d:
            o.pocket_item_list = d['pocket_item_list']
        return o


