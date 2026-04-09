#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteOpAppInfo import InteOpAppInfo
from alipay.aop.api.domain.InteOpBusinessLicenseInfo import InteOpBusinessLicenseInfo
from alipay.aop.api.domain.InteOpHtmlFiveInfo import InteOpHtmlFiveInfo
from alipay.aop.api.domain.InteOpMerchantInfo import InteOpMerchantInfo
from alipay.aop.api.domain.InteOpMiniAppInfo import InteOpMiniAppInfo
from alipay.aop.api.domain.ProductDetail import ProductDetail
from alipay.aop.api.domain.ProductPriceInfo import ProductPriceInfo
from alipay.aop.api.domain.InteOpShopInfo import InteOpShopInfo
from alipay.aop.api.domain.InteOpSpecialLicenseInfo import InteOpSpecialLicenseInfo
from alipay.aop.api.domain.InteOpSpecialLicenseInfo import InteOpSpecialLicenseInfo
from alipay.aop.api.domain.InteOpWebSiteInfo import InteOpWebSiteInfo


class AlipayOpenSpInteopProductCreateModel(object):

    def __init__(self):
        self._inteop_app_info = None
        self._inteop_business_license_info = None
        self._inteop_h_5_info = None
        self._inteop_merchant_info = None
        self._inteop_mini_app_info = None
        self._inteop_order_no = None
        self._inteop_product_details = None
        self._inteop_product_price_details = None
        self._inteop_shop_info = None
        self._inteop_special_license_info = None
        self._inteop_special_license_infos = None
        self._inteop_web_site_info = None
        self._mcc_code = None
        self._mobile_type = None
        self._product_code = None
        self._trade_scene = None

    @property
    def inteop_app_info(self):
        return self._inteop_app_info

    @inteop_app_info.setter
    def inteop_app_info(self, value):
        if isinstance(value, InteOpAppInfo):
            self._inteop_app_info = value
        else:
            self._inteop_app_info = InteOpAppInfo.from_alipay_dict(value)
    @property
    def inteop_business_license_info(self):
        return self._inteop_business_license_info

    @inteop_business_license_info.setter
    def inteop_business_license_info(self, value):
        if isinstance(value, InteOpBusinessLicenseInfo):
            self._inteop_business_license_info = value
        else:
            self._inteop_business_license_info = InteOpBusinessLicenseInfo.from_alipay_dict(value)
    @property
    def inteop_h_5_info(self):
        return self._inteop_h_5_info

    @inteop_h_5_info.setter
    def inteop_h_5_info(self, value):
        if isinstance(value, InteOpHtmlFiveInfo):
            self._inteop_h_5_info = value
        else:
            self._inteop_h_5_info = InteOpHtmlFiveInfo.from_alipay_dict(value)
    @property
    def inteop_merchant_info(self):
        return self._inteop_merchant_info

    @inteop_merchant_info.setter
    def inteop_merchant_info(self, value):
        if isinstance(value, InteOpMerchantInfo):
            self._inteop_merchant_info = value
        else:
            self._inteop_merchant_info = InteOpMerchantInfo.from_alipay_dict(value)
    @property
    def inteop_mini_app_info(self):
        return self._inteop_mini_app_info

    @inteop_mini_app_info.setter
    def inteop_mini_app_info(self, value):
        if isinstance(value, InteOpMiniAppInfo):
            self._inteop_mini_app_info = value
        else:
            self._inteop_mini_app_info = InteOpMiniAppInfo.from_alipay_dict(value)
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def inteop_product_details(self):
        return self._inteop_product_details

    @inteop_product_details.setter
    def inteop_product_details(self, value):
        if isinstance(value, list):
            self._inteop_product_details = list()
            for i in value:
                if isinstance(i, ProductDetail):
                    self._inteop_product_details.append(i)
                else:
                    self._inteop_product_details.append(ProductDetail.from_alipay_dict(i))
    @property
    def inteop_product_price_details(self):
        return self._inteop_product_price_details

    @inteop_product_price_details.setter
    def inteop_product_price_details(self, value):
        if isinstance(value, list):
            self._inteop_product_price_details = list()
            for i in value:
                if isinstance(i, ProductPriceInfo):
                    self._inteop_product_price_details.append(i)
                else:
                    self._inteop_product_price_details.append(ProductPriceInfo.from_alipay_dict(i))
    @property
    def inteop_shop_info(self):
        return self._inteop_shop_info

    @inteop_shop_info.setter
    def inteop_shop_info(self, value):
        if isinstance(value, InteOpShopInfo):
            self._inteop_shop_info = value
        else:
            self._inteop_shop_info = InteOpShopInfo.from_alipay_dict(value)
    @property
    def inteop_special_license_info(self):
        return self._inteop_special_license_info

    @inteop_special_license_info.setter
    def inteop_special_license_info(self, value):
        if isinstance(value, InteOpSpecialLicenseInfo):
            self._inteop_special_license_info = value
        else:
            self._inteop_special_license_info = InteOpSpecialLicenseInfo.from_alipay_dict(value)
    @property
    def inteop_special_license_infos(self):
        return self._inteop_special_license_infos

    @inteop_special_license_infos.setter
    def inteop_special_license_infos(self, value):
        if isinstance(value, list):
            self._inteop_special_license_infos = list()
            for i in value:
                if isinstance(i, InteOpSpecialLicenseInfo):
                    self._inteop_special_license_infos.append(i)
                else:
                    self._inteop_special_license_infos.append(InteOpSpecialLicenseInfo.from_alipay_dict(i))
    @property
    def inteop_web_site_info(self):
        return self._inteop_web_site_info

    @inteop_web_site_info.setter
    def inteop_web_site_info(self, value):
        if isinstance(value, InteOpWebSiteInfo):
            self._inteop_web_site_info = value
        else:
            self._inteop_web_site_info = InteOpWebSiteInfo.from_alipay_dict(value)
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mobile_type(self):
        return self._mobile_type

    @mobile_type.setter
    def mobile_type(self, value):
        self._mobile_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def trade_scene(self):
        return self._trade_scene

    @trade_scene.setter
    def trade_scene(self, value):
        self._trade_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.inteop_app_info:
            if hasattr(self.inteop_app_info, 'to_alipay_dict'):
                params['inteop_app_info'] = self.inteop_app_info.to_alipay_dict()
            else:
                params['inteop_app_info'] = self.inteop_app_info
        if self.inteop_business_license_info:
            if hasattr(self.inteop_business_license_info, 'to_alipay_dict'):
                params['inteop_business_license_info'] = self.inteop_business_license_info.to_alipay_dict()
            else:
                params['inteop_business_license_info'] = self.inteop_business_license_info
        if self.inteop_h_5_info:
            if hasattr(self.inteop_h_5_info, 'to_alipay_dict'):
                params['inteop_h_5_info'] = self.inteop_h_5_info.to_alipay_dict()
            else:
                params['inteop_h_5_info'] = self.inteop_h_5_info
        if self.inteop_merchant_info:
            if hasattr(self.inteop_merchant_info, 'to_alipay_dict'):
                params['inteop_merchant_info'] = self.inteop_merchant_info.to_alipay_dict()
            else:
                params['inteop_merchant_info'] = self.inteop_merchant_info
        if self.inteop_mini_app_info:
            if hasattr(self.inteop_mini_app_info, 'to_alipay_dict'):
                params['inteop_mini_app_info'] = self.inteop_mini_app_info.to_alipay_dict()
            else:
                params['inteop_mini_app_info'] = self.inteop_mini_app_info
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.inteop_product_details:
            if isinstance(self.inteop_product_details, list):
                for i in range(0, len(self.inteop_product_details)):
                    element = self.inteop_product_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteop_product_details[i] = element.to_alipay_dict()
            if hasattr(self.inteop_product_details, 'to_alipay_dict'):
                params['inteop_product_details'] = self.inteop_product_details.to_alipay_dict()
            else:
                params['inteop_product_details'] = self.inteop_product_details
        if self.inteop_product_price_details:
            if isinstance(self.inteop_product_price_details, list):
                for i in range(0, len(self.inteop_product_price_details)):
                    element = self.inteop_product_price_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteop_product_price_details[i] = element.to_alipay_dict()
            if hasattr(self.inteop_product_price_details, 'to_alipay_dict'):
                params['inteop_product_price_details'] = self.inteop_product_price_details.to_alipay_dict()
            else:
                params['inteop_product_price_details'] = self.inteop_product_price_details
        if self.inteop_shop_info:
            if hasattr(self.inteop_shop_info, 'to_alipay_dict'):
                params['inteop_shop_info'] = self.inteop_shop_info.to_alipay_dict()
            else:
                params['inteop_shop_info'] = self.inteop_shop_info
        if self.inteop_special_license_info:
            if hasattr(self.inteop_special_license_info, 'to_alipay_dict'):
                params['inteop_special_license_info'] = self.inteop_special_license_info.to_alipay_dict()
            else:
                params['inteop_special_license_info'] = self.inteop_special_license_info
        if self.inteop_special_license_infos:
            if isinstance(self.inteop_special_license_infos, list):
                for i in range(0, len(self.inteop_special_license_infos)):
                    element = self.inteop_special_license_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteop_special_license_infos[i] = element.to_alipay_dict()
            if hasattr(self.inteop_special_license_infos, 'to_alipay_dict'):
                params['inteop_special_license_infos'] = self.inteop_special_license_infos.to_alipay_dict()
            else:
                params['inteop_special_license_infos'] = self.inteop_special_license_infos
        if self.inteop_web_site_info:
            if hasattr(self.inteop_web_site_info, 'to_alipay_dict'):
                params['inteop_web_site_info'] = self.inteop_web_site_info.to_alipay_dict()
            else:
                params['inteop_web_site_info'] = self.inteop_web_site_info
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.mobile_type:
            if hasattr(self.mobile_type, 'to_alipay_dict'):
                params['mobile_type'] = self.mobile_type.to_alipay_dict()
            else:
                params['mobile_type'] = self.mobile_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.trade_scene:
            if hasattr(self.trade_scene, 'to_alipay_dict'):
                params['trade_scene'] = self.trade_scene.to_alipay_dict()
            else:
                params['trade_scene'] = self.trade_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopProductCreateModel()
        if 'inteop_app_info' in d:
            o.inteop_app_info = d['inteop_app_info']
        if 'inteop_business_license_info' in d:
            o.inteop_business_license_info = d['inteop_business_license_info']
        if 'inteop_h_5_info' in d:
            o.inteop_h_5_info = d['inteop_h_5_info']
        if 'inteop_merchant_info' in d:
            o.inteop_merchant_info = d['inteop_merchant_info']
        if 'inteop_mini_app_info' in d:
            o.inteop_mini_app_info = d['inteop_mini_app_info']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'inteop_product_details' in d:
            o.inteop_product_details = d['inteop_product_details']
        if 'inteop_product_price_details' in d:
            o.inteop_product_price_details = d['inteop_product_price_details']
        if 'inteop_shop_info' in d:
            o.inteop_shop_info = d['inteop_shop_info']
        if 'inteop_special_license_info' in d:
            o.inteop_special_license_info = d['inteop_special_license_info']
        if 'inteop_special_license_infos' in d:
            o.inteop_special_license_infos = d['inteop_special_license_infos']
        if 'inteop_web_site_info' in d:
            o.inteop_web_site_info = d['inteop_web_site_info']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'mobile_type' in d:
            o.mobile_type = d['mobile_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'trade_scene' in d:
            o.trade_scene = d['trade_scene']
        return o


