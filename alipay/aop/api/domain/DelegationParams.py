#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DelegationTaskParams import DelegationTaskParams


class DelegationParams(object):

    def __init__(self):
        self._acpid = None
        self._delegation_desc = None
        self._delegation_scene = None
        self._delegation_tag = None
        self._delegation_task_params = None
        self._external_delegation_id = None
        self._external_tradeno_list = None
        self._first_deduct_time = None
        self._goods_logo = None
        self._goods_name = None
        self._goods_sku_info = None
        self._max_total_amount = None
        self._merchant_name = None
        self._package_name = None
        self._pay_operation_info = None
        self._quantity = None
        self._quota_amount = None
        self._times_limit = None
        self._times_timit = None
        self._validity_end_time = None
        self._validity_start_time = None

    @property
    def acpid(self):
        return self._acpid

    @acpid.setter
    def acpid(self, value):
        self._acpid = value
    @property
    def delegation_desc(self):
        return self._delegation_desc

    @delegation_desc.setter
    def delegation_desc(self, value):
        self._delegation_desc = value
    @property
    def delegation_scene(self):
        return self._delegation_scene

    @delegation_scene.setter
    def delegation_scene(self, value):
        self._delegation_scene = value
    @property
    def delegation_tag(self):
        return self._delegation_tag

    @delegation_tag.setter
    def delegation_tag(self, value):
        self._delegation_tag = value
    @property
    def delegation_task_params(self):
        return self._delegation_task_params

    @delegation_task_params.setter
    def delegation_task_params(self, value):
        if isinstance(value, DelegationTaskParams):
            self._delegation_task_params = value
        else:
            self._delegation_task_params = DelegationTaskParams.from_alipay_dict(value)
    @property
    def external_delegation_id(self):
        return self._external_delegation_id

    @external_delegation_id.setter
    def external_delegation_id(self, value):
        self._external_delegation_id = value
    @property
    def external_tradeno_list(self):
        return self._external_tradeno_list

    @external_tradeno_list.setter
    def external_tradeno_list(self, value):
        self._external_tradeno_list = value
    @property
    def first_deduct_time(self):
        return self._first_deduct_time

    @first_deduct_time.setter
    def first_deduct_time(self, value):
        self._first_deduct_time = value
    @property
    def goods_logo(self):
        return self._goods_logo

    @goods_logo.setter
    def goods_logo(self, value):
        self._goods_logo = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_sku_info(self):
        return self._goods_sku_info

    @goods_sku_info.setter
    def goods_sku_info(self, value):
        self._goods_sku_info = value
    @property
    def max_total_amount(self):
        return self._max_total_amount

    @max_total_amount.setter
    def max_total_amount(self, value):
        self._max_total_amount = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def pay_operation_info(self):
        return self._pay_operation_info

    @pay_operation_info.setter
    def pay_operation_info(self, value):
        self._pay_operation_info = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quota_amount(self):
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, value):
        self._quota_amount = value
    @property
    def times_limit(self):
        return self._times_limit

    @times_limit.setter
    def times_limit(self, value):
        self._times_limit = value
    @property
    def times_timit(self):
        return self._times_timit

    @times_timit.setter
    def times_timit(self, value):
        self._times_timit = value
    @property
    def validity_end_time(self):
        return self._validity_end_time

    @validity_end_time.setter
    def validity_end_time(self, value):
        self._validity_end_time = value
    @property
    def validity_start_time(self):
        return self._validity_start_time

    @validity_start_time.setter
    def validity_start_time(self, value):
        self._validity_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.acpid:
            if hasattr(self.acpid, 'to_alipay_dict'):
                params['acpid'] = self.acpid.to_alipay_dict()
            else:
                params['acpid'] = self.acpid
        if self.delegation_desc:
            if hasattr(self.delegation_desc, 'to_alipay_dict'):
                params['delegation_desc'] = self.delegation_desc.to_alipay_dict()
            else:
                params['delegation_desc'] = self.delegation_desc
        if self.delegation_scene:
            if hasattr(self.delegation_scene, 'to_alipay_dict'):
                params['delegation_scene'] = self.delegation_scene.to_alipay_dict()
            else:
                params['delegation_scene'] = self.delegation_scene
        if self.delegation_tag:
            if hasattr(self.delegation_tag, 'to_alipay_dict'):
                params['delegation_tag'] = self.delegation_tag.to_alipay_dict()
            else:
                params['delegation_tag'] = self.delegation_tag
        if self.delegation_task_params:
            if hasattr(self.delegation_task_params, 'to_alipay_dict'):
                params['delegation_task_params'] = self.delegation_task_params.to_alipay_dict()
            else:
                params['delegation_task_params'] = self.delegation_task_params
        if self.external_delegation_id:
            if hasattr(self.external_delegation_id, 'to_alipay_dict'):
                params['external_delegation_id'] = self.external_delegation_id.to_alipay_dict()
            else:
                params['external_delegation_id'] = self.external_delegation_id
        if self.external_tradeno_list:
            if hasattr(self.external_tradeno_list, 'to_alipay_dict'):
                params['external_tradeno_list'] = self.external_tradeno_list.to_alipay_dict()
            else:
                params['external_tradeno_list'] = self.external_tradeno_list
        if self.first_deduct_time:
            if hasattr(self.first_deduct_time, 'to_alipay_dict'):
                params['first_deduct_time'] = self.first_deduct_time.to_alipay_dict()
            else:
                params['first_deduct_time'] = self.first_deduct_time
        if self.goods_logo:
            if hasattr(self.goods_logo, 'to_alipay_dict'):
                params['goods_logo'] = self.goods_logo.to_alipay_dict()
            else:
                params['goods_logo'] = self.goods_logo
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_sku_info:
            if hasattr(self.goods_sku_info, 'to_alipay_dict'):
                params['goods_sku_info'] = self.goods_sku_info.to_alipay_dict()
            else:
                params['goods_sku_info'] = self.goods_sku_info
        if self.max_total_amount:
            if hasattr(self.max_total_amount, 'to_alipay_dict'):
                params['max_total_amount'] = self.max_total_amount.to_alipay_dict()
            else:
                params['max_total_amount'] = self.max_total_amount
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.pay_operation_info:
            if hasattr(self.pay_operation_info, 'to_alipay_dict'):
                params['pay_operation_info'] = self.pay_operation_info.to_alipay_dict()
            else:
                params['pay_operation_info'] = self.pay_operation_info
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quota_amount:
            if hasattr(self.quota_amount, 'to_alipay_dict'):
                params['quota_amount'] = self.quota_amount.to_alipay_dict()
            else:
                params['quota_amount'] = self.quota_amount
        if self.times_limit:
            if hasattr(self.times_limit, 'to_alipay_dict'):
                params['times_limit'] = self.times_limit.to_alipay_dict()
            else:
                params['times_limit'] = self.times_limit
        if self.times_timit:
            if hasattr(self.times_timit, 'to_alipay_dict'):
                params['times_timit'] = self.times_timit.to_alipay_dict()
            else:
                params['times_timit'] = self.times_timit
        if self.validity_end_time:
            if hasattr(self.validity_end_time, 'to_alipay_dict'):
                params['validity_end_time'] = self.validity_end_time.to_alipay_dict()
            else:
                params['validity_end_time'] = self.validity_end_time
        if self.validity_start_time:
            if hasattr(self.validity_start_time, 'to_alipay_dict'):
                params['validity_start_time'] = self.validity_start_time.to_alipay_dict()
            else:
                params['validity_start_time'] = self.validity_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DelegationParams()
        if 'acpid' in d:
            o.acpid = d['acpid']
        if 'delegation_desc' in d:
            o.delegation_desc = d['delegation_desc']
        if 'delegation_scene' in d:
            o.delegation_scene = d['delegation_scene']
        if 'delegation_tag' in d:
            o.delegation_tag = d['delegation_tag']
        if 'delegation_task_params' in d:
            o.delegation_task_params = d['delegation_task_params']
        if 'external_delegation_id' in d:
            o.external_delegation_id = d['external_delegation_id']
        if 'external_tradeno_list' in d:
            o.external_tradeno_list = d['external_tradeno_list']
        if 'first_deduct_time' in d:
            o.first_deduct_time = d['first_deduct_time']
        if 'goods_logo' in d:
            o.goods_logo = d['goods_logo']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_sku_info' in d:
            o.goods_sku_info = d['goods_sku_info']
        if 'max_total_amount' in d:
            o.max_total_amount = d['max_total_amount']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'pay_operation_info' in d:
            o.pay_operation_info = d['pay_operation_info']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quota_amount' in d:
            o.quota_amount = d['quota_amount']
        if 'times_limit' in d:
            o.times_limit = d['times_limit']
        if 'times_timit' in d:
            o.times_timit = d['times_timit']
        if 'validity_end_time' in d:
            o.validity_end_time = d['validity_end_time']
        if 'validity_start_time' in d:
            o.validity_start_time = d['validity_start_time']
        return o


