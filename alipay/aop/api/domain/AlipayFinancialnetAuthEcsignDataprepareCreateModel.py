#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthEcsignDataprepareCreateModel(object):

    def __init__(self):
        self._back_type = None
        self._back_url = None
        self._ext_info = None
        self._jump_type = None
        self._out_order_no = None
        self._partner_id = None
        self._sign_product_id = None
        self._solution_code = None
        self._third_part_schema = None

    @property
    def back_type(self):
        return self._back_type

    @back_type.setter
    def back_type(self, value):
        self._back_type = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def jump_type(self):
        return self._jump_type

    @jump_type.setter
    def jump_type(self, value):
        self._jump_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def sign_product_id(self):
        return self._sign_product_id

    @sign_product_id.setter
    def sign_product_id(self, value):
        self._sign_product_id = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def third_part_schema(self):
        return self._third_part_schema

    @third_part_schema.setter
    def third_part_schema(self, value):
        self._third_part_schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_type:
            if hasattr(self.back_type, 'to_alipay_dict'):
                params['back_type'] = self.back_type.to_alipay_dict()
            else:
                params['back_type'] = self.back_type
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.jump_type:
            if hasattr(self.jump_type, 'to_alipay_dict'):
                params['jump_type'] = self.jump_type.to_alipay_dict()
            else:
                params['jump_type'] = self.jump_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.sign_product_id:
            if hasattr(self.sign_product_id, 'to_alipay_dict'):
                params['sign_product_id'] = self.sign_product_id.to_alipay_dict()
            else:
                params['sign_product_id'] = self.sign_product_id
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.third_part_schema:
            if hasattr(self.third_part_schema, 'to_alipay_dict'):
                params['third_part_schema'] = self.third_part_schema.to_alipay_dict()
            else:
                params['third_part_schema'] = self.third_part_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthEcsignDataprepareCreateModel()
        if 'back_type' in d:
            o.back_type = d['back_type']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'jump_type' in d:
            o.jump_type = d['jump_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'sign_product_id' in d:
            o.sign_product_id = d['sign_product_id']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'third_part_schema' in d:
            o.third_part_schema = d['third_part_schema']
        return o


