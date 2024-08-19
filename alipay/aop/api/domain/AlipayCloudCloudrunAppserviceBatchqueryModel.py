#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunAppserviceBatchqueryModel(object):

    def __init__(self):
        self._app_service_uuid = None

    @property
    def app_service_uuid(self):
        return self._app_service_uuid

    @app_service_uuid.setter
    def app_service_uuid(self, value):
        self._app_service_uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_service_uuid:
            if hasattr(self.app_service_uuid, 'to_alipay_dict'):
                params['app_service_uuid'] = self.app_service_uuid.to_alipay_dict()
            else:
                params['app_service_uuid'] = self.app_service_uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunAppserviceBatchqueryModel()
        if 'app_service_uuid' in d:
            o.app_service_uuid = d['app_service_uuid']
        return o


