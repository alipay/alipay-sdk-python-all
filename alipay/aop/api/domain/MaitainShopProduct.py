#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaitainShopProduct(object):

    def __init__(self):
        self._off_price = None
        self._orig_price = None
        self._out_privilege_id = None
        self._out_shop_id = None
        self._privilege_close_time = None
        self._privilege_price = None
        self._privilege_start_time = None
        self._privilege_tags = None
        self._product_desc = None
        self._product_name = None
        self._service_category_id = None
        self._status = None

    @property
    def off_price(self):
        return self._off_price

    @off_price.setter
    def off_price(self, value):
        self._off_price = value
    @property
    def orig_price(self):
        return self._orig_price

    @orig_price.setter
    def orig_price(self, value):
        self._orig_price = value
    @property
    def out_privilege_id(self):
        return self._out_privilege_id

    @out_privilege_id.setter
    def out_privilege_id(self, value):
        self._out_privilege_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def privilege_close_time(self):
        return self._privilege_close_time

    @privilege_close_time.setter
    def privilege_close_time(self, value):
        self._privilege_close_time = value
    @property
    def privilege_price(self):
        return self._privilege_price

    @privilege_price.setter
    def privilege_price(self, value):
        self._privilege_price = value
    @property
    def privilege_start_time(self):
        return self._privilege_start_time

    @privilege_start_time.setter
    def privilege_start_time(self, value):
        self._privilege_start_time = value
    @property
    def privilege_tags(self):
        return self._privilege_tags

    @privilege_tags.setter
    def privilege_tags(self, value):
        self._privilege_tags = value
    @property
    def product_desc(self):
        return self._product_desc

    @product_desc.setter
    def product_desc(self, value):
        self._product_desc = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def service_category_id(self):
        return self._service_category_id

    @service_category_id.setter
    def service_category_id(self, value):
        self._service_category_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.off_price:
            if hasattr(self.off_price, 'to_alipay_dict'):
                params['off_price'] = self.off_price.to_alipay_dict()
            else:
                params['off_price'] = self.off_price
        if self.orig_price:
            if hasattr(self.orig_price, 'to_alipay_dict'):
                params['orig_price'] = self.orig_price.to_alipay_dict()
            else:
                params['orig_price'] = self.orig_price
        if self.out_privilege_id:
            if hasattr(self.out_privilege_id, 'to_alipay_dict'):
                params['out_privilege_id'] = self.out_privilege_id.to_alipay_dict()
            else:
                params['out_privilege_id'] = self.out_privilege_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.privilege_close_time:
            if hasattr(self.privilege_close_time, 'to_alipay_dict'):
                params['privilege_close_time'] = self.privilege_close_time.to_alipay_dict()
            else:
                params['privilege_close_time'] = self.privilege_close_time
        if self.privilege_price:
            if hasattr(self.privilege_price, 'to_alipay_dict'):
                params['privilege_price'] = self.privilege_price.to_alipay_dict()
            else:
                params['privilege_price'] = self.privilege_price
        if self.privilege_start_time:
            if hasattr(self.privilege_start_time, 'to_alipay_dict'):
                params['privilege_start_time'] = self.privilege_start_time.to_alipay_dict()
            else:
                params['privilege_start_time'] = self.privilege_start_time
        if self.privilege_tags:
            if hasattr(self.privilege_tags, 'to_alipay_dict'):
                params['privilege_tags'] = self.privilege_tags.to_alipay_dict()
            else:
                params['privilege_tags'] = self.privilege_tags
        if self.product_desc:
            if hasattr(self.product_desc, 'to_alipay_dict'):
                params['product_desc'] = self.product_desc.to_alipay_dict()
            else:
                params['product_desc'] = self.product_desc
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.service_category_id:
            if hasattr(self.service_category_id, 'to_alipay_dict'):
                params['service_category_id'] = self.service_category_id.to_alipay_dict()
            else:
                params['service_category_id'] = self.service_category_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaitainShopProduct()
        if 'off_price' in d:
            o.off_price = d['off_price']
        if 'orig_price' in d:
            o.orig_price = d['orig_price']
        if 'out_privilege_id' in d:
            o.out_privilege_id = d['out_privilege_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'privilege_close_time' in d:
            o.privilege_close_time = d['privilege_close_time']
        if 'privilege_price' in d:
            o.privilege_price = d['privilege_price']
        if 'privilege_start_time' in d:
            o.privilege_start_time = d['privilege_start_time']
        if 'privilege_tags' in d:
            o.privilege_tags = d['privilege_tags']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'service_category_id' in d:
            o.service_category_id = d['service_category_id']
        if 'status' in d:
            o.status = d['status']
        return o


