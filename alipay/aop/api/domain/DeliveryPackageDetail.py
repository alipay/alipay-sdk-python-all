#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryPackageDetail(object):

    def __init__(self):
        self._express_code = None
        self._gmt_create = None
        self._gmt_modified = None
        self._goods_code = None
        self._goods_quantity = None
        self._package_code = None

    @property
    def express_code(self):
        return self._express_code

    @express_code.setter
    def express_code(self, value):
        self._express_code = value
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
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def goods_quantity(self):
        return self._goods_quantity

    @goods_quantity.setter
    def goods_quantity(self, value):
        self._goods_quantity = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_code:
            if hasattr(self.express_code, 'to_alipay_dict'):
                params['express_code'] = self.express_code.to_alipay_dict()
            else:
                params['express_code'] = self.express_code
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
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.goods_quantity:
            if hasattr(self.goods_quantity, 'to_alipay_dict'):
                params['goods_quantity'] = self.goods_quantity.to_alipay_dict()
            else:
                params['goods_quantity'] = self.goods_quantity
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryPackageDetail()
        if 'express_code' in d:
            o.express_code = d['express_code']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'goods_quantity' in d:
            o.goods_quantity = d['goods_quantity']
        if 'package_code' in d:
            o.package_code = d['package_code']
        return o


