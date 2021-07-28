#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IoTBPaaSMerchantOrderItemInfo import IoTBPaaSMerchantOrderItemInfo
from alipay.aop.api.domain.IoTBPaaSMerchantOrderItemInfo import IoTBPaaSMerchantOrderItemInfo
from alipay.aop.api.domain.IoTBPaaSMerchantOrderRequireInfo import IoTBPaaSMerchantOrderRequireInfo


class IoTBPaaSMerchantOrderInfo(object):

    def __init__(self):
        self._activity_item_list = None
        self._courier_fee = None
        self._gender = None
        self._order_address = None
        self._order_contact = None
        self._order_id = None
        self._order_item_list = None
        self._order_item_total_quantity = None
        self._order_memo = None
        self._order_num = None
        self._order_price = None
        self._order_real_price = None
        self._order_time = None
        self._order_type = None
        self._package_fee = None
        self._require_info_list = None
        self._shop_name = None
        self._table_name = None
        self._user_name = None

    @property
    def activity_item_list(self):
        return self._activity_item_list

    @activity_item_list.setter
    def activity_item_list(self, value):
        if isinstance(value, list):
            self._activity_item_list = list()
            for i in value:
                if isinstance(i, IoTBPaaSMerchantOrderItemInfo):
                    self._activity_item_list.append(i)
                else:
                    self._activity_item_list.append(IoTBPaaSMerchantOrderItemInfo.from_alipay_dict(i))
    @property
    def courier_fee(self):
        return self._courier_fee

    @courier_fee.setter
    def courier_fee(self, value):
        self._courier_fee = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def order_address(self):
        return self._order_address

    @order_address.setter
    def order_address(self, value):
        self._order_address = value
    @property
    def order_contact(self):
        return self._order_contact

    @order_contact.setter
    def order_contact(self, value):
        self._order_contact = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, value):
        if isinstance(value, list):
            self._order_item_list = list()
            for i in value:
                if isinstance(i, IoTBPaaSMerchantOrderItemInfo):
                    self._order_item_list.append(i)
                else:
                    self._order_item_list.append(IoTBPaaSMerchantOrderItemInfo.from_alipay_dict(i))
    @property
    def order_item_total_quantity(self):
        return self._order_item_total_quantity

    @order_item_total_quantity.setter
    def order_item_total_quantity(self, value):
        self._order_item_total_quantity = value
    @property
    def order_memo(self):
        return self._order_memo

    @order_memo.setter
    def order_memo(self, value):
        self._order_memo = value
    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, value):
        self._order_num = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def order_real_price(self):
        return self._order_real_price

    @order_real_price.setter
    def order_real_price(self, value):
        self._order_real_price = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def package_fee(self):
        return self._package_fee

    @package_fee.setter
    def package_fee(self, value):
        self._package_fee = value
    @property
    def require_info_list(self):
        return self._require_info_list

    @require_info_list.setter
    def require_info_list(self, value):
        if isinstance(value, list):
            self._require_info_list = list()
            for i in value:
                if isinstance(i, IoTBPaaSMerchantOrderRequireInfo):
                    self._require_info_list.append(i)
                else:
                    self._require_info_list.append(IoTBPaaSMerchantOrderRequireInfo.from_alipay_dict(i))
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_item_list:
            if isinstance(self.activity_item_list, list):
                for i in range(0, len(self.activity_item_list)):
                    element = self.activity_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_item_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_item_list, 'to_alipay_dict'):
                params['activity_item_list'] = self.activity_item_list.to_alipay_dict()
            else:
                params['activity_item_list'] = self.activity_item_list
        if self.courier_fee:
            if hasattr(self.courier_fee, 'to_alipay_dict'):
                params['courier_fee'] = self.courier_fee.to_alipay_dict()
            else:
                params['courier_fee'] = self.courier_fee
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.order_address:
            if hasattr(self.order_address, 'to_alipay_dict'):
                params['order_address'] = self.order_address.to_alipay_dict()
            else:
                params['order_address'] = self.order_address
        if self.order_contact:
            if hasattr(self.order_contact, 'to_alipay_dict'):
                params['order_contact'] = self.order_contact.to_alipay_dict()
            else:
                params['order_contact'] = self.order_contact
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_item_list:
            if isinstance(self.order_item_list, list):
                for i in range(0, len(self.order_item_list)):
                    element = self.order_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_item_list[i] = element.to_alipay_dict()
            if hasattr(self.order_item_list, 'to_alipay_dict'):
                params['order_item_list'] = self.order_item_list.to_alipay_dict()
            else:
                params['order_item_list'] = self.order_item_list
        if self.order_item_total_quantity:
            if hasattr(self.order_item_total_quantity, 'to_alipay_dict'):
                params['order_item_total_quantity'] = self.order_item_total_quantity.to_alipay_dict()
            else:
                params['order_item_total_quantity'] = self.order_item_total_quantity
        if self.order_memo:
            if hasattr(self.order_memo, 'to_alipay_dict'):
                params['order_memo'] = self.order_memo.to_alipay_dict()
            else:
                params['order_memo'] = self.order_memo
        if self.order_num:
            if hasattr(self.order_num, 'to_alipay_dict'):
                params['order_num'] = self.order_num.to_alipay_dict()
            else:
                params['order_num'] = self.order_num
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.order_real_price:
            if hasattr(self.order_real_price, 'to_alipay_dict'):
                params['order_real_price'] = self.order_real_price.to_alipay_dict()
            else:
                params['order_real_price'] = self.order_real_price
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.package_fee:
            if hasattr(self.package_fee, 'to_alipay_dict'):
                params['package_fee'] = self.package_fee.to_alipay_dict()
            else:
                params['package_fee'] = self.package_fee
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
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IoTBPaaSMerchantOrderInfo()
        if 'activity_item_list' in d:
            o.activity_item_list = d['activity_item_list']
        if 'courier_fee' in d:
            o.courier_fee = d['courier_fee']
        if 'gender' in d:
            o.gender = d['gender']
        if 'order_address' in d:
            o.order_address = d['order_address']
        if 'order_contact' in d:
            o.order_contact = d['order_contact']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_item_list' in d:
            o.order_item_list = d['order_item_list']
        if 'order_item_total_quantity' in d:
            o.order_item_total_quantity = d['order_item_total_quantity']
        if 'order_memo' in d:
            o.order_memo = d['order_memo']
        if 'order_num' in d:
            o.order_num = d['order_num']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'order_real_price' in d:
            o.order_real_price = d['order_real_price']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'package_fee' in d:
            o.package_fee = d['package_fee']
        if 'require_info_list' in d:
            o.require_info_list = d['require_info_list']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'table_name' in d:
            o.table_name = d['table_name']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


