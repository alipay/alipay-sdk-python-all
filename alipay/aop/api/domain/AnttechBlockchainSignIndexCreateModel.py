#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainSignIndexCreateModel(object):

    def __init__(self):
        self._app_name = None
        self._biz_corp = None
        self._biz_from = None
        self._biz_scene = None
        self._biz_unique_key = None
        self._principal_id = None
        self._principal_type = None
        self._sign_version = None
        self._tenant = None
        self._valid_end_date = None
        self._valid_start_date = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_corp(self):
        return self._biz_corp

    @biz_corp.setter
    def biz_corp(self, value):
        self._biz_corp = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_unique_key(self):
        return self._biz_unique_key

    @biz_unique_key.setter
    def biz_unique_key(self, value):
        self._biz_unique_key = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def sign_version(self):
        return self._sign_version

    @sign_version.setter
    def sign_version(self, value):
        self._sign_version = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def valid_end_date(self):
        return self._valid_end_date

    @valid_end_date.setter
    def valid_end_date(self, value):
        self._valid_end_date = value
    @property
    def valid_start_date(self):
        return self._valid_start_date

    @valid_start_date.setter
    def valid_start_date(self, value):
        self._valid_start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_corp:
            if hasattr(self.biz_corp, 'to_alipay_dict'):
                params['biz_corp'] = self.biz_corp.to_alipay_dict()
            else:
                params['biz_corp'] = self.biz_corp
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_unique_key:
            if hasattr(self.biz_unique_key, 'to_alipay_dict'):
                params['biz_unique_key'] = self.biz_unique_key.to_alipay_dict()
            else:
                params['biz_unique_key'] = self.biz_unique_key
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        if self.sign_version:
            if hasattr(self.sign_version, 'to_alipay_dict'):
                params['sign_version'] = self.sign_version.to_alipay_dict()
            else:
                params['sign_version'] = self.sign_version
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.valid_end_date:
            if hasattr(self.valid_end_date, 'to_alipay_dict'):
                params['valid_end_date'] = self.valid_end_date.to_alipay_dict()
            else:
                params['valid_end_date'] = self.valid_end_date
        if self.valid_start_date:
            if hasattr(self.valid_start_date, 'to_alipay_dict'):
                params['valid_start_date'] = self.valid_start_date.to_alipay_dict()
            else:
                params['valid_start_date'] = self.valid_start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainSignIndexCreateModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_corp' in d:
            o.biz_corp = d['biz_corp']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_unique_key' in d:
            o.biz_unique_key = d['biz_unique_key']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'sign_version' in d:
            o.sign_version = d['sign_version']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'valid_end_date' in d:
            o.valid_end_date = d['valid_end_date']
        if 'valid_start_date' in d:
            o.valid_start_date = d['valid_start_date']
        return o


