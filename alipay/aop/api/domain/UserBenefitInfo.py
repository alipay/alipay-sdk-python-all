#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserBenefitInfo(object):

    def __init__(self):
        self._end_date = None
        self._id = None
        self._jump_url = None
        self._product_type = None
        self._start_date = None
        self._sub_title = None
        self._title = None
        self._voucher_quantity = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserBenefitInfo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'id' in d:
            o.id = d['id']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        return o


