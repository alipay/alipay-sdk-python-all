#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MstDataSyncServiceEntity import MstDataSyncServiceEntity


class AlipayEbppInspectCreateModel(object):

    def __init__(self):
        self._biz_type = None
        self._creator = None
        self._data_from_type = None
        self._is_sync_check = None
        self._out_biz_no = None
        self._service_list = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def data_from_type(self):
        return self._data_from_type

    @data_from_type.setter
    def data_from_type(self, value):
        self._data_from_type = value
    @property
    def is_sync_check(self):
        return self._is_sync_check

    @is_sync_check.setter
    def is_sync_check(self, value):
        self._is_sync_check = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, MstDataSyncServiceEntity):
                    self._service_list.append(i)
                else:
                    self._service_list.append(MstDataSyncServiceEntity.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.data_from_type:
            if hasattr(self.data_from_type, 'to_alipay_dict'):
                params['data_from_type'] = self.data_from_type.to_alipay_dict()
            else:
                params['data_from_type'] = self.data_from_type
        if self.is_sync_check:
            if hasattr(self.is_sync_check, 'to_alipay_dict'):
                params['is_sync_check'] = self.is_sync_check.to_alipay_dict()
            else:
                params['is_sync_check'] = self.is_sync_check
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.service_list:
            if isinstance(self.service_list, list):
                for i in range(0, len(self.service_list)):
                    element = self.service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_list[i] = element.to_alipay_dict()
            if hasattr(self.service_list, 'to_alipay_dict'):
                params['service_list'] = self.service_list.to_alipay_dict()
            else:
                params['service_list'] = self.service_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInspectCreateModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'creator' in d:
            o.creator = d['creator']
        if 'data_from_type' in d:
            o.data_from_type = d['data_from_type']
        if 'is_sync_check' in d:
            o.is_sync_check = d['is_sync_check']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'service_list' in d:
            o.service_list = d['service_list']
        return o


