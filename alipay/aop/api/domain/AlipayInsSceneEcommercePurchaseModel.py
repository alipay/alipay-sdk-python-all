#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.PurchaseInsurePlanDTO import PurchaseInsurePlanDTO
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommercePurchaseModel(object):

    def __init__(self):
        self._biz_data = None
        self._check_quote = None
        self._effect_time = None
        self._end_time = None
        self._item = None
        self._partner_org_id = None
        self._purchase_insure_plan_dto = None
        self._recommend_flow_id = None
        self._renew = None
        self._renew_period = None
        self._seller = None
        self._total_amount = None
        self._user_client = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def check_quote(self):
        return self._check_quote

    @check_quote.setter
    def check_quote(self, value):
        self._check_quote = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def purchase_insure_plan_dto(self):
        return self._purchase_insure_plan_dto

    @purchase_insure_plan_dto.setter
    def purchase_insure_plan_dto(self, value):
        if isinstance(value, PurchaseInsurePlanDTO):
            self._purchase_insure_plan_dto = value
        else:
            self._purchase_insure_plan_dto = PurchaseInsurePlanDTO.from_alipay_dict(value)
    @property
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value
    @property
    def renew(self):
        return self._renew

    @renew.setter
    def renew(self, value):
        self._renew = value
    @property
    def renew_period(self):
        return self._renew_period

    @renew_period.setter
    def renew_period(self, value):
        if isinstance(value, InsPeriodDTO):
            self._renew_period = value
        else:
            self._renew_period = InsPeriodDTO.from_alipay_dict(value)
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
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.check_quote:
            if hasattr(self.check_quote, 'to_alipay_dict'):
                params['check_quote'] = self.check_quote.to_alipay_dict()
            else:
                params['check_quote'] = self.check_quote
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.purchase_insure_plan_dto:
            if hasattr(self.purchase_insure_plan_dto, 'to_alipay_dict'):
                params['purchase_insure_plan_dto'] = self.purchase_insure_plan_dto.to_alipay_dict()
            else:
                params['purchase_insure_plan_dto'] = self.purchase_insure_plan_dto
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
        if self.renew:
            if hasattr(self.renew, 'to_alipay_dict'):
                params['renew'] = self.renew.to_alipay_dict()
            else:
                params['renew'] = self.renew
        if self.renew_period:
            if hasattr(self.renew_period, 'to_alipay_dict'):
                params['renew_period'] = self.renew_period.to_alipay_dict()
            else:
                params['renew_period'] = self.renew_period
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        o = AlipayInsSceneEcommercePurchaseModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'check_quote' in d:
            o.check_quote = d['check_quote']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'item' in d:
            o.item = d['item']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'purchase_insure_plan_dto' in d:
            o.purchase_insure_plan_dto = d['purchase_insure_plan_dto']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        if 'renew' in d:
            o.renew = d['renew']
        if 'renew_period' in d:
            o.renew_period = d['renew_period']
        if 'seller' in d:
            o.seller = d['seller']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


