#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddServicesInfo import AddServicesInfo
from alipay.aop.api.domain.PlatformDrugInfo import PlatformDrugInfo


class AlipayCommerceMedicalIndustrydataDrugorderSyncModel(object):

    def __init__(self):
        self._add_services = None
        self._alipay_open_id = None
        self._alipay_order_id = None
        self._alipay_prescription_id = None
        self._alipay_user_id = None
        self._comments = None
        self._drug_list = None
        self._drug_order_create_time = None
        self._drug_order_pay_time = None
        self._drug_order_price = None
        self._drug_order_price_real = None
        self._drug_order_source = None
        self._drug_order_status = None
        self._merchant_user_id = None
        self._out_drug_order_id = None
        self._out_drug_order_url = None
        self._out_order_id = None
        self._out_prescription_id = None
        self._pharmacy_id = None
        self._pharmacy_name = None
        self._platform_code = None
        self._receiver_address = None
        self._receiver_name = None
        self._receiver_phone = None

    @property
    def add_services(self):
        return self._add_services

    @add_services.setter
    def add_services(self, value):
        if isinstance(value, list):
            self._add_services = list()
            for i in value:
                if isinstance(i, AddServicesInfo):
                    self._add_services.append(i)
                else:
                    self._add_services.append(AddServicesInfo.from_alipay_dict(i))
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_prescription_id(self):
        return self._alipay_prescription_id

    @alipay_prescription_id.setter
    def alipay_prescription_id(self, value):
        self._alipay_prescription_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value
    @property
    def drug_list(self):
        return self._drug_list

    @drug_list.setter
    def drug_list(self, value):
        if isinstance(value, list):
            self._drug_list = list()
            for i in value:
                if isinstance(i, PlatformDrugInfo):
                    self._drug_list.append(i)
                else:
                    self._drug_list.append(PlatformDrugInfo.from_alipay_dict(i))
    @property
    def drug_order_create_time(self):
        return self._drug_order_create_time

    @drug_order_create_time.setter
    def drug_order_create_time(self, value):
        self._drug_order_create_time = value
    @property
    def drug_order_pay_time(self):
        return self._drug_order_pay_time

    @drug_order_pay_time.setter
    def drug_order_pay_time(self, value):
        self._drug_order_pay_time = value
    @property
    def drug_order_price(self):
        return self._drug_order_price

    @drug_order_price.setter
    def drug_order_price(self, value):
        self._drug_order_price = value
    @property
    def drug_order_price_real(self):
        return self._drug_order_price_real

    @drug_order_price_real.setter
    def drug_order_price_real(self, value):
        self._drug_order_price_real = value
    @property
    def drug_order_source(self):
        return self._drug_order_source

    @drug_order_source.setter
    def drug_order_source(self, value):
        self._drug_order_source = value
    @property
    def drug_order_status(self):
        return self._drug_order_status

    @drug_order_status.setter
    def drug_order_status(self, value):
        self._drug_order_status = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def out_drug_order_id(self):
        return self._out_drug_order_id

    @out_drug_order_id.setter
    def out_drug_order_id(self, value):
        self._out_drug_order_id = value
    @property
    def out_drug_order_url(self):
        return self._out_drug_order_url

    @out_drug_order_url.setter
    def out_drug_order_url(self, value):
        self._out_drug_order_url = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_prescription_id(self):
        return self._out_prescription_id

    @out_prescription_id.setter
    def out_prescription_id(self, value):
        self._out_prescription_id = value
    @property
    def pharmacy_id(self):
        return self._pharmacy_id

    @pharmacy_id.setter
    def pharmacy_id(self, value):
        self._pharmacy_id = value
    @property
    def pharmacy_name(self):
        return self._pharmacy_name

    @pharmacy_name.setter
    def pharmacy_name(self, value):
        self._pharmacy_name = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.add_services:
            if isinstance(self.add_services, list):
                for i in range(0, len(self.add_services)):
                    element = self.add_services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_services[i] = element.to_alipay_dict()
            if hasattr(self.add_services, 'to_alipay_dict'):
                params['add_services'] = self.add_services.to_alipay_dict()
            else:
                params['add_services'] = self.add_services
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.alipay_prescription_id:
            if hasattr(self.alipay_prescription_id, 'to_alipay_dict'):
                params['alipay_prescription_id'] = self.alipay_prescription_id.to_alipay_dict()
            else:
                params['alipay_prescription_id'] = self.alipay_prescription_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.comments:
            if hasattr(self.comments, 'to_alipay_dict'):
                params['comments'] = self.comments.to_alipay_dict()
            else:
                params['comments'] = self.comments
        if self.drug_list:
            if isinstance(self.drug_list, list):
                for i in range(0, len(self.drug_list)):
                    element = self.drug_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drug_list[i] = element.to_alipay_dict()
            if hasattr(self.drug_list, 'to_alipay_dict'):
                params['drug_list'] = self.drug_list.to_alipay_dict()
            else:
                params['drug_list'] = self.drug_list
        if self.drug_order_create_time:
            if hasattr(self.drug_order_create_time, 'to_alipay_dict'):
                params['drug_order_create_time'] = self.drug_order_create_time.to_alipay_dict()
            else:
                params['drug_order_create_time'] = self.drug_order_create_time
        if self.drug_order_pay_time:
            if hasattr(self.drug_order_pay_time, 'to_alipay_dict'):
                params['drug_order_pay_time'] = self.drug_order_pay_time.to_alipay_dict()
            else:
                params['drug_order_pay_time'] = self.drug_order_pay_time
        if self.drug_order_price:
            if hasattr(self.drug_order_price, 'to_alipay_dict'):
                params['drug_order_price'] = self.drug_order_price.to_alipay_dict()
            else:
                params['drug_order_price'] = self.drug_order_price
        if self.drug_order_price_real:
            if hasattr(self.drug_order_price_real, 'to_alipay_dict'):
                params['drug_order_price_real'] = self.drug_order_price_real.to_alipay_dict()
            else:
                params['drug_order_price_real'] = self.drug_order_price_real
        if self.drug_order_source:
            if hasattr(self.drug_order_source, 'to_alipay_dict'):
                params['drug_order_source'] = self.drug_order_source.to_alipay_dict()
            else:
                params['drug_order_source'] = self.drug_order_source
        if self.drug_order_status:
            if hasattr(self.drug_order_status, 'to_alipay_dict'):
                params['drug_order_status'] = self.drug_order_status.to_alipay_dict()
            else:
                params['drug_order_status'] = self.drug_order_status
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.out_drug_order_id:
            if hasattr(self.out_drug_order_id, 'to_alipay_dict'):
                params['out_drug_order_id'] = self.out_drug_order_id.to_alipay_dict()
            else:
                params['out_drug_order_id'] = self.out_drug_order_id
        if self.out_drug_order_url:
            if hasattr(self.out_drug_order_url, 'to_alipay_dict'):
                params['out_drug_order_url'] = self.out_drug_order_url.to_alipay_dict()
            else:
                params['out_drug_order_url'] = self.out_drug_order_url
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_prescription_id:
            if hasattr(self.out_prescription_id, 'to_alipay_dict'):
                params['out_prescription_id'] = self.out_prescription_id.to_alipay_dict()
            else:
                params['out_prescription_id'] = self.out_prescription_id
        if self.pharmacy_id:
            if hasattr(self.pharmacy_id, 'to_alipay_dict'):
                params['pharmacy_id'] = self.pharmacy_id.to_alipay_dict()
            else:
                params['pharmacy_id'] = self.pharmacy_id
        if self.pharmacy_name:
            if hasattr(self.pharmacy_name, 'to_alipay_dict'):
                params['pharmacy_name'] = self.pharmacy_name.to_alipay_dict()
            else:
                params['pharmacy_name'] = self.pharmacy_name
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataDrugorderSyncModel()
        if 'add_services' in d:
            o.add_services = d['add_services']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'alipay_prescription_id' in d:
            o.alipay_prescription_id = d['alipay_prescription_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'comments' in d:
            o.comments = d['comments']
        if 'drug_list' in d:
            o.drug_list = d['drug_list']
        if 'drug_order_create_time' in d:
            o.drug_order_create_time = d['drug_order_create_time']
        if 'drug_order_pay_time' in d:
            o.drug_order_pay_time = d['drug_order_pay_time']
        if 'drug_order_price' in d:
            o.drug_order_price = d['drug_order_price']
        if 'drug_order_price_real' in d:
            o.drug_order_price_real = d['drug_order_price_real']
        if 'drug_order_source' in d:
            o.drug_order_source = d['drug_order_source']
        if 'drug_order_status' in d:
            o.drug_order_status = d['drug_order_status']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'out_drug_order_id' in d:
            o.out_drug_order_id = d['out_drug_order_id']
        if 'out_drug_order_url' in d:
            o.out_drug_order_url = d['out_drug_order_url']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_prescription_id' in d:
            o.out_prescription_id = d['out_prescription_id']
        if 'pharmacy_id' in d:
            o.pharmacy_id = d['pharmacy_id']
        if 'pharmacy_name' in d:
            o.pharmacy_name = d['pharmacy_name']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        return o


