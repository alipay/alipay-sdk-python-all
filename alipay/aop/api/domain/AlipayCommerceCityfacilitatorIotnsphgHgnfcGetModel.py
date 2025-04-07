#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorIotnsphgHgnfcGetModel(object):

    def __init__(self):
        self._biz_info = None
        self._biz_tid = None
        self._ext_info = None
        self._push_product_name = None
        self._req_id = None
        self._service_id = None
        self._sn = None
        self._upper_biz_tid = None
        self._upper_sn = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def push_product_name(self):
        return self._push_product_name

    @push_product_name.setter
    def push_product_name(self, value):
        self._push_product_name = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def upper_biz_tid(self):
        return self._upper_biz_tid

    @upper_biz_tid.setter
    def upper_biz_tid(self, value):
        self._upper_biz_tid = value
    @property
    def upper_sn(self):
        return self._upper_sn

    @upper_sn.setter
    def upper_sn(self, value):
        self._upper_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.push_product_name:
            if hasattr(self.push_product_name, 'to_alipay_dict'):
                params['push_product_name'] = self.push_product_name.to_alipay_dict()
            else:
                params['push_product_name'] = self.push_product_name
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.upper_biz_tid:
            if hasattr(self.upper_biz_tid, 'to_alipay_dict'):
                params['upper_biz_tid'] = self.upper_biz_tid.to_alipay_dict()
            else:
                params['upper_biz_tid'] = self.upper_biz_tid
        if self.upper_sn:
            if hasattr(self.upper_sn, 'to_alipay_dict'):
                params['upper_sn'] = self.upper_sn.to_alipay_dict()
            else:
                params['upper_sn'] = self.upper_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorIotnsphgHgnfcGetModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'push_product_name' in d:
            o.push_product_name = d['push_product_name']
        if 'req_id' in d:
            o.req_id = d['req_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'upper_biz_tid' in d:
            o.upper_biz_tid = d['upper_biz_tid']
        if 'upper_sn' in d:
            o.upper_sn = d['upper_sn']
        return o


