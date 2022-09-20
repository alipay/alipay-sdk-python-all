#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantIndirectSmidVerifyResultRecord(object):

    def __init__(self):
        self._org_id = None
        self._smid = None
        self._source_id = None
        self._verifiy_failed_msg = None
        self._verifiy_result = None

    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def verifiy_failed_msg(self):
        return self._verifiy_failed_msg

    @verifiy_failed_msg.setter
    def verifiy_failed_msg(self, value):
        self._verifiy_failed_msg = value
    @property
    def verifiy_result(self):
        return self._verifiy_result

    @verifiy_result.setter
    def verifiy_result(self, value):
        self._verifiy_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.verifiy_failed_msg:
            if hasattr(self.verifiy_failed_msg, 'to_alipay_dict'):
                params['verifiy_failed_msg'] = self.verifiy_failed_msg.to_alipay_dict()
            else:
                params['verifiy_failed_msg'] = self.verifiy_failed_msg
        if self.verifiy_result:
            if hasattr(self.verifiy_result, 'to_alipay_dict'):
                params['verifiy_result'] = self.verifiy_result.to_alipay_dict()
            else:
                params['verifiy_result'] = self.verifiy_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantIndirectSmidVerifyResultRecord()
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'smid' in d:
            o.smid = d['smid']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'verifiy_failed_msg' in d:
            o.verifiy_failed_msg = d['verifiy_failed_msg']
        if 'verifiy_result' in d:
            o.verifiy_result = d['verifiy_result']
        return o


