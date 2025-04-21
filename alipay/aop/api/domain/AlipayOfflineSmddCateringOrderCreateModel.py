#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBean import ActivityBean
from alipay.aop.api.domain.CodeExtBean import CodeExtBean
from alipay.aop.api.domain.RequireBean import RequireBean
from alipay.aop.api.domain.SkuBean import SkuBean


class AlipayOfflineSmddCateringOrderCreateModel(object):

    def __init__(self):
        self._activity_list = None
        self._buyer_id = None
        self._code_ext = None
        self._dining_number = None
        self._memo = None
        self._out_biz_type = None
        self._out_order_id = None
        self._request_stamp = None
        self._require_info_list = None
        self._shop_id = None
        self._sku_list = None
        self._view_delivery_cost = None
        self._view_total_price = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, ActivityBean):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(ActivityBean.from_alipay_dict(i))
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def code_ext(self):
        return self._code_ext

    @code_ext.setter
    def code_ext(self, value):
        if isinstance(value, CodeExtBean):
            self._code_ext = value
        else:
            self._code_ext = CodeExtBean.from_alipay_dict(value)
    @property
    def dining_number(self):
        return self._dining_number

    @dining_number.setter
    def dining_number(self, value):
        self._dining_number = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def request_stamp(self):
        return self._request_stamp

    @request_stamp.setter
    def request_stamp(self, value):
        self._request_stamp = value
    @property
    def require_info_list(self):
        return self._require_info_list

    @require_info_list.setter
    def require_info_list(self, value):
        if isinstance(value, list):
            self._require_info_list = list()
            for i in value:
                if isinstance(i, RequireBean):
                    self._require_info_list.append(i)
                else:
                    self._require_info_list.append(RequireBean.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuBean):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuBean.from_alipay_dict(i))
    @property
    def view_delivery_cost(self):
        return self._view_delivery_cost

    @view_delivery_cost.setter
    def view_delivery_cost(self, value):
        self._view_delivery_cost = value
    @property
    def view_total_price(self):
        return self._view_total_price

    @view_total_price.setter
    def view_total_price(self, value):
        self._view_total_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_list:
            if isinstance(self.activity_list, list):
                for i in range(0, len(self.activity_list)):
                    element = self.activity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_list, 'to_alipay_dict'):
                params['activity_list'] = self.activity_list.to_alipay_dict()
            else:
                params['activity_list'] = self.activity_list
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.code_ext:
            if hasattr(self.code_ext, 'to_alipay_dict'):
                params['code_ext'] = self.code_ext.to_alipay_dict()
            else:
                params['code_ext'] = self.code_ext
        if self.dining_number:
            if hasattr(self.dining_number, 'to_alipay_dict'):
                params['dining_number'] = self.dining_number.to_alipay_dict()
            else:
                params['dining_number'] = self.dining_number
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.request_stamp:
            if hasattr(self.request_stamp, 'to_alipay_dict'):
                params['request_stamp'] = self.request_stamp.to_alipay_dict()
            else:
                params['request_stamp'] = self.request_stamp
        if self.require_info_list:
            if isinstance(self.require_info_list, list):
                for i in range(0, len(self.require_info_list)):
                    element = self.require_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.require_info_list[i] = element.to_alipay_dict()
            if hasattr(self.require_info_list, 'to_alipay_dict'):
                params['require_info_list'] = self.require_info_list.to_alipay_dict()
            else:
                params['require_info_list'] = self.require_info_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.view_delivery_cost:
            if hasattr(self.view_delivery_cost, 'to_alipay_dict'):
                params['view_delivery_cost'] = self.view_delivery_cost.to_alipay_dict()
            else:
                params['view_delivery_cost'] = self.view_delivery_cost
        if self.view_total_price:
            if hasattr(self.view_total_price, 'to_alipay_dict'):
                params['view_total_price'] = self.view_total_price.to_alipay_dict()
            else:
                params['view_total_price'] = self.view_total_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddCateringOrderCreateModel()
        if 'activity_list' in d:
            o.activity_list = d['activity_list']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'code_ext' in d:
            o.code_ext = d['code_ext']
        if 'dining_number' in d:
            o.dining_number = d['dining_number']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'request_stamp' in d:
            o.request_stamp = d['request_stamp']
        if 'require_info_list' in d:
            o.require_info_list = d['require_info_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'view_delivery_cost' in d:
            o.view_delivery_cost = d['view_delivery_cost']
        if 'view_total_price' in d:
            o.view_total_price = d['view_total_price']
        return o


