#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantApplyInfo import MerchantApplyInfo


class MerchantSettleInInfo(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._indirect_period_card_status = None
        self._last_apply_orders = None
        self._mcc_code = None
        self._merchant_id = None
        self._name = None
        self._period_card_status = None
        self._status = None
        self._xian_xiang_times_card_status = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def indirect_period_card_status(self):
        return self._indirect_period_card_status

    @indirect_period_card_status.setter
    def indirect_period_card_status(self, value):
        self._indirect_period_card_status = value
    @property
    def last_apply_orders(self):
        return self._last_apply_orders

    @last_apply_orders.setter
    def last_apply_orders(self, value):
        if isinstance(value, list):
            self._last_apply_orders = list()
            for i in value:
                if isinstance(i, MerchantApplyInfo):
                    self._last_apply_orders.append(i)
                else:
                    self._last_apply_orders.append(MerchantApplyInfo.from_alipay_dict(i))
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def period_card_status(self):
        return self._period_card_status

    @period_card_status.setter
    def period_card_status(self, value):
        self._period_card_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def xian_xiang_times_card_status(self):
        return self._xian_xiang_times_card_status

    @xian_xiang_times_card_status.setter
    def xian_xiang_times_card_status(self, value):
        self._xian_xiang_times_card_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.indirect_period_card_status:
            if hasattr(self.indirect_period_card_status, 'to_alipay_dict'):
                params['indirect_period_card_status'] = self.indirect_period_card_status.to_alipay_dict()
            else:
                params['indirect_period_card_status'] = self.indirect_period_card_status
        if self.last_apply_orders:
            if isinstance(self.last_apply_orders, list):
                for i in range(0, len(self.last_apply_orders)):
                    element = self.last_apply_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.last_apply_orders[i] = element.to_alipay_dict()
            if hasattr(self.last_apply_orders, 'to_alipay_dict'):
                params['last_apply_orders'] = self.last_apply_orders.to_alipay_dict()
            else:
                params['last_apply_orders'] = self.last_apply_orders
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.period_card_status:
            if hasattr(self.period_card_status, 'to_alipay_dict'):
                params['period_card_status'] = self.period_card_status.to_alipay_dict()
            else:
                params['period_card_status'] = self.period_card_status
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.xian_xiang_times_card_status:
            if hasattr(self.xian_xiang_times_card_status, 'to_alipay_dict'):
                params['xian_xiang_times_card_status'] = self.xian_xiang_times_card_status.to_alipay_dict()
            else:
                params['xian_xiang_times_card_status'] = self.xian_xiang_times_card_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantSettleInInfo()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'indirect_period_card_status' in d:
            o.indirect_period_card_status = d['indirect_period_card_status']
        if 'last_apply_orders' in d:
            o.last_apply_orders = d['last_apply_orders']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'name' in d:
            o.name = d['name']
        if 'period_card_status' in d:
            o.period_card_status = d['period_card_status']
        if 'status' in d:
            o.status = d['status']
        if 'xian_xiang_times_card_status' in d:
            o.xian_xiang_times_card_status = d['xian_xiang_times_card_status']
        return o


