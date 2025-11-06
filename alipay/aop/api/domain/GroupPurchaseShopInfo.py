#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupPurchaseBankCard import GroupPurchaseBankCard
from alipay.aop.api.domain.CategoryQualificationCombineInfo import CategoryQualificationCombineInfo
from alipay.aop.api.domain.GroupPurchaseSettleInfo import GroupPurchaseSettleInfo
from alipay.aop.api.domain.GroupPurchaseShopModel import GroupPurchaseShopModel


class GroupPurchaseShopInfo(object):

    def __init__(self):
        self._bank_cards = None
        self._brand_id = None
        self._business_type = None
        self._contact_mobile = None
        self._main_business_category = None
        self._operate_type = None
        self._qualification_combines = None
        self._settle_infos = None
        self._shop_models = None
        self._store_id = None
        self._store_name = None
        self._store_type = None

    @property
    def bank_cards(self):
        return self._bank_cards

    @bank_cards.setter
    def bank_cards(self, value):
        if isinstance(value, list):
            self._bank_cards = list()
            for i in value:
                if isinstance(i, GroupPurchaseBankCard):
                    self._bank_cards.append(i)
                else:
                    self._bank_cards.append(GroupPurchaseBankCard.from_alipay_dict(i))
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def main_business_category(self):
        return self._main_business_category

    @main_business_category.setter
    def main_business_category(self, value):
        if isinstance(value, list):
            self._main_business_category = list()
            for i in value:
                self._main_business_category.append(i)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def qualification_combines(self):
        return self._qualification_combines

    @qualification_combines.setter
    def qualification_combines(self, value):
        if isinstance(value, list):
            self._qualification_combines = list()
            for i in value:
                if isinstance(i, CategoryQualificationCombineInfo):
                    self._qualification_combines.append(i)
                else:
                    self._qualification_combines.append(CategoryQualificationCombineInfo.from_alipay_dict(i))
    @property
    def settle_infos(self):
        return self._settle_infos

    @settle_infos.setter
    def settle_infos(self, value):
        if isinstance(value, list):
            self._settle_infos = list()
            for i in value:
                if isinstance(i, GroupPurchaseSettleInfo):
                    self._settle_infos.append(i)
                else:
                    self._settle_infos.append(GroupPurchaseSettleInfo.from_alipay_dict(i))
    @property
    def shop_models(self):
        return self._shop_models

    @shop_models.setter
    def shop_models(self, value):
        if isinstance(value, list):
            self._shop_models = list()
            for i in value:
                if isinstance(i, GroupPurchaseShopModel):
                    self._shop_models.append(i)
                else:
                    self._shop_models.append(GroupPurchaseShopModel.from_alipay_dict(i))
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_type(self):
        return self._store_type

    @store_type.setter
    def store_type(self, value):
        self._store_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_cards:
            if isinstance(self.bank_cards, list):
                for i in range(0, len(self.bank_cards)):
                    element = self.bank_cards[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_cards[i] = element.to_alipay_dict()
            if hasattr(self.bank_cards, 'to_alipay_dict'):
                params['bank_cards'] = self.bank_cards.to_alipay_dict()
            else:
                params['bank_cards'] = self.bank_cards
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.main_business_category:
            if isinstance(self.main_business_category, list):
                for i in range(0, len(self.main_business_category)):
                    element = self.main_business_category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.main_business_category[i] = element.to_alipay_dict()
            if hasattr(self.main_business_category, 'to_alipay_dict'):
                params['main_business_category'] = self.main_business_category.to_alipay_dict()
            else:
                params['main_business_category'] = self.main_business_category
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.qualification_combines:
            if isinstance(self.qualification_combines, list):
                for i in range(0, len(self.qualification_combines)):
                    element = self.qualification_combines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualification_combines[i] = element.to_alipay_dict()
            if hasattr(self.qualification_combines, 'to_alipay_dict'):
                params['qualification_combines'] = self.qualification_combines.to_alipay_dict()
            else:
                params['qualification_combines'] = self.qualification_combines
        if self.settle_infos:
            if isinstance(self.settle_infos, list):
                for i in range(0, len(self.settle_infos)):
                    element = self.settle_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_infos[i] = element.to_alipay_dict()
            if hasattr(self.settle_infos, 'to_alipay_dict'):
                params['settle_infos'] = self.settle_infos.to_alipay_dict()
            else:
                params['settle_infos'] = self.settle_infos
        if self.shop_models:
            if isinstance(self.shop_models, list):
                for i in range(0, len(self.shop_models)):
                    element = self.shop_models[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_models[i] = element.to_alipay_dict()
            if hasattr(self.shop_models, 'to_alipay_dict'):
                params['shop_models'] = self.shop_models.to_alipay_dict()
            else:
                params['shop_models'] = self.shop_models
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_type:
            if hasattr(self.store_type, 'to_alipay_dict'):
                params['store_type'] = self.store_type.to_alipay_dict()
            else:
                params['store_type'] = self.store_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPurchaseShopInfo()
        if 'bank_cards' in d:
            o.bank_cards = d['bank_cards']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'main_business_category' in d:
            o.main_business_category = d['main_business_category']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'qualification_combines' in d:
            o.qualification_combines = d['qualification_combines']
        if 'settle_infos' in d:
            o.settle_infos = d['settle_infos']
        if 'shop_models' in d:
            o.shop_models = d['shop_models']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_type' in d:
            o.store_type = d['store_type']
        return o


