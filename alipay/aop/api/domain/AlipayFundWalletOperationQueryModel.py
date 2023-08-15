#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletOperationQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._biz_types = None
        self._current_page = None
        self._end_biz_dt = None
        self._page_size = None
        self._product_code = None
        self._start_biz_dt = None
        self._user_wallet_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_types(self):
        return self._biz_types

    @biz_types.setter
    def biz_types(self, value):
        if isinstance(value, list):
            self._biz_types = list()
            for i in value:
                self._biz_types.append(i)
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def end_biz_dt(self):
        return self._end_biz_dt

    @end_biz_dt.setter
    def end_biz_dt(self, value):
        self._end_biz_dt = value
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
    def start_biz_dt(self):
        return self._start_biz_dt

    @start_biz_dt.setter
    def start_biz_dt(self, value):
        self._start_biz_dt = value
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
        if self.biz_types:
            if isinstance(self.biz_types, list):
                for i in range(0, len(self.biz_types)):
                    element = self.biz_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_types[i] = element.to_alipay_dict()
            if hasattr(self.biz_types, 'to_alipay_dict'):
                params['biz_types'] = self.biz_types.to_alipay_dict()
            else:
                params['biz_types'] = self.biz_types
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.end_biz_dt:
            if hasattr(self.end_biz_dt, 'to_alipay_dict'):
                params['end_biz_dt'] = self.end_biz_dt.to_alipay_dict()
            else:
                params['end_biz_dt'] = self.end_biz_dt
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
        if self.start_biz_dt:
            if hasattr(self.start_biz_dt, 'to_alipay_dict'):
                params['start_biz_dt'] = self.start_biz_dt.to_alipay_dict()
            else:
                params['start_biz_dt'] = self.start_biz_dt
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
        o = AlipayFundWalletOperationQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_types' in d:
            o.biz_types = d['biz_types']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'end_biz_dt' in d:
            o.end_biz_dt = d['end_biz_dt']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'start_biz_dt' in d:
            o.start_biz_dt = d['start_biz_dt']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


