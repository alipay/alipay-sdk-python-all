#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingRtaAuthModel(object):

    def __init__(self):
        self._campaign_ids = None
        self._mobile_sha_256 = None
        self._operation_type = None
        self._request_id = None
        self._resource_id = None

    @property
    def campaign_ids(self):
        return self._campaign_ids

    @campaign_ids.setter
    def campaign_ids(self, value):
        if isinstance(value, list):
            self._campaign_ids = list()
            for i in value:
                self._campaign_ids.append(i)
    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_ids:
            if isinstance(self.campaign_ids, list):
                for i in range(0, len(self.campaign_ids)):
                    element = self.campaign_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.campaign_ids[i] = element.to_alipay_dict()
            if hasattr(self.campaign_ids, 'to_alipay_dict'):
                params['campaign_ids'] = self.campaign_ids.to_alipay_dict()
            else:
                params['campaign_ids'] = self.campaign_ids
        if self.mobile_sha_256:
            if hasattr(self.mobile_sha_256, 'to_alipay_dict'):
                params['mobile_sha_256'] = self.mobile_sha_256.to_alipay_dict()
            else:
                params['mobile_sha_256'] = self.mobile_sha_256
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingRtaAuthModel()
        if 'campaign_ids' in d:
            o.campaign_ids = d['campaign_ids']
        if 'mobile_sha_256' in d:
            o.mobile_sha_256 = d['mobile_sha_256']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        return o


