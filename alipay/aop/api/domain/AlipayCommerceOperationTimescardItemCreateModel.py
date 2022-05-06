#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCreateExtInfo import ItemCreateExtInfo


class AlipayCommerceOperationTimescardItemCreateModel(object):

    def __init__(self):
        self._desc = None
        self._end_date = None
        self._ext_info = None
        self._isv_partner_id = None
        self._logo = None
        self._original_price = None
        self._out_biz_no = None
        self._partner_id = None
        self._price = None
        self._product_code = None
        self._scene_code = None
        self._start_date = None
        self._times = None
        self._title = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ItemCreateExtInfo):
            self._ext_info = value
        else:
            self._ext_info = ItemCreateExtInfo.from_alipay_dict(value)
    @property
    def isv_partner_id(self):
        return self._isv_partner_id

    @isv_partner_id.setter
    def isv_partner_id(self, value):
        self._isv_partner_id = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, value):
        self._times = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.isv_partner_id:
            if hasattr(self.isv_partner_id, 'to_alipay_dict'):
                params['isv_partner_id'] = self.isv_partner_id.to_alipay_dict()
            else:
                params['isv_partner_id'] = self.isv_partner_id
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.times:
            if hasattr(self.times, 'to_alipay_dict'):
                params['times'] = self.times.to_alipay_dict()
            else:
                params['times'] = self.times
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTimescardItemCreateModel()
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'isv_partner_id' in d:
            o.isv_partner_id = d['isv_partner_id']
        if 'logo' in d:
            o.logo = d['logo']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'price' in d:
            o.price = d['price']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'times' in d:
            o.times = d['times']
        if 'title' in d:
            o.title = d['title']
        return o


