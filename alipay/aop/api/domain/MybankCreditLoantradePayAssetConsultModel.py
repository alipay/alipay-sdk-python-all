#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayUserVO import CreditPayUserVO


class MybankCreditLoantradePayAssetConsultModel(object):

    def __init__(self):
        self._alipay_partner_id = None
        self._apply_amt = None
        self._biz_scene = None
        self._credit_asset_types = None
        self._order_infos = None
        self._payment_sale_pd_code = None
        self._platform_type = None
        self._sub_biz_scene = None
        self._sub_platform_type = None
        self._user = None

    @property
    def alipay_partner_id(self):
        return self._alipay_partner_id

    @alipay_partner_id.setter
    def alipay_partner_id(self, value):
        self._alipay_partner_id = value
    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._apply_amt = value
        else:
            self._apply_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def credit_asset_types(self):
        return self._credit_asset_types

    @credit_asset_types.setter
    def credit_asset_types(self, value):
        if isinstance(value, list):
            self._credit_asset_types = list()
            for i in value:
                self._credit_asset_types.append(i)
    @property
    def order_infos(self):
        return self._order_infos

    @order_infos.setter
    def order_infos(self, value):
        self._order_infos = value
    @property
    def payment_sale_pd_code(self):
        return self._payment_sale_pd_code

    @payment_sale_pd_code.setter
    def payment_sale_pd_code(self, value):
        self._payment_sale_pd_code = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def sub_platform_type(self):
        return self._sub_platform_type

    @sub_platform_type.setter
    def sub_platform_type(self, value):
        self._sub_platform_type = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, CreditPayUserVO):
            self._user = value
        else:
            self._user = CreditPayUserVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_partner_id:
            if hasattr(self.alipay_partner_id, 'to_alipay_dict'):
                params['alipay_partner_id'] = self.alipay_partner_id.to_alipay_dict()
            else:
                params['alipay_partner_id'] = self.alipay_partner_id
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.credit_asset_types:
            if isinstance(self.credit_asset_types, list):
                for i in range(0, len(self.credit_asset_types)):
                    element = self.credit_asset_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_asset_types[i] = element.to_alipay_dict()
            if hasattr(self.credit_asset_types, 'to_alipay_dict'):
                params['credit_asset_types'] = self.credit_asset_types.to_alipay_dict()
            else:
                params['credit_asset_types'] = self.credit_asset_types
        if self.order_infos:
            if hasattr(self.order_infos, 'to_alipay_dict'):
                params['order_infos'] = self.order_infos.to_alipay_dict()
            else:
                params['order_infos'] = self.order_infos
        if self.payment_sale_pd_code:
            if hasattr(self.payment_sale_pd_code, 'to_alipay_dict'):
                params['payment_sale_pd_code'] = self.payment_sale_pd_code.to_alipay_dict()
            else:
                params['payment_sale_pd_code'] = self.payment_sale_pd_code
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.sub_platform_type:
            if hasattr(self.sub_platform_type, 'to_alipay_dict'):
                params['sub_platform_type'] = self.sub_platform_type.to_alipay_dict()
            else:
                params['sub_platform_type'] = self.sub_platform_type
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradePayAssetConsultModel()
        if 'alipay_partner_id' in d:
            o.alipay_partner_id = d['alipay_partner_id']
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'credit_asset_types' in d:
            o.credit_asset_types = d['credit_asset_types']
        if 'order_infos' in d:
            o.order_infos = d['order_infos']
        if 'payment_sale_pd_code' in d:
            o.payment_sale_pd_code = d['payment_sale_pd_code']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'sub_platform_type' in d:
            o.sub_platform_type = d['sub_platform_type']
        if 'user' in d:
            o.user = d['user']
        return o


