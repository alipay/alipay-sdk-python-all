#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NameOuterIdPair import NameOuterIdPair
from alipay.aop.api.domain.NameOuterIdPair import NameOuterIdPair


class KbPosOrderDishDetail(object):

    def __init__(self):
        self._change_price = None
        self._change_reason = None
        self._cook_id = None
        self._cook_version = None
        self._discountable = None
        self._dish_id = None
        self._dish_name = None
        self._dish_num = None
        self._dish_unit = None
        self._dish_version = None
        self._ext_info = None
        self._has_change = None
        self._main_flag = None
        self._main_out_detail_no = None
        self._make_status = None
        self._member_price = None
        self._memo = None
        self._operator = None
        self._order_time = None
        self._out_detail_no = None
        self._outer_id = None
        self._practice_info = None
        self._practice_price = None
        self._refund_reason = None
        self._refund_time = None
        self._remind_time = None
        self._sales_properties = None
        self._sales_properties_ext = None
        self._sell_price = None
        self._sku_id = None
        self._sort = None
        self._spec_name = None
        self._spec_name_ext = None
        self._type = None
        self._user_identity = None
        self._wake_status = None

    @property
    def change_price(self):
        return self._change_price

    @change_price.setter
    def change_price(self, value):
        self._change_price = value
    @property
    def change_reason(self):
        return self._change_reason

    @change_reason.setter
    def change_reason(self, value):
        self._change_reason = value
    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def cook_version(self):
        return self._cook_version

    @cook_version.setter
    def cook_version(self, value):
        self._cook_version = value
    @property
    def discountable(self):
        return self._discountable

    @discountable.setter
    def discountable(self, value):
        self._discountable = value
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
    def dish_num(self):
        return self._dish_num

    @dish_num.setter
    def dish_num(self, value):
        self._dish_num = value
    @property
    def dish_unit(self):
        return self._dish_unit

    @dish_unit.setter
    def dish_unit(self, value):
        self._dish_unit = value
    @property
    def dish_version(self):
        return self._dish_version

    @dish_version.setter
    def dish_version(self, value):
        self._dish_version = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def has_change(self):
        return self._has_change

    @has_change.setter
    def has_change(self, value):
        self._has_change = value
    @property
    def main_flag(self):
        return self._main_flag

    @main_flag.setter
    def main_flag(self, value):
        self._main_flag = value
    @property
    def main_out_detail_no(self):
        return self._main_out_detail_no

    @main_out_detail_no.setter
    def main_out_detail_no(self, value):
        self._main_out_detail_no = value
    @property
    def make_status(self):
        return self._make_status

    @make_status.setter
    def make_status(self, value):
        self._make_status = value
    @property
    def member_price(self):
        return self._member_price

    @member_price.setter
    def member_price(self, value):
        self._member_price = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_detail_no(self):
        return self._out_detail_no

    @out_detail_no.setter
    def out_detail_no(self, value):
        self._out_detail_no = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def practice_info(self):
        return self._practice_info

    @practice_info.setter
    def practice_info(self, value):
        self._practice_info = value
    @property
    def practice_price(self):
        return self._practice_price

    @practice_price.setter
    def practice_price(self, value):
        self._practice_price = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def remind_time(self):
        return self._remind_time

    @remind_time.setter
    def remind_time(self, value):
        self._remind_time = value
    @property
    def sales_properties(self):
        return self._sales_properties

    @sales_properties.setter
    def sales_properties(self, value):
        self._sales_properties = value
    @property
    def sales_properties_ext(self):
        return self._sales_properties_ext

    @sales_properties_ext.setter
    def sales_properties_ext(self, value):
        if isinstance(value, list):
            self._sales_properties_ext = list()
            for i in value:
                if isinstance(i, NameOuterIdPair):
                    self._sales_properties_ext.append(i)
                else:
                    self._sales_properties_ext.append(NameOuterIdPair.from_alipay_dict(i))
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def spec_name_ext(self):
        return self._spec_name_ext

    @spec_name_ext.setter
    def spec_name_ext(self, value):
        if isinstance(value, list):
            self._spec_name_ext = list()
            for i in value:
                if isinstance(i, NameOuterIdPair):
                    self._spec_name_ext.append(i)
                else:
                    self._spec_name_ext.append(NameOuterIdPair.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_identity(self):
        return self._user_identity

    @user_identity.setter
    def user_identity(self, value):
        self._user_identity = value
    @property
    def wake_status(self):
        return self._wake_status

    @wake_status.setter
    def wake_status(self, value):
        self._wake_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_price:
            if hasattr(self.change_price, 'to_alipay_dict'):
                params['change_price'] = self.change_price.to_alipay_dict()
            else:
                params['change_price'] = self.change_price
        if self.change_reason:
            if hasattr(self.change_reason, 'to_alipay_dict'):
                params['change_reason'] = self.change_reason.to_alipay_dict()
            else:
                params['change_reason'] = self.change_reason
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.cook_version:
            if hasattr(self.cook_version, 'to_alipay_dict'):
                params['cook_version'] = self.cook_version.to_alipay_dict()
            else:
                params['cook_version'] = self.cook_version
        if self.discountable:
            if hasattr(self.discountable, 'to_alipay_dict'):
                params['discountable'] = self.discountable.to_alipay_dict()
            else:
                params['discountable'] = self.discountable
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
        if self.dish_num:
            if hasattr(self.dish_num, 'to_alipay_dict'):
                params['dish_num'] = self.dish_num.to_alipay_dict()
            else:
                params['dish_num'] = self.dish_num
        if self.dish_unit:
            if hasattr(self.dish_unit, 'to_alipay_dict'):
                params['dish_unit'] = self.dish_unit.to_alipay_dict()
            else:
                params['dish_unit'] = self.dish_unit
        if self.dish_version:
            if hasattr(self.dish_version, 'to_alipay_dict'):
                params['dish_version'] = self.dish_version.to_alipay_dict()
            else:
                params['dish_version'] = self.dish_version
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.has_change:
            if hasattr(self.has_change, 'to_alipay_dict'):
                params['has_change'] = self.has_change.to_alipay_dict()
            else:
                params['has_change'] = self.has_change
        if self.main_flag:
            if hasattr(self.main_flag, 'to_alipay_dict'):
                params['main_flag'] = self.main_flag.to_alipay_dict()
            else:
                params['main_flag'] = self.main_flag
        if self.main_out_detail_no:
            if hasattr(self.main_out_detail_no, 'to_alipay_dict'):
                params['main_out_detail_no'] = self.main_out_detail_no.to_alipay_dict()
            else:
                params['main_out_detail_no'] = self.main_out_detail_no
        if self.make_status:
            if hasattr(self.make_status, 'to_alipay_dict'):
                params['make_status'] = self.make_status.to_alipay_dict()
            else:
                params['make_status'] = self.make_status
        if self.member_price:
            if hasattr(self.member_price, 'to_alipay_dict'):
                params['member_price'] = self.member_price.to_alipay_dict()
            else:
                params['member_price'] = self.member_price
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_detail_no:
            if hasattr(self.out_detail_no, 'to_alipay_dict'):
                params['out_detail_no'] = self.out_detail_no.to_alipay_dict()
            else:
                params['out_detail_no'] = self.out_detail_no
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        if self.practice_info:
            if hasattr(self.practice_info, 'to_alipay_dict'):
                params['practice_info'] = self.practice_info.to_alipay_dict()
            else:
                params['practice_info'] = self.practice_info
        if self.practice_price:
            if hasattr(self.practice_price, 'to_alipay_dict'):
                params['practice_price'] = self.practice_price.to_alipay_dict()
            else:
                params['practice_price'] = self.practice_price
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.remind_time:
            if hasattr(self.remind_time, 'to_alipay_dict'):
                params['remind_time'] = self.remind_time.to_alipay_dict()
            else:
                params['remind_time'] = self.remind_time
        if self.sales_properties:
            if hasattr(self.sales_properties, 'to_alipay_dict'):
                params['sales_properties'] = self.sales_properties.to_alipay_dict()
            else:
                params['sales_properties'] = self.sales_properties
        if self.sales_properties_ext:
            if isinstance(self.sales_properties_ext, list):
                for i in range(0, len(self.sales_properties_ext)):
                    element = self.sales_properties_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sales_properties_ext[i] = element.to_alipay_dict()
            if hasattr(self.sales_properties_ext, 'to_alipay_dict'):
                params['sales_properties_ext'] = self.sales_properties_ext.to_alipay_dict()
            else:
                params['sales_properties_ext'] = self.sales_properties_ext
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.spec_name_ext:
            if isinstance(self.spec_name_ext, list):
                for i in range(0, len(self.spec_name_ext)):
                    element = self.spec_name_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.spec_name_ext[i] = element.to_alipay_dict()
            if hasattr(self.spec_name_ext, 'to_alipay_dict'):
                params['spec_name_ext'] = self.spec_name_ext.to_alipay_dict()
            else:
                params['spec_name_ext'] = self.spec_name_ext
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_identity:
            if hasattr(self.user_identity, 'to_alipay_dict'):
                params['user_identity'] = self.user_identity.to_alipay_dict()
            else:
                params['user_identity'] = self.user_identity
        if self.wake_status:
            if hasattr(self.wake_status, 'to_alipay_dict'):
                params['wake_status'] = self.wake_status.to_alipay_dict()
            else:
                params['wake_status'] = self.wake_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbPosOrderDishDetail()
        if 'change_price' in d:
            o.change_price = d['change_price']
        if 'change_reason' in d:
            o.change_reason = d['change_reason']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'cook_version' in d:
            o.cook_version = d['cook_version']
        if 'discountable' in d:
            o.discountable = d['discountable']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_num' in d:
            o.dish_num = d['dish_num']
        if 'dish_unit' in d:
            o.dish_unit = d['dish_unit']
        if 'dish_version' in d:
            o.dish_version = d['dish_version']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'has_change' in d:
            o.has_change = d['has_change']
        if 'main_flag' in d:
            o.main_flag = d['main_flag']
        if 'main_out_detail_no' in d:
            o.main_out_detail_no = d['main_out_detail_no']
        if 'make_status' in d:
            o.make_status = d['make_status']
        if 'member_price' in d:
            o.member_price = d['member_price']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_detail_no' in d:
            o.out_detail_no = d['out_detail_no']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'practice_info' in d:
            o.practice_info = d['practice_info']
        if 'practice_price' in d:
            o.practice_price = d['practice_price']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'remind_time' in d:
            o.remind_time = d['remind_time']
        if 'sales_properties' in d:
            o.sales_properties = d['sales_properties']
        if 'sales_properties_ext' in d:
            o.sales_properties_ext = d['sales_properties_ext']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sort' in d:
            o.sort = d['sort']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'spec_name_ext' in d:
            o.spec_name_ext = d['spec_name_ext']
        if 'type' in d:
            o.type = d['type']
        if 'user_identity' in d:
            o.user_identity = d['user_identity']
        if 'wake_status' in d:
            o.wake_status = d['wake_status']
        return o


