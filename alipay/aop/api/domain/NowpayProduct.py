#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PricingModeForList import PricingModeForList


class NowpayProduct(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._out_product_id = None
        self._pricing_mode_list = None
        self._product_description = None
        self._product_icon_url = None
        self._product_id = None
        self._product_name = None
        self._product_url = None
        self._record_status = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def pricing_mode_list(self):
        return self._pricing_mode_list

    @pricing_mode_list.setter
    def pricing_mode_list(self, value):
        if isinstance(value, list):
            self._pricing_mode_list = list()
            for i in value:
                if isinstance(i, PricingModeForList):
                    self._pricing_mode_list.append(i)
                else:
                    self._pricing_mode_list.append(PricingModeForList.from_alipay_dict(i))
    @property
    def product_description(self):
        return self._product_description

    @product_description.setter
    def product_description(self, value):
        self._product_description = value
    @property
    def product_icon_url(self):
        return self._product_icon_url

    @product_icon_url.setter
    def product_icon_url(self, value):
        self._product_icon_url = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_url(self):
        return self._product_url

    @product_url.setter
    def product_url(self, value):
        self._product_url = value
    @property
    def record_status(self):
        return self._record_status

    @record_status.setter
    def record_status(self, value):
        self._record_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.pricing_mode_list:
            if isinstance(self.pricing_mode_list, list):
                for i in range(0, len(self.pricing_mode_list)):
                    element = self.pricing_mode_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pricing_mode_list[i] = element.to_alipay_dict()
            if hasattr(self.pricing_mode_list, 'to_alipay_dict'):
                params['pricing_mode_list'] = self.pricing_mode_list.to_alipay_dict()
            else:
                params['pricing_mode_list'] = self.pricing_mode_list
        if self.product_description:
            if hasattr(self.product_description, 'to_alipay_dict'):
                params['product_description'] = self.product_description.to_alipay_dict()
            else:
                params['product_description'] = self.product_description
        if self.product_icon_url:
            if hasattr(self.product_icon_url, 'to_alipay_dict'):
                params['product_icon_url'] = self.product_icon_url.to_alipay_dict()
            else:
                params['product_icon_url'] = self.product_icon_url
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_url:
            if hasattr(self.product_url, 'to_alipay_dict'):
                params['product_url'] = self.product_url.to_alipay_dict()
            else:
                params['product_url'] = self.product_url
        if self.record_status:
            if hasattr(self.record_status, 'to_alipay_dict'):
                params['record_status'] = self.record_status.to_alipay_dict()
            else:
                params['record_status'] = self.record_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NowpayProduct()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'pricing_mode_list' in d:
            o.pricing_mode_list = d['pricing_mode_list']
        if 'product_description' in d:
            o.product_description = d['product_description']
        if 'product_icon_url' in d:
            o.product_icon_url = d['product_icon_url']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_url' in d:
            o.product_url = d['product_url']
        if 'record_status' in d:
            o.record_status = d['record_status']
        return o


