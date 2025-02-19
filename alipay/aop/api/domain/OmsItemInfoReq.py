#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OmsItemSkuInfoReq import OmsItemSkuInfoReq


class OmsItemInfoReq(object):

    def __init__(self):
        self._account_name = None
        self._create_time = None
        self._insurance = None
        self._item_code = None
        self._item_id = None
        self._item_name = None
        self._platform = None
        self._sku_info_list = None
        self._status = None
        self._tag_code = None
        self._tag_name = None
        self._update_time = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def insurance(self):
        return self._insurance

    @insurance.setter
    def insurance(self, value):
        self._insurance = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def sku_info_list(self):
        return self._sku_info_list

    @sku_info_list.setter
    def sku_info_list(self, value):
        if isinstance(value, OmsItemSkuInfoReq):
            self._sku_info_list = value
        else:
            self._sku_info_list = OmsItemSkuInfoReq.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.insurance:
            if hasattr(self.insurance, 'to_alipay_dict'):
                params['insurance'] = self.insurance.to_alipay_dict()
            else:
                params['insurance'] = self.insurance
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.sku_info_list:
            if hasattr(self.sku_info_list, 'to_alipay_dict'):
                params['sku_info_list'] = self.sku_info_list.to_alipay_dict()
            else:
                params['sku_info_list'] = self.sku_info_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OmsItemInfoReq()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'insurance' in d:
            o.insurance = d['insurance']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'platform' in d:
            o.platform = d['platform']
        if 'sku_info_list' in d:
            o.sku_info_list = d['sku_info_list']
        if 'status' in d:
            o.status = d['status']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


