#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmEpBondRatingInfo(object):

    def __init__(self):
        self._issuer_name = None
        self._rating = None
        self._rating_change = None
        self._rating_company = None
        self._rating_date = None
        self._rating_object = None
        self._rating_outlook = None
        self._rating_type = None

    @property
    def issuer_name(self):
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self._issuer_name = value
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
    @property
    def rating_change(self):
        return self._rating_change

    @rating_change.setter
    def rating_change(self, value):
        self._rating_change = value
    @property
    def rating_company(self):
        return self._rating_company

    @rating_company.setter
    def rating_company(self, value):
        self._rating_company = value
    @property
    def rating_date(self):
        return self._rating_date

    @rating_date.setter
    def rating_date(self, value):
        self._rating_date = value
    @property
    def rating_object(self):
        return self._rating_object

    @rating_object.setter
    def rating_object(self, value):
        self._rating_object = value
    @property
    def rating_outlook(self):
        return self._rating_outlook

    @rating_outlook.setter
    def rating_outlook(self, value):
        self._rating_outlook = value
    @property
    def rating_type(self):
        return self._rating_type

    @rating_type.setter
    def rating_type(self, value):
        self._rating_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.issuer_name:
            if hasattr(self.issuer_name, 'to_alipay_dict'):
                params['issuer_name'] = self.issuer_name.to_alipay_dict()
            else:
                params['issuer_name'] = self.issuer_name
        if self.rating:
            if hasattr(self.rating, 'to_alipay_dict'):
                params['rating'] = self.rating.to_alipay_dict()
            else:
                params['rating'] = self.rating
        if self.rating_change:
            if hasattr(self.rating_change, 'to_alipay_dict'):
                params['rating_change'] = self.rating_change.to_alipay_dict()
            else:
                params['rating_change'] = self.rating_change
        if self.rating_company:
            if hasattr(self.rating_company, 'to_alipay_dict'):
                params['rating_company'] = self.rating_company.to_alipay_dict()
            else:
                params['rating_company'] = self.rating_company
        if self.rating_date:
            if hasattr(self.rating_date, 'to_alipay_dict'):
                params['rating_date'] = self.rating_date.to_alipay_dict()
            else:
                params['rating_date'] = self.rating_date
        if self.rating_object:
            if hasattr(self.rating_object, 'to_alipay_dict'):
                params['rating_object'] = self.rating_object.to_alipay_dict()
            else:
                params['rating_object'] = self.rating_object
        if self.rating_outlook:
            if hasattr(self.rating_outlook, 'to_alipay_dict'):
                params['rating_outlook'] = self.rating_outlook.to_alipay_dict()
            else:
                params['rating_outlook'] = self.rating_outlook
        if self.rating_type:
            if hasattr(self.rating_type, 'to_alipay_dict'):
                params['rating_type'] = self.rating_type.to_alipay_dict()
            else:
                params['rating_type'] = self.rating_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmEpBondRatingInfo()
        if 'issuer_name' in d:
            o.issuer_name = d['issuer_name']
        if 'rating' in d:
            o.rating = d['rating']
        if 'rating_change' in d:
            o.rating_change = d['rating_change']
        if 'rating_company' in d:
            o.rating_company = d['rating_company']
        if 'rating_date' in d:
            o.rating_date = d['rating_date']
        if 'rating_object' in d:
            o.rating_object = d['rating_object']
        if 'rating_outlook' in d:
            o.rating_outlook = d['rating_outlook']
        if 'rating_type' in d:
            o.rating_type = d['rating_type']
        return o


