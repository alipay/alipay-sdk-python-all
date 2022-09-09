#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommercePurchaseRecommendModel(object):

    def __init__(self):
        self._authorized_token = None
        self._item = None
        self._partner_org_id = None
        self._related_subject_type = None
        self._scene_code = None
        self._seller = None
        self._user_client = None

    @property
    def authorized_token(self):
        return self._authorized_token

    @authorized_token.setter
    def authorized_token(self, value):
        self._authorized_token = value
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
    def related_subject_type(self):
        return self._related_subject_type

    @related_subject_type.setter
    def related_subject_type(self, value):
        self._related_subject_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
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
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_token:
            if hasattr(self.authorized_token, 'to_alipay_dict'):
                params['authorized_token'] = self.authorized_token.to_alipay_dict()
            else:
                params['authorized_token'] = self.authorized_token
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
        if self.related_subject_type:
            if hasattr(self.related_subject_type, 'to_alipay_dict'):
                params['related_subject_type'] = self.related_subject_type.to_alipay_dict()
            else:
                params['related_subject_type'] = self.related_subject_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
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
        o = AlipayInsSceneEcommercePurchaseRecommendModel()
        if 'authorized_token' in d:
            o.authorized_token = d['authorized_token']
        if 'item' in d:
            o.item = d['item']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'related_subject_type' in d:
            o.related_subject_type = d['related_subject_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'seller' in d:
            o.seller = d['seller']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


