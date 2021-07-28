#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtendParams(object):

    def __init__(self):
        self._card_type = None
        self._hb_fq_num = None
        self._hb_fq_seller_percent = None
        self._industry_reflux_info = None
        self._specified_seller_name = None
        self._sys_service_provider_id = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def hb_fq_num(self):
        return self._hb_fq_num

    @hb_fq_num.setter
    def hb_fq_num(self, value):
        self._hb_fq_num = value
    @property
    def hb_fq_seller_percent(self):
        return self._hb_fq_seller_percent

    @hb_fq_seller_percent.setter
    def hb_fq_seller_percent(self, value):
        self._hb_fq_seller_percent = value
    @property
    def industry_reflux_info(self):
        return self._industry_reflux_info

    @industry_reflux_info.setter
    def industry_reflux_info(self, value):
        self._industry_reflux_info = value
    @property
    def specified_seller_name(self):
        return self._specified_seller_name

    @specified_seller_name.setter
    def specified_seller_name(self, value):
        self._specified_seller_name = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.hb_fq_num:
            if hasattr(self.hb_fq_num, 'to_alipay_dict'):
                params['hb_fq_num'] = self.hb_fq_num.to_alipay_dict()
            else:
                params['hb_fq_num'] = self.hb_fq_num
        if self.hb_fq_seller_percent:
            if hasattr(self.hb_fq_seller_percent, 'to_alipay_dict'):
                params['hb_fq_seller_percent'] = self.hb_fq_seller_percent.to_alipay_dict()
            else:
                params['hb_fq_seller_percent'] = self.hb_fq_seller_percent
        if self.industry_reflux_info:
            if hasattr(self.industry_reflux_info, 'to_alipay_dict'):
                params['industry_reflux_info'] = self.industry_reflux_info.to_alipay_dict()
            else:
                params['industry_reflux_info'] = self.industry_reflux_info
        if self.specified_seller_name:
            if hasattr(self.specified_seller_name, 'to_alipay_dict'):
                params['specified_seller_name'] = self.specified_seller_name.to_alipay_dict()
            else:
                params['specified_seller_name'] = self.specified_seller_name
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtendParams()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'hb_fq_num' in d:
            o.hb_fq_num = d['hb_fq_num']
        if 'hb_fq_seller_percent' in d:
            o.hb_fq_seller_percent = d['hb_fq_seller_percent']
        if 'industry_reflux_info' in d:
            o.industry_reflux_info = d['industry_reflux_info']
        if 'specified_seller_name' in d:
            o.specified_seller_name = d['specified_seller_name']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


