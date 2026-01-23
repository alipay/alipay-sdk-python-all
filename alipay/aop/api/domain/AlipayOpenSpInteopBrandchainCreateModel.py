#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandChainBankCardInfo import BrandChainBankCardInfo
from alipay.aop.api.domain.BusinessLicenseInfo import BusinessLicenseInfo
from alipay.aop.api.domain.BrandChainContactInfo import BrandChainContactInfo
from alipay.aop.api.domain.BrandChainShopInfo import BrandChainShopInfo
from alipay.aop.api.domain.SpecialLicenseInfo import SpecialLicenseInfo


class AlipayOpenSpInteopBrandchainCreateModel(object):

    def __init__(self):
        self._bank_card_info = None
        self._brand_app_id = None
        self._business_license_info = None
        self._contact_info = None
        self._face_to_face_rate = None
        self._inteop_order_no = None
        self._jsapi_pay_rate = None
        self._mcc_code = None
        self._shop_info = None
        self._special_license_info = None

    @property
    def bank_card_info(self):
        return self._bank_card_info

    @bank_card_info.setter
    def bank_card_info(self, value):
        if isinstance(value, BrandChainBankCardInfo):
            self._bank_card_info = value
        else:
            self._bank_card_info = BrandChainBankCardInfo.from_alipay_dict(value)
    @property
    def brand_app_id(self):
        return self._brand_app_id

    @brand_app_id.setter
    def brand_app_id(self, value):
        self._brand_app_id = value
    @property
    def business_license_info(self):
        return self._business_license_info

    @business_license_info.setter
    def business_license_info(self, value):
        if isinstance(value, BusinessLicenseInfo):
            self._business_license_info = value
        else:
            self._business_license_info = BusinessLicenseInfo.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, BrandChainContactInfo):
            self._contact_info = value
        else:
            self._contact_info = BrandChainContactInfo.from_alipay_dict(value)
    @property
    def face_to_face_rate(self):
        return self._face_to_face_rate

    @face_to_face_rate.setter
    def face_to_face_rate(self, value):
        self._face_to_face_rate = value
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def jsapi_pay_rate(self):
        return self._jsapi_pay_rate

    @jsapi_pay_rate.setter
    def jsapi_pay_rate(self, value):
        self._jsapi_pay_rate = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, BrandChainShopInfo):
            self._shop_info = value
        else:
            self._shop_info = BrandChainShopInfo.from_alipay_dict(value)
    @property
    def special_license_info(self):
        return self._special_license_info

    @special_license_info.setter
    def special_license_info(self, value):
        if isinstance(value, SpecialLicenseInfo):
            self._special_license_info = value
        else:
            self._special_license_info = SpecialLicenseInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_info:
            if hasattr(self.bank_card_info, 'to_alipay_dict'):
                params['bank_card_info'] = self.bank_card_info.to_alipay_dict()
            else:
                params['bank_card_info'] = self.bank_card_info
        if self.brand_app_id:
            if hasattr(self.brand_app_id, 'to_alipay_dict'):
                params['brand_app_id'] = self.brand_app_id.to_alipay_dict()
            else:
                params['brand_app_id'] = self.brand_app_id
        if self.business_license_info:
            if hasattr(self.business_license_info, 'to_alipay_dict'):
                params['business_license_info'] = self.business_license_info.to_alipay_dict()
            else:
                params['business_license_info'] = self.business_license_info
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.face_to_face_rate:
            if hasattr(self.face_to_face_rate, 'to_alipay_dict'):
                params['face_to_face_rate'] = self.face_to_face_rate.to_alipay_dict()
            else:
                params['face_to_face_rate'] = self.face_to_face_rate
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.jsapi_pay_rate:
            if hasattr(self.jsapi_pay_rate, 'to_alipay_dict'):
                params['jsapi_pay_rate'] = self.jsapi_pay_rate.to_alipay_dict()
            else:
                params['jsapi_pay_rate'] = self.jsapi_pay_rate
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        if self.special_license_info:
            if hasattr(self.special_license_info, 'to_alipay_dict'):
                params['special_license_info'] = self.special_license_info.to_alipay_dict()
            else:
                params['special_license_info'] = self.special_license_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopBrandchainCreateModel()
        if 'bank_card_info' in d:
            o.bank_card_info = d['bank_card_info']
        if 'brand_app_id' in d:
            o.brand_app_id = d['brand_app_id']
        if 'business_license_info' in d:
            o.business_license_info = d['business_license_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'face_to_face_rate' in d:
            o.face_to_face_rate = d['face_to_face_rate']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'jsapi_pay_rate' in d:
            o.jsapi_pay_rate = d['jsapi_pay_rate']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'special_license_info' in d:
            o.special_license_info = d['special_license_info']
        return o


