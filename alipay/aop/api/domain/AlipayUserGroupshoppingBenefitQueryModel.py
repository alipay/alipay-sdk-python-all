#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGroupshoppingBenefitQueryModel(object):

    def __init__(self):
        self._group_id = None
        self._is_platform_invest = None
        self._item_id = None
        self._original_prize = None
        self._pin_prize = None
        self._pin_status = None
        self._scene = None
        self._user_id = None
        self._user_id_list = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def is_platform_invest(self):
        return self._is_platform_invest

    @is_platform_invest.setter
    def is_platform_invest(self, value):
        self._is_platform_invest = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def original_prize(self):
        return self._original_prize

    @original_prize.setter
    def original_prize(self, value):
        self._original_prize = value
    @property
    def pin_prize(self):
        return self._pin_prize

    @pin_prize.setter
    def pin_prize(self, value):
        self._pin_prize = value
    @property
    def pin_status(self):
        return self._pin_status

    @pin_status.setter
    def pin_status(self, value):
        self._pin_status = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_list(self):
        return self._user_id_list

    @user_id_list.setter
    def user_id_list(self, value):
        if isinstance(value, list):
            self._user_id_list = list()
            for i in value:
                self._user_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.is_platform_invest:
            if hasattr(self.is_platform_invest, 'to_alipay_dict'):
                params['is_platform_invest'] = self.is_platform_invest.to_alipay_dict()
            else:
                params['is_platform_invest'] = self.is_platform_invest
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.original_prize:
            if hasattr(self.original_prize, 'to_alipay_dict'):
                params['original_prize'] = self.original_prize.to_alipay_dict()
            else:
                params['original_prize'] = self.original_prize
        if self.pin_prize:
            if hasattr(self.pin_prize, 'to_alipay_dict'):
                params['pin_prize'] = self.pin_prize.to_alipay_dict()
            else:
                params['pin_prize'] = self.pin_prize
        if self.pin_status:
            if hasattr(self.pin_status, 'to_alipay_dict'):
                params['pin_status'] = self.pin_status.to_alipay_dict()
            else:
                params['pin_status'] = self.pin_status
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_list:
            if isinstance(self.user_id_list, list):
                for i in range(0, len(self.user_id_list)):
                    element = self.user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_id_list, 'to_alipay_dict'):
                params['user_id_list'] = self.user_id_list.to_alipay_dict()
            else:
                params['user_id_list'] = self.user_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGroupshoppingBenefitQueryModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'is_platform_invest' in d:
            o.is_platform_invest = d['is_platform_invest']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'original_prize' in d:
            o.original_prize = d['original_prize']
        if 'pin_prize' in d:
            o.pin_prize = d['pin_prize']
        if 'pin_status' in d:
            o.pin_status = d['pin_status']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


