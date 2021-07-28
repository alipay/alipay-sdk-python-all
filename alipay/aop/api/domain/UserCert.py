#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserCert(object):

    def __init__(self):
        self._apply_time = None
        self._certificate_id = None
        self._ext_info = None
        self._forest_id = None
        self._ngo_name = None
        self._planted = None
        self._region = None
        self._tree_name = None
        self._type = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def forest_id(self):
        return self._forest_id

    @forest_id.setter
    def forest_id(self, value):
        self._forest_id = value
    @property
    def ngo_name(self):
        return self._ngo_name

    @ngo_name.setter
    def ngo_name(self, value):
        self._ngo_name = value
    @property
    def planted(self):
        return self._planted

    @planted.setter
    def planted(self, value):
        self._planted = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def tree_name(self):
        return self._tree_name

    @tree_name.setter
    def tree_name(self, value):
        self._tree_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.forest_id:
            if hasattr(self.forest_id, 'to_alipay_dict'):
                params['forest_id'] = self.forest_id.to_alipay_dict()
            else:
                params['forest_id'] = self.forest_id
        if self.ngo_name:
            if hasattr(self.ngo_name, 'to_alipay_dict'):
                params['ngo_name'] = self.ngo_name.to_alipay_dict()
            else:
                params['ngo_name'] = self.ngo_name
        if self.planted:
            if hasattr(self.planted, 'to_alipay_dict'):
                params['planted'] = self.planted.to_alipay_dict()
            else:
                params['planted'] = self.planted
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.tree_name:
            if hasattr(self.tree_name, 'to_alipay_dict'):
                params['tree_name'] = self.tree_name.to_alipay_dict()
            else:
                params['tree_name'] = self.tree_name
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
        o = UserCert()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'forest_id' in d:
            o.forest_id = d['forest_id']
        if 'ngo_name' in d:
            o.ngo_name = d['ngo_name']
        if 'planted' in d:
            o.planted = d['planted']
        if 'region' in d:
            o.region = d['region']
        if 'tree_name' in d:
            o.tree_name = d['tree_name']
        if 'type' in d:
            o.type = d['type']
        return o


