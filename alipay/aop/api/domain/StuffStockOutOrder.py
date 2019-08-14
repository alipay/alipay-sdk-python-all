#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StuffStockOutOrderItem import StuffStockOutOrderItem


class StuffStockOutOrder(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._district_code = None
        self._district_name = None
        self._erp_order = None
        self._erp_order_type = None
        self._ext_info = None
        self._order_items = None
        self._province_code = None
        self._province_name = None
        self._receiver_address = None
        self._receiver_company = None
        self._receiver_name = None
        self._receiver_phone = None
        self._receiver_zip_code = None
        self._sf_order_type = None
        self._warehouse_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def erp_order(self):
        return self._erp_order

    @erp_order.setter
    def erp_order(self, value):
        self._erp_order = value
    @property
    def erp_order_type(self):
        return self._erp_order_type

    @erp_order_type.setter
    def erp_order_type(self, value):
        self._erp_order_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def order_items(self):
        return self._order_items

    @order_items.setter
    def order_items(self, value):
        if isinstance(value, list):
            self._order_items = list()
            for i in value:
                if isinstance(i, StuffStockOutOrderItem):
                    self._order_items.append(i)
                else:
                    self._order_items.append(StuffStockOutOrderItem.from_alipay_dict(i))
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_company(self):
        return self._receiver_company

    @receiver_company.setter
    def receiver_company(self, value):
        self._receiver_company = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value
    @property
    def receiver_zip_code(self):
        return self._receiver_zip_code

    @receiver_zip_code.setter
    def receiver_zip_code(self, value):
        self._receiver_zip_code = value
    @property
    def sf_order_type(self):
        return self._sf_order_type

    @sf_order_type.setter
    def sf_order_type(self, value):
        self._sf_order_type = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.erp_order:
            if hasattr(self.erp_order, 'to_alipay_dict'):
                params['erp_order'] = self.erp_order.to_alipay_dict()
            else:
                params['erp_order'] = self.erp_order
        if self.erp_order_type:
            if hasattr(self.erp_order_type, 'to_alipay_dict'):
                params['erp_order_type'] = self.erp_order_type.to_alipay_dict()
            else:
                params['erp_order_type'] = self.erp_order_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.order_items:
            if isinstance(self.order_items, list):
                for i in range(0, len(self.order_items)):
                    element = self.order_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_items[i] = element.to_alipay_dict()
            if hasattr(self.order_items, 'to_alipay_dict'):
                params['order_items'] = self.order_items.to_alipay_dict()
            else:
                params['order_items'] = self.order_items
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_company:
            if hasattr(self.receiver_company, 'to_alipay_dict'):
                params['receiver_company'] = self.receiver_company.to_alipay_dict()
            else:
                params['receiver_company'] = self.receiver_company
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        if self.receiver_zip_code:
            if hasattr(self.receiver_zip_code, 'to_alipay_dict'):
                params['receiver_zip_code'] = self.receiver_zip_code.to_alipay_dict()
            else:
                params['receiver_zip_code'] = self.receiver_zip_code
        if self.sf_order_type:
            if hasattr(self.sf_order_type, 'to_alipay_dict'):
                params['sf_order_type'] = self.sf_order_type.to_alipay_dict()
            else:
                params['sf_order_type'] = self.sf_order_type
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StuffStockOutOrder()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'erp_order' in d:
            o.erp_order = d['erp_order']
        if 'erp_order_type' in d:
            o.erp_order_type = d['erp_order_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'order_items' in d:
            o.order_items = d['order_items']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_company' in d:
            o.receiver_company = d['receiver_company']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'receiver_zip_code' in d:
            o.receiver_zip_code = d['receiver_zip_code']
        if 'sf_order_type' in d:
            o.sf_order_type = d['sf_order_type']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


