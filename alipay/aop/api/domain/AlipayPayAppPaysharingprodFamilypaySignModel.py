#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FamilyPayBizUserInfo import FamilyPayBizUserInfo
from alipay.aop.api.domain.FamilyPayQuotaInfo import FamilyPayQuotaInfo
from alipay.aop.api.domain.FamilyPayBizUserInfo import FamilyPayBizUserInfo


class AlipayPayAppPaysharingprodFamilypaySignModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._payer_info = None
        self._quota_info = None
        self._return_path = None
        self._source = None
        self._spender_info = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, FamilyPayBizUserInfo):
            self._payer_info = value
        else:
            self._payer_info = FamilyPayBizUserInfo.from_alipay_dict(value)
    @property
    def quota_info(self):
        return self._quota_info

    @quota_info.setter
    def quota_info(self, value):
        if isinstance(value, FamilyPayQuotaInfo):
            self._quota_info = value
        else:
            self._quota_info = FamilyPayQuotaInfo.from_alipay_dict(value)
    @property
    def return_path(self):
        return self._return_path

    @return_path.setter
    def return_path(self, value):
        self._return_path = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def spender_info(self):
        return self._spender_info

    @spender_info.setter
    def spender_info(self, value):
        if isinstance(value, FamilyPayBizUserInfo):
            self._spender_info = value
        else:
            self._spender_info = FamilyPayBizUserInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.quota_info:
            if hasattr(self.quota_info, 'to_alipay_dict'):
                params['quota_info'] = self.quota_info.to_alipay_dict()
            else:
                params['quota_info'] = self.quota_info
        if self.return_path:
            if hasattr(self.return_path, 'to_alipay_dict'):
                params['return_path'] = self.return_path.to_alipay_dict()
            else:
                params['return_path'] = self.return_path
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.spender_info:
            if hasattr(self.spender_info, 'to_alipay_dict'):
                params['spender_info'] = self.spender_info.to_alipay_dict()
            else:
                params['spender_info'] = self.spender_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppPaysharingprodFamilypaySignModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'quota_info' in d:
            o.quota_info = d['quota_info']
        if 'return_path' in d:
            o.return_path = d['return_path']
        if 'source' in d:
            o.source = d['source']
        if 'spender_info' in d:
            o.spender_info = d['spender_info']
        return o


