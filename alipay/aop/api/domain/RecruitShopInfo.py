#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitShopInfo(object):

    def __init__(self):
        self._confirm_status = None
        self._shop_category = None
        self._shop_id = None
        self._shop_name = None

    @property
    def confirm_status(self):
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, value):
        self._confirm_status = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_status:
            if hasattr(self.confirm_status, 'to_alipay_dict'):
                params['confirm_status'] = self.confirm_status.to_alipay_dict()
            else:
                params['confirm_status'] = self.confirm_status
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitShopInfo()
        if 'confirm_status' in d:
            o.confirm_status = d['confirm_status']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


