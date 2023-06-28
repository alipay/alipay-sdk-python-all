#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GeneralWithholdInfoDTO import GeneralWithholdInfoDTO


class AlipayFundZcardprodUserBindModel(object):

    def __init__(self):
        self._account_id = None
        self._biz_scene_code = None
        self._business_params = None
        self._general_withhold_info = None
        self._identity = None
        self._identity_type = None
        self._out_card_no = None
        self._product_code = None
        self._real_name = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def general_withhold_info(self):
        return self._general_withhold_info

    @general_withhold_info.setter
    def general_withhold_info(self, value):
        if isinstance(value, GeneralWithholdInfoDTO):
            self._general_withhold_info = value
        else:
            self._general_withhold_info = GeneralWithholdInfoDTO.from_alipay_dict(value)
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
    def out_card_no(self):
        return self._out_card_no

    @out_card_no.setter
    def out_card_no(self, value):
        self._out_card_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.biz_scene_code:
            if hasattr(self.biz_scene_code, 'to_alipay_dict'):
                params['biz_scene_code'] = self.biz_scene_code.to_alipay_dict()
            else:
                params['biz_scene_code'] = self.biz_scene_code
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.general_withhold_info:
            if hasattr(self.general_withhold_info, 'to_alipay_dict'):
                params['general_withhold_info'] = self.general_withhold_info.to_alipay_dict()
            else:
                params['general_withhold_info'] = self.general_withhold_info
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
        if self.out_card_no:
            if hasattr(self.out_card_no, 'to_alipay_dict'):
                params['out_card_no'] = self.out_card_no.to_alipay_dict()
            else:
                params['out_card_no'] = self.out_card_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundZcardprodUserBindModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'biz_scene_code' in d:
            o.biz_scene_code = d['biz_scene_code']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'general_withhold_info' in d:
            o.general_withhold_info = d['general_withhold_info']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'out_card_no' in d:
            o.out_card_no = d['out_card_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'real_name' in d:
            o.real_name = d['real_name']
        return o


