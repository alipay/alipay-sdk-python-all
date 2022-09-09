#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO


class AlipayInsSceneEcommercePreorderquoteConsultModel(object):

    def __init__(self):
        self._order = None
        self._partner_org_id = None
        self._pre_order_id = None

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if isinstance(value, EcomOrderDTO):
            self._order = value
        else:
            self._order = EcomOrderDTO.from_alipay_dict(value)
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


    def to_alipay_dict(self):
        params = dict()
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommercePreorderquoteConsultModel()
        if 'order' in d:
            o.order = d['order']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


