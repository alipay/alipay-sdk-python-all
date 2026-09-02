#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalFulfillmentSampletestSyncModel(object):

    def __init__(self):
        self._fulfillment_id = None
        self._out_biz_no = None
        self._sample_status = None
        self._sample_status_time = None
        self._type = None

    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sample_status(self):
        return self._sample_status

    @sample_status.setter
    def sample_status(self, value):
        self._sample_status = value
    @property
    def sample_status_time(self):
        return self._sample_status_time

    @sample_status_time.setter
    def sample_status_time(self, value):
        self._sample_status_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sample_status:
            if hasattr(self.sample_status, 'to_alipay_dict'):
                params['sample_status'] = self.sample_status.to_alipay_dict()
            else:
                params['sample_status'] = self.sample_status
        if self.sample_status_time:
            if hasattr(self.sample_status_time, 'to_alipay_dict'):
                params['sample_status_time'] = self.sample_status_time.to_alipay_dict()
            else:
                params['sample_status_time'] = self.sample_status_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFulfillmentSampletestSyncModel()
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sample_status' in d:
            o.sample_status = d['sample_status']
        if 'sample_status_time' in d:
            o.sample_status_time = d['sample_status_time']
        if 'type' in d:
            o.type = d['type']
        return o


