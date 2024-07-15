#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcActivityInfo import EcActivityInfo
from alipay.aop.api.domain.EcMccInfo import EcMccInfo
from alipay.aop.api.domain.EcTradeIdentityInfo import EcTradeIdentityInfo
from alipay.aop.api.domain.EcTradingAreaInfo import EcTradingAreaInfo


class EcShopDetail(object):

    def __init__(self):
        self._accuracy_level = None
        self._activity_info_list = None
        self._city_id = None
        self._city_name = None
        self._district_id = None
        self._district_name = None
        self._has_legal_cert_no = None
        self._has_out_door_pic = None
        self._latitude = None
        self._longitude = None
        self._mcc_list = None
        self._poi_id = None
        self._province_id = None
        self._province_name = None
        self._shop_address = None
        self._shop_alias = None
        self._shop_id = None
        self._shop_name = None
        self._shop_type = None
        self._support_invoice = None
        self._trade_identity_info_list = None
        self._trading_area_info = None

    @property
    def accuracy_level(self):
        return self._accuracy_level

    @accuracy_level.setter
    def accuracy_level(self, value):
        self._accuracy_level = value
    @property
    def activity_info_list(self):
        return self._activity_info_list

    @activity_info_list.setter
    def activity_info_list(self, value):
        if isinstance(value, list):
            self._activity_info_list = list()
            for i in value:
                if isinstance(i, EcActivityInfo):
                    self._activity_info_list.append(i)
                else:
                    self._activity_info_list.append(EcActivityInfo.from_alipay_dict(i))
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def district_id(self):
        return self._district_id

    @district_id.setter
    def district_id(self, value):
        self._district_id = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def has_legal_cert_no(self):
        return self._has_legal_cert_no

    @has_legal_cert_no.setter
    def has_legal_cert_no(self, value):
        self._has_legal_cert_no = value
    @property
    def has_out_door_pic(self):
        return self._has_out_door_pic

    @has_out_door_pic.setter
    def has_out_door_pic(self, value):
        self._has_out_door_pic = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mcc_list(self):
        return self._mcc_list

    @mcc_list.setter
    def mcc_list(self, value):
        if isinstance(value, list):
            self._mcc_list = list()
            for i in value:
                if isinstance(i, EcMccInfo):
                    self._mcc_list.append(i)
                else:
                    self._mcc_list.append(EcMccInfo.from_alipay_dict(i))
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def province_id(self):
        return self._province_id

    @province_id.setter
    def province_id(self, value):
        self._province_id = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_alias(self):
        return self._shop_alias

    @shop_alias.setter
    def shop_alias(self, value):
        self._shop_alias = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def support_invoice(self):
        return self._support_invoice

    @support_invoice.setter
    def support_invoice(self, value):
        self._support_invoice = value
    @property
    def trade_identity_info_list(self):
        return self._trade_identity_info_list

    @trade_identity_info_list.setter
    def trade_identity_info_list(self, value):
        if isinstance(value, list):
            self._trade_identity_info_list = list()
            for i in value:
                if isinstance(i, EcTradeIdentityInfo):
                    self._trade_identity_info_list.append(i)
                else:
                    self._trade_identity_info_list.append(EcTradeIdentityInfo.from_alipay_dict(i))
    @property
    def trading_area_info(self):
        return self._trading_area_info

    @trading_area_info.setter
    def trading_area_info(self, value):
        if isinstance(value, EcTradingAreaInfo):
            self._trading_area_info = value
        else:
            self._trading_area_info = EcTradingAreaInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.accuracy_level:
            if hasattr(self.accuracy_level, 'to_alipay_dict'):
                params['accuracy_level'] = self.accuracy_level.to_alipay_dict()
            else:
                params['accuracy_level'] = self.accuracy_level
        if self.activity_info_list:
            if isinstance(self.activity_info_list, list):
                for i in range(0, len(self.activity_info_list)):
                    element = self.activity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_info_list, 'to_alipay_dict'):
                params['activity_info_list'] = self.activity_info_list.to_alipay_dict()
            else:
                params['activity_info_list'] = self.activity_info_list
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.district_id:
            if hasattr(self.district_id, 'to_alipay_dict'):
                params['district_id'] = self.district_id.to_alipay_dict()
            else:
                params['district_id'] = self.district_id
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.has_legal_cert_no:
            if hasattr(self.has_legal_cert_no, 'to_alipay_dict'):
                params['has_legal_cert_no'] = self.has_legal_cert_no.to_alipay_dict()
            else:
                params['has_legal_cert_no'] = self.has_legal_cert_no
        if self.has_out_door_pic:
            if hasattr(self.has_out_door_pic, 'to_alipay_dict'):
                params['has_out_door_pic'] = self.has_out_door_pic.to_alipay_dict()
            else:
                params['has_out_door_pic'] = self.has_out_door_pic
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mcc_list:
            if isinstance(self.mcc_list, list):
                for i in range(0, len(self.mcc_list)):
                    element = self.mcc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mcc_list[i] = element.to_alipay_dict()
            if hasattr(self.mcc_list, 'to_alipay_dict'):
                params['mcc_list'] = self.mcc_list.to_alipay_dict()
            else:
                params['mcc_list'] = self.mcc_list
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.province_id:
            if hasattr(self.province_id, 'to_alipay_dict'):
                params['province_id'] = self.province_id.to_alipay_dict()
            else:
                params['province_id'] = self.province_id
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_alias:
            if hasattr(self.shop_alias, 'to_alipay_dict'):
                params['shop_alias'] = self.shop_alias.to_alipay_dict()
            else:
                params['shop_alias'] = self.shop_alias
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.support_invoice:
            if hasattr(self.support_invoice, 'to_alipay_dict'):
                params['support_invoice'] = self.support_invoice.to_alipay_dict()
            else:
                params['support_invoice'] = self.support_invoice
        if self.trade_identity_info_list:
            if isinstance(self.trade_identity_info_list, list):
                for i in range(0, len(self.trade_identity_info_list)):
                    element = self.trade_identity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_identity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_identity_info_list, 'to_alipay_dict'):
                params['trade_identity_info_list'] = self.trade_identity_info_list.to_alipay_dict()
            else:
                params['trade_identity_info_list'] = self.trade_identity_info_list
        if self.trading_area_info:
            if hasattr(self.trading_area_info, 'to_alipay_dict'):
                params['trading_area_info'] = self.trading_area_info.to_alipay_dict()
            else:
                params['trading_area_info'] = self.trading_area_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcShopDetail()
        if 'accuracy_level' in d:
            o.accuracy_level = d['accuracy_level']
        if 'activity_info_list' in d:
            o.activity_info_list = d['activity_info_list']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'district_id' in d:
            o.district_id = d['district_id']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'has_legal_cert_no' in d:
            o.has_legal_cert_no = d['has_legal_cert_no']
        if 'has_out_door_pic' in d:
            o.has_out_door_pic = d['has_out_door_pic']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mcc_list' in d:
            o.mcc_list = d['mcc_list']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_id' in d:
            o.province_id = d['province_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_alias' in d:
            o.shop_alias = d['shop_alias']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'support_invoice' in d:
            o.support_invoice = d['support_invoice']
        if 'trade_identity_info_list' in d:
            o.trade_identity_info_list = d['trade_identity_info_list']
        if 'trading_area_info' in d:
            o.trading_area_info = d['trading_area_info']
        return o


