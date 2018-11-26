#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCloudDetailQueryModel(object):

    def __init__(self):
        self._mini_appid = None
        self._partner_id = None

    @property
    def mini_appid(self):
        return self._mini_appid

    @mini_appid.setter
    def mini_appid(self, value):
        self._mini_appid = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_appid:
            if hasattr(self.mini_appid, 'to_alipay_dict'):
                params['mini_appid'] = self.mini_appid.to_alipay_dict()
            else:
                params['mini_appid'] = self.mini_appid
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudDetailQueryModel()
        if 'mini_appid' in d:
            o.mini_appid = d['mini_appid']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


