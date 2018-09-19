#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDataMonitordeviceQualitycenterModifyModel(object):

    def __init__(self):
        self._asset_id = None
        self._fault_type = None
        self._invoke_id = None
        self._quality_center_id = None
        self._result = None
        self._result_date = None
        self._result_msg = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def fault_type(self):
        return self._fault_type

    @fault_type.setter
    def fault_type(self, value):
        self._fault_type = value
    @property
    def invoke_id(self):
        return self._invoke_id

    @invoke_id.setter
    def invoke_id(self, value):
        self._invoke_id = value
    @property
    def quality_center_id(self):
        return self._quality_center_id

    @quality_center_id.setter
    def quality_center_id(self, value):
        self._quality_center_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_date(self):
        return self._result_date

    @result_date.setter
    def result_date(self, value):
        self._result_date = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.fault_type:
            if hasattr(self.fault_type, 'to_alipay_dict'):
                params['fault_type'] = self.fault_type.to_alipay_dict()
            else:
                params['fault_type'] = self.fault_type
        if self.invoke_id:
            if hasattr(self.invoke_id, 'to_alipay_dict'):
                params['invoke_id'] = self.invoke_id.to_alipay_dict()
            else:
                params['invoke_id'] = self.invoke_id
        if self.quality_center_id:
            if hasattr(self.quality_center_id, 'to_alipay_dict'):
                params['quality_center_id'] = self.quality_center_id.to_alipay_dict()
            else:
                params['quality_center_id'] = self.quality_center_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.result_date:
            if hasattr(self.result_date, 'to_alipay_dict'):
                params['result_date'] = self.result_date.to_alipay_dict()
            else:
                params['result_date'] = self.result_date
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataMonitordeviceQualitycenterModifyModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'fault_type' in d:
            o.fault_type = d['fault_type']
        if 'invoke_id' in d:
            o.invoke_id = d['invoke_id']
        if 'quality_center_id' in d:
            o.quality_center_id = d['quality_center_id']
        if 'result' in d:
            o.result = d['result']
        if 'result_date' in d:
            o.result_date = d['result_date']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        return o


