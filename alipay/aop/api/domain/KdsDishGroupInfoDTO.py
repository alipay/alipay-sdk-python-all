#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KdsDishGroupInfoDTO(object):

    def __init__(self):
        self._cook_cost = None
        self._dish_id = None
        self._dish_name = None
        self._dish_sku_id = None
        self._dish_time = None
        self._dish_unit = None
        self._ext_info = None
        self._max_cook_num = None
        self._memo = None
        self._out_dish_id = None
        self._out_dish_info = None
        self._out_dish_sku_id = None
        self._out_parent_id = None
        self._practice_desc = None
        self._practice_id = None
        self._quantity = None
        self._sales_properties = None
        self._sku_spec_desc = None
        self._spec_id = None
        self._type = None

    @property
    def cook_cost(self):
        return self._cook_cost

    @cook_cost.setter
    def cook_cost(self, value):
        self._cook_cost = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_sku_id(self):
        return self._dish_sku_id

    @dish_sku_id.setter
    def dish_sku_id(self, value):
        self._dish_sku_id = value
    @property
    def dish_time(self):
        return self._dish_time

    @dish_time.setter
    def dish_time(self, value):
        self._dish_time = value
    @property
    def dish_unit(self):
        return self._dish_unit

    @dish_unit.setter
    def dish_unit(self, value):
        self._dish_unit = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def max_cook_num(self):
        return self._max_cook_num

    @max_cook_num.setter
    def max_cook_num(self, value):
        self._max_cook_num = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_dish_info(self):
        return self._out_dish_info

    @out_dish_info.setter
    def out_dish_info(self, value):
        self._out_dish_info = value
    @property
    def out_dish_sku_id(self):
        return self._out_dish_sku_id

    @out_dish_sku_id.setter
    def out_dish_sku_id(self, value):
        self._out_dish_sku_id = value
    @property
    def out_parent_id(self):
        return self._out_parent_id

    @out_parent_id.setter
    def out_parent_id(self, value):
        self._out_parent_id = value
    @property
    def practice_desc(self):
        return self._practice_desc

    @practice_desc.setter
    def practice_desc(self, value):
        self._practice_desc = value
    @property
    def practice_id(self):
        return self._practice_id

    @practice_id.setter
    def practice_id(self, value):
        self._practice_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sales_properties(self):
        return self._sales_properties

    @sales_properties.setter
    def sales_properties(self, value):
        self._sales_properties = value
    @property
    def sku_spec_desc(self):
        return self._sku_spec_desc

    @sku_spec_desc.setter
    def sku_spec_desc(self, value):
        self._sku_spec_desc = value
    @property
    def spec_id(self):
        return self._spec_id

    @spec_id.setter
    def spec_id(self, value):
        self._spec_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_cost:
            if hasattr(self.cook_cost, 'to_alipay_dict'):
                params['cook_cost'] = self.cook_cost.to_alipay_dict()
            else:
                params['cook_cost'] = self.cook_cost
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_sku_id:
            if hasattr(self.dish_sku_id, 'to_alipay_dict'):
                params['dish_sku_id'] = self.dish_sku_id.to_alipay_dict()
            else:
                params['dish_sku_id'] = self.dish_sku_id
        if self.dish_time:
            if hasattr(self.dish_time, 'to_alipay_dict'):
                params['dish_time'] = self.dish_time.to_alipay_dict()
            else:
                params['dish_time'] = self.dish_time
        if self.dish_unit:
            if hasattr(self.dish_unit, 'to_alipay_dict'):
                params['dish_unit'] = self.dish_unit.to_alipay_dict()
            else:
                params['dish_unit'] = self.dish_unit
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.max_cook_num:
            if hasattr(self.max_cook_num, 'to_alipay_dict'):
                params['max_cook_num'] = self.max_cook_num.to_alipay_dict()
            else:
                params['max_cook_num'] = self.max_cook_num
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_dish_info:
            if hasattr(self.out_dish_info, 'to_alipay_dict'):
                params['out_dish_info'] = self.out_dish_info.to_alipay_dict()
            else:
                params['out_dish_info'] = self.out_dish_info
        if self.out_dish_sku_id:
            if hasattr(self.out_dish_sku_id, 'to_alipay_dict'):
                params['out_dish_sku_id'] = self.out_dish_sku_id.to_alipay_dict()
            else:
                params['out_dish_sku_id'] = self.out_dish_sku_id
        if self.out_parent_id:
            if hasattr(self.out_parent_id, 'to_alipay_dict'):
                params['out_parent_id'] = self.out_parent_id.to_alipay_dict()
            else:
                params['out_parent_id'] = self.out_parent_id
        if self.practice_desc:
            if hasattr(self.practice_desc, 'to_alipay_dict'):
                params['practice_desc'] = self.practice_desc.to_alipay_dict()
            else:
                params['practice_desc'] = self.practice_desc
        if self.practice_id:
            if hasattr(self.practice_id, 'to_alipay_dict'):
                params['practice_id'] = self.practice_id.to_alipay_dict()
            else:
                params['practice_id'] = self.practice_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sales_properties:
            if hasattr(self.sales_properties, 'to_alipay_dict'):
                params['sales_properties'] = self.sales_properties.to_alipay_dict()
            else:
                params['sales_properties'] = self.sales_properties
        if self.sku_spec_desc:
            if hasattr(self.sku_spec_desc, 'to_alipay_dict'):
                params['sku_spec_desc'] = self.sku_spec_desc.to_alipay_dict()
            else:
                params['sku_spec_desc'] = self.sku_spec_desc
        if self.spec_id:
            if hasattr(self.spec_id, 'to_alipay_dict'):
                params['spec_id'] = self.spec_id.to_alipay_dict()
            else:
                params['spec_id'] = self.spec_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KdsDishGroupInfoDTO()
        if 'cook_cost' in d:
            o.cook_cost = d['cook_cost']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_sku_id' in d:
            o.dish_sku_id = d['dish_sku_id']
        if 'dish_time' in d:
            o.dish_time = d['dish_time']
        if 'dish_unit' in d:
            o.dish_unit = d['dish_unit']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'max_cook_num' in d:
            o.max_cook_num = d['max_cook_num']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_dish_info' in d:
            o.out_dish_info = d['out_dish_info']
        if 'out_dish_sku_id' in d:
            o.out_dish_sku_id = d['out_dish_sku_id']
        if 'out_parent_id' in d:
            o.out_parent_id = d['out_parent_id']
        if 'practice_desc' in d:
            o.practice_desc = d['practice_desc']
        if 'practice_id' in d:
            o.practice_id = d['practice_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sales_properties' in d:
            o.sales_properties = d['sales_properties']
        if 'sku_spec_desc' in d:
            o.sku_spec_desc = d['sku_spec_desc']
        if 'spec_id' in d:
            o.spec_id = d['spec_id']
        if 'type' in d:
            o.type = d['type']
        return o


