#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantBorrowEntityUploadModel(object):

    def __init__(self):
        self._address_desc = None
        self._can_borrow = None
        self._can_borrow_cnt = None
        self._category_code = None
        self._collect_rent = None
        self._contact_number = None
        self._entity_code = None
        self._entity_name = None
        self._latitude = None
        self._longitude = None
        self._office_hours_desc = None
        self._product_code = None
        self._rent_desc = None
        self._total_borrow_cnt = None
        self._upload_time = None

    @property
    def address_desc(self):
        return self._address_desc

    @address_desc.setter
    def address_desc(self, value):
        self._address_desc = value
    @property
    def can_borrow(self):
        return self._can_borrow

    @can_borrow.setter
    def can_borrow(self, value):
        self._can_borrow = value
    @property
    def can_borrow_cnt(self):
        return self._can_borrow_cnt

    @can_borrow_cnt.setter
    def can_borrow_cnt(self, value):
        self._can_borrow_cnt = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def collect_rent(self):
        return self._collect_rent

    @collect_rent.setter
    def collect_rent(self, value):
        self._collect_rent = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def office_hours_desc(self):
        return self._office_hours_desc

    @office_hours_desc.setter
    def office_hours_desc(self, value):
        self._office_hours_desc = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rent_desc(self):
        return self._rent_desc

    @rent_desc.setter
    def rent_desc(self, value):
        self._rent_desc = value
    @property
    def total_borrow_cnt(self):
        return self._total_borrow_cnt

    @total_borrow_cnt.setter
    def total_borrow_cnt(self, value):
        self._total_borrow_cnt = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_desc:
            if hasattr(self.address_desc, 'to_alipay_dict'):
                params['address_desc'] = self.address_desc.to_alipay_dict()
            else:
                params['address_desc'] = self.address_desc
        if self.can_borrow:
            if hasattr(self.can_borrow, 'to_alipay_dict'):
                params['can_borrow'] = self.can_borrow.to_alipay_dict()
            else:
                params['can_borrow'] = self.can_borrow
        if self.can_borrow_cnt:
            if hasattr(self.can_borrow_cnt, 'to_alipay_dict'):
                params['can_borrow_cnt'] = self.can_borrow_cnt.to_alipay_dict()
            else:
                params['can_borrow_cnt'] = self.can_borrow_cnt
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.collect_rent:
            if hasattr(self.collect_rent, 'to_alipay_dict'):
                params['collect_rent'] = self.collect_rent.to_alipay_dict()
            else:
                params['collect_rent'] = self.collect_rent
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.office_hours_desc:
            if hasattr(self.office_hours_desc, 'to_alipay_dict'):
                params['office_hours_desc'] = self.office_hours_desc.to_alipay_dict()
            else:
                params['office_hours_desc'] = self.office_hours_desc
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rent_desc:
            if hasattr(self.rent_desc, 'to_alipay_dict'):
                params['rent_desc'] = self.rent_desc.to_alipay_dict()
            else:
                params['rent_desc'] = self.rent_desc
        if self.total_borrow_cnt:
            if hasattr(self.total_borrow_cnt, 'to_alipay_dict'):
                params['total_borrow_cnt'] = self.total_borrow_cnt.to_alipay_dict()
            else:
                params['total_borrow_cnt'] = self.total_borrow_cnt
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantBorrowEntityUploadModel()
        if 'address_desc' in d:
            o.address_desc = d['address_desc']
        if 'can_borrow' in d:
            o.can_borrow = d['can_borrow']
        if 'can_borrow_cnt' in d:
            o.can_borrow_cnt = d['can_borrow_cnt']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'collect_rent' in d:
            o.collect_rent = d['collect_rent']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'office_hours_desc' in d:
            o.office_hours_desc = d['office_hours_desc']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rent_desc' in d:
            o.rent_desc = d['rent_desc']
        if 'total_borrow_cnt' in d:
            o.total_borrow_cnt = d['total_borrow_cnt']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        return o


