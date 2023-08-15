#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessRelationShopMemberAddOption import BusinessRelationShopMemberAddOption


class AlipayBusinessRelationShopmemberAddModel(object):

    def __init__(self):
        self._add_option = None
        self._group_id = None
        self._group_sub_type = None
        self._group_type = None
        self._real_shop_id = None
        self._real_shop_no = None

    @property
    def add_option(self):
        return self._add_option

    @add_option.setter
    def add_option(self, value):
        if isinstance(value, BusinessRelationShopMemberAddOption):
            self._add_option = value
        else:
            self._add_option = BusinessRelationShopMemberAddOption.from_alipay_dict(value)
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_sub_type(self):
        return self._group_sub_type

    @group_sub_type.setter
    def group_sub_type(self, value):
        self._group_sub_type = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_option:
            if hasattr(self.add_option, 'to_alipay_dict'):
                params['add_option'] = self.add_option.to_alipay_dict()
            else:
                params['add_option'] = self.add_option
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_sub_type:
            if hasattr(self.group_sub_type, 'to_alipay_dict'):
                params['group_sub_type'] = self.group_sub_type.to_alipay_dict()
            else:
                params['group_sub_type'] = self.group_sub_type
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        if self.real_shop_no:
            if hasattr(self.real_shop_no, 'to_alipay_dict'):
                params['real_shop_no'] = self.real_shop_no.to_alipay_dict()
            else:
                params['real_shop_no'] = self.real_shop_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessRelationShopmemberAddModel()
        if 'add_option' in d:
            o.add_option = d['add_option']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_sub_type' in d:
            o.group_sub_type = d['group_sub_type']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        return o


