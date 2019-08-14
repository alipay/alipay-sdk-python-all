#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OuterTargetingItem import OuterTargetingItem


class AlipayDataDataserviceAdGroupCreateormodifyModel(object):

    def __init__(self):
        self._biz_token = None
        self._extend_info = None
        self._group_charge = None
        self._group_name = None
        self._group_outer_id = None
        self._item_id_list = None
        self._plan_outer_id = None
        self._targeting_list = None
        self._time_option = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def group_charge(self):
        return self._group_charge

    @group_charge.setter
    def group_charge(self, value):
        self._group_charge = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def group_outer_id(self):
        return self._group_outer_id

    @group_outer_id.setter
    def group_outer_id(self, value):
        self._group_outer_id = value
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, list):
            self._item_id_list = list()
            for i in value:
                self._item_id_list.append(i)
    @property
    def plan_outer_id(self):
        return self._plan_outer_id

    @plan_outer_id.setter
    def plan_outer_id(self, value):
        self._plan_outer_id = value
    @property
    def targeting_list(self):
        return self._targeting_list

    @targeting_list.setter
    def targeting_list(self, value):
        if isinstance(value, list):
            self._targeting_list = list()
            for i in value:
                if isinstance(i, OuterTargetingItem):
                    self._targeting_list.append(i)
                else:
                    self._targeting_list.append(OuterTargetingItem.from_alipay_dict(i))
    @property
    def time_option(self):
        return self._time_option

    @time_option.setter
    def time_option(self, value):
        self._time_option = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.group_charge:
            if hasattr(self.group_charge, 'to_alipay_dict'):
                params['group_charge'] = self.group_charge.to_alipay_dict()
            else:
                params['group_charge'] = self.group_charge
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.group_outer_id:
            if hasattr(self.group_outer_id, 'to_alipay_dict'):
                params['group_outer_id'] = self.group_outer_id.to_alipay_dict()
            else:
                params['group_outer_id'] = self.group_outer_id
        if self.item_id_list:
            if isinstance(self.item_id_list, list):
                for i in range(0, len(self.item_id_list)):
                    element = self.item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.plan_outer_id:
            if hasattr(self.plan_outer_id, 'to_alipay_dict'):
                params['plan_outer_id'] = self.plan_outer_id.to_alipay_dict()
            else:
                params['plan_outer_id'] = self.plan_outer_id
        if self.targeting_list:
            if isinstance(self.targeting_list, list):
                for i in range(0, len(self.targeting_list)):
                    element = self.targeting_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.targeting_list[i] = element.to_alipay_dict()
            if hasattr(self.targeting_list, 'to_alipay_dict'):
                params['targeting_list'] = self.targeting_list.to_alipay_dict()
            else:
                params['targeting_list'] = self.targeting_list
        if self.time_option:
            if hasattr(self.time_option, 'to_alipay_dict'):
                params['time_option'] = self.time_option.to_alipay_dict()
            else:
                params['time_option'] = self.time_option
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdGroupCreateormodifyModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'group_charge' in d:
            o.group_charge = d['group_charge']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'group_outer_id' in d:
            o.group_outer_id = d['group_outer_id']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'plan_outer_id' in d:
            o.plan_outer_id = d['plan_outer_id']
        if 'targeting_list' in d:
            o.targeting_list = d['targeting_list']
        if 'time_option' in d:
            o.time_option = d['time_option']
        return o


