#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodSerprogressSyncModel(object):

    def __init__(self):
        self._ant_ser_contract_no = None
        self._ant_ser_prod_no = None
        self._biz_data = None
        self._change_time = None
        self._out_biz_no = None
        self._ser_biz_no = None
        self._ser_biz_type = None
        self._status = None

    @property
    def ant_ser_contract_no(self):
        return self._ant_ser_contract_no

    @ant_ser_contract_no.setter
    def ant_ser_contract_no(self, value):
        self._ant_ser_contract_no = value
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
    def change_time(self):
        return self._change_time

    @change_time.setter
    def change_time(self, value):
        self._change_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def ser_biz_no(self):
        return self._ser_biz_no

    @ser_biz_no.setter
    def ser_biz_no(self, value):
        self._ser_biz_no = value
    @property
    def ser_biz_type(self):
        return self._ser_biz_type

    @ser_biz_type.setter
    def ser_biz_type(self, value):
        self._ser_biz_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_contract_no:
            if hasattr(self.ant_ser_contract_no, 'to_alipay_dict'):
                params['ant_ser_contract_no'] = self.ant_ser_contract_no.to_alipay_dict()
            else:
                params['ant_ser_contract_no'] = self.ant_ser_contract_no
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
        if self.change_time:
            if hasattr(self.change_time, 'to_alipay_dict'):
                params['change_time'] = self.change_time.to_alipay_dict()
            else:
                params['change_time'] = self.change_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.ser_biz_no:
            if hasattr(self.ser_biz_no, 'to_alipay_dict'):
                params['ser_biz_no'] = self.ser_biz_no.to_alipay_dict()
            else:
                params['ser_biz_no'] = self.ser_biz_no
        if self.ser_biz_type:
            if hasattr(self.ser_biz_type, 'to_alipay_dict'):
                params['ser_biz_type'] = self.ser_biz_type.to_alipay_dict()
            else:
                params['ser_biz_type'] = self.ser_biz_type
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
        o = AlipayInsSceneInsserviceprodSerprogressSyncModel()
        if 'ant_ser_contract_no' in d:
            o.ant_ser_contract_no = d['ant_ser_contract_no']
        if 'ant_ser_prod_no' in d:
            o.ant_ser_prod_no = d['ant_ser_prod_no']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'change_time' in d:
            o.change_time = d['change_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'ser_biz_no' in d:
            o.ser_biz_no = d['ser_biz_no']
        if 'ser_biz_type' in d:
            o.ser_biz_type = d['ser_biz_type']
        if 'status' in d:
            o.status = d['status']
        return o


