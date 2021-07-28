#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodSerinfoSyncModel(object):

    def __init__(self):
        self._ant_ser_prod_no = None
        self._ser_biz_no = None
        self._ser_biz_type = None
        self._service_info = None

    @property
    def ant_ser_prod_no(self):
        return self._ant_ser_prod_no

    @ant_ser_prod_no.setter
    def ant_ser_prod_no(self, value):
        self._ant_ser_prod_no = value
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
    def service_info(self):
        return self._service_info

    @service_info.setter
    def service_info(self, value):
        self._service_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_prod_no:
            if hasattr(self.ant_ser_prod_no, 'to_alipay_dict'):
                params['ant_ser_prod_no'] = self.ant_ser_prod_no.to_alipay_dict()
            else:
                params['ant_ser_prod_no'] = self.ant_ser_prod_no
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
        if self.service_info:
            if hasattr(self.service_info, 'to_alipay_dict'):
                params['service_info'] = self.service_info.to_alipay_dict()
            else:
                params['service_info'] = self.service_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsserviceprodSerinfoSyncModel()
        if 'ant_ser_prod_no' in d:
            o.ant_ser_prod_no = d['ant_ser_prod_no']
        if 'ser_biz_no' in d:
            o.ser_biz_no = d['ser_biz_no']
        if 'ser_biz_type' in d:
            o.ser_biz_type = d['ser_biz_type']
        if 'service_info' in d:
            o.service_info = d['service_info']
        return o


