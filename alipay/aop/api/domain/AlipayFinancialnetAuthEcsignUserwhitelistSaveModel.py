#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractTemplateOpenVO import ContractTemplateOpenVO


class AlipayFinancialnetAuthEcsignUserwhitelistSaveModel(object):

    def __init__(self):
        self._back_type = None
        self._back_url = None
        self._binded_mobile = None
        self._cert_no = None
        self._cert_type = None
        self._out_order_no = None
        self._solution_code = None
        self._template_vo_list = None
        self._third_part_schema = None
        self._user_name = None

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
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def template_vo_list(self):
        return self._template_vo_list

    @template_vo_list.setter
    def template_vo_list(self, value):
        if isinstance(value, list):
            self._template_vo_list = list()
            for i in value:
                if isinstance(i, ContractTemplateOpenVO):
                    self._template_vo_list.append(i)
                else:
                    self._template_vo_list.append(ContractTemplateOpenVO.from_alipay_dict(i))
    @property
    def third_part_schema(self):
        return self._third_part_schema

    @third_part_schema.setter
    def third_part_schema(self, value):
        self._third_part_schema = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


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
        if self.binded_mobile:
            if hasattr(self.binded_mobile, 'to_alipay_dict'):
                params['binded_mobile'] = self.binded_mobile.to_alipay_dict()
            else:
                params['binded_mobile'] = self.binded_mobile
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.template_vo_list:
            if isinstance(self.template_vo_list, list):
                for i in range(0, len(self.template_vo_list)):
                    element = self.template_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.template_vo_list, 'to_alipay_dict'):
                params['template_vo_list'] = self.template_vo_list.to_alipay_dict()
            else:
                params['template_vo_list'] = self.template_vo_list
        if self.third_part_schema:
            if hasattr(self.third_part_schema, 'to_alipay_dict'):
                params['third_part_schema'] = self.third_part_schema.to_alipay_dict()
            else:
                params['third_part_schema'] = self.third_part_schema
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthEcsignUserwhitelistSaveModel()
        if 'back_type' in d:
            o.back_type = d['back_type']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'binded_mobile' in d:
            o.binded_mobile = d['binded_mobile']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'template_vo_list' in d:
            o.template_vo_list = d['template_vo_list']
        if 'third_part_schema' in d:
            o.third_part_schema = d['third_part_schema']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


