#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsScenePositionPolicyNotifyModel(object):

    def __init__(self):
        self._device_serial_number = None
        self._inst_id = None
        self._out_user_id = None
        self._partner_org_id = None
        self._policy_no = None
        self._prod_no = None

    @property
    def device_serial_number(self):
        return self._device_serial_number

    @device_serial_number.setter
    def device_serial_number(self, value):
        self._device_serial_number = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_serial_number:
            if hasattr(self.device_serial_number, 'to_alipay_dict'):
                params['device_serial_number'] = self.device_serial_number.to_alipay_dict()
            else:
                params['device_serial_number'] = self.device_serial_number
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsScenePositionPolicyNotifyModel()
        if 'device_serial_number' in d:
            o.device_serial_number = d['device_serial_number']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        return o


