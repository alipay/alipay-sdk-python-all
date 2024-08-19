#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO
from alipay.aop.api.domain.InviteMemberBusinessParamsDTO import InviteMemberBusinessParamsDTO
from alipay.aop.api.domain.IdentityVerifiedInfoDTO import IdentityVerifiedInfoDTO


class AlipayFundJointaccountMemberBindModel(object):

    def __init__(self):
        self._account_id = None
        self._account_quota = None
        self._agreement_no = None
        self._agreement_sign_info = None
        self._biz_scene = None
        self._business_params = None
        self._identity = None
        self._identity_type = None
        self._identity_verified_info = None
        self._name = None
        self._product_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_quota(self):
        return self._account_quota

    @account_quota.setter
    def account_quota(self, value):
        if isinstance(value, JointAccountQuotaDTO):
            self._account_quota = value
        else:
            self._account_quota = JointAccountQuotaDTO.from_alipay_dict(value)
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_sign_info(self):
        return self._agreement_sign_info

    @agreement_sign_info.setter
    def agreement_sign_info(self, value):
        self._agreement_sign_info = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, InviteMemberBusinessParamsDTO):
            self._business_params = value
        else:
            self._business_params = InviteMemberBusinessParamsDTO.from_alipay_dict(value)
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def identity_verified_info(self):
        return self._identity_verified_info

    @identity_verified_info.setter
    def identity_verified_info(self, value):
        if isinstance(value, IdentityVerifiedInfoDTO):
            self._identity_verified_info = value
        else:
            self._identity_verified_info = IdentityVerifiedInfoDTO.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_quota:
            if hasattr(self.account_quota, 'to_alipay_dict'):
                params['account_quota'] = self.account_quota.to_alipay_dict()
            else:
                params['account_quota'] = self.account_quota
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_sign_info:
            if hasattr(self.agreement_sign_info, 'to_alipay_dict'):
                params['agreement_sign_info'] = self.agreement_sign_info.to_alipay_dict()
            else:
                params['agreement_sign_info'] = self.agreement_sign_info
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.identity_verified_info:
            if hasattr(self.identity_verified_info, 'to_alipay_dict'):
                params['identity_verified_info'] = self.identity_verified_info.to_alipay_dict()
            else:
                params['identity_verified_info'] = self.identity_verified_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountMemberBindModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_quota' in d:
            o.account_quota = d['account_quota']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_sign_info' in d:
            o.agreement_sign_info = d['agreement_sign_info']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'identity_verified_info' in d:
            o.identity_verified_info = d['identity_verified_info']
        if 'name' in d:
            o.name = d['name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


