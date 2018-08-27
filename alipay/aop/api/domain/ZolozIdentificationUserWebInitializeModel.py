#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdentityParam import IdentityParam


class ZolozIdentificationUserWebInitializeModel(object):

    def __init__(self):
        self._biz_id = None
        self._extern_param = None
        self._identity_param = None
        self._metainfo = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def extern_param(self):
        return self._extern_param

    @extern_param.setter
    def extern_param(self, value):
        self._extern_param = value
    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        if isinstance(value, IdentityParam):
            self._identity_param = value
        else:
            self._identity_param = IdentityParam.from_alipay_dict(value)
    @property
    def metainfo(self):
        return self._metainfo

    @metainfo.setter
    def metainfo(self, value):
        self._metainfo = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.extern_param:
            if hasattr(self.extern_param, 'to_alipay_dict'):
                params['extern_param'] = self.extern_param.to_alipay_dict()
            else:
                params['extern_param'] = self.extern_param
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        if self.metainfo:
            if hasattr(self.metainfo, 'to_alipay_dict'):
                params['metainfo'] = self.metainfo.to_alipay_dict()
            else:
                params['metainfo'] = self.metainfo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationUserWebInitializeModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'extern_param' in d:
            o.extern_param = d['extern_param']
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        if 'metainfo' in d:
            o.metainfo = d['metainfo']
        return o


