#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinancePfQuotaQueryModel(object):

    def __init__(self):
        self._client_no = None
        self._crf_type = None
        self._id_num = None
        self._parm = None
        self._platform_id = None

    @property
    def client_no(self):
        return self._client_no

    @client_no.setter
    def client_no(self, value):
        self._client_no = value
    @property
    def crf_type(self):
        return self._crf_type

    @crf_type.setter
    def crf_type(self, value):
        self._crf_type = value
    @property
    def id_num(self):
        return self._id_num

    @id_num.setter
    def id_num(self, value):
        self._id_num = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_no:
            if hasattr(self.client_no, 'to_alipay_dict'):
                params['client_no'] = self.client_no.to_alipay_dict()
            else:
                params['client_no'] = self.client_no
        if self.crf_type:
            if hasattr(self.crf_type, 'to_alipay_dict'):
                params['crf_type'] = self.crf_type.to_alipay_dict()
            else:
                params['crf_type'] = self.crf_type
        if self.id_num:
            if hasattr(self.id_num, 'to_alipay_dict'):
                params['id_num'] = self.id_num.to_alipay_dict()
            else:
                params['id_num'] = self.id_num
        if self.parm:
            if hasattr(self.parm, 'to_alipay_dict'):
                params['parm'] = self.parm.to_alipay_dict()
            else:
                params['parm'] = self.parm
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinancePfQuotaQueryModel()
        if 'client_no' in d:
            o.client_no = d['client_no']
        if 'crf_type' in d:
            o.crf_type = d['crf_type']
        if 'id_num' in d:
            o.id_num = d['id_num']
        if 'parm' in d:
            o.parm = d['parm']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        return o


