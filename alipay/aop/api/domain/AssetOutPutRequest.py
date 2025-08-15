#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetOutPutRequest(object):

    def __init__(self):
        self._cert_no = None
        self._out_biz_no = None
        self._out_voucher_id = None
        self._project_id = None
        self._tele_no = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_voucher_id(self):
        return self._out_voucher_id

    @out_voucher_id.setter
    def out_voucher_id(self, value):
        self._out_voucher_id = value
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
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_voucher_id:
            if hasattr(self.out_voucher_id, 'to_alipay_dict'):
                params['out_voucher_id'] = self.out_voucher_id.to_alipay_dict()
            else:
                params['out_voucher_id'] = self.out_voucher_id
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
        o = AssetOutPutRequest()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_voucher_id' in d:
            o.out_voucher_id = d['out_voucher_id']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'tele_no' in d:
            o.tele_no = d['tele_no']
        return o


