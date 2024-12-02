#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StoreRentalEbikeDetail(object):

    def __init__(self):
        self._ebike_id = None
        self._ebike_image_url = None
        self._ebike_name = None
        self._ebike_service_desc = None
        self._order_link_url = None
        self._rental_period_type = None
        self._rental_price = None

    @property
    def ebike_id(self):
        return self._ebike_id

    @ebike_id.setter
    def ebike_id(self, value):
        self._ebike_id = value
    @property
    def ebike_image_url(self):
        return self._ebike_image_url

    @ebike_image_url.setter
    def ebike_image_url(self, value):
        self._ebike_image_url = value
    @property
    def ebike_name(self):
        return self._ebike_name

    @ebike_name.setter
    def ebike_name(self, value):
        self._ebike_name = value
    @property
    def ebike_service_desc(self):
        return self._ebike_service_desc

    @ebike_service_desc.setter
    def ebike_service_desc(self, value):
        if isinstance(value, list):
            self._ebike_service_desc = list()
            for i in value:
                self._ebike_service_desc.append(i)
    @property
    def order_link_url(self):
        return self._order_link_url

    @order_link_url.setter
    def order_link_url(self, value):
        self._order_link_url = value
    @property
    def rental_period_type(self):
        return self._rental_period_type

    @rental_period_type.setter
    def rental_period_type(self, value):
        self._rental_period_type = value
    @property
    def rental_price(self):
        return self._rental_price

    @rental_price.setter
    def rental_price(self, value):
        self._rental_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.ebike_id:
            if hasattr(self.ebike_id, 'to_alipay_dict'):
                params['ebike_id'] = self.ebike_id.to_alipay_dict()
            else:
                params['ebike_id'] = self.ebike_id
        if self.ebike_image_url:
            if hasattr(self.ebike_image_url, 'to_alipay_dict'):
                params['ebike_image_url'] = self.ebike_image_url.to_alipay_dict()
            else:
                params['ebike_image_url'] = self.ebike_image_url
        if self.ebike_name:
            if hasattr(self.ebike_name, 'to_alipay_dict'):
                params['ebike_name'] = self.ebike_name.to_alipay_dict()
            else:
                params['ebike_name'] = self.ebike_name
        if self.ebike_service_desc:
            if isinstance(self.ebike_service_desc, list):
                for i in range(0, len(self.ebike_service_desc)):
                    element = self.ebike_service_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ebike_service_desc[i] = element.to_alipay_dict()
            if hasattr(self.ebike_service_desc, 'to_alipay_dict'):
                params['ebike_service_desc'] = self.ebike_service_desc.to_alipay_dict()
            else:
                params['ebike_service_desc'] = self.ebike_service_desc
        if self.order_link_url:
            if hasattr(self.order_link_url, 'to_alipay_dict'):
                params['order_link_url'] = self.order_link_url.to_alipay_dict()
            else:
                params['order_link_url'] = self.order_link_url
        if self.rental_period_type:
            if hasattr(self.rental_period_type, 'to_alipay_dict'):
                params['rental_period_type'] = self.rental_period_type.to_alipay_dict()
            else:
                params['rental_period_type'] = self.rental_period_type
        if self.rental_price:
            if hasattr(self.rental_price, 'to_alipay_dict'):
                params['rental_price'] = self.rental_price.to_alipay_dict()
            else:
                params['rental_price'] = self.rental_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StoreRentalEbikeDetail()
        if 'ebike_id' in d:
            o.ebike_id = d['ebike_id']
        if 'ebike_image_url' in d:
            o.ebike_image_url = d['ebike_image_url']
        if 'ebike_name' in d:
            o.ebike_name = d['ebike_name']
        if 'ebike_service_desc' in d:
            o.ebike_service_desc = d['ebike_service_desc']
        if 'order_link_url' in d:
            o.order_link_url = d['order_link_url']
        if 'rental_period_type' in d:
            o.rental_period_type = d['rental_period_type']
        if 'rental_price' in d:
            o.rental_price = d['rental_price']
        return o


