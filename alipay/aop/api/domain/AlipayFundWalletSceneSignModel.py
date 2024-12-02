#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WalletMarketingRule import WalletMarketingRule
from alipay.aop.api.domain.WalletUserIdentityInfo import WalletUserIdentityInfo


class AlipayFundWalletSceneSignModel(object):

    def __init__(self):
        self._biz_scene = None
        self._need_check_identity = None
        self._out_biz_no = None
        self._principal_open_id = None
        self._product_code = None
        self._user_id = None
        self._wallet_marketing_rule = None
        self._wallet_template_id = None
        self._wallet_user_identity_info = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def need_check_identity(self):
        return self._need_check_identity

    @need_check_identity.setter
    def need_check_identity(self, value):
        self._need_check_identity = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_open_id(self):
        return self._principal_open_id

    @principal_open_id.setter
    def principal_open_id(self, value):
        self._principal_open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def wallet_marketing_rule(self):
        return self._wallet_marketing_rule

    @wallet_marketing_rule.setter
    def wallet_marketing_rule(self, value):
        if isinstance(value, WalletMarketingRule):
            self._wallet_marketing_rule = value
        else:
            self._wallet_marketing_rule = WalletMarketingRule.from_alipay_dict(value)
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value
    @property
    def wallet_user_identity_info(self):
        return self._wallet_user_identity_info

    @wallet_user_identity_info.setter
    def wallet_user_identity_info(self, value):
        if isinstance(value, WalletUserIdentityInfo):
            self._wallet_user_identity_info = value
        else:
            self._wallet_user_identity_info = WalletUserIdentityInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.need_check_identity:
            if hasattr(self.need_check_identity, 'to_alipay_dict'):
                params['need_check_identity'] = self.need_check_identity.to_alipay_dict()
            else:
                params['need_check_identity'] = self.need_check_identity
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_open_id:
            if hasattr(self.principal_open_id, 'to_alipay_dict'):
                params['principal_open_id'] = self.principal_open_id.to_alipay_dict()
            else:
                params['principal_open_id'] = self.principal_open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.wallet_marketing_rule:
            if hasattr(self.wallet_marketing_rule, 'to_alipay_dict'):
                params['wallet_marketing_rule'] = self.wallet_marketing_rule.to_alipay_dict()
            else:
                params['wallet_marketing_rule'] = self.wallet_marketing_rule
        if self.wallet_template_id:
            if hasattr(self.wallet_template_id, 'to_alipay_dict'):
                params['wallet_template_id'] = self.wallet_template_id.to_alipay_dict()
            else:
                params['wallet_template_id'] = self.wallet_template_id
        if self.wallet_user_identity_info:
            if hasattr(self.wallet_user_identity_info, 'to_alipay_dict'):
                params['wallet_user_identity_info'] = self.wallet_user_identity_info.to_alipay_dict()
            else:
                params['wallet_user_identity_info'] = self.wallet_user_identity_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletSceneSignModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'need_check_identity' in d:
            o.need_check_identity = d['need_check_identity']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_open_id' in d:
            o.principal_open_id = d['principal_open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'wallet_marketing_rule' in d:
            o.wallet_marketing_rule = d['wallet_marketing_rule']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        if 'wallet_user_identity_info' in d:
            o.wallet_user_identity_info = d['wallet_user_identity_info']
        return o


