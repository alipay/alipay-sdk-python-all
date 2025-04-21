#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBusinessbillGoodsQueryModel(object):

    def __init__(self):
        self._activity_scene = None
        self._goods_code = None
        self._goods_model_number = None
        self._goods_title = None
        self._open_id = None
        self._page_num = None
        self._page_size = None
        self._user_id = None

    @property
    def activity_scene(self):
        return self._activity_scene

    @activity_scene.setter
    def activity_scene(self, value):
        self._activity_scene = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def goods_model_number(self):
        return self._goods_model_number

    @goods_model_number.setter
    def goods_model_number(self, value):
        self._goods_model_number = value
    @property
    def goods_title(self):
        return self._goods_title

    @goods_title.setter
    def goods_title(self, value):
        self._goods_title = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_scene:
            if hasattr(self.activity_scene, 'to_alipay_dict'):
                params['activity_scene'] = self.activity_scene.to_alipay_dict()
            else:
                params['activity_scene'] = self.activity_scene
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.goods_model_number:
            if hasattr(self.goods_model_number, 'to_alipay_dict'):
                params['goods_model_number'] = self.goods_model_number.to_alipay_dict()
            else:
                params['goods_model_number'] = self.goods_model_number
        if self.goods_title:
            if hasattr(self.goods_title, 'to_alipay_dict'):
                params['goods_title'] = self.goods_title.to_alipay_dict()
            else:
                params['goods_title'] = self.goods_title
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        o = AlipayMarketingBusinessbillGoodsQueryModel()
        if 'activity_scene' in d:
            o.activity_scene = d['activity_scene']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'goods_model_number' in d:
            o.goods_model_number = d['goods_model_number']
        if 'goods_title' in d:
            o.goods_title = d['goods_title']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


