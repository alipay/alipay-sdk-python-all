#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CVGoodsInfo import CVGoodsInfo


class AlipayMsaasMediarecogMmportalCvgoodsSyncModel(object):

    def __init__(self):
        self._apply_id = None
        self._audit_time = None
        self._ext_info = None
        self._goods_info = None
        self._goods_type = None
        self._isv_pid = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, CVGoodsInfo):
            self._goods_info = value
        else:
            self._goods_info = CVGoodsInfo.from_alipay_dict(value)
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmportalCvgoodsSyncModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        return o


