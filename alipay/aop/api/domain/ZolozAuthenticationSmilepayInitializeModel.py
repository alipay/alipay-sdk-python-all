#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FaceExtParams import FaceExtParams
from alipay.aop.api.domain.FaceMachineInfo import FaceMachineInfo
from alipay.aop.api.domain.FaceMerchantInfo import FaceMerchantInfo


class ZolozAuthenticationSmilepayInitializeModel(object):

    def __init__(self):
        self._apdid_token = None
        self._app_name = None
        self._app_version = None
        self._base_ver = None
        self._bio_meta_info = None
        self._device_model = None
        self._device_type = None
        self._ext_info = None
        self._machine_info = None
        self._merchant_info = None
        self._os_version = None
        self._remote_log_id = None
        self._zim_ver = None

    @property
    def apdid_token(self):
        return self._apdid_token

    @apdid_token.setter
    def apdid_token(self, value):
        self._apdid_token = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def base_ver(self):
        return self._base_ver

    @base_ver.setter
    def base_ver(self, value):
        self._base_ver = value
    @property
    def bio_meta_info(self):
        return self._bio_meta_info

    @bio_meta_info.setter
    def bio_meta_info(self, value):
        self._bio_meta_info = value
    @property
    def device_model(self):
        return self._device_model

    @device_model.setter
    def device_model(self, value):
        self._device_model = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, FaceExtParams):
            self._ext_info = value
        else:
            self._ext_info = FaceExtParams.from_alipay_dict(value)
    @property
    def machine_info(self):
        return self._machine_info

    @machine_info.setter
    def machine_info(self, value):
        if isinstance(value, FaceMachineInfo):
            self._machine_info = value
        else:
            self._machine_info = FaceMachineInfo.from_alipay_dict(value)
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, FaceMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = FaceMerchantInfo.from_alipay_dict(value)
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value
    @property
    def remote_log_id(self):
        return self._remote_log_id

    @remote_log_id.setter
    def remote_log_id(self, value):
        self._remote_log_id = value
    @property
    def zim_ver(self):
        return self._zim_ver

    @zim_ver.setter
    def zim_ver(self, value):
        self._zim_ver = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid_token:
            if hasattr(self.apdid_token, 'to_alipay_dict'):
                params['apdid_token'] = self.apdid_token.to_alipay_dict()
            else:
                params['apdid_token'] = self.apdid_token
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.base_ver:
            if hasattr(self.base_ver, 'to_alipay_dict'):
                params['base_ver'] = self.base_ver.to_alipay_dict()
            else:
                params['base_ver'] = self.base_ver
        if self.bio_meta_info:
            if hasattr(self.bio_meta_info, 'to_alipay_dict'):
                params['bio_meta_info'] = self.bio_meta_info.to_alipay_dict()
            else:
                params['bio_meta_info'] = self.bio_meta_info
        if self.device_model:
            if hasattr(self.device_model, 'to_alipay_dict'):
                params['device_model'] = self.device_model.to_alipay_dict()
            else:
                params['device_model'] = self.device_model
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.machine_info:
            if hasattr(self.machine_info, 'to_alipay_dict'):
                params['machine_info'] = self.machine_info.to_alipay_dict()
            else:
                params['machine_info'] = self.machine_info
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.os_version:
            if hasattr(self.os_version, 'to_alipay_dict'):
                params['os_version'] = self.os_version.to_alipay_dict()
            else:
                params['os_version'] = self.os_version
        if self.remote_log_id:
            if hasattr(self.remote_log_id, 'to_alipay_dict'):
                params['remote_log_id'] = self.remote_log_id.to_alipay_dict()
            else:
                params['remote_log_id'] = self.remote_log_id
        if self.zim_ver:
            if hasattr(self.zim_ver, 'to_alipay_dict'):
                params['zim_ver'] = self.zim_ver.to_alipay_dict()
            else:
                params['zim_ver'] = self.zim_ver
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationSmilepayInitializeModel()
        if 'apdid_token' in d:
            o.apdid_token = d['apdid_token']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'base_ver' in d:
            o.base_ver = d['base_ver']
        if 'bio_meta_info' in d:
            o.bio_meta_info = d['bio_meta_info']
        if 'device_model' in d:
            o.device_model = d['device_model']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'machine_info' in d:
            o.machine_info = d['machine_info']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'os_version' in d:
            o.os_version = d['os_version']
        if 'remote_log_id' in d:
            o.remote_log_id = d['remote_log_id']
        if 'zim_ver' in d:
            o.zim_ver = d['zim_ver']
        return o


