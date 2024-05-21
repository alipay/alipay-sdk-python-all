#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommerceInsurequoteConsultModel(object):

    def __init__(self):
        self._buyer = None
        self._ins_period = None
        self._item = None
        self._order_dto = None
        self._partner_org_id = None
        self._recommend_flow_id = None
        self._seller = None
        self._sum_insured = None
        self._user_client = None

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
    def ins_period(self):
        return self._ins_period

    @ins_period.setter
    def ins_period(self, value):
        if isinstance(value, InsPeriodDTO):
            self._ins_period = value
        else:
            self._ins_period = InsPeriodDTO.from_alipay_dict(value)
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
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, EcomSellerDTO):
            self._seller = value
        else:
            self._seller = EcomSellerDTO.from_alipay_dict(value)
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.ins_period:
            if hasattr(self.ins_period, 'to_alipay_dict'):
                params['ins_period'] = self.ins_period.to_alipay_dict()
            else:
                params['ins_period'] = self.ins_period
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
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.user_client:
            if hasattr(self.user_client, 'to_alipay_dict'):
                params['user_client'] = self.user_client.to_alipay_dict()
            else:
                params['user_client'] = self.user_client
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommerceInsurequoteConsultModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'ins_period' in d:
            o.ins_period = d['ins_period']
        if 'item' in d:
            o.item = d['item']
        if 'order_dto' in d:
            o.order_dto = d['order_dto']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        if 'seller' in d:
            o.seller = d['seller']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


