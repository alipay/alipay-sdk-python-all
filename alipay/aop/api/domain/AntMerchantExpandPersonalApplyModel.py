#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BaseInfo import BaseInfo
from alipay.aop.api.domain.BusinessLicenceInfo import BusinessLicenceInfo
from alipay.aop.api.domain.OperatorInfo import OperatorInfo
from alipay.aop.api.domain.PersonnalBankAccountInfo import PersonnalBankAccountInfo
from alipay.aop.api.domain.ShopInfo import ShopInfo


class AntMerchantExpandPersonalApplyModel(object):

    def __init__(self):
        self._base_info = None
        self._business_license_info = None
        self._login_id = None
        self._operator_info = None
        self._out_biz_no = None
        self._personal_bank_account_info = None
        self._shop_info = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, BaseInfo):
            self._base_info = value
        else:
            self._base_info = BaseInfo.from_alipay_dict(value)
    @property
    def business_license_info(self):
        return self._business_license_info

    @business_license_info.setter
    def business_license_info(self, value):
        if isinstance(value, BusinessLicenceInfo):
            self._business_license_info = value
        else:
            self._business_license_info = BusinessLicenceInfo.from_alipay_dict(value)
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def operator_info(self):
        return self._operator_info

    @operator_info.setter
    def operator_info(self, value):
        if isinstance(value, OperatorInfo):
            self._operator_info = value
        else:
            self._operator_info = OperatorInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def personal_bank_account_info(self):
        return self._personal_bank_account_info

    @personal_bank_account_info.setter
    def personal_bank_account_info(self, value):
        if isinstance(value, PersonnalBankAccountInfo):
            self._personal_bank_account_info = value
        else:
            self._personal_bank_account_info = PersonnalBankAccountInfo.from_alipay_dict(value)
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, ShopInfo):
            self._shop_info = value
        else:
            self._shop_info = ShopInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.business_license_info:
            if hasattr(self.business_license_info, 'to_alipay_dict'):
                params['business_license_info'] = self.business_license_info.to_alipay_dict()
            else:
                params['business_license_info'] = self.business_license_info
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.operator_info:
            if hasattr(self.operator_info, 'to_alipay_dict'):
                params['operator_info'] = self.operator_info.to_alipay_dict()
            else:
                params['operator_info'] = self.operator_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.personal_bank_account_info:
            if hasattr(self.personal_bank_account_info, 'to_alipay_dict'):
                params['personal_bank_account_info'] = self.personal_bank_account_info.to_alipay_dict()
            else:
                params['personal_bank_account_info'] = self.personal_bank_account_info
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandPersonalApplyModel()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'business_license_info' in d:
            o.business_license_info = d['business_license_info']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'operator_info' in d:
            o.operator_info = d['operator_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'personal_bank_account_info' in d:
            o.personal_bank_account_info = d['personal_bank_account_info']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        return o


