#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasOpenIndrbeneficiaryCreateModel(object):

    def __init__(self):
        self._business_partner = None
        self._partner_type = None
        self._remark = None
        self._request_id = None
        self._scene_type = None
        self._status = None
        self._sub_type = None
        self._valid_status = None

    @property
    def business_partner(self):
        return self._business_partner

    @business_partner.setter
    def business_partner(self, value):
        self._business_partner = value
    @property
    def partner_type(self):
        return self._partner_type

    @partner_type.setter
    def partner_type(self, value):
        self._partner_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def valid_status(self):
        return self._valid_status

    @valid_status.setter
    def valid_status(self, value):
        self._valid_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_partner:
            if hasattr(self.business_partner, 'to_alipay_dict'):
                params['business_partner'] = self.business_partner.to_alipay_dict()
            else:
                params['business_partner'] = self.business_partner
        if self.partner_type:
            if hasattr(self.partner_type, 'to_alipay_dict'):
                params['partner_type'] = self.partner_type.to_alipay_dict()
            else:
                params['partner_type'] = self.partner_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.valid_status:
            if hasattr(self.valid_status, 'to_alipay_dict'):
                params['valid_status'] = self.valid_status.to_alipay_dict()
            else:
                params['valid_status'] = self.valid_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndrbeneficiaryCreateModel()
        if 'business_partner' in d:
            o.business_partner = d['business_partner']
        if 'partner_type' in d:
            o.partner_type = d['partner_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'status' in d:
            o.status = d['status']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'valid_status' in d:
            o.valid_status = d['valid_status']
        return o


