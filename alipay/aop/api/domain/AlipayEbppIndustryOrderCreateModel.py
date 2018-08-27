#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryOrderCreateModel(object):

    def __init__(self):
        self._ability_code = None
        self._bill_date = None
        self._bill_key = None
        self._biz_amount = None
        self._biz_inst_short_name = None
        self._biz_type = None
        self._city_code = None
        self._extend_field = None
        self._fine_amount = None
        self._identity_no = None
        self._mobile = None
        self._out_order_no = None
        self._owner_name = None
        self._province_code = None
        self._sub_biz_type = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_amount(self):
        return self._biz_amount

    @biz_amount.setter
    def biz_amount(self, value):
        self._biz_amount = value
    @property
    def biz_inst_short_name(self):
        return self._biz_inst_short_name

    @biz_inst_short_name.setter
    def biz_inst_short_name(self, value):
        self._biz_inst_short_name = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def fine_amount(self):
        return self._fine_amount

    @fine_amount.setter
    def fine_amount(self, value):
        self._fine_amount = value
    @property
    def identity_no(self):
        return self._identity_no

    @identity_no.setter
    def identity_no(self, value):
        self._identity_no = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_amount:
            if hasattr(self.biz_amount, 'to_alipay_dict'):
                params['biz_amount'] = self.biz_amount.to_alipay_dict()
            else:
                params['biz_amount'] = self.biz_amount
        if self.biz_inst_short_name:
            if hasattr(self.biz_inst_short_name, 'to_alipay_dict'):
                params['biz_inst_short_name'] = self.biz_inst_short_name.to_alipay_dict()
            else:
                params['biz_inst_short_name'] = self.biz_inst_short_name
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.fine_amount:
            if hasattr(self.fine_amount, 'to_alipay_dict'):
                params['fine_amount'] = self.fine_amount.to_alipay_dict()
            else:
                params['fine_amount'] = self.fine_amount
        if self.identity_no:
            if hasattr(self.identity_no, 'to_alipay_dict'):
                params['identity_no'] = self.identity_no.to_alipay_dict()
            else:
                params['identity_no'] = self.identity_no
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryOrderCreateModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_amount' in d:
            o.biz_amount = d['biz_amount']
        if 'biz_inst_short_name' in d:
            o.biz_inst_short_name = d['biz_inst_short_name']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'fine_amount' in d:
            o.fine_amount = d['fine_amount']
        if 'identity_no' in d:
            o.identity_no = d['identity_no']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


