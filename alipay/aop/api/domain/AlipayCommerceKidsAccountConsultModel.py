#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InfoSource import InfoSource


class AlipayCommerceKidsAccountConsultModel(object):

    def __init__(self):
        self._child_cert_no = None
        self._child_cert_type = None
        self._info_source = None
        self._operator_uid = None
        self._parent_uid = None
        self._scene_code = None

    @property
    def child_cert_no(self):
        return self._child_cert_no

    @child_cert_no.setter
    def child_cert_no(self, value):
        self._child_cert_no = value
    @property
    def child_cert_type(self):
        return self._child_cert_type

    @child_cert_type.setter
    def child_cert_type(self, value):
        self._child_cert_type = value
    @property
    def info_source(self):
        return self._info_source

    @info_source.setter
    def info_source(self, value):
        if isinstance(value, InfoSource):
            self._info_source = value
        else:
            self._info_source = InfoSource.from_alipay_dict(value)
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def parent_uid(self):
        return self._parent_uid

    @parent_uid.setter
    def parent_uid(self, value):
        self._parent_uid = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.child_cert_no:
            if hasattr(self.child_cert_no, 'to_alipay_dict'):
                params['child_cert_no'] = self.child_cert_no.to_alipay_dict()
            else:
                params['child_cert_no'] = self.child_cert_no
        if self.child_cert_type:
            if hasattr(self.child_cert_type, 'to_alipay_dict'):
                params['child_cert_type'] = self.child_cert_type.to_alipay_dict()
            else:
                params['child_cert_type'] = self.child_cert_type
        if self.info_source:
            if hasattr(self.info_source, 'to_alipay_dict'):
                params['info_source'] = self.info_source.to_alipay_dict()
            else:
                params['info_source'] = self.info_source
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.parent_uid:
            if hasattr(self.parent_uid, 'to_alipay_dict'):
                params['parent_uid'] = self.parent_uid.to_alipay_dict()
            else:
                params['parent_uid'] = self.parent_uid
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceKidsAccountConsultModel()
        if 'child_cert_no' in d:
            o.child_cert_no = d['child_cert_no']
        if 'child_cert_type' in d:
            o.child_cert_type = d['child_cert_type']
        if 'info_source' in d:
            o.info_source = d['info_source']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'parent_uid' in d:
            o.parent_uid = d['parent_uid']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


