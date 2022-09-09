#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneOpenprodPermissionAuthModel(object):

    def __init__(self):
        self._auth_type = None
        self._buyer = None
        self._item = None
        self._login_user_id = None
        self._out_session_expiration = None
        self._out_session_id = None
        self._partner_org_id = None
        self._seller = None

    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
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
    def login_user_id(self):
        return self._login_user_id

    @login_user_id.setter
    def login_user_id(self, value):
        self._login_user_id = value
    @property
    def out_session_expiration(self):
        return self._out_session_expiration

    @out_session_expiration.setter
    def out_session_expiration(self, value):
        self._out_session_expiration = value
    @property
    def out_session_id(self):
        return self._out_session_id

    @out_session_id.setter
    def out_session_id(self, value):
        self._out_session_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
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
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
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
        if self.login_user_id:
            if hasattr(self.login_user_id, 'to_alipay_dict'):
                params['login_user_id'] = self.login_user_id.to_alipay_dict()
            else:
                params['login_user_id'] = self.login_user_id
        if self.out_session_expiration:
            if hasattr(self.out_session_expiration, 'to_alipay_dict'):
                params['out_session_expiration'] = self.out_session_expiration.to_alipay_dict()
            else:
                params['out_session_expiration'] = self.out_session_expiration
        if self.out_session_id:
            if hasattr(self.out_session_id, 'to_alipay_dict'):
                params['out_session_id'] = self.out_session_id.to_alipay_dict()
            else:
                params['out_session_id'] = self.out_session_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
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
        o = AlipayInsSceneOpenprodPermissionAuthModel()
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'item' in d:
            o.item = d['item']
        if 'login_user_id' in d:
            o.login_user_id = d['login_user_id']
        if 'out_session_expiration' in d:
            o.out_session_expiration = d['out_session_expiration']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'seller' in d:
            o.seller = d['seller']
        return o


