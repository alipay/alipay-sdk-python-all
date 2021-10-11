#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OuterTargetingItem import OuterTargetingItem


class AlipayDataDataserviceAdGroupCreateormodifyModel(object):

    def __init__(self):
        self._biz_token = None
        self._conversion_data_id_list = None
        self._conversion_id = None
        self._conversion_id_list = None
        self._conversion_type = None
        self._extend_info = None
        self._group_charge = None
        self._group_name = None
        self._group_outer_id = None
        self._group_status = None
        self._item_id_list = None
        self._ocpx_switch = None
        self._plan_outer_id = None
        self._target_cpa = None
        self._targeting_extend_info = None
        self._targeting_list = None
        self._time_option = None
        self._time_schema = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def conversion_data_id_list(self):
        return self._conversion_data_id_list

    @conversion_data_id_list.setter
    def conversion_data_id_list(self, value):
        if isinstance(value, list):
            self._conversion_data_id_list = list()
            for i in value:
                self._conversion_data_id_list.append(i)
    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def conversion_id_list(self):
        return self._conversion_id_list

    @conversion_id_list.setter
    def conversion_id_list(self, value):
        if isinstance(value, list):
            self._conversion_id_list = list()
            for i in value:
                self._conversion_id_list.append(i)
    @property
    def conversion_type(self):
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        self._conversion_type = value
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
    def group_status(self):
        return self._group_status

    @group_status.setter
    def group_status(self, value):
        self._group_status = value
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
    def ocpx_switch(self):
        return self._ocpx_switch

    @ocpx_switch.setter
    def ocpx_switch(self, value):
        self._ocpx_switch = value
    @property
    def plan_outer_id(self):
        return self._plan_outer_id

    @plan_outer_id.setter
    def plan_outer_id(self, value):
        self._plan_outer_id = value
    @property
    def target_cpa(self):
        return self._target_cpa

    @target_cpa.setter
    def target_cpa(self, value):
        self._target_cpa = value
    @property
    def targeting_extend_info(self):
        return self._targeting_extend_info

    @targeting_extend_info.setter
    def targeting_extend_info(self, value):
        self._targeting_extend_info = value
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
    @property
    def time_schema(self):
        return self._time_schema

    @time_schema.setter
    def time_schema(self, value):
        self._time_schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.conversion_data_id_list:
            if isinstance(self.conversion_data_id_list, list):
                for i in range(0, len(self.conversion_data_id_list)):
                    element = self.conversion_data_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversion_data_id_list[i] = element.to_alipay_dict()
            if hasattr(self.conversion_data_id_list, 'to_alipay_dict'):
                params['conversion_data_id_list'] = self.conversion_data_id_list.to_alipay_dict()
            else:
                params['conversion_data_id_list'] = self.conversion_data_id_list
        if self.conversion_id:
            if hasattr(self.conversion_id, 'to_alipay_dict'):
                params['conversion_id'] = self.conversion_id.to_alipay_dict()
            else:
                params['conversion_id'] = self.conversion_id
        if self.conversion_id_list:
            if isinstance(self.conversion_id_list, list):
                for i in range(0, len(self.conversion_id_list)):
                    element = self.conversion_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversion_id_list[i] = element.to_alipay_dict()
            if hasattr(self.conversion_id_list, 'to_alipay_dict'):
                params['conversion_id_list'] = self.conversion_id_list.to_alipay_dict()
            else:
                params['conversion_id_list'] = self.conversion_id_list
        if self.conversion_type:
            if hasattr(self.conversion_type, 'to_alipay_dict'):
                params['conversion_type'] = self.conversion_type.to_alipay_dict()
            else:
                params['conversion_type'] = self.conversion_type
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
        if self.group_status:
            if hasattr(self.group_status, 'to_alipay_dict'):
                params['group_status'] = self.group_status.to_alipay_dict()
            else:
                params['group_status'] = self.group_status
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
        if self.ocpx_switch:
            if hasattr(self.ocpx_switch, 'to_alipay_dict'):
                params['ocpx_switch'] = self.ocpx_switch.to_alipay_dict()
            else:
                params['ocpx_switch'] = self.ocpx_switch
        if self.plan_outer_id:
            if hasattr(self.plan_outer_id, 'to_alipay_dict'):
                params['plan_outer_id'] = self.plan_outer_id.to_alipay_dict()
            else:
                params['plan_outer_id'] = self.plan_outer_id
        if self.target_cpa:
            if hasattr(self.target_cpa, 'to_alipay_dict'):
                params['target_cpa'] = self.target_cpa.to_alipay_dict()
            else:
                params['target_cpa'] = self.target_cpa
        if self.targeting_extend_info:
            if hasattr(self.targeting_extend_info, 'to_alipay_dict'):
                params['targeting_extend_info'] = self.targeting_extend_info.to_alipay_dict()
            else:
                params['targeting_extend_info'] = self.targeting_extend_info
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
        if self.time_schema:
            if hasattr(self.time_schema, 'to_alipay_dict'):
                params['time_schema'] = self.time_schema.to_alipay_dict()
            else:
                params['time_schema'] = self.time_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdGroupCreateormodifyModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'conversion_data_id_list' in d:
            o.conversion_data_id_list = d['conversion_data_id_list']
        if 'conversion_id' in d:
            o.conversion_id = d['conversion_id']
        if 'conversion_id_list' in d:
            o.conversion_id_list = d['conversion_id_list']
        if 'conversion_type' in d:
            o.conversion_type = d['conversion_type']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'group_charge' in d:
            o.group_charge = d['group_charge']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'group_outer_id' in d:
            o.group_outer_id = d['group_outer_id']
        if 'group_status' in d:
            o.group_status = d['group_status']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'ocpx_switch' in d:
            o.ocpx_switch = d['ocpx_switch']
        if 'plan_outer_id' in d:
            o.plan_outer_id = d['plan_outer_id']
        if 'target_cpa' in d:
            o.target_cpa = d['target_cpa']
        if 'targeting_extend_info' in d:
            o.targeting_extend_info = d['targeting_extend_info']
        if 'targeting_list' in d:
            o.targeting_list = d['targeting_list']
        if 'time_option' in d:
            o.time_option = d['time_option']
        if 'time_schema' in d:
            o.time_schema = d['time_schema']
        return o


