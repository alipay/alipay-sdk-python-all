#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdSeAppletQueryModel(object):

    def __init__(self):
        self._opt_type = None
        self._param = None
        self._partner_id = None
        self._se_id = None
        self._se_version = None
        self._sub_opt_type = None

    @property
    def opt_type(self):
        return self._opt_type

    @opt_type.setter
    def opt_type(self, value):
        self._opt_type = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def se_id(self):
        return self._se_id

    @se_id.setter
    def se_id(self, value):
        self._se_id = value
    @property
    def se_version(self):
        return self._se_version

    @se_version.setter
    def se_version(self, value):
        self._se_version = value
    @property
    def sub_opt_type(self):
        return self._sub_opt_type

    @sub_opt_type.setter
    def sub_opt_type(self, value):
        self._sub_opt_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.opt_type:
            if hasattr(self.opt_type, 'to_alipay_dict'):
                params['opt_type'] = self.opt_type.to_alipay_dict()
            else:
                params['opt_type'] = self.opt_type
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.se_id:
            if hasattr(self.se_id, 'to_alipay_dict'):
                params['se_id'] = self.se_id.to_alipay_dict()
            else:
                params['se_id'] = self.se_id
        if self.se_version:
            if hasattr(self.se_version, 'to_alipay_dict'):
                params['se_version'] = self.se_version.to_alipay_dict()
            else:
                params['se_version'] = self.se_version
        if self.sub_opt_type:
            if hasattr(self.sub_opt_type, 'to_alipay_dict'):
                params['sub_opt_type'] = self.sub_opt_type.to_alipay_dict()
            else:
                params['sub_opt_type'] = self.sub_opt_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdSeAppletQueryModel()
        if 'opt_type' in d:
            o.opt_type = d['opt_type']
        if 'param' in d:
            o.param = d['param']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'se_id' in d:
            o.se_id = d['se_id']
        if 'se_version' in d:
            o.se_version = d['se_version']
        if 'sub_opt_type' in d:
            o.sub_opt_type = d['sub_opt_type']
        return o


