#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PartnerVO(object):

    def __init__(self):
        self._biz_status = None
        self._partner_id = None
        self._partner_name = None
        self._short_code = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
    @property
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, value):
        self._short_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        if self.short_code:
            if hasattr(self.short_code, 'to_alipay_dict'):
                params['short_code'] = self.short_code.to_alipay_dict()
            else:
                params['short_code'] = self.short_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PartnerVO()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'short_code' in d:
            o.short_code = d['short_code']
        return o


