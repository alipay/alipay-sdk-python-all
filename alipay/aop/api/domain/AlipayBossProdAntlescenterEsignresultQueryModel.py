#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlescenterEsignresultQueryModel(object):

    def __init__(self):
        self._app_name = None
        self._business_unique_id = None
        self._seal_request_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def business_unique_id(self):
        return self._business_unique_id

    @business_unique_id.setter
    def business_unique_id(self, value):
        self._business_unique_id = value
    @property
    def seal_request_id(self):
        return self._seal_request_id

    @seal_request_id.setter
    def seal_request_id(self, value):
        self._seal_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.business_unique_id:
            if hasattr(self.business_unique_id, 'to_alipay_dict'):
                params['business_unique_id'] = self.business_unique_id.to_alipay_dict()
            else:
                params['business_unique_id'] = self.business_unique_id
        if self.seal_request_id:
            if hasattr(self.seal_request_id, 'to_alipay_dict'):
                params['seal_request_id'] = self.seal_request_id.to_alipay_dict()
            else:
                params['seal_request_id'] = self.seal_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlescenterEsignresultQueryModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'business_unique_id' in d:
            o.business_unique_id = d['business_unique_id']
        if 'seal_request_id' in d:
            o.seal_request_id = d['seal_request_id']
        return o


