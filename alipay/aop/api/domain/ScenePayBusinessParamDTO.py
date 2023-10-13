#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StoreInfoDTO import StoreInfoDTO


class ScenePayBusinessParamDTO(object):

    def __init__(self):
        self._custom_params = None
        self._hit_store_info = None
        self._mall_cell_id = None
        self._mall_cell_type = None
        self._mall_id = None
        self._mall_pid = None
        self._plan_id = None
        self._real_store_id = None
        self._voucher_id = None

    @property
    def custom_params(self):
        return self._custom_params

    @custom_params.setter
    def custom_params(self, value):
        self._custom_params = value
    @property
    def hit_store_info(self):
        return self._hit_store_info

    @hit_store_info.setter
    def hit_store_info(self, value):
        if isinstance(value, StoreInfoDTO):
            self._hit_store_info = value
        else:
            self._hit_store_info = StoreInfoDTO.from_alipay_dict(value)
    @property
    def mall_cell_id(self):
        return self._mall_cell_id

    @mall_cell_id.setter
    def mall_cell_id(self, value):
        self._mall_cell_id = value
    @property
    def mall_cell_type(self):
        return self._mall_cell_type

    @mall_cell_type.setter
    def mall_cell_type(self, value):
        self._mall_cell_type = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def mall_pid(self):
        return self._mall_pid

    @mall_pid.setter
    def mall_pid(self, value):
        self._mall_pid = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def real_store_id(self):
        return self._real_store_id

    @real_store_id.setter
    def real_store_id(self, value):
        self._real_store_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_params:
            if hasattr(self.custom_params, 'to_alipay_dict'):
                params['custom_params'] = self.custom_params.to_alipay_dict()
            else:
                params['custom_params'] = self.custom_params
        if self.hit_store_info:
            if hasattr(self.hit_store_info, 'to_alipay_dict'):
                params['hit_store_info'] = self.hit_store_info.to_alipay_dict()
            else:
                params['hit_store_info'] = self.hit_store_info
        if self.mall_cell_id:
            if hasattr(self.mall_cell_id, 'to_alipay_dict'):
                params['mall_cell_id'] = self.mall_cell_id.to_alipay_dict()
            else:
                params['mall_cell_id'] = self.mall_cell_id
        if self.mall_cell_type:
            if hasattr(self.mall_cell_type, 'to_alipay_dict'):
                params['mall_cell_type'] = self.mall_cell_type.to_alipay_dict()
            else:
                params['mall_cell_type'] = self.mall_cell_type
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.mall_pid:
            if hasattr(self.mall_pid, 'to_alipay_dict'):
                params['mall_pid'] = self.mall_pid.to_alipay_dict()
            else:
                params['mall_pid'] = self.mall_pid
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.real_store_id:
            if hasattr(self.real_store_id, 'to_alipay_dict'):
                params['real_store_id'] = self.real_store_id.to_alipay_dict()
            else:
                params['real_store_id'] = self.real_store_id
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenePayBusinessParamDTO()
        if 'custom_params' in d:
            o.custom_params = d['custom_params']
        if 'hit_store_info' in d:
            o.hit_store_info = d['hit_store_info']
        if 'mall_cell_id' in d:
            o.mall_cell_id = d['mall_cell_id']
        if 'mall_cell_type' in d:
            o.mall_cell_type = d['mall_cell_type']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'mall_pid' in d:
            o.mall_pid = d['mall_pid']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'real_store_id' in d:
            o.real_store_id = d['real_store_id']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


