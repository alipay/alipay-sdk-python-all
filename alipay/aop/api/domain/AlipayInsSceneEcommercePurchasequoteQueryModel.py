#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommercePurchasequoteQueryModel(object):

    def __init__(self):
        self._item = None
        self._partner_org_id = None
        self._quote_scope = None
        self._related_subject_type = None
        self._seller = None

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
    def quote_scope(self):
        return self._quote_scope

    @quote_scope.setter
    def quote_scope(self, value):
        self._quote_scope = value
    @property
    def related_subject_type(self):
        return self._related_subject_type

    @related_subject_type.setter
    def related_subject_type(self, value):
        self._related_subject_type = value
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
        if self.quote_scope:
            if hasattr(self.quote_scope, 'to_alipay_dict'):
                params['quote_scope'] = self.quote_scope.to_alipay_dict()
            else:
                params['quote_scope'] = self.quote_scope
        if self.related_subject_type:
            if hasattr(self.related_subject_type, 'to_alipay_dict'):
                params['related_subject_type'] = self.related_subject_type.to_alipay_dict()
            else:
                params['related_subject_type'] = self.related_subject_type
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
        o = AlipayInsSceneEcommercePurchasequoteQueryModel()
        if 'item' in d:
            o.item = d['item']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'quote_scope' in d:
            o.quote_scope = d['quote_scope']
        if 'related_subject_type' in d:
            o.related_subject_type = d['related_subject_type']
        if 'seller' in d:
            o.seller = d['seller']
        return o


