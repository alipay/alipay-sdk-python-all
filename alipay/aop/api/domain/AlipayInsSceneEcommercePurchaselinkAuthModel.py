#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommercePurchaselinkAuthModel(object):

    def __init__(self):
        self._assign_withdraw_account_no = None
        self._at_least_days = None
        self._buyer = None
        self._ecom_item = None
        self._login_user_id = None
        self._out_session_expiration = None
        self._out_session_id = None
        self._partner_org_id = None
        self._product_code = None
        self._product_plan_ids = None
        self._purchase_user_type = None
        self._related_subject_type = None
        self._seller = None
        self._user_client = None

    @property
    def assign_withdraw_account_no(self):
        return self._assign_withdraw_account_no

    @assign_withdraw_account_no.setter
    def assign_withdraw_account_no(self, value):
        self._assign_withdraw_account_no = value
    @property
    def at_least_days(self):
        return self._at_least_days

    @at_least_days.setter
    def at_least_days(self, value):
        self._at_least_days = value
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
    def ecom_item(self):
        return self._ecom_item

    @ecom_item.setter
    def ecom_item(self, value):
        if isinstance(value, EcomItemDTO):
            self._ecom_item = value
        else:
            self._ecom_item = EcomItemDTO.from_alipay_dict(value)
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
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        if isinstance(value, list):
            self._product_code = list()
            for i in value:
                self._product_code.append(i)
    @property
    def product_plan_ids(self):
        return self._product_plan_ids

    @product_plan_ids.setter
    def product_plan_ids(self, value):
        if isinstance(value, list):
            self._product_plan_ids = list()
            for i in value:
                self._product_plan_ids.append(i)
    @property
    def purchase_user_type(self):
        return self._purchase_user_type

    @purchase_user_type.setter
    def purchase_user_type(self, value):
        self._purchase_user_type = value
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
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_withdraw_account_no:
            if hasattr(self.assign_withdraw_account_no, 'to_alipay_dict'):
                params['assign_withdraw_account_no'] = self.assign_withdraw_account_no.to_alipay_dict()
            else:
                params['assign_withdraw_account_no'] = self.assign_withdraw_account_no
        if self.at_least_days:
            if hasattr(self.at_least_days, 'to_alipay_dict'):
                params['at_least_days'] = self.at_least_days.to_alipay_dict()
            else:
                params['at_least_days'] = self.at_least_days
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.ecom_item:
            if hasattr(self.ecom_item, 'to_alipay_dict'):
                params['ecom_item'] = self.ecom_item.to_alipay_dict()
            else:
                params['ecom_item'] = self.ecom_item
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
        if self.product_code:
            if isinstance(self.product_code, list):
                for i in range(0, len(self.product_code)):
                    element = self.product_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_code[i] = element.to_alipay_dict()
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_plan_ids:
            if isinstance(self.product_plan_ids, list):
                for i in range(0, len(self.product_plan_ids)):
                    element = self.product_plan_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_plan_ids[i] = element.to_alipay_dict()
            if hasattr(self.product_plan_ids, 'to_alipay_dict'):
                params['product_plan_ids'] = self.product_plan_ids.to_alipay_dict()
            else:
                params['product_plan_ids'] = self.product_plan_ids
        if self.purchase_user_type:
            if hasattr(self.purchase_user_type, 'to_alipay_dict'):
                params['purchase_user_type'] = self.purchase_user_type.to_alipay_dict()
            else:
                params['purchase_user_type'] = self.purchase_user_type
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
        o = AlipayInsSceneEcommercePurchaselinkAuthModel()
        if 'assign_withdraw_account_no' in d:
            o.assign_withdraw_account_no = d['assign_withdraw_account_no']
        if 'at_least_days' in d:
            o.at_least_days = d['at_least_days']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'ecom_item' in d:
            o.ecom_item = d['ecom_item']
        if 'login_user_id' in d:
            o.login_user_id = d['login_user_id']
        if 'out_session_expiration' in d:
            o.out_session_expiration = d['out_session_expiration']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_plan_ids' in d:
            o.product_plan_ids = d['product_plan_ids']
        if 'purchase_user_type' in d:
            o.purchase_user_type = d['purchase_user_type']
        if 'related_subject_type' in d:
            o.related_subject_type = d['related_subject_type']
        if 'seller' in d:
            o.seller = d['seller']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


