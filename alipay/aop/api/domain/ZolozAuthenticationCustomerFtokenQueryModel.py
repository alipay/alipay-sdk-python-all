#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FaceExtInfo import FaceExtInfo


class ZolozAuthenticationCustomerFtokenQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._ext_info = None
        self._ftoken = None
        self._zim_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, FaceExtInfo):
            self._ext_info = value
        else:
            self._ext_info = FaceExtInfo.from_alipay_dict(value)
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.zim_id:
            if hasattr(self.zim_id, 'to_alipay_dict'):
                params['zim_id'] = self.zim_id.to_alipay_dict()
            else:
                params['zim_id'] = self.zim_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerFtokenQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'zim_id' in d:
            o.zim_id = d['zim_id']
        return o


