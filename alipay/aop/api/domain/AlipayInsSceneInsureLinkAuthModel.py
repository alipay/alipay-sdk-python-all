#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsureLinkAuthModel(object):

    def __init__(self):
        self._device_activation_time = None
        self._device_serial_number = None
        self._equipment_model = None
        self._login_user_id = None
        self._out_session_expiration = None
        self._out_session_id = None
        self._partner_org_id = None
        self._prod_no = None
        self._user_client = None

    @property
    def device_activation_time(self):
        return self._device_activation_time

    @device_activation_time.setter
    def device_activation_time(self, value):
        self._device_activation_time = value
    @property
    def device_serial_number(self):
        return self._device_serial_number

    @device_serial_number.setter
    def device_serial_number(self, value):
        self._device_serial_number = value
    @property
    def equipment_model(self):
        return self._equipment_model

    @equipment_model.setter
    def equipment_model(self, value):
        self._equipment_model = value
    @property
    def login_user_id(self):
        return self._login_user_id

    @login_user_id.setter
    def login_user_id(self, value):
        self._login_user_id = value
    @property
    def out_session_expiration(self):
        return self._out_session_expiration

    @out_session_expiration.setter
    def out_session_expiration(self, value):
        self._out_session_expiration = value
    @property
    def out_session_id(self):
        return self._out_session_id

    @out_session_id.setter
    def out_session_id(self, value):
        self._out_session_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_activation_time:
            if hasattr(self.device_activation_time, 'to_alipay_dict'):
                params['device_activation_time'] = self.device_activation_time.to_alipay_dict()
            else:
                params['device_activation_time'] = self.device_activation_time
        if self.device_serial_number:
            if hasattr(self.device_serial_number, 'to_alipay_dict'):
                params['device_serial_number'] = self.device_serial_number.to_alipay_dict()
            else:
                params['device_serial_number'] = self.device_serial_number
        if self.equipment_model:
            if hasattr(self.equipment_model, 'to_alipay_dict'):
                params['equipment_model'] = self.equipment_model.to_alipay_dict()
            else:
                params['equipment_model'] = self.equipment_model
        if self.login_user_id:
            if hasattr(self.login_user_id, 'to_alipay_dict'):
                params['login_user_id'] = self.login_user_id.to_alipay_dict()
            else:
                params['login_user_id'] = self.login_user_id
        if self.out_session_expiration:
            if hasattr(self.out_session_expiration, 'to_alipay_dict'):
                params['out_session_expiration'] = self.out_session_expiration.to_alipay_dict()
            else:
                params['out_session_expiration'] = self.out_session_expiration
        if self.out_session_id:
            if hasattr(self.out_session_id, 'to_alipay_dict'):
                params['out_session_id'] = self.out_session_id.to_alipay_dict()
            else:
                params['out_session_id'] = self.out_session_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        if self.user_client:
            if hasattr(self.user_client, 'to_alipay_dict'):
                params['user_client'] = self.user_client.to_alipay_dict()
            else:
                params['user_client'] = self.user_client
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsureLinkAuthModel()
        if 'device_activation_time' in d:
            o.device_activation_time = d['device_activation_time']
        if 'device_serial_number' in d:
            o.device_serial_number = d['device_serial_number']
        if 'equipment_model' in d:
            o.equipment_model = d['equipment_model']
        if 'login_user_id' in d:
            o.login_user_id = d['login_user_id']
        if 'out_session_expiration' in d:
            o.out_session_expiration = d['out_session_expiration']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


