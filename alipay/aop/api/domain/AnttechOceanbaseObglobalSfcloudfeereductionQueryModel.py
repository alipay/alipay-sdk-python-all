#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfcloudfeereductionQueryModel(object):

    def __init__(self):
        self._cloud_fee_reduction_id = None
        self._salesforce_id = None

    @property
    def cloud_fee_reduction_id(self):
        return self._cloud_fee_reduction_id

    @cloud_fee_reduction_id.setter
    def cloud_fee_reduction_id(self, value):
        self._cloud_fee_reduction_id = value
    @property
    def salesforce_id(self):
        return self._salesforce_id

    @salesforce_id.setter
    def salesforce_id(self, value):
        self._salesforce_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_fee_reduction_id:
            if hasattr(self.cloud_fee_reduction_id, 'to_alipay_dict'):
                params['cloud_fee_reduction_id'] = self.cloud_fee_reduction_id.to_alipay_dict()
            else:
                params['cloud_fee_reduction_id'] = self.cloud_fee_reduction_id
        if self.salesforce_id:
            if hasattr(self.salesforce_id, 'to_alipay_dict'):
                params['salesforce_id'] = self.salesforce_id.to_alipay_dict()
            else:
                params['salesforce_id'] = self.salesforce_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcloudfeereductionQueryModel()
        if 'cloud_fee_reduction_id' in d:
            o.cloud_fee_reduction_id = d['cloud_fee_reduction_id']
        if 'salesforce_id' in d:
            o.salesforce_id = d['salesforce_id']
        return o


