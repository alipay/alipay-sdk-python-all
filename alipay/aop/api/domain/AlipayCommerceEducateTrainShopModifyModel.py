#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopAddressInfo import ShopAddressInfo
from alipay.aop.api.domain.ShopMerchantInfo import ShopMerchantInfo


class AlipayCommerceEducateTrainShopModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._applet_appid = None
        self._biz_type = None
        self._desc = None
        self._income_account = None
        self._merchant_info = None
        self._name = None
        self._out_shop_id = None
        self._pic = None
        self._service_phone = None
        self._shop_id = None
        self._source_type = None
        self._url = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, ShopAddressInfo):
            self._address_info = value
        else:
            self._address_info = ShopAddressInfo.from_alipay_dict(value)
    @property
    def applet_appid(self):
        return self._applet_appid

    @applet_appid.setter
    def applet_appid(self, value):
        self._applet_appid = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def income_account(self):
        return self._income_account

    @income_account.setter
    def income_account(self, value):
        self._income_account = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, ShopMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = ShopMerchantInfo.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def pic(self):
        return self._pic

    @pic.setter
    def pic(self, value):
        self._pic = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        if isinstance(value, list):
            self._service_phone = list()
            for i in value:
                self._service_phone.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.applet_appid:
            if hasattr(self.applet_appid, 'to_alipay_dict'):
                params['applet_appid'] = self.applet_appid.to_alipay_dict()
            else:
                params['applet_appid'] = self.applet_appid
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.income_account:
            if hasattr(self.income_account, 'to_alipay_dict'):
                params['income_account'] = self.income_account.to_alipay_dict()
            else:
                params['income_account'] = self.income_account
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.pic:
            if hasattr(self.pic, 'to_alipay_dict'):
                params['pic'] = self.pic.to_alipay_dict()
            else:
                params['pic'] = self.pic
        if self.service_phone:
            if isinstance(self.service_phone, list):
                for i in range(0, len(self.service_phone)):
                    element = self.service_phone[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_phone[i] = element.to_alipay_dict()
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTrainShopModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'applet_appid' in d:
            o.applet_appid = d['applet_appid']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'income_account' in d:
            o.income_account = d['income_account']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'name' in d:
            o.name = d['name']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'pic' in d:
            o.pic = d['pic']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'url' in d:
            o.url = d['url']
        return o


