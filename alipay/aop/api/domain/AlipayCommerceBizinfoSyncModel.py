#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizUnit import BizUnit
from alipay.aop.api.domain.HouseBizInfo import HouseBizInfo


class AlipayCommerceBizinfoSyncModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_info_id = None
        self._biz_time = None
        self._biz_unit_info = None
        self._house_biz_info = None
        self._info_type = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_info_id(self):
        return self._biz_info_id

    @biz_info_id.setter
    def biz_info_id(self, value):
        self._biz_info_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def biz_unit_info(self):
        return self._biz_unit_info

    @biz_unit_info.setter
    def biz_unit_info(self, value):
        if isinstance(value, BizUnit):
            self._biz_unit_info = value
        else:
            self._biz_unit_info = BizUnit.from_alipay_dict(value)
    @property
    def house_biz_info(self):
        return self._house_biz_info

    @house_biz_info.setter
    def house_biz_info(self, value):
        if isinstance(value, HouseBizInfo):
            self._house_biz_info = value
        else:
            self._house_biz_info = HouseBizInfo.from_alipay_dict(value)
    @property
    def info_type(self):
        return self._info_type

    @info_type.setter
    def info_type(self, value):
        self._info_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_info_id:
            if hasattr(self.biz_info_id, 'to_alipay_dict'):
                params['biz_info_id'] = self.biz_info_id.to_alipay_dict()
            else:
                params['biz_info_id'] = self.biz_info_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.biz_unit_info:
            if hasattr(self.biz_unit_info, 'to_alipay_dict'):
                params['biz_unit_info'] = self.biz_unit_info.to_alipay_dict()
            else:
                params['biz_unit_info'] = self.biz_unit_info
        if self.house_biz_info:
            if hasattr(self.house_biz_info, 'to_alipay_dict'):
                params['house_biz_info'] = self.house_biz_info.to_alipay_dict()
            else:
                params['house_biz_info'] = self.house_biz_info
        if self.info_type:
            if hasattr(self.info_type, 'to_alipay_dict'):
                params['info_type'] = self.info_type.to_alipay_dict()
            else:
                params['info_type'] = self.info_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceBizinfoSyncModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_info_id' in d:
            o.biz_info_id = d['biz_info_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'biz_unit_info' in d:
            o.biz_unit_info = d['biz_unit_info']
        if 'house_biz_info' in d:
            o.house_biz_info = d['house_biz_info']
        if 'info_type' in d:
            o.info_type = d['info_type']
        return o


