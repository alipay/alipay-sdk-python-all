#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourOrderSyncDetail(object):

    def __init__(self):
        self._biz_source_num = None
        self._cert_no = None
        self._name = None
        self._order_info = None
        self._out_biz_no = None
        self._project_id = None
        self._tele_no = None

    @property
    def biz_source_num(self):
        return self._biz_source_num

    @biz_source_num.setter
    def biz_source_num(self, value):
        self._biz_source_num = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        self._order_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def tele_no(self):
        return self._tele_no

    @tele_no.setter
    def tele_no(self, value):
        self._tele_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source_num:
            if hasattr(self.biz_source_num, 'to_alipay_dict'):
                params['biz_source_num'] = self.biz_source_num.to_alipay_dict()
            else:
                params['biz_source_num'] = self.biz_source_num
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.tele_no:
            if hasattr(self.tele_no, 'to_alipay_dict'):
                params['tele_no'] = self.tele_no.to_alipay_dict()
            else:
                params['tele_no'] = self.tele_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourOrderSyncDetail()
        if 'biz_source_num' in d:
            o.biz_source_num = d['biz_source_num']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'name' in d:
            o.name = d['name']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'tele_no' in d:
            o.tele_no = d['tele_no']
        return o


