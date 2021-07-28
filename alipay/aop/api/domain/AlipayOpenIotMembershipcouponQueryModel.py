#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotMembershipcouponQueryModel(object):

    def __init__(self):
        self._application_id = None
        self._membership_id = None
        self._service_id = None
        self._sn = None

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def membership_id(self):
        return self._membership_id

    @membership_id.setter
    def membership_id(self, value):
        self._membership_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.membership_id:
            if hasattr(self.membership_id, 'to_alipay_dict'):
                params['membership_id'] = self.membership_id.to_alipay_dict()
            else:
                params['membership_id'] = self.membership_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotMembershipcouponQueryModel()
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'membership_id' in d:
            o.membership_id = d['membership_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sn' in d:
            o.sn = d['sn']
        return o


