#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncModel(object):

    def __init__(self):
        self._biz_id = None
        self._device_id = None
        self._external_info = None
        self._goods_list = None
        self._isv_pid = None
        self._submit_time = None
        self._type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def external_info(self):
        return self._external_info

    @external_info.setter
    def external_info(self, value):
        self._external_info = value
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                self._goods_list.append(i)
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.external_info:
            if hasattr(self.external_info, 'to_alipay_dict'):
                params['external_info'] = self.external_info.to_alipay_dict()
            else:
                params['external_info'] = self.external_info
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'external_info' in d:
            o.external_info = d['external_info']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        if 'type' in d:
            o.type = d['type']
        return o


