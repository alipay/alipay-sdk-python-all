#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CollaborateTask(object):

    def __init__(self):
        self._activity_desc = None
        self._activity_id = None
        self._activity_type = None
        self._address = None
        self._city_code = None
        self._city_name = None
        self._contact_name = None
        self._dispatched_time = None
        self._district_code = None
        self._district_name = None
        self._installer_no = None
        self._product_id = None
        self._product_name = None
        self._product_tags = None
        self._province_code = None
        self._province_name = None
        self._shop_name = None
        self._smid_list = None
        self._task_no = None
        self._task_tags = None
        self._tel = None

    @property
    def activity_desc(self):
        return self._activity_desc

    @activity_desc.setter
    def activity_desc(self, value):
        self._activity_desc = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def dispatched_time(self):
        return self._dispatched_time

    @dispatched_time.setter
    def dispatched_time(self, value):
        self._dispatched_time = value
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
    def installer_no(self):
        return self._installer_no

    @installer_no.setter
    def installer_no(self, value):
        self._installer_no = value
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
    def product_tags(self):
        return self._product_tags

    @product_tags.setter
    def product_tags(self, value):
        if isinstance(value, list):
            self._product_tags = list()
            for i in value:
                self._product_tags.append(i)
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
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def smid_list(self):
        return self._smid_list

    @smid_list.setter
    def smid_list(self, value):
        if isinstance(value, list):
            self._smid_list = list()
            for i in value:
                self._smid_list.append(i)
    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value
    @property
    def task_tags(self):
        return self._task_tags

    @task_tags.setter
    def task_tags(self, value):
        if isinstance(value, list):
            self._task_tags = list()
            for i in value:
                self._task_tags.append(i)
    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_desc:
            if hasattr(self.activity_desc, 'to_alipay_dict'):
                params['activity_desc'] = self.activity_desc.to_alipay_dict()
            else:
                params['activity_desc'] = self.activity_desc
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
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
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.dispatched_time:
            if hasattr(self.dispatched_time, 'to_alipay_dict'):
                params['dispatched_time'] = self.dispatched_time.to_alipay_dict()
            else:
                params['dispatched_time'] = self.dispatched_time
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
        if self.installer_no:
            if hasattr(self.installer_no, 'to_alipay_dict'):
                params['installer_no'] = self.installer_no.to_alipay_dict()
            else:
                params['installer_no'] = self.installer_no
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
        if self.product_tags:
            if isinstance(self.product_tags, list):
                for i in range(0, len(self.product_tags)):
                    element = self.product_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_tags[i] = element.to_alipay_dict()
            if hasattr(self.product_tags, 'to_alipay_dict'):
                params['product_tags'] = self.product_tags.to_alipay_dict()
            else:
                params['product_tags'] = self.product_tags
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
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.smid_list:
            if isinstance(self.smid_list, list):
                for i in range(0, len(self.smid_list)):
                    element = self.smid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.smid_list[i] = element.to_alipay_dict()
            if hasattr(self.smid_list, 'to_alipay_dict'):
                params['smid_list'] = self.smid_list.to_alipay_dict()
            else:
                params['smid_list'] = self.smid_list
        if self.task_no:
            if hasattr(self.task_no, 'to_alipay_dict'):
                params['task_no'] = self.task_no.to_alipay_dict()
            else:
                params['task_no'] = self.task_no
        if self.task_tags:
            if isinstance(self.task_tags, list):
                for i in range(0, len(self.task_tags)):
                    element = self.task_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_tags[i] = element.to_alipay_dict()
            if hasattr(self.task_tags, 'to_alipay_dict'):
                params['task_tags'] = self.task_tags.to_alipay_dict()
            else:
                params['task_tags'] = self.task_tags
        if self.tel:
            if hasattr(self.tel, 'to_alipay_dict'):
                params['tel'] = self.tel.to_alipay_dict()
            else:
                params['tel'] = self.tel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollaborateTask()
        if 'activity_desc' in d:
            o.activity_desc = d['activity_desc']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'dispatched_time' in d:
            o.dispatched_time = d['dispatched_time']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'installer_no' in d:
            o.installer_no = d['installer_no']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_tags' in d:
            o.product_tags = d['product_tags']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'smid_list' in d:
            o.smid_list = d['smid_list']
        if 'task_no' in d:
            o.task_no = d['task_no']
        if 'task_tags' in d:
            o.task_tags = d['task_tags']
        if 'tel' in d:
            o.tel = d['tel']
        return o


