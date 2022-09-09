#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneEcommercePreorderQueryModel(object):

    def __init__(self):
        self._order_id = None
        self._partner_org_id = None
        self._pre_order_ids = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def pre_order_ids(self):
        return self._pre_order_ids

    @pre_order_ids.setter
    def pre_order_ids(self, value):
        if isinstance(value, list):
            self._pre_order_ids = list()
            for i in value:
                self._pre_order_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.pre_order_ids:
            if isinstance(self.pre_order_ids, list):
                for i in range(0, len(self.pre_order_ids)):
                    element = self.pre_order_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pre_order_ids[i] = element.to_alipay_dict()
            if hasattr(self.pre_order_ids, 'to_alipay_dict'):
                params['pre_order_ids'] = self.pre_order_ids.to_alipay_dict()
            else:
                params['pre_order_ids'] = self.pre_order_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommercePreorderQueryModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pre_order_ids' in d:
            o.pre_order_ids = d['pre_order_ids']
        return o


