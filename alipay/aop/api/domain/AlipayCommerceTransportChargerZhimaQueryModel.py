#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerZhimaQueryModel(object):

    def __init__(self):
        self._device_id = None
        self._id_num = None
        self._ip_address = None
        self._open_id = None
        self._out_agreement_no = None
        self._phone_num = None
        self._service_id = None
        self._user_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def id_num(self):
        return self._id_num

    @id_num.setter
    def id_num(self, value):
        self._id_num = value
    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, value):
        self._phone_num = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.id_num:
            if hasattr(self.id_num, 'to_alipay_dict'):
                params['id_num'] = self.id_num.to_alipay_dict()
            else:
                params['id_num'] = self.id_num
        if self.ip_address:
            if hasattr(self.ip_address, 'to_alipay_dict'):
                params['ip_address'] = self.ip_address.to_alipay_dict()
            else:
                params['ip_address'] = self.ip_address
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.phone_num:
            if hasattr(self.phone_num, 'to_alipay_dict'):
                params['phone_num'] = self.phone_num.to_alipay_dict()
            else:
                params['phone_num'] = self.phone_num
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerZhimaQueryModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'id_num' in d:
            o.id_num = d['id_num']
        if 'ip_address' in d:
            o.ip_address = d['ip_address']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'phone_num' in d:
            o.phone_num = d['phone_num']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


