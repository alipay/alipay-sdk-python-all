#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletPageoperationQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._biz_type = None
        self._end_time = None
        self._offset_key = None
        self._open_id = None
        self._page_size = None
        self._product_code = None
        self._start_time = None
        self._status_list = None
        self._sub_biz_type_list = None
        self._user_id = None
        self._user_wallet_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def offset_key(self):
        return self._offset_key

    @offset_key.setter
    def offset_key(self, value):
        self._offset_key = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def sub_biz_type_list(self):
        return self._sub_biz_type_list

    @sub_biz_type_list.setter
    def sub_biz_type_list(self, value):
        if isinstance(value, list):
            self._sub_biz_type_list = list()
            for i in value:
                self._sub_biz_type_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.offset_key:
            if hasattr(self.offset_key, 'to_alipay_dict'):
                params['offset_key'] = self.offset_key.to_alipay_dict()
            else:
                params['offset_key'] = self.offset_key
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.sub_biz_type_list:
            if isinstance(self.sub_biz_type_list, list):
                for i in range(0, len(self.sub_biz_type_list)):
                    element = self.sub_biz_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_biz_type_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_biz_type_list, 'to_alipay_dict'):
                params['sub_biz_type_list'] = self.sub_biz_type_list.to_alipay_dict()
            else:
                params['sub_biz_type_list'] = self.sub_biz_type_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletPageoperationQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'offset_key' in d:
            o.offset_key = d['offset_key']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'sub_biz_type_list' in d:
            o.sub_biz_type_list = d['sub_biz_type_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


