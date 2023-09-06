#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertifyConfig(object):

    def __init__(self):
        self._certify_biz_code = None
        self._component_out_id = None
        self._need_address = None
        self._need_certify_id = None
        self._need_gender = None
        self._need_phone = None
        self._need_user_nation = None
        self._verify_channel = None

    @property
    def certify_biz_code(self):
        return self._certify_biz_code

    @certify_biz_code.setter
    def certify_biz_code(self, value):
        self._certify_biz_code = value
    @property
    def component_out_id(self):
        return self._component_out_id

    @component_out_id.setter
    def component_out_id(self, value):
        self._component_out_id = value
    @property
    def need_address(self):
        return self._need_address

    @need_address.setter
    def need_address(self, value):
        self._need_address = value
    @property
    def need_certify_id(self):
        return self._need_certify_id

    @need_certify_id.setter
    def need_certify_id(self, value):
        self._need_certify_id = value
    @property
    def need_gender(self):
        return self._need_gender

    @need_gender.setter
    def need_gender(self, value):
        self._need_gender = value
    @property
    def need_phone(self):
        return self._need_phone

    @need_phone.setter
    def need_phone(self, value):
        self._need_phone = value
    @property
    def need_user_nation(self):
        return self._need_user_nation

    @need_user_nation.setter
    def need_user_nation(self, value):
        self._need_user_nation = value
    @property
    def verify_channel(self):
        return self._verify_channel

    @verify_channel.setter
    def verify_channel(self, value):
        self._verify_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_biz_code:
            if hasattr(self.certify_biz_code, 'to_alipay_dict'):
                params['certify_biz_code'] = self.certify_biz_code.to_alipay_dict()
            else:
                params['certify_biz_code'] = self.certify_biz_code
        if self.component_out_id:
            if hasattr(self.component_out_id, 'to_alipay_dict'):
                params['component_out_id'] = self.component_out_id.to_alipay_dict()
            else:
                params['component_out_id'] = self.component_out_id
        if self.need_address:
            if hasattr(self.need_address, 'to_alipay_dict'):
                params['need_address'] = self.need_address.to_alipay_dict()
            else:
                params['need_address'] = self.need_address
        if self.need_certify_id:
            if hasattr(self.need_certify_id, 'to_alipay_dict'):
                params['need_certify_id'] = self.need_certify_id.to_alipay_dict()
            else:
                params['need_certify_id'] = self.need_certify_id
        if self.need_gender:
            if hasattr(self.need_gender, 'to_alipay_dict'):
                params['need_gender'] = self.need_gender.to_alipay_dict()
            else:
                params['need_gender'] = self.need_gender
        if self.need_phone:
            if hasattr(self.need_phone, 'to_alipay_dict'):
                params['need_phone'] = self.need_phone.to_alipay_dict()
            else:
                params['need_phone'] = self.need_phone
        if self.need_user_nation:
            if hasattr(self.need_user_nation, 'to_alipay_dict'):
                params['need_user_nation'] = self.need_user_nation.to_alipay_dict()
            else:
                params['need_user_nation'] = self.need_user_nation
        if self.verify_channel:
            if hasattr(self.verify_channel, 'to_alipay_dict'):
                params['verify_channel'] = self.verify_channel.to_alipay_dict()
            else:
                params['verify_channel'] = self.verify_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertifyConfig()
        if 'certify_biz_code' in d:
            o.certify_biz_code = d['certify_biz_code']
        if 'component_out_id' in d:
            o.component_out_id = d['component_out_id']
        if 'need_address' in d:
            o.need_address = d['need_address']
        if 'need_certify_id' in d:
            o.need_certify_id = d['need_certify_id']
        if 'need_gender' in d:
            o.need_gender = d['need_gender']
        if 'need_phone' in d:
            o.need_phone = d['need_phone']
        if 'need_user_nation' in d:
            o.need_user_nation = d['need_user_nation']
        if 'verify_channel' in d:
            o.verify_channel = d['verify_channel']
        return o


