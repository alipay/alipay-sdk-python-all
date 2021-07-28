#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountTypeSyncData import AmountTypeSyncData
from alipay.aop.api.domain.DiscountTypeSyncData import DiscountTypeSyncData
from alipay.aop.api.domain.TimesTypeSyncData import TimesTypeSyncData


class ZhimaMerchantZmgoCumulateSyncModel(object):

    def __init__(self):
        self._agreement_id = None
        self._amount_type_sync_data = None
        self._biz_action = None
        self._biz_time = None
        self._data_type = None
        self._discount_type_sync_data = None
        self._out_biz_no = None
        self._provider_pid = None
        self._refer_out_biz_no = None
        self._sub_biz_action = None
        self._times_type_sync_data = None
        self._user_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def amount_type_sync_data(self):
        return self._amount_type_sync_data

    @amount_type_sync_data.setter
    def amount_type_sync_data(self, value):
        if isinstance(value, AmountTypeSyncData):
            self._amount_type_sync_data = value
        else:
            self._amount_type_sync_data = AmountTypeSyncData.from_alipay_dict(value)
    @property
    def biz_action(self):
        return self._biz_action

    @biz_action.setter
    def biz_action(self, value):
        self._biz_action = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def discount_type_sync_data(self):
        return self._discount_type_sync_data

    @discount_type_sync_data.setter
    def discount_type_sync_data(self, value):
        if isinstance(value, DiscountTypeSyncData):
            self._discount_type_sync_data = value
        else:
            self._discount_type_sync_data = DiscountTypeSyncData.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def provider_pid(self):
        return self._provider_pid

    @provider_pid.setter
    def provider_pid(self, value):
        self._provider_pid = value
    @property
    def refer_out_biz_no(self):
        return self._refer_out_biz_no

    @refer_out_biz_no.setter
    def refer_out_biz_no(self, value):
        self._refer_out_biz_no = value
    @property
    def sub_biz_action(self):
        return self._sub_biz_action

    @sub_biz_action.setter
    def sub_biz_action(self, value):
        self._sub_biz_action = value
    @property
    def times_type_sync_data(self):
        return self._times_type_sync_data

    @times_type_sync_data.setter
    def times_type_sync_data(self, value):
        if isinstance(value, TimesTypeSyncData):
            self._times_type_sync_data = value
        else:
            self._times_type_sync_data = TimesTypeSyncData.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.amount_type_sync_data:
            if hasattr(self.amount_type_sync_data, 'to_alipay_dict'):
                params['amount_type_sync_data'] = self.amount_type_sync_data.to_alipay_dict()
            else:
                params['amount_type_sync_data'] = self.amount_type_sync_data
        if self.biz_action:
            if hasattr(self.biz_action, 'to_alipay_dict'):
                params['biz_action'] = self.biz_action.to_alipay_dict()
            else:
                params['biz_action'] = self.biz_action
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.discount_type_sync_data:
            if hasattr(self.discount_type_sync_data, 'to_alipay_dict'):
                params['discount_type_sync_data'] = self.discount_type_sync_data.to_alipay_dict()
            else:
                params['discount_type_sync_data'] = self.discount_type_sync_data
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.provider_pid:
            if hasattr(self.provider_pid, 'to_alipay_dict'):
                params['provider_pid'] = self.provider_pid.to_alipay_dict()
            else:
                params['provider_pid'] = self.provider_pid
        if self.refer_out_biz_no:
            if hasattr(self.refer_out_biz_no, 'to_alipay_dict'):
                params['refer_out_biz_no'] = self.refer_out_biz_no.to_alipay_dict()
            else:
                params['refer_out_biz_no'] = self.refer_out_biz_no
        if self.sub_biz_action:
            if hasattr(self.sub_biz_action, 'to_alipay_dict'):
                params['sub_biz_action'] = self.sub_biz_action.to_alipay_dict()
            else:
                params['sub_biz_action'] = self.sub_biz_action
        if self.times_type_sync_data:
            if hasattr(self.times_type_sync_data, 'to_alipay_dict'):
                params['times_type_sync_data'] = self.times_type_sync_data.to_alipay_dict()
            else:
                params['times_type_sync_data'] = self.times_type_sync_data
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
        o = ZhimaMerchantZmgoCumulateSyncModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'amount_type_sync_data' in d:
            o.amount_type_sync_data = d['amount_type_sync_data']
        if 'biz_action' in d:
            o.biz_action = d['biz_action']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'discount_type_sync_data' in d:
            o.discount_type_sync_data = d['discount_type_sync_data']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'provider_pid' in d:
            o.provider_pid = d['provider_pid']
        if 'refer_out_biz_no' in d:
            o.refer_out_biz_no = d['refer_out_biz_no']
        if 'sub_biz_action' in d:
            o.sub_biz_action = d['sub_biz_action']
        if 'times_type_sync_data' in d:
            o.times_type_sync_data = d['times_type_sync_data']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


