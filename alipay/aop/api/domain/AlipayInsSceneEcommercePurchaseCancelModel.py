#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneEcommercePurchaseCancelModel(object):

    def __init__(self):
        self._partner_org_id = None
        self._purchase_contract_id = None
        self._seller_id = None

    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def purchase_contract_id(self):
        return self._purchase_contract_id

    @purchase_contract_id.setter
    def purchase_contract_id(self, value):
        self._purchase_contract_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.purchase_contract_id:
            if hasattr(self.purchase_contract_id, 'to_alipay_dict'):
                params['purchase_contract_id'] = self.purchase_contract_id.to_alipay_dict()
            else:
                params['purchase_contract_id'] = self.purchase_contract_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommercePurchaseCancelModel()
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'purchase_contract_id' in d:
            o.purchase_contract_id = d['purchase_contract_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        return o


