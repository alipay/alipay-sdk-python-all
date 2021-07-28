#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbVirtualShopInfo import KbVirtualShopInfo


class KoubeiCateringDishVirtualdishSyncModel(object):

    def __init__(self):
        self._create_user = None
        self._kbdish_virtual_dish_info_list = None
        self._update_user = None

    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def kbdish_virtual_dish_info_list(self):
        return self._kbdish_virtual_dish_info_list

    @kbdish_virtual_dish_info_list.setter
    def kbdish_virtual_dish_info_list(self, value):
        if isinstance(value, list):
            self._kbdish_virtual_dish_info_list = list()
            for i in value:
                if isinstance(i, KbVirtualShopInfo):
                    self._kbdish_virtual_dish_info_list.append(i)
                else:
                    self._kbdish_virtual_dish_info_list.append(KbVirtualShopInfo.from_alipay_dict(i))
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.kbdish_virtual_dish_info_list:
            if isinstance(self.kbdish_virtual_dish_info_list, list):
                for i in range(0, len(self.kbdish_virtual_dish_info_list)):
                    element = self.kbdish_virtual_dish_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kbdish_virtual_dish_info_list[i] = element.to_alipay_dict()
            if hasattr(self.kbdish_virtual_dish_info_list, 'to_alipay_dict'):
                params['kbdish_virtual_dish_info_list'] = self.kbdish_virtual_dish_info_list.to_alipay_dict()
            else:
                params['kbdish_virtual_dish_info_list'] = self.kbdish_virtual_dish_info_list
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
        o = KoubeiCateringDishVirtualdishSyncModel()
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'kbdish_virtual_dish_info_list' in d:
            o.kbdish_virtual_dish_info_list = d['kbdish_virtual_dish_info_list']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


