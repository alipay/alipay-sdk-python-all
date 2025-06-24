#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudSwnetflowCardfullSyncModel(object):

    def __init__(self):
        self._active_time = None
        self._biling_cycle = None
        self._card_status = None
        self._credential_name = None
        self._data_type = None
        self._destroy_time = None
        self._gprs_status = None
        self._icc_id = None
        self._imei = None
        self._is_over_limit = None
        self._last_stop_date = None
        self._os_status = None
        self._pool_id = None
        self._sw_order_id = None
        self._total_flow_amount = None
        self._vendor_id = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def biling_cycle(self):
        return self._biling_cycle

    @biling_cycle.setter
    def biling_cycle(self, value):
        self._biling_cycle = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def credential_name(self):
        return self._credential_name

    @credential_name.setter
    def credential_name(self, value):
        self._credential_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def destroy_time(self):
        return self._destroy_time

    @destroy_time.setter
    def destroy_time(self, value):
        self._destroy_time = value
    @property
    def gprs_status(self):
        return self._gprs_status

    @gprs_status.setter
    def gprs_status(self, value):
        self._gprs_status = value
    @property
    def icc_id(self):
        return self._icc_id

    @icc_id.setter
    def icc_id(self, value):
        self._icc_id = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def is_over_limit(self):
        return self._is_over_limit

    @is_over_limit.setter
    def is_over_limit(self, value):
        self._is_over_limit = value
    @property
    def last_stop_date(self):
        return self._last_stop_date

    @last_stop_date.setter
    def last_stop_date(self, value):
        self._last_stop_date = value
    @property
    def os_status(self):
        return self._os_status

    @os_status.setter
    def os_status(self, value):
        self._os_status = value
    @property
    def pool_id(self):
        return self._pool_id

    @pool_id.setter
    def pool_id(self, value):
        self._pool_id = value
    @property
    def sw_order_id(self):
        return self._sw_order_id

    @sw_order_id.setter
    def sw_order_id(self, value):
        self._sw_order_id = value
    @property
    def total_flow_amount(self):
        return self._total_flow_amount

    @total_flow_amount.setter
    def total_flow_amount(self, value):
        self._total_flow_amount = value
    @property
    def vendor_id(self):
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, value):
        self._vendor_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.biling_cycle:
            if hasattr(self.biling_cycle, 'to_alipay_dict'):
                params['biling_cycle'] = self.biling_cycle.to_alipay_dict()
            else:
                params['biling_cycle'] = self.biling_cycle
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.credential_name:
            if hasattr(self.credential_name, 'to_alipay_dict'):
                params['credential_name'] = self.credential_name.to_alipay_dict()
            else:
                params['credential_name'] = self.credential_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.destroy_time:
            if hasattr(self.destroy_time, 'to_alipay_dict'):
                params['destroy_time'] = self.destroy_time.to_alipay_dict()
            else:
                params['destroy_time'] = self.destroy_time
        if self.gprs_status:
            if hasattr(self.gprs_status, 'to_alipay_dict'):
                params['gprs_status'] = self.gprs_status.to_alipay_dict()
            else:
                params['gprs_status'] = self.gprs_status
        if self.icc_id:
            if hasattr(self.icc_id, 'to_alipay_dict'):
                params['icc_id'] = self.icc_id.to_alipay_dict()
            else:
                params['icc_id'] = self.icc_id
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.is_over_limit:
            if hasattr(self.is_over_limit, 'to_alipay_dict'):
                params['is_over_limit'] = self.is_over_limit.to_alipay_dict()
            else:
                params['is_over_limit'] = self.is_over_limit
        if self.last_stop_date:
            if hasattr(self.last_stop_date, 'to_alipay_dict'):
                params['last_stop_date'] = self.last_stop_date.to_alipay_dict()
            else:
                params['last_stop_date'] = self.last_stop_date
        if self.os_status:
            if hasattr(self.os_status, 'to_alipay_dict'):
                params['os_status'] = self.os_status.to_alipay_dict()
            else:
                params['os_status'] = self.os_status
        if self.pool_id:
            if hasattr(self.pool_id, 'to_alipay_dict'):
                params['pool_id'] = self.pool_id.to_alipay_dict()
            else:
                params['pool_id'] = self.pool_id
        if self.sw_order_id:
            if hasattr(self.sw_order_id, 'to_alipay_dict'):
                params['sw_order_id'] = self.sw_order_id.to_alipay_dict()
            else:
                params['sw_order_id'] = self.sw_order_id
        if self.total_flow_amount:
            if hasattr(self.total_flow_amount, 'to_alipay_dict'):
                params['total_flow_amount'] = self.total_flow_amount.to_alipay_dict()
            else:
                params['total_flow_amount'] = self.total_flow_amount
        if self.vendor_id:
            if hasattr(self.vendor_id, 'to_alipay_dict'):
                params['vendor_id'] = self.vendor_id.to_alipay_dict()
            else:
                params['vendor_id'] = self.vendor_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudSwnetflowCardfullSyncModel()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'biling_cycle' in d:
            o.biling_cycle = d['biling_cycle']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'credential_name' in d:
            o.credential_name = d['credential_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'destroy_time' in d:
            o.destroy_time = d['destroy_time']
        if 'gprs_status' in d:
            o.gprs_status = d['gprs_status']
        if 'icc_id' in d:
            o.icc_id = d['icc_id']
        if 'imei' in d:
            o.imei = d['imei']
        if 'is_over_limit' in d:
            o.is_over_limit = d['is_over_limit']
        if 'last_stop_date' in d:
            o.last_stop_date = d['last_stop_date']
        if 'os_status' in d:
            o.os_status = d['os_status']
        if 'pool_id' in d:
            o.pool_id = d['pool_id']
        if 'sw_order_id' in d:
            o.sw_order_id = d['sw_order_id']
        if 'total_flow_amount' in d:
            o.total_flow_amount = d['total_flow_amount']
        if 'vendor_id' in d:
            o.vendor_id = d['vendor_id']
        return o


