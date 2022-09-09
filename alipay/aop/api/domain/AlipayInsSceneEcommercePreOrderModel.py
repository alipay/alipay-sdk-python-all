#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.InsurePlanDTO import InsurePlanDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO
from alipay.aop.api.domain.InsUserTraceDTO import InsUserTraceDTO


class AlipayInsSceneEcommercePreOrderModel(object):

    def __init__(self):
        self._buyer = None
        self._check_quote = None
        self._insure_plan_dto = None
        self._item = None
        self._order_dto = None
        self._partner_org_id = None
        self._recommend_flow_id = None
        self._seller = None
        self._trace_list = None
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
    def check_quote(self):
        return self._check_quote

    @check_quote.setter
    def check_quote(self, value):
        self._check_quote = value
    @property
    def insure_plan_dto(self):
        return self._insure_plan_dto

    @insure_plan_dto.setter
    def insure_plan_dto(self, value):
        if isinstance(value, InsurePlanDTO):
            self._insure_plan_dto = value
        else:
            self._insure_plan_dto = InsurePlanDTO.from_alipay_dict(value)
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
    def trace_list(self):
        return self._trace_list

    @trace_list.setter
    def trace_list(self, value):
        if isinstance(value, list):
            self._trace_list = list()
            for i in value:
                if isinstance(i, InsUserTraceDTO):
                    self._trace_list.append(i)
                else:
                    self._trace_list.append(InsUserTraceDTO.from_alipay_dict(i))
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
        if self.check_quote:
            if hasattr(self.check_quote, 'to_alipay_dict'):
                params['check_quote'] = self.check_quote.to_alipay_dict()
            else:
                params['check_quote'] = self.check_quote
        if self.insure_plan_dto:
            if hasattr(self.insure_plan_dto, 'to_alipay_dict'):
                params['insure_plan_dto'] = self.insure_plan_dto.to_alipay_dict()
            else:
                params['insure_plan_dto'] = self.insure_plan_dto
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
        if self.trace_list:
            if isinstance(self.trace_list, list):
                for i in range(0, len(self.trace_list)):
                    element = self.trace_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trace_list[i] = element.to_alipay_dict()
            if hasattr(self.trace_list, 'to_alipay_dict'):
                params['trace_list'] = self.trace_list.to_alipay_dict()
            else:
                params['trace_list'] = self.trace_list
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
        o = AlipayInsSceneEcommercePreOrderModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'check_quote' in d:
            o.check_quote = d['check_quote']
        if 'insure_plan_dto' in d:
            o.insure_plan_dto = d['insure_plan_dto']
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
        if 'trace_list' in d:
            o.trace_list = d['trace_list']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


