#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishVirtualDishInfo(object):

    def __init__(self):
        self._catetory_id = None
        self._create_user = None
        self._dish_id = None
        self._ext_info = None
        self._shop_id = None
        self._sort = None
        self._update_user = None

    @property
    def catetory_id(self):
        return self._catetory_id

    @catetory_id.setter
    def catetory_id(self, value):
        self._catetory_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_id:
            if hasattr(self.catetory_id, 'to_alipay_dict'):
                params['catetory_id'] = self.catetory_id.to_alipay_dict()
            else:
                params['catetory_id'] = self.catetory_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishVirtualDishInfo()
        if 'catetory_id' in d:
            o.catetory_id = d['catetory_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sort' in d:
            o.sort = d['sort']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


