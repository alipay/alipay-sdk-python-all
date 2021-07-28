#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCardQueryModel(object):

    def __init__(self):
        self._auth_code = None
        self._buyer_id = None
        self._card_org_no = None
        self._extend_params = None
        self._ins_type = None
        self._return_url = None
        self._scene = None
        self._version_no = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def card_org_no(self):
        return self._card_org_no

    @card_org_no.setter
    def card_org_no(self, value):
        self._card_org_no = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def ins_type(self):
        return self._ins_type

    @ins_type.setter
    def ins_type(self, value):
        self._ins_type = value
    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.card_org_no:
            if hasattr(self.card_org_no, 'to_alipay_dict'):
                params['card_org_no'] = self.card_org_no.to_alipay_dict()
            else:
                params['card_org_no'] = self.card_org_no
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.ins_type:
            if hasattr(self.ins_type, 'to_alipay_dict'):
                params['ins_type'] = self.ins_type.to_alipay_dict()
            else:
                params['ins_type'] = self.ins_type
        if self.return_url:
            if hasattr(self.return_url, 'to_alipay_dict'):
                params['return_url'] = self.return_url.to_alipay_dict()
            else:
                params['return_url'] = self.return_url
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCardQueryModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'card_org_no' in d:
            o.card_org_no = d['card_org_no']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'ins_type' in d:
            o.ins_type = d['ins_type']
        if 'return_url' in d:
            o.return_url = d['return_url']
        if 'scene' in d:
            o.scene = d['scene']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


