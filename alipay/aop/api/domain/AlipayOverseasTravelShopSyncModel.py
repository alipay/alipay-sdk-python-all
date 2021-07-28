#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessHour import BusinessHour
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.ShopExtendParams import ShopExtendParams
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.ShopRating import ShopRating


class AlipayOverseasTravelShopSyncModel(object):

    def __init__(self):
        self._address = None
        self._brand_logo = None
        self._brand_name = None
        self._business_hours = None
        self._country_code = None
        self._delivery_fee = None
        self._extend_params = None
        self._external_link_url = None
        self._fee = None
        self._latitude = None
        self._longitude = None
        self._merchant_id = None
        self._out_shop_id = None
        self._partner_id = None
        self._promotion_text = None
        self._rating = None
        self._recommend = None
        self._scenarios = None
        self._shop_logo_photo = None
        self._shop_name = None
        self._shop_tags = None
        self._status = None
        self._store_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def business_hours(self):
        return self._business_hours

    @business_hours.setter
    def business_hours(self, value):
        if isinstance(value, list):
            self._business_hours = list()
            for i in value:
                if isinstance(i, BusinessHour):
                    self._business_hours.append(i)
                else:
                    self._business_hours.append(BusinessHour.from_alipay_dict(i))
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        if isinstance(value, Amount):
            self._delivery_fee = value
        else:
            self._delivery_fee = Amount.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ShopExtendParams):
            self._extend_params = value
        else:
            self._extend_params = ShopExtendParams.from_alipay_dict(value)
    @property
    def external_link_url(self):
        return self._external_link_url

    @external_link_url.setter
    def external_link_url(self, value):
        self._external_link_url = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        if isinstance(value, Amount):
            self._fee = value
        else:
            self._fee = Amount.from_alipay_dict(value)
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
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def promotion_text(self):
        return self._promotion_text

    @promotion_text.setter
    def promotion_text(self, value):
        self._promotion_text = value
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, ShopRating):
            self._rating = value
        else:
            self._rating = ShopRating.from_alipay_dict(value)
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def scenarios(self):
        return self._scenarios

    @scenarios.setter
    def scenarios(self, value):
        if isinstance(value, list):
            self._scenarios = list()
            for i in value:
                self._scenarios.append(i)
    @property
    def shop_logo_photo(self):
        return self._shop_logo_photo

    @shop_logo_photo.setter
    def shop_logo_photo(self, value):
        self._shop_logo_photo = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_tags(self):
        return self._shop_tags

    @shop_tags.setter
    def shop_tags(self, value):
        if isinstance(value, list):
            self._shop_tags = list()
            for i in value:
                self._shop_tags.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.business_hours:
            if isinstance(self.business_hours, list):
                for i in range(0, len(self.business_hours)):
                    element = self.business_hours[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_hours[i] = element.to_alipay_dict()
            if hasattr(self.business_hours, 'to_alipay_dict'):
                params['business_hours'] = self.business_hours.to_alipay_dict()
            else:
                params['business_hours'] = self.business_hours
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.delivery_fee:
            if hasattr(self.delivery_fee, 'to_alipay_dict'):
                params['delivery_fee'] = self.delivery_fee.to_alipay_dict()
            else:
                params['delivery_fee'] = self.delivery_fee
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.external_link_url:
            if hasattr(self.external_link_url, 'to_alipay_dict'):
                params['external_link_url'] = self.external_link_url.to_alipay_dict()
            else:
                params['external_link_url'] = self.external_link_url
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
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
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.promotion_text:
            if hasattr(self.promotion_text, 'to_alipay_dict'):
                params['promotion_text'] = self.promotion_text.to_alipay_dict()
            else:
                params['promotion_text'] = self.promotion_text
        if self.rating:
            if hasattr(self.rating, 'to_alipay_dict'):
                params['rating'] = self.rating.to_alipay_dict()
            else:
                params['rating'] = self.rating
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.scenarios:
            if isinstance(self.scenarios, list):
                for i in range(0, len(self.scenarios)):
                    element = self.scenarios[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenarios[i] = element.to_alipay_dict()
            if hasattr(self.scenarios, 'to_alipay_dict'):
                params['scenarios'] = self.scenarios.to_alipay_dict()
            else:
                params['scenarios'] = self.scenarios
        if self.shop_logo_photo:
            if hasattr(self.shop_logo_photo, 'to_alipay_dict'):
                params['shop_logo_photo'] = self.shop_logo_photo.to_alipay_dict()
            else:
                params['shop_logo_photo'] = self.shop_logo_photo
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_tags:
            if isinstance(self.shop_tags, list):
                for i in range(0, len(self.shop_tags)):
                    element = self.shop_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_tags[i] = element.to_alipay_dict()
            if hasattr(self.shop_tags, 'to_alipay_dict'):
                params['shop_tags'] = self.shop_tags.to_alipay_dict()
            else:
                params['shop_tags'] = self.shop_tags
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelShopSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'business_hours' in d:
            o.business_hours = d['business_hours']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'delivery_fee' in d:
            o.delivery_fee = d['delivery_fee']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'external_link_url' in d:
            o.external_link_url = d['external_link_url']
        if 'fee' in d:
            o.fee = d['fee']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'promotion_text' in d:
            o.promotion_text = d['promotion_text']
        if 'rating' in d:
            o.rating = d['rating']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'scenarios' in d:
            o.scenarios = d['scenarios']
        if 'shop_logo_photo' in d:
            o.shop_logo_photo = d['shop_logo_photo']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_tags' in d:
            o.shop_tags = d['shop_tags']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


