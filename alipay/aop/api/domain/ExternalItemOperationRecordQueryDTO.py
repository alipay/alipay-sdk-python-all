#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalItemOperationRecordQueryDTO(object):

    def __init__(self):
        self._ant_ser_prod_no = None
        self._biz_data = None
        self._finish_time = None
        self._init_time = None
        self._merchant_item_code = None
        self._record_id = None
        self._refresh_type = None
        self._status = None

    @property
    def ant_ser_prod_no(self):
        return self._ant_ser_prod_no

    @ant_ser_prod_no.setter
    def ant_ser_prod_no(self, value):
        self._ant_ser_prod_no = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def init_time(self):
        return self._init_time

    @init_time.setter
    def init_time(self, value):
        self._init_time = value
    @property
    def merchant_item_code(self):
        return self._merchant_item_code

    @merchant_item_code.setter
    def merchant_item_code(self, value):
        self._merchant_item_code = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def refresh_type(self):
        return self._refresh_type

    @refresh_type.setter
    def refresh_type(self, value):
        self._refresh_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_prod_no:
            if hasattr(self.ant_ser_prod_no, 'to_alipay_dict'):
                params['ant_ser_prod_no'] = self.ant_ser_prod_no.to_alipay_dict()
            else:
                params['ant_ser_prod_no'] = self.ant_ser_prod_no
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.init_time:
            if hasattr(self.init_time, 'to_alipay_dict'):
                params['init_time'] = self.init_time.to_alipay_dict()
            else:
                params['init_time'] = self.init_time
        if self.merchant_item_code:
            if hasattr(self.merchant_item_code, 'to_alipay_dict'):
                params['merchant_item_code'] = self.merchant_item_code.to_alipay_dict()
            else:
                params['merchant_item_code'] = self.merchant_item_code
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.refresh_type:
            if hasattr(self.refresh_type, 'to_alipay_dict'):
                params['refresh_type'] = self.refresh_type.to_alipay_dict()
            else:
                params['refresh_type'] = self.refresh_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalItemOperationRecordQueryDTO()
        if 'ant_ser_prod_no' in d:
            o.ant_ser_prod_no = d['ant_ser_prod_no']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'init_time' in d:
            o.init_time = d['init_time']
        if 'merchant_item_code' in d:
            o.merchant_item_code = d['merchant_item_code']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'refresh_type' in d:
            o.refresh_type = d['refresh_type']
        if 'status' in d:
            o.status = d['status']
        return o


