#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceAnthotlinemngRecordingQueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_sign = None
        self._contact_id = None
        self._instance_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_sign(self):
        return self._biz_sign

    @biz_sign.setter
    def biz_sign(self, value):
        self._biz_sign = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_sign:
            if hasattr(self.biz_sign, 'to_alipay_dict'):
                params['biz_sign'] = self.biz_sign.to_alipay_dict()
            else:
                params['biz_sign'] = self.biz_sign
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceAnthotlinemngRecordingQueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_sign' in d:
            o.biz_sign = d['biz_sign']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        return o


