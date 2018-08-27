#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BeaconTemplate import BeaconTemplate


class BeaconDeviceInfo(object):

    def __init__(self):
        self._actiontype = None
        self._inuse = None
        self._remark = None
        self._sn = None
        self._template = None
        self._uuid = None

    @property
    def actiontype(self):
        return self._actiontype

    @actiontype.setter
    def actiontype(self, value):
        self._actiontype = value
    @property
    def inuse(self):
        return self._inuse

    @inuse.setter
    def inuse(self, value):
        self._inuse = value
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
        self._sn = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, BeaconTemplate):
            self._template = value
        else:
            self._template = BeaconTemplate.from_alipay_dict(value)
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.actiontype:
            if hasattr(self.actiontype, 'to_alipay_dict'):
                params['actiontype'] = self.actiontype.to_alipay_dict()
            else:
                params['actiontype'] = self.actiontype
        if self.inuse:
            if hasattr(self.inuse, 'to_alipay_dict'):
                params['inuse'] = self.inuse.to_alipay_dict()
            else:
                params['inuse'] = self.inuse
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BeaconDeviceInfo()
        if 'actiontype' in d:
            o.actiontype = d['actiontype']
        if 'inuse' in d:
            o.inuse = d['inuse']
        if 'remark' in d:
            o.remark = d['remark']
        if 'sn' in d:
            o.sn = d['sn']
        if 'template' in d:
            o.template = d['template']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


