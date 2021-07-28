#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceUpgradeappCreateModel(object):

    def __init__(self):
        self._remark = None
        self._sn = None
        self._target_app_id = None
        self._target_app_version = None

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        if isinstance(value, list):
            self._sn = list()
            for i in value:
                self._sn.append(i)
    @property
    def target_app_id(self):
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, value):
        self._target_app_id = value
    @property
    def target_app_version(self):
        return self._target_app_version

    @target_app_version.setter
    def target_app_version(self, value):
        self._target_app_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sn:
            if isinstance(self.sn, list):
                for i in range(0, len(self.sn)):
                    element = self.sn[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn[i] = element.to_alipay_dict()
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.target_app_id:
            if hasattr(self.target_app_id, 'to_alipay_dict'):
                params['target_app_id'] = self.target_app_id.to_alipay_dict()
            else:
                params['target_app_id'] = self.target_app_id
        if self.target_app_version:
            if hasattr(self.target_app_version, 'to_alipay_dict'):
                params['target_app_version'] = self.target_app_version.to_alipay_dict()
            else:
                params['target_app_version'] = self.target_app_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceUpgradeappCreateModel()
        if 'remark' in d:
            o.remark = d['remark']
        if 'sn' in d:
            o.sn = d['sn']
        if 'target_app_id' in d:
            o.target_app_id = d['target_app_id']
        if 'target_app_version' in d:
            o.target_app_version = d['target_app_version']
        return o


