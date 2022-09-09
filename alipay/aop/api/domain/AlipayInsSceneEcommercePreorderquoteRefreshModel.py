#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommercePreorderquoteRefreshModel(object):

    def __init__(self):
        self._buyer = None
        self._item = None
        self._order_dto = None
        self._partner_org_id = None
        self._pre_order_id = None
        self._seller = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, EcomBuyerDTO):
            self._buyer = value
        else:
            self._buyer = EcomBuyerDTO.from_alipay_dict(value)
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, EcomItemDTO):
            self._item = value
        else:
            self._item = EcomItemDTO.from_alipay_dict(value)
    @property
    def order_dto(self):
        return self._order_dto

    @order_dto.setter
    def order_dto(self, value):
        if isinstance(value, EcomOrderDTO):
            self._order_dto = value
        else:
            self._order_dto = EcomOrderDTO.from_alipay_dict(value)
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
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.order_dto:
            if hasattr(self.order_dto, 'to_alipay_dict'):
                params['order_dto'] = self.order_dto.to_alipay_dict()
            else:
                params['order_dto'] = self.order_dto
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
        o = AlipayInsSceneEcommercePreorderquoteRefreshModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'item' in d:
            o.item = d['item']
        if 'order_dto' in d:
            o.order_dto = d['order_dto']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'seller' in d:
            o.seller = d['seller']
        return o


