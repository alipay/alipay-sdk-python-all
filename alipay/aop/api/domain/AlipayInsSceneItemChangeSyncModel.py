#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneItemChangeSyncModel(object):

    def __init__(self):
        self._item_list = None
        self._partner_org_id = None
        self._product_code = None
        self._purchase_contract_id = None
        self._seller = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, EcomItemDTO):
                    self._item_list.append(i)
                else:
                    self._item_list.append(EcomItemDTO.from_alipay_dict(i))
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def purchase_contract_id(self):
        return self._purchase_contract_id

    @purchase_contract_id.setter
    def purchase_contract_id(self, value):
        self._purchase_contract_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, EcomSellerDTO):
            self._seller = value
        else:
            self._seller = EcomSellerDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.purchase_contract_id:
            if hasattr(self.purchase_contract_id, 'to_alipay_dict'):
                params['purchase_contract_id'] = self.purchase_contract_id.to_alipay_dict()
            else:
                params['purchase_contract_id'] = self.purchase_contract_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneItemChangeSyncModel()
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'purchase_contract_id' in d:
            o.purchase_contract_id = d['purchase_contract_id']
        if 'seller' in d:
            o.seller = d['seller']
        return o


