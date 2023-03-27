#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessParamDTO import BusinessParamDTO
from alipay.aop.api.domain.PrincipalInfoDTO import PrincipalInfoDTO


class AlipayFundAccountbookPageCreateModel(object):

    def __init__(self):
        self._account_book_alias = None
        self._biz_scene = None
        self._business_param = None
        self._out_biz_no = None
        self._principal_info = None
        self._product_code = None

    @property
    def account_book_alias(self):
        return self._account_book_alias

    @account_book_alias.setter
    def account_book_alias(self, value):
        self._account_book_alias = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_param(self):
        return self._business_param

    @business_param.setter
    def business_param(self, value):
        if isinstance(value, BusinessParamDTO):
            self._business_param = value
        else:
            self._business_param = BusinessParamDTO.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, PrincipalInfoDTO):
            self._principal_info = value
        else:
            self._principal_info = PrincipalInfoDTO.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_book_alias:
            if hasattr(self.account_book_alias, 'to_alipay_dict'):
                params['account_book_alias'] = self.account_book_alias.to_alipay_dict()
            else:
                params['account_book_alias'] = self.account_book_alias
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_param:
            if hasattr(self.business_param, 'to_alipay_dict'):
                params['business_param'] = self.business_param.to_alipay_dict()
            else:
                params['business_param'] = self.business_param
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
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
        o = AlipayFundAccountbookPageCreateModel()
        if 'account_book_alias' in d:
            o.account_book_alias = d['account_book_alias']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_param' in d:
            o.business_param = d['business_param']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


