#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringCommodityOrderBuyModel(object):

    def __init__(self):
        self._agent_id = None
        self._agent_type = None
        self._consumer_card_no = None
        self._merchandise_id = None
        self._shop_ids = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_type(self):
        return self._agent_type

    @agent_type.setter
    def agent_type(self, value):
        self._agent_type = value
    @property
    def consumer_card_no(self):
        return self._consumer_card_no

    @consumer_card_no.setter
    def consumer_card_no(self, value):
        self._consumer_card_no = value
    @property
    def merchandise_id(self):
        return self._merchandise_id

    @merchandise_id.setter
    def merchandise_id(self, value):
        self._merchandise_id = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_type:
            if hasattr(self.agent_type, 'to_alipay_dict'):
                params['agent_type'] = self.agent_type.to_alipay_dict()
            else:
                params['agent_type'] = self.agent_type
        if self.consumer_card_no:
            if hasattr(self.consumer_card_no, 'to_alipay_dict'):
                params['consumer_card_no'] = self.consumer_card_no.to_alipay_dict()
            else:
                params['consumer_card_no'] = self.consumer_card_no
        if self.merchandise_id:
            if hasattr(self.merchandise_id, 'to_alipay_dict'):
                params['merchandise_id'] = self.merchandise_id.to_alipay_dict()
            else:
                params['merchandise_id'] = self.merchandise_id
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringCommodityOrderBuyModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_type' in d:
            o.agent_type = d['agent_type']
        if 'consumer_card_no' in d:
            o.consumer_card_no = d['consumer_card_no']
        if 'merchandise_id' in d:
            o.merchandise_id = d['merchandise_id']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        return o


