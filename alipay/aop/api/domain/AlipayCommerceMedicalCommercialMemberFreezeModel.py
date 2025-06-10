#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCommercialMemberFreezeModel(object):

    def __init__(self):
        self._benefit_id_list = None
        self._benefit_order_id = None
        self._open_id = None
        self._out_biz_no = None
        self._out_product_id = None
        self._product_type = None
        self._source_channel = None
        self._type = None
        self._user_id = None

    @property
    def benefit_id_list(self):
        return self._benefit_id_list

    @benefit_id_list.setter
    def benefit_id_list(self, value):
        if isinstance(value, list):
            self._benefit_id_list = list()
            for i in value:
                self._benefit_id_list.append(i)
    @property
    def benefit_order_id(self):
        return self._benefit_order_id

    @benefit_order_id.setter
    def benefit_order_id(self, value):
        self._benefit_order_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id_list:
            if isinstance(self.benefit_id_list, list):
                for i in range(0, len(self.benefit_id_list)):
                    element = self.benefit_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_id_list[i] = element.to_alipay_dict()
            if hasattr(self.benefit_id_list, 'to_alipay_dict'):
                params['benefit_id_list'] = self.benefit_id_list.to_alipay_dict()
            else:
                params['benefit_id_list'] = self.benefit_id_list
        if self.benefit_order_id:
            if hasattr(self.benefit_order_id, 'to_alipay_dict'):
                params['benefit_order_id'] = self.benefit_order_id.to_alipay_dict()
            else:
                params['benefit_order_id'] = self.benefit_order_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCommercialMemberFreezeModel()
        if 'benefit_id_list' in d:
            o.benefit_id_list = d['benefit_id_list']
        if 'benefit_order_id' in d:
            o.benefit_order_id = d['benefit_order_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


