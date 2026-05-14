#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExaminationBookInfo(object):

    def __init__(self):
        self._book_end_time = None
        self._book_start_time = None
        self._gender = None
        self._id_card = None
        self._id_type = None
        self._name = None
        self._phone = None
        self._store_address = None
        self._store_name = None
        self._time = None

    @property
    def book_end_time(self):
        return self._book_end_time

    @book_end_time.setter
    def book_end_time(self, value):
        self._book_end_time = value
    @property
    def book_start_time(self):
        return self._book_start_time

    @book_start_time.setter
    def book_start_time(self, value):
        self._book_start_time = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_end_time:
            if hasattr(self.book_end_time, 'to_alipay_dict'):
                params['book_end_time'] = self.book_end_time.to_alipay_dict()
            else:
                params['book_end_time'] = self.book_end_time
        if self.book_start_time:
            if hasattr(self.book_start_time, 'to_alipay_dict'):
                params['book_start_time'] = self.book_start_time.to_alipay_dict()
            else:
                params['book_start_time'] = self.book_start_time
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationBookInfo()
        if 'book_end_time' in d:
            o.book_end_time = d['book_end_time']
        if 'book_start_time' in d:
            o.book_start_time = d['book_start_time']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'time' in d:
            o.time = d['time']
        return o


