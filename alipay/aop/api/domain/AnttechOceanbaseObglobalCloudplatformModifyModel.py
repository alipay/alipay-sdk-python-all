#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaokeCreateOrUpdateCustomerCloudPlatformRequest import FxiaokeCreateOrUpdateCustomerCloudPlatformRequest


class AnttechOceanbaseObglobalCloudplatformModifyModel(object):

    def __init__(self):
        self._create_or_update_customer_cloud_platform_request = None

    @property
    def create_or_update_customer_cloud_platform_request(self):
        return self._create_or_update_customer_cloud_platform_request

    @create_or_update_customer_cloud_platform_request.setter
    def create_or_update_customer_cloud_platform_request(self, value):
        if isinstance(value, FxiaokeCreateOrUpdateCustomerCloudPlatformRequest):
            self._create_or_update_customer_cloud_platform_request = value
        else:
            self._create_or_update_customer_cloud_platform_request = FxiaokeCreateOrUpdateCustomerCloudPlatformRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_or_update_customer_cloud_platform_request:
            if hasattr(self.create_or_update_customer_cloud_platform_request, 'to_alipay_dict'):
                params['create_or_update_customer_cloud_platform_request'] = self.create_or_update_customer_cloud_platform_request.to_alipay_dict()
            else:
                params['create_or_update_customer_cloud_platform_request'] = self.create_or_update_customer_cloud_platform_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCloudplatformModifyModel()
        if 'create_or_update_customer_cloud_platform_request' in d:
            o.create_or_update_customer_cloud_platform_request = d['create_or_update_customer_cloud_platform_request']
        return o


